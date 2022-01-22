from flask import Flask, request
from flask-sqlalchemy import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy(app)

@app.route('/')
def front_page():
    return 'Hello everybody! It is a pleasure having you here'

@app.route('/song', methods =['GET', 'POST'])
def crud_song():
    if request.method == 'GET':
        return 'esto fue un get'
    elif request.method == 'POST':

        request_data = request.form

        name = request_data['name']
        artist = request_data['artist']
        genre = request_data['genre']

        print("Nombre: " + name)
        print("Artista: " + artist)
        print("Genero: " + genre)
        
        return 'se registro esa canción exitosamente'

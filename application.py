from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:root@localhost:5432/rockoladb"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'some-secret-key'

db = SQLAlchemy(app)

#from app import routes, models
from models import Song

db.create_all()
db.session.commit()


@app.route('/')
def front_page():
    return 'Hello everybody! It is a pleasure having you here'

@app.route('/room')
def room_page():
    return render_template("room.html")

@app.route('/song', methods=['GET', 'POST'])
def crud_song():

    if request.method == 'GET':
        name = "natural"
        artist = "imagine dragons"
        genre = "rock"
        album = "Origins"
        year = 2018
        link = "https://www.youtube.com/watch?v=0I647GU3Jsc"
        
        #objeto de la clase canción
        entry = Song(name,artist,genre,album,year,link)
        db.session.add(entry)
        db.session.commit()

        return 'esto fue un GET'

    elif request.method == 'POST':

        request_data = request.form

        name = request_data['name']
        artist = request_data['artist']
        genre = request_data['genre']

        print("Nombre: " + name)
        print("Artista: " + artist)
        print("Genero: " + genre)
        
        return 'se registro esa canción exitosamente' 

@app.route('/updatesong', methods=['GET', 'POST'])
def update_song():
    old_name = "imagine"
    new_name = "Despacito"
    old_song = Song.query.filter_by(name=old_name).first()
    old_song.name = new_name
    db.session.commit()
    return 'actualización exitosa'

@app.route('/getsongs')
def get_songs():
    songs = Song.query.all()
    print(songs[0].artist)
    return "se trabajó las canciones"

@app.route('/deletesong')
def delete_song():
    song_name = "Despacito"
    song = Song.query.filter_by(name=song_name).first()
    db.session.delete(song)
    db.session.commit()
    return "se borró la canción"
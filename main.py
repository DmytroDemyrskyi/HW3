from flask import Flask
from faker import Faker
import sqlite3

app = Flask(__name__)

fake = Faker()

conn = sqlite3.connect('info.db')
cursor = conn.cursor()


@app.route('/names/')
def get_unique_names():
    conn = sqlite3.connect('info.db')
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(DISTINCT first_name) FROM customers')
    count = cursor.fetchone()[0]
    conn.close()
    return f"Кількість унікальних імен: {count}"


@app.route('/tracks/')
def get_tracks_count():
    conn = sqlite3.connect('info.db')
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM tracks')
    count = cursor.fetchone()[0]
    conn.close()
    return f"Кількість записів в таблиці tracks: {count}"


@app.route('/tracks-sec/')
def get_track_info():
    conn = sqlite3.connect('info.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, artist, length_seconds, release_date FROM tracks')
    tracks_info = cursor.fetchall()
    conn.close()

    result = "Інформація про треки:<br>"
    for track in tracks_info:
        result += f"ID: {track[0]}, Виконавець: {track[1]}, Довжина (сек): {track[2]}, Дата випуску: {track[3]}<br>"

    return result

from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/home')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/subsites/hall_of_fame.html')#this is not the file path, this is the url path, displayed in the browser, the file path is in the send_from_directory function
def hall_of_fame():
    return send_from_directory('subsites', 'hall_of_fame.html')

@app.route('/subsites/photos.html')#this is not the file path, this is the url path, displayed in the browser, the file path is in the send_from_directory function
def photos():
    return send_from_directory('subsites', 'photos.html')

@app.route('/subsites/projects.html')
def projects():
    return send_from_directory('subsites', 'projects.html')

@app.route('/subsites/radio.html')
def radio():
    return send_from_directory('subsites', 'radio.html')

@app.route('/subsites/school_announcements.html')
def school_announcements():
    return send_from_directory('subsites', 'school_announcements.html')

@app.route('/subsites/teachers_quotes.html')
def teachers_quotes():
    return send_from_directory('subsites', 'teachers_quotes.html')

@app.route('/subsites/timetable.html')
def timetable():
    return send_from_directory('subsites', 'timetable.html')

@app.route('/subsites/website_announcements.html')
def website_announcements():
    return send_from_directory('subsites', 'website_announcements.html')
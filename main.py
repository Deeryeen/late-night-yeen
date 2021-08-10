from flask import Flask, render_template, Markup, request
from pathlib import Path
from note import Note
from datetime import datetime
from yaml import load, Loader
import json

app = Flask(__name__, template_folder='templates/', static_folder='static/')

notes_folder = Path('static/notes/')

@app.route('/')
def home():
    notes=[]
    for element in notes_folder.rglob('*.md'):
        note_dict=Note(element).to_dict()
        notes.append(note_dict)
    return render_template('index.html', notes=notes)

@app.route('/note/<note_name>')
def note(note_name):
    note_file = Path(notes_folder, note_name)
    if not note_file.exists():
        return render_template('error.html', filename=note_name)
    note_object = Note(note_file)
    return render_template('note.html', name=note_object.name, description=note_object.description, contents=Markup(note_object.contents))

# Managing the notes.
@app.route('/manage/list', methods=['GET'])
def manage_list():
    notes = []
    for note in notes_folder.rglob('*.md'):
        notes.append(Note(note).metadata())

    return json.dumps(notes)

if __name__ == '__main__':
    app.run(debug=True)
from urllib import request
import pymongo
import datetime
from flask import Flask, render_template, request, redirect
from bson.objectid import ObjectId

app = Flask('notemanager')

client = pymongo.MongoClient("mongodb+srv://kingaryaprince:OtczMGyaLwsZFOV8@cluster0.zzqvh.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.Note_Manager

@app.route('/', methods = ['GET', 'POST'])


def index():
    if request.method == 'GET':
        notes = db.Notes.find()
        return render_template('index.html', notes = notes)
    elif request.method == 'POST':
        print(request.form)
        if request.form['note'].strip() == "":
            print('Unable to Submit')
        doc = {
            'note': request.form['note'],
            'timestamp' : datetime.datetime.utcnow()
        }
        db.Notes.insert_one(doc)
        return redirect('/')

@app.route('/delete/<note_id>')

def delete(note_id):
    db.Notes.delete_one({'_id':ObjectId(note_id)})
    return redirect('/')
    
app.run(debug = True)
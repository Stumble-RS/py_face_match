import face_recognition
from flask import Flask,request,jsonify
import urllib

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/compare", methods=['POST'])
def comparePhotos():
  resp = compareImages(request.form['path1'], request.form['path2'], request.form['local'])
  return jsonify({"result": 1 if resp else 0})

def compareImages(path1, path2, local = 0):
  print(path1, path2, local)

  if local == 1:
    image1 = face_recognition.load_image_file(path1)
    image2 = face_recognition.load_image_file(path2)
  else:
    response1 = urllib.request.urlopen(path1)
    image1 = face_recognition.load_image_file(response1)
    response2 = urllib.request.urlopen(path2)
    image2 = face_recognition.load_image_file(response2)

  face_encodings1 = face_recognition.face_encodings(image1)[0]
  face_encodings2 = face_recognition.face_encodings(image2)[0]

  results = face_recognition.compare_faces([face_encodings1],face_encodings2)
  return results[0]

import face_recognition
# from multiprocessing import Pool
from flask import Flask,request,jsonify
import urllib

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/compare", methods=['POST'])
def comparePhotos():
  target = request.json['target']
  paths = request.json['paths']
  local = request.json['local']
  if not target or not paths:
    return jsonify({"result": -1})
  resp = compareMultipleImages(target, paths, local)
  return jsonify({"result": 1 if resp else 0})

def compareMultipleImages(target, paths, local = 0):
  # paths = list(map(lambda x: [target, x, local], paths))
  # pool = Pool(processes=len(paths)) not worth it due process creation overhead
  # pool.map(compareTwoImages, paths)
  for path in paths:
    if compareTwoImages(target, path, local):
      return True
  # resp = await asyncio.gather(*[compareTwoImages(i) for i in paths]) // async process not worth it, need to downgrade package
  # print(resp)
  return False

def compareTwoImages(path1, path2, local):
  if local:
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

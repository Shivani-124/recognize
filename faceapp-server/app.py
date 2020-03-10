from flask import Flask, request
from database import Database
from person import Person
from faceencoding import Faceencoding
from face_recognition. face_recognition_cli import face_recognition
import base64
from PIL import Image
import numpy as np
import io
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route(rule='/')
def index():
    return "Hello World"


@app.route(rule='/getuser')
def getuser():
    a = {}
    a['name'] = 'abcd'
    a['roll'] = 10

    b = {}
    b['city'] = 'Solapur'
    b['pin'] = 413001

    a['address'] = b

    return a


@app.route(rule='/adduser', methods=['POST'])
def adduser():
    data = request.json
    print(type(data))
    # print(data)

    d = Database()

    p = Person()
    p.name = data['name']
    p.phoneticname = data['name']
    p.details = data['details']

    photo = data['photo']
    # decode base64
    # d=base64.b64decode(photo)
    # print(d)
    bytes = base64.decodebytes(photo.encode())
    image = Image.open(io.BytesIO(bytes))
    image = image.convert('RGB')
    print('image', image)
    print(dir(image))
    # imagearr=np.array([image])
    encoding = face_recognition.face_encodings(np.array(image))[0]
    print('encoding', encoding)
    # decode image from memory using pillow(python)

    # compute face encoding

    # add faceencoding to db

    pid = d.addperson(p)

    fe = Faceencoding()
    fe.pid = pid
    fe.encoding = encoding

    d.addfaceencoding(fe)

    d.close()

    result = {}
    result['status'] = 'success'
    result['message'] = "User Added"

    return result


@app.route(rule='/findstudent', methods=['POST'])
def findstudent():
    data = request.json
    print(type(data))
    # print(data)
    # print(data)
    photo = data['photo']
    bytes = base64.decodebytes(photo.encode())
    image = Image.open(io.BytesIO(bytes))
    image = image.convert('RGB')
    # print('image', image)
    # print(dir(image))
    # imagearr=np.array([image])
    inputencoding = face_recognition.face_encodings(np.array(image))[0]
    print('encoding', inputencoding)

    d = Database()
    encodings = d.getfaceencoding()

    for encoding in encodings:
        array = np.array([float(x) for x in str(encoding[2][1:-2]).split()], dtype='float32')
        id=int(encoding[1])
        # student = {'id': , 'array': array}
        # students.append(student)
        dist=face_recognition.face_distance(np.array([array], dtype='float32'), inputencoding)
        # print(student.__dict__)
        if dist<0.6:
            print(dist)
            s=d.getstudent(id)
            result={}
            result['status']='success'
            result['student']=s
            d.close()
            return result

    result={}
    result['status']='error'
    result['message']='Student not found'

    d.close()
    return result


# d = Database()
# array = d.getfaceencoding()
# for encoding in array:
#     array = np.array(
#         [float(x) for x in str(encoding[2][1:-2]).split()])
#     student = {'id': int(encoding[1]), 'array': array}
#     print(student)
# d.close()

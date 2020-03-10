import face_recognition.api  as fr
import os
import csv


dir='face_photos_small'
files=os.listdir(dir)
csv=open('dataset.csv',mode='w')

encodingmap={}

for file in files:
    filepath=dir+"/"+file
    image=fr.load_image_file(filepath)
    encoding=fr.face_encodings(image)[0]
    encodingmap[file]=encoding
    # print(file,encoding)
    csv.write('"'+file+'"')
    for e in encoding:
        csv.write(','+str(e))
    csv.write('\n')
csv.close()

for f1 in encodingmap.keys():
    for f2 in encodingmap.keys():
        if f1==f2:
            continue
        e1=encodingmap[f1]
        e2=encodingmap[f2]
        # print(f1,e1,f2,e2)
        dist=fr.face_distance([e1],e2)
        print(f1,f2,dist)

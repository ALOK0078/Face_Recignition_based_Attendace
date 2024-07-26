import cv2
import face_recognition
import os
import pickle
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://face-attendance-a50d6-default-rtdb.firebaseio.com/",
    'storageBucket':"face-attendance-a50d6.appspot.com"
})

folderpath = 'Images'
Pathlist = os.listdir(folderpath)
print(Pathlist)
imgList = []
studentIds = []
for path in Pathlist:
    imgList.append(cv2.imread(os.path.join(folderpath, path)))
    studentIds.append(os.path.splitext(path)[0])

    fileName = f'{folderpath}/{path}'
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)
print(studentIds)


def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        # Convert image from BGR to RGB
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # Find face encodings
        encode = face_recognition.face_encodings(img_rgb)
        # Check if at least one face encoding was found
        if encode:
            encodeList.append(encode[0])
        else:
            print("No face found in the image")
    return encodeList

print("Encoding started...")
encodListknown = findEncodings(imgList)
encodListknwonwithIds = [encodListknown , studentIds]
print("Encoding Complete")
file =open("EncodeFile.p","wb")
pickle.dump(encodListknwonwithIds,file)
file.close()
print("file saved")

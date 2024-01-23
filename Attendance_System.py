import cv2
import face_recognition as fr
import os
import csv
import threading
import MySql
from datetime import datetime
import numpy as np
import Shared_credentials as SC
import MailSystem as MS
from Shared_credentials import rw


def Database_Name_Updation(list):
    if SC.Connected == True:
        for a in list:
            a = a.split('_')
            query = "INSERT IGNORE INTO attendence (roll,Name) VALUES(" + a[0] + ',' + '"' + a[1] + '"' + ");"
            MySql.exc(query, SC.username, SC.password)

def imres(scale, img):
    width = int(img.shape[1] * scale / 100)
    height = int(img.shape[0] * scale / 100)
    dim = (width, height)
    im = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    return im
def mark_attendance(name):
    global name_list
    global Date
    global time
    print(name_list, time, Date)


    if name not in name_list:
        now = datetime.now()
        Roll = name.split('_')
        print(Roll[0])
        dt_string = now.strftime('%H:%M:%S')
        time_stamp = now.strftime('%H : %M')

        dt_time = dt_string.split('_')
        print(dt_time)
        date_string = now.date().strftime('%Y-%m-%d')  # Format date as desired
        query = "update  attendence set " + str(MySql.today) + "= " + "'" + time_stamp + "'" + " where roll =" + Roll[0]
        print(query)
        MySql.exc(query, password=SC.password, user=SC.username, get="update")
        mail=Roll[0]+"@iiitu.ac.in"
        msg="Dear "+ Roll[1]+", your attendence has been marked present  on "+MySql.today+", at time: "+time_stamp+" IST."
        MS.send_email(body=msg,to_email=mail)
        thread = threading.Thread(target=MS.send_email(body=msg,to_email=mail))
        thread.start()
        SC.update = True
        Date += [date_string]
        time += [dt_string]
        name_list += [name]


def match(dist):
    return dist <= 0.5
def encode_img(images):
    encode_list = []
    face_loc_list = []
    for img in images:
        face_locations = fr.face_locations(img)
        face_location = face_locations[0] if face_locations else None
        if face_location:
            encoded_face_img = fr.face_encodings(img, [face_location])[0]
            encode_list.append(encoded_face_img)
            face_loc_list.append(face_location)

    return encode_list, face_loc_list

def camere():
    # Using the camera to capture video
    video_cap = cv2.VideoCapture(0)

    while True:
        success, frame = video_cap.read()
        frame_resized = imres(100, frame)
        face_loc_frame = fr.face_locations(frame_resized)
        img_cam = fr.face_encodings(frame_resized, face_loc_frame)

        for encoded_img_test, loc in zip(img_cam, face_loc_frame):
            face_dist = fr.face_distance(encoded_img_data, encoded_img_test)
            min_val = np.min(face_dist)
            min_idx = np.argmin(face_dist)  # returns index of minimum

            if match(min_val):
                name = names[min_idx]
                # print(name)
                mark_attendance(name)

                y1, x2, y2, x1 = loc
                cv2.rectangle(frame_resized, (x1, y1), (x2, y2), (0, 255, 255), 2)
                cv2.rectangle(frame_resized, (x1, y2 - 20), (x2, y2), (0, 255, 255), cv2.FILLED)
                cv2.putText(frame_resized, name.capitalize(), (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255),
                            2)
        cv2.imshow("Video Live", frame_resized)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break

def filething():
    fl = open(filename, 'w')
    c = csv.reader(fl, delimiter=",")
    for a in range(len(name_list)):
        fl.writelines(f'{name_list[a]},{Date[a]},{time[a]},\n')
    fl.close()

# data feild to be entered live
name_list = []
Date = []
time = []

filename='DATA/'+MySql.today+"_Attendance.csv"
fl = open(filename, 'w+')
c = csv.reader(fl, delimiter=",")
for data in c:
    if (len(data) >= 3):
        name_list += [data[0]]
        time += [data[2]]
        Date += [data[1]]

fl.close()
print("Name Reading Done \n")

path = 'Images'
images = []
names = []
dir_list = os.listdir(path)

for file in dir_list:
    current_img = imres(15, cv2.imread(f'{path}/{file}'))
    images.append(current_img)
    names.append(file.split('.')[0])

encoded_img_data, face_loc_data = encode_img(images)
print("Encoding Done:")
Database_Name_Updation(names)

if __name__=='__main__':
    camere()
    thread2 = threading.Thread(target=camere())
    thread2.start()
    filething()



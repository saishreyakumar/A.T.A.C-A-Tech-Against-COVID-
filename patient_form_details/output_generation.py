import numpy as np

import tensorflow.keras

from PIL import Image, ImageOps
from flask import session
from tensorflow.keras.preprocessing.image import load_img


class OutputGeneration:
    def __init__(self, dbconnection):
        self.con = dbconnection
        self.unique = None
        self.temp = None
        self.oxy = None
        self.fvc = None
        self.fec = None
        self.img = None
        session['self.output_vals'] = []

    def get_data_from_medical_details(self):
        cur = self.con.cursor()
        rows = cur.execute(
            "SELECT unique_code,temp, oxymeter, spiro_fec,spiro_fvc FROM medical_details WHERE unique_code = ?",
            (session['unique'],),
        ).fetchone()
        print(rows)
        print(session['unique'])
        # self.output_vals[0] = session['unique']
        self.unique = rows[0]
        self.temp = rows[1]
        self.oxy = rows[2]
        self.fec = rows[3]
        self.fvc = rows[4]
        # self.img = None
        print(self.fvc)

        self.temp_check()
        self.oxy_check()
        self.spiro_check()
        self.get_from_xray()
        path_of_retrieved_image = self.read_blob_data()
        print(path_of_retrieved_image)
        # self.xray_check(path_of_retrieved_image)
        self.calling_keras(path_of_retrieved_image)
        # print(session['self.output_vals'][0])

        self.put_output_into_db()

    def put_output_into_db(self):
        cur = self.con.cursor()
        # data = cur.fetchall()
        # print(data)
        cur.execute(
            "INSERT INTO output (unique_code,temp_output,oxy_output,spiro_output,xray_output)VALUES (?,?,?,?,?)",
            (
                self.unique, session['self.output_vals'][0], session['self.output_vals'][1],
                session['self.output_vals'][2],
                session['self.output_vals'][3]
            ))
        self.con.commit()
        print("record added")

    def get_from_xray(self):
        cur = self.con.cursor()
        row = cur.execute(
            "SELECT x_ray_img from x_ray WHERE unique_code = ?",
            (session['unique'],),
        ).fetchone()
        print(row)
        print(session['unique'])
        # self.output_vals[0] = session['unique']
        self.img = row[0]
        print(self.img)

    def temp_check(self):
        if int(self.temp) > 98:
            session['self.output_vals'].append(1)
            print(1)
        else:
            session['self.output_vals'].append(0)
            print(0)

    def oxy_check(self):
        if self.oxy <= 95:
            session['self.output_vals'].append(1)
            print(1)
        else:
            session['self.output_vals'].append(0)
            print(0)

    def spiro_check(self):
        ratio = self.fec / self.fvc

        percentage = ratio * 100
        percentage = float(percentage)

        if percentage >= 70.0:
            session['self.output_vals'].append(0)
            print(0)
        elif percentage >= 60.0 and percentage <= 69.0:
            session['self.output_vals'].append(1)
            print(1)
        elif percentage >= 50.0 and percentage <= 59.0:
            session['self.output_vals'].append(2)

            print(2)
        else:
            session['self.output_vals'].append(3)
            print(3)

    def write_to_file(self, img_bin, filename):
        # Convert binary data to proper format and write it on Hard Disk
        with open(filename, 'wb') as file:
            file.write(img_bin)
        print("Stored blob data into: ", filename, "\n")

    def read_blob_data(self):
        session['photo_path'] = "C:/Users/yaswanthi/Documents/Github/A.T.A.C/xray_images\\" + session['unique'] + ".jpeg"

        self.write_to_file(self.img, session['photo_path'])

        return session['photo_path']

    def calling_keras(self, path_of_retrieved_image):
        # self.new_keras_model()
        np.set_printoptions(suppress=True)
        model = tensorflow.keras.models.load_model('C:/Users/yaswanthi/Documents/Github/A.T.A.C/keras_model.h5')
        # model.compile()
        img = load_img(path_of_retrieved_image)
        size = (224, 224)
        img = ImageOps.fit(img, size, Image.ANTIALIAS)  # resizing the image
        img_array = np.asarray(img)
        img_array = img_array.reshape(1, 224, 224, 3)
        img_array = img_array.astype('float32')
        # size = (64, 64)

        img_array = img_array - [123.68, 116.779, 103.939]
        img.show()
        # prediction = model.predict(img_array)
        print(model)
        result = model.predict(img_array)
        print(result)
        single_array_output = (result[0])
        if single_array_output[0] > 0.5:
            session['self.output_vals'].append(0)
            print(0)
        elif single_array_output[1] > 0.5:
            session['self.output_vals'].append(1)
            print(1)

from flask import request, session
import os

class XrayDetails:

    def __init__(self, dbconnection):
        self.con = dbconnection
        self.chestxray = None



    def xray_input(self,unique_code,app_root):
        self.chestxray = request.files.get('chestxray')
        self.unique_code = unique_code
        self.upload1(unique_code,app_root)

    def upload1(self,unique_code,app_root):
        target = os.path.join(app_root, 'images')
        if not os.path.isdir(target):
            os.mkdir(target)
        for fil in request.files.getlist("file"):
            # print(fil)
            # print("fil")
            self.filename = unique_code + ".jpeg"  # fil.filename
            self.destination = '/'.join([target, self.filename])
            print(self.destination)
            fil.save(self.destination)
            self.convertToBinaryData(self.destination)

    def convertToBinaryData(self,destination):
        # Convert digital data to binary format
        with open(destination, 'rb') as file:
            self.blobData = file.read()
        # return blobData
        self.session_for_xray_input(self.blobData)

    def session_for_xray_input(self,blobData):
        session['listOfVariable'] = {}
        session['listOfVariable'].update(
            {'chestxray': blobData})
        session.modified = True
        list_var = {}
        list_var.update(session['listOfVariable'])
        self.inserting_into_database_xray_details(list_var)

    def inserting_into_database_xray_details(self, list_var):
        cur = self.con.cursor()



        cur.execute("INSERT INTO x_ray (unique_code,x_ray_img)VALUES (?,?)",(session['unique'],list_var['chestxray'],))




        self.con.commit()
        print("record added ")

from flask import request, session

#from general_details_positive import GeneralDetailsPositive

class MedicalDetails:
    def __init__(self, dbconnection):
        self.con = dbconnection
        self.temp = None
        self.oxymeter = None
        self.spiro_fec = None
        self.spiro_fvc = None



    def medical_details_input(self):

        self.temp = request.form.get('temp')
        self.oxymeter = request.form.get('oxymeter')
        self.spiro_fec = request.form.get('spiro_fec')
        self.spiro_fvc = request.form.get('spiro_fvc')

        self.session_for_medical_details()

    def session_for_medical_details(self):
        session['listOfVariable'] = {}
        session['listOfVariable'].update(
            {'temp': self.temp, 'oxymeter': self.oxymeter, 'spiro_fec': self.spiro_fec, 'spiro_fvc': self.spiro_fvc})

        session.modified = True
        list_var = {}
        list_var.update(session['listOfVariable'])
        self.inserting_into_database_medical_details(list_var)



    def inserting_into_database_medical_details(self, list_var):
        cur = self.con.cursor()

        cur.execute(
                "INSERT INTO medical_details (unique_code,temp,oxymeter,spiro_fec,spiro_fvc)VALUES (?,?,?,?,?)",
                (session['unique'],list_var['temp'], list_var['oxymeter'], list_var['spiro_fec'],
                 list_var['spiro_fvc']
                 ))
        self.con.commit()
        print("record added ")
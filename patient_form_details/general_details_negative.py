from flask import request, session


class GeneralDetailsNegative:
    def __init__(self, dbconnection):
        self.con = dbconnection
        self.name = None
        self.age = None
        self.gender = None
        self.phno = None
        self.address = None
        self.adhaar = None
        self.negative_code = None

    def general_details_negative_input(self, Negative_code):

        self.name = request.form.get('name')
        self.age = request.form.get('age')
        self.gender = request.form.get('gender')
        self.phno = request.form.get('phno')
        self.address = request.form.get('address')
        self.adhaar = request.form.get('adhaar')
        self.negative_code = Negative_code
        self.session_for_general_details_negative(self.negative_code)

    def session_for_general_details_negative(self, negative_code):
        session['listOfVariable'] = {}
        session['listOfVariable'].update(
            {'unique_code': negative_code, 'name': self.name, 'age': self.age, 'gender': self.gender, 'phno': self.phno,
             'address': self.address, 'adhaar': self.adhaar})

        session.modified = True
        list_var = {}
        list_var.update(session['listOfVariable'])
        self.inserting_into_database_general_details_negative(list_var)

    def inserting_into_database_general_details_negative(self, list_var):
        cur = self.con.cursor()

        cur.execute(
                "INSERT INTO general_details (unique_code,name,age,gender,phno,address,adhaar)VALUES (?,?,?,?,?,?,?)",
                (list_var['unique_code'], list_var['name'], list_var['age'], list_var['gender'],
                 list_var['phno'], list_var['address'], list_var['adhaar']
                 ))
        self.con.commit()

        session['data'] = cur.lastrowid
        session['last_key'] = session['data']
        str_data = str(session['data'])
        print(session['data'])

        var = cur.execute("SELECT unique_code FROM general_details WHERE ID = ?", (str_data,))
        for row in cur.fetchone():
            session['unique'] = row

        print(var)
        self.con.commit()
        print("record added ")
        return session['unique']

        # data = cur.lastrowid
        # session['last_key'] = data
        # print(data)
        # self.con.commit()
        # print("record added ")

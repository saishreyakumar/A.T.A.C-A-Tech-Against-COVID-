from flask import request, session


class GeneralDetailsPositive:
    def __init__(self, dbconnection):
        self.con = dbconnection
        self.name = None
        self.age = None
        self.gender = None
        self.phno = None
        self.address = None
        self.adhaar = None
        self.positive_code = None

    def general_details_positive_input(self, positive_code):

        self.name = request.form.get('name')
        self.age = request.form.get('age')
        self.gender = request.form.get('gender')
        self.phno = request.form.get('phno')
        self.address = request.form.get('address')
        self.adhaar = request.form.get('adhaar')
        self.positive_code = positive_code
        self.session_for_general_details_positive(self.positive_code)
        return session['unique']

    def session_for_general_details_positive(self, positive_code):
        session['listOfVariable'] = {}
        session['listOfVariable'].update(
            {'unique_code': positive_code, 'name': self.name, 'age': self.age, 'gender': self.gender, 'phno': self.phno,
             'address': self.address, 'adhaar': self.adhaar})

        session.modified = True
        list_var = {}
        list_var.update(session['listOfVariable'])
        self.inserting_into_database_general_details_positive(list_var)

    def inserting_into_database_general_details_positive(self, list_var):
        cur = self.con.cursor()
        # data = cur.fetchall()
        # print(data)
        cur.execute(
                "INSERT INTO general_details (unique_code,name,age,gender,phno,address,adhaar)VALUES (?,?,?,?,?,?,?)",
                (list_var['unique_code'], list_var['name'], list_var['age'], list_var['gender'],
                 list_var['phno'], list_var['address'], list_var['adhaar']
                 ))
        self.con.commit()
        # print (cur.)
        # last_id = cur.fetchone()
        # print(last_id)
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

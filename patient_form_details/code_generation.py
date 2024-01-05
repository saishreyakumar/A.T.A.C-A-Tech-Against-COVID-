import random
import string

class CodeGeneration:

    def __init__(self):
        # self.con = dbconnection
        # self.request = request
        # self.mail = mail
        self.a = None
        self.b = None
        self.d = None
        self.unique_code = None

    def ran_gen(self, size, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for x in range(size))

    def positive_code(self):
        self.a = self.ran_gen(6, "13456789AXCNMLERTSJHERTFGBVEKIASDDYYZZWJHGFREWSDFVBMJ5679SQJH")
        self.b = "COV19"
        self.d = "20P"
        self.unique_code = self.b + self.a + self.d
        return self.unique_code

    def negative_code(self):
        self.a = self.ran_gen(6, "13456789AXCNMLERTSEKIASDDYYZZWJJIRTHDCMSHGFREWSDFVBMJ5679SQJH")
        self.b = "COV19"
        self.d = "20N"
        self.unique_code = self.b + self.a + self.d


        return self.unique_code

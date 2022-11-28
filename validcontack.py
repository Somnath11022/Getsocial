import re

class checkcontact():
    def __init__(self):
        number = input('Enter contact number  :  ')
        self.number = number
    def validnumber(self):
        vn = re.findall('[+|1]?[ |(|-]?\d{3}[ |.|)|-]?[-]?[ |-|.]?\d{3}[ |.|(|-]?\d{4}', self.number)
       
        for i in vn:
            if self.number == vn[0]:
                print('Number is valid')
            else:
                print('Number is not valid')
        
check= checkcontact()

check.validnumber()
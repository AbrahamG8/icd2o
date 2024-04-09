name = {'lastname':'Harvey', 'firstname':'Steve'}
# student = {'name':name, 'phone': '416-555-1212', 'student_no':'1126804'}

address = {'street' :'123 Monkey street', 'city':'Houston','Province' : 'Yuk', 'Postal' :'90210'}
# print(address['street'])
# print(address['city'])
# print(address['street'], {address['Postal']})

student = {'name':name, 'phone': '416-555-1212', 'student_no':'1126804', 'address' : address}
print(student['name']['lastname'])
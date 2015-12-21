import json

data = '''{
    "name":"Consta",
    "telefono":{
        "type":"intl",
        "numero":"0112123343"
        },
    "email":{"nascondi":"si"},
    "anni":"3"
}'''

info = json.loads(data)
# print info
print "Name: ", info["name"]
print "Numero Telefono: ", info["telefono"]["numero"]
print "Email: ", info["email"]["nascondi"]
print "Eta': ", info["anni"]

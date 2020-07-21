
# Как вывести на экран номер мобильного телефона в приведённом выше JSON

a = {
    "firstName":"Иван",
    "lastName":"Иванов",
    "isAlive":True,
    "age":32,
    "adress":{
        "streetAddress":"Нейбута 32",
        "city":"Владивосток",
        "state":"",
        "PostalCode":""
    },
    "phoneNumbers":[
        {
            "type":"mob",
            "number":"123-333-4455"
        },
        {
            "type":"office",
            "number":"123 111-4567"
        }
    ],
    "children":[],
    "spouse":None
}

print('Номер:', a['phoneNumbers'][0]['number'])
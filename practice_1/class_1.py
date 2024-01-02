events = [
    {"date":"10/05/2023",
     "name":"Ivan",
     "age":17},

    {"date":"01/08/2020",
     "name":"Maria",
     "age":25},

    {"date":"18/06/1988",
     "name":"Petr",
     "age":40}
]

class Event:
    def __init__(self, date="01/01/2000", name="", age=""):
        self.date = date
        self.name = name
        self.age = age

    def ini_from_dict(self, dict):
        self.date = dict.get("date")
        self.name = dict.get("name")
        self.age = dict.get("age")

for event in events:
    object = Event()
    object.ini_from_dict(event)
    print(object.date)
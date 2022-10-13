class Cat:
    def __init__(self, name="", age="", gender=""):
        self.name = name
        self.age = age
        self.gender = gender
    def init_from_dict(self, event_dict):
        self.name = event_dict.get("name")
        self.gender = event_dict.get("gender")
        self.age = event_dict.get("age")
    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    def getGender(self):
        return self.gender
    def display(self):
        print(self.gender,self.age,self.name)

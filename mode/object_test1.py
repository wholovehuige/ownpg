class Person(object):
    def __init__(self,name,gender,age,**kwargs):
        self.name = name
        self.gender = gender
        self.age = age
        for k,v in kwargs.items():
            setattr(self,k,v)

xiaoming = Person("Xiao Ming","Male","18",job="Student")

print(xiaoming.age)
print(xiaoming.job)
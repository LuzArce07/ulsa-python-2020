from User import User
import csv

print("Hello World")

name = 'Nombre'
print(name)

#variable2 = variable1 + num(esto da erros no puedes sumar string con int, solo strings)

number1 = 10
print(number1)

#el tap es importante para que sepa que es lo que tiene el if dentro
if 4 < 2: 
    print("is minor")
else:  
    print("is not minor")

vector1 = ["joel", "eliud", "ana", "ana c", "pancho", "karen", "pablo", "yo"]

print(vector1)
print(vector1[3])

movies = ["the warrios", "amores perros", "the simpson", "balto", "soy leyenda", "toy story"]

for m in movies:
    m = m + "(clasificación: B-15)"
    print(m)


#Las funciones no necesitan self en su argumento
def showName():
    print('Nombre perron: Luz')

user1 = User("Usuario", 22, "algo@gmail.com")
print(user1.name)
user1.getInfo()

showName()


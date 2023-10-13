import json

lst = list(range(5))
tp = (1.2, 221, 604, 'Mahesh', [2, 556])
dct = {'name': 'Ganesh', 'age': 25, 'gender': "Male"}
a = json.dumps(lst)
print('This is a tuple:', json.dumps(tp), type(json.dumps(tp)))
print('This is a dict:', json.dumps(dct), type(json.dumps(dct)))
print('This is a int:', json.dumps(11), type(json.dumps(11)))
print('This is a string:', json.dumps("Hello"), type(json.dumps("Hello")))
print('This is a string:', json.dumps("Hello"), type(json.dumps("Hello")))
print('This is a Bool:', json.dumps(True), type(json.dumps(True)))
print(json.dumps(False), type(json.dumps(False)))
print(a, type(a))
print(lst)
d = json.dumps(lst)
# This will convert into json string
print(d, type(d))
org = json.loads(d)
print(org, type(org))

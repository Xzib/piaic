import json

student = {
    'Name': 'Zohaib',
    'Age': '42',
    'Class': 'AI'
}

# with open("myJson.json","w") as fd:
#     json.dump(student,fd)
try:
    print(10/0)
    with open("myJson.json","r") as fd:
        student = json.load(fd)
        
        print(student)
except FileNotFoundError:
    print("file does not exist")
except:
    print("an unknkown ")


#create a dictionary to translate alein language into english,
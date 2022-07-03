import json
def greet_user():
    try :
        with open('favoritenumber.json','r') as f:
            number = json.load(f)
        print(f"I know your favorite number! It's {number} ")
    except:
        number = int(input("Enter your favorite number: "))
        with open('favoritenumber.json','w') as f:
            json.dump(number,f)
        print("We'll remember your favorite number!!!")

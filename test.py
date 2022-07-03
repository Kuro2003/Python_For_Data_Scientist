import json
def get_stored_information():
    try:
        with open('username.json','r') as f:
            username = json.load(f)
    except:
        return None
    else:
        return username

def get_new_information():
    username = input("Enter your name: ")
    with open("username.json",'w') as f:
        json.dump(username,f)
    return username

def greet_user():
    username = get_stored_information()
    if username :
        print(f'Welcome back,{username}')
    else:
        username = get_new_information()
        print("we'll remember you when you come back, {}".format(username))
greet_user()
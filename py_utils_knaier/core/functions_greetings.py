def greet_user(username, suffix="", age=None, attributes={}):
    if suffix:
        print("We have a suffix entered! (Non empty strings evaluate to True)")

    print(f"Greetings {username} {suffix}")
    userInfo = {"username": username, "suffix": suffix}

    for key, value in attributes.items():
        userInfo[key] = value

    if age:
        userInfo["age"] = age

    return userInfo

# *
def additional_greetings(userInfo, *greetings):
    """ * indicates a variable number of parameter arguments """
    for greeting in greetings:
        print(f"greetings from {greeting} {userInfo}")

# ** 
def additional_args(userInfo, **kwargs):
    """ ** indicates a keyword arguments type key=value dict passed in"""
    for key, value in kwargs.items():
        userInfo[key] = value
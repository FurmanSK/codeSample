import re

# Class User
class User():
    
    Name = "John Doe"                # Default name is John Doe starting out
    email = "name@something.com"     # email address of user
    Nickname = "Slick"               # Nickname of user


    # constructor of the Character object.
    def __init__(self, name, email, nickname):
        self.Name = name
        self.email = email
        self.Nickname = nickname

    # Getter Methods
    def getName(self):
        return self.Name
    
    def getEmail(self):
        return self.email

    def getNickname(self):
        return self.Nickname

    # Setter Methods

    def setName(self, name):
        if( input("Do you really want to change your name Y/n?") == "Y"):
            self.Name = name
        else:
            print("Ok we won't change your name then")
    
    # Converts object to be stored as JSON format in text
    def toJson(self):
        return "{{Name:{0}, email:{1}, Nickname:{2} }}".format(self.Name, self.email, self.Nickname)

def importUsers():
    """Imports User List from disk

    Looks for savedUsers.txt file and creates a list of Class objects

    Returns a list of User class objects"""
    with open("savedUsers.txt", "r") as fp:
        Users = []
        for line in fp:
            #expload string on comma
            lineArray = line.split(",")
            #Split each var up
            name = lineArray[0].split(":")[1]
            email = lineArray[1].split(":")[1]
            nickname = lineArray[2].split(":")[1].strip(" }")
            # clean up end of nickname string
            nickname = nickname.strip(" }\n")
            Users.append(User(name, email, nickname))
    return Users

def checkEmail(email):
    """Checks if the user input a valid email address.

    Takes in a string and uses regex to make sure it is a valid email.
    
    Returns boolean True/False"""

    isValid = re.search('^\w+@\w+.\w+$', email)
    if isValid:
        return True
    else:
        return False

def createUser():
    """Creates new user prompting for values.

    Takes in nothing and returns a new User class.
    """

    print("--------------Creating User--------------")
    
    name = input("Enter a name:")

    # Loop until they enter a valid email then store and go onto the next index
    while(True):
        email = input("Enter a valid email. something@yeah.com: ")
        if(not checkEmail(email)):
            print("You didn't enter a correct type of email")
            continue
        else:
            break

    nickname = input("Enter a nickname:")

    usr = User(name, email, nickname)

    return usr
import random

print("This is a password generator.\n")
size = 0

chars = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnÑñOoPpQqRrSsTtUuVvWwXxYyZz1234567890!#$%&/()=?¡¨´+[],.-;:_*+"

def generator():
    size = int(input("Pick the length of your password. (a 10+ size is recomended)\n"))
    pwd = ""
    for i in range(size):
        pwd += random.choice(chars)
    return pwd

print("Your password is:"+generator(),"\n")


while True:
    again = input("Do you want to create another password? Y/N\n")
    if again.upper() == "Y":
        print("Your password is:"+generator(),"\n")
    if again.upper() == "N":
        print("Bye!")
        break




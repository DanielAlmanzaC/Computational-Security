message = input("Write your message\n")

original = "abcdefghijklmnopqrstuvwxyz"
key = "ZYXVUTSRQPONMLKJIHGFEDCBA"
encrypted = ""

for i in message.lower():
    if(i in original):
        encrypted += key[original.index(i)]

print("Tu mensaje ha sido cifrado: "+encrypted)

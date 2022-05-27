import string
import random
alphabet_string = string.ascii_letters
alphabet_list = list(alphabet_string)


alphabet_list = alphabet_list + \
    list(range(0, 10)) + ["@", "#", "%", "&", "*", "_", "/", "-", "+"]
# print(alphabet_list)
l = int(input("Enter number of characters you want in password: "))
pswd = ""
for i in range(0, l):
    j = random.randint(0, 70)
    pswd = pswd + alphabet_list[j]
print(pswd)

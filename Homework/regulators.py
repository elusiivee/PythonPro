import re
#1


txt = "We are looking Rbbbbr in asdadasdRbbbbrasdasw"
x = re.findall("([rR]b+[rR])", txt)

print(x)



#2


cart = "My credit-cart: 4324-1534-1246-7965"
y = re.findall("([0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{4})", cart)

print(y)


#3
email=input('input your email')

check = re.findall("^[^\s@]+@[^\s@]+\.[^\s@]+$", email)
if check:
    print("Email is correct: ", check)
else:
    print("Email isn`t correct")

#4

nickname=input('input your nickname')

check_nick = re.findall("^[a-zA-Z0-9]{2,10}$", nickname)
if check_nick:
    print("Nickname is correct: ", check_nick)
else:
    print("Nickname isn`t correct")
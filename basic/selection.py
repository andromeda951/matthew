
password = "rahasia"

if password == "rahasia":
    print("Selamat datang")
    

x = 8
if x % 2 == 0:
    print("genap")
    print("genap")
    print("genap")
else:
    print("ganjil")
    print("ganjil")
    print("ganjil")

print("Andromeda")


x = int(input())
if x > 0:
    print("positif")
    print("positif")
elif x < 0:
    print("negatif")
    print("negatif")
else:
    print("nol")
    print("nol")

# > < >= <= == !=

# logic operator
# not and or

# True and True = True
# True and False = False
# False and True = False
# False and False = False

# True or True = True
# True or False = True
# False or True = True
# False or False = False

# not True = False
# not False = True


#  = True or False and False 
#  = True or False
#  = True

#  = (True or False) and False 
#  = True and False 
#  = False 

x = 7
if x > 0 and x % 2 == 0:
    print("genap positif")
elif x < 0 and x % 2 == 0:
    print("genap negatif")
elif x > 0 and x % 2 == 1:
    print("ganjil positif")
elif x < 0 and x % 2 == 1:
    print("ganjil negatif")
else:
    print("nol")
    
# nested if
x = 0
if x > 0:
    if x % 2 == 0:
        print("genap positif")
    else:
        print("ganjil positif")
elif x < 0:
    if x % 2 == 0:
        print("genap negatif")
    else:
        print("ganjil negatif")
else:
    print("nol")
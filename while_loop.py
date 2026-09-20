i=0
while i<5:
    print("hello")
    i += 1

# i=0   0<5 true   print hello     i=1
# i=1   1<5 true   print hello     i=2
# i=2   2<5 true   print hello      i=3
# i=3   3<5 true   print hello      i=4
# i=4   4<5 true    print hello     i=5
# i=5   5<5 false


i=3
while i<=10:
    print(i)
    i += 1



i=0
total = 0
while i<5:
    total = total + i
    i += 1
print(total)

# 0+1+2+3+4
# i=0   0<5 true   total=0+0=0     i=1
# i=1   1<5 true   total=0+1=1     i=2
# i=2   2<5 true   total=1+2=3      i=3
# i=3   3<5 true   total=3+3=6      i=4
# i=4   4<5 true   total=6+4=10     i=5
# i=5   5<5 false



x = int(input())
while x != 0:
    print(f"X = {x}")
    x = int(input())
    
    
x = 1
while x != 0:
    x = int(input())
    print(f"X = {x}")

    

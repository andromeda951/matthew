for i in range(5):
    print("hello")
    print("test")

# i=0   print hello print test
# i=1   print hello print test
# i=2   print hello print test
# i=3   print hello print test
# i=4   print hello print test

for i in range(5):
    print(i)
# i=0   print 0
# i=1   print 1
# i=2   print 2
# i=3   print 3
# i=4   print 4

# total=0+1+2+3+4=10
total = 0
for i in range(5):
    total = total + i
print(total)
print(total/5)

# i=0   total=0+0=0
# i=1   total=0+1=1
# i=2   total=1+2=3
# i=3   total=3+3=6
# i=4   total=6+4=10

total = 0
for i in range(5):
    x = int(input())
    total = total + x
print(total)


# range(end)
# range(start, end)
# range(start, end, step)
for i in range(2, 10, 3):
    print(i)
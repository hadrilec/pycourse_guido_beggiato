x = 3
y = 5
z = 7


if x > 9:
    print("x is greater than 9")
elif x == 9:
    print("x is 9")
else:
    print("x is less than 9")
print("------------------")


if x==3 and y==4:
    print("case 1")
elif x==4 or y==5:
    print("case 2")
print("------------------")


if not x%2==0:
    print("x is odd")
print("------------------")
if x%2:
    print("x is odd")
print("------------------")


for i in range(y):
    print(i)
print("------------------")


i = 0
while i < x:
    print(i)
    i += 1 
print("------------------")


from time import sleep # ignore this for the moment
while True:
    print("CTRL + C to interrupt infinite loop !")
    sleep(.7)

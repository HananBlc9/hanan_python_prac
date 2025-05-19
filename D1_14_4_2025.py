for i in range(5):
    print("*****")

x = input("Enter an integer: ")
for i in range(int(x)*2):
    if i%2 == 1:
        print("*"*i)

y = int(input("Enter an integer: "))
q = y
for i in range(y*2):
    if i%2 == 1:
        print((" "*q)+"*"*i)
        q-=1

print("This is first day!")
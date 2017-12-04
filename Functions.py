#Functions - set of instructions. All the functions will start with the keyword def

def myAddFunction(a,b):
    result = a+b
    return result
#lets call this fuction
print(myAddFunction(1,2))


def fibo(n):
    a=0
    b=1
    for x in range(n):
        a=b
        b=a+b
        print(a)
    return b
num=int(input("enter a fibo no:")) #typecast is needed here
print(fibo(num))

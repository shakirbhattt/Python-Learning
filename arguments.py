#arguments are used to pass the values

def greet(first , last):
    print (f"Hi {first}")
    print ("welcome")
    
greet("shakir" , "bhat")


# keyword arguments to make code more readable
def increment (number , by):
    return number + by 


print (increment(2, by=1))


#   default arguments to put default arguments or optional parameter

def increment (number , by=1):
    return number + by 


print (increment(2))


#xargs is a colection of arguments , pass commandline args to a script


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total

print(multiply(2,3,4,5))

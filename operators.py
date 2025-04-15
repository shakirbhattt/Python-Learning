#comparsion operators to compare values
10 > 3 #greater
10 < 3 #less
10 == 10 # equal
10 != 10 # not equal 
"bag" > "apple" # we can use strings also to compare , it will work on numerical represation in programming
#to check numeric represantatiomn
ord(b) # it will give you a order i.e 98 for 



#logical operators to model complex conditions 3 : and , or , not

#and
high_income = True
good_credit = True

if high_income and good_credit:
    print("eligible")
else:
    print("not eligible")
    
#or
high_income = False
good_credit = True

if high_income or good_credit:
    print("eligible")
else:
    print("not eligible")
    
#not
high_income = False
good_credit = True
student = False

if not student:
    print("eligible")
else:
    print("not eligible")

# we can put all 3 in one program to model more complex conditions 
high_income = False
good_credit = True
student = False

if (high_income or good_credit) and not student:
    print("eligible")
else:
    print("not eligible")
    
# short circuit evaluation is evaualtion stops as soon as we get the value, if this false rest all false deoesnt matter
# in python logical operats are short circuit


#chaining comparison operators to make comparison clean and easy
age = 32
if 18 <= age < 65:
    print("eligible")
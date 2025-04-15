x = 1 #integers
x = 1.2 #float ie decimal
x = 1 + 2j  # complex numbers a +bi


#arithmetic operations
print(1+2) #addition
print(1-2) #sub
print(1*2) #multiplication
print(1/2) #div , there are 2 types of divisiom, one normal full value which can give float and other integer only
print(1//2) # intgeerr only //
print(1%2) # modulas i.e remainder
print(1**2) # exponent ie power e.g 1 is to power 2


#augmented arithemetic operation for increment decremnet etc
x = 10
x += 3 # to add 3


#working with numbers , use functions and for more you modules like math module for math work
import math
print(round(2.9)) #givs round number close
print(abs(2.9)) # gives absolutley no
math.sin # math module with bunch of fns
#module is a file containing python definations and statements

#type conversion
# int(x)    float(x)    bool()    #str()
#to check type of class type(x)
x = input("x:")
y = int(x) + 1
print(f"x:{x}, y:{y}")


#specila for boolean few used will be always false i.e 0 , emplty string "" , Falsy and None
bool(0) 
bool(None)
bool("")
bool(Falsy)
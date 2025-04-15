# loops to repeat a tas no of times

#forloops repeat attempt 3 times with count numberx, for this do that
for number in range(3):
    print("attempt" , number + 1 , (number + 1 ) * ".") #print attempt with sequence and . multiple
    
    
#for else , for this do that else that 

success = False
for number in range(3):
    print("attempt")
    if success:
        print("successss")
        break # break statement is used to break the loop
else:
    print("failed")


#nested loop to put one loop into another loop

for x in range(5):   #outer loop
    for y in range(3):   #inner loop
        print(f"({x} , {y})")
#it will print all sequence from 0,0 till whatever possible
#inner loop will get executed and theb outer loop


#iterbales ti returb members one a a time allowing you to loop through its elemnents
for x in range(5):  #range is an iterable , string is also an iterable
#for x in [1,2,4]:   #list is also an iterable
    print(x)
    
#while loops to repeat as long as condition is true
number = 100
while number > 0:
    print(number)
    number // 2
    
#infinite loops which runs forever
while True:
    command = input(">")
    print ("ECHO" , command)
    if command.lower() == "quit":
        break
    
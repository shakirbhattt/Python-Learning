#conditional statemnets to make decisions
#if elif else statemnet i.e if this do that elif do that else do that
temp = 15 
if temp > 30:  # if statement to put statement
    print("its warm")
elif temp > 20: # elif if if is not true
    print("its good")
else:          # else if none of the above is true , do this
    print("its cold")

    
#insted of print everytime, use ternary operator to make code look clean, simple and short
age = 20
message = "eligible" if age >= 18 else "not eligible"
print("message")
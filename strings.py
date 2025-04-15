course = "abc"  
#functions is a resusable code , there are bunch of builtin functions used e.g below
print(len(course)) # len() to print length of string
print(course[0]) # [] to print the specific element
print(course[0:3]) # to print 3 letters
print(course[0:]) #print all
print(course[:3]) #print all
print(course[:]) #print all
#ingenral everythingf in programming is considered as object and if you put . dot after object it will give you a list of all builtin functions
print(course.capitalize) #e.g builtin fns
#more examples of functions
print(course.upper()) #uppercase letters
print(course.lower()) # lowercase letters
print(course.title()) #title
print(course.strip()) #strip to trim any whitespace from both beigining and end other leftstrip, rigghtstrip to remove left an right space respectively
print(course.find(a)) # to find index
print("pro" in course) # to check expresiion in variable in a boolean either yes no




#escape sequences
course = "abc \" shakir" # escape sequence \ to escape character after  "" error e.g if we need single quote inside a string 
course = "abc \' shakir" 
course = "abc \\ shakir" 
course = "abc \n shakir" 
#\' or \""  or \\ or \n single quote , double quote or backslash in a string or new line i.e \n




#formatted strings
first = "shakir"
last = "bhat"
full = f"{first} {last}"
# it will format the code whatver is inside curly and f with double quotes i.e you can put any valid expressions inbetween curly braces
print(full)

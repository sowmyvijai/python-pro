
#Write a Python function to find the Max of three numbers

def Max_number (n1,n2,n3):
    return max (n1,n2,n3)

Max_number (100,999,13)


#Write a Python program to reverse a string

def reverse_string (s):
    a=s[::-1]
    return (a)

reverse_string ("Hello")

#Write a Python function to check whether a number falls in a given range

def check_range (n1,n2,a):
        if n1<=a<=n2:
            print("The number falls in given range")
        else:
            print("The number doesn't falls in given range")

check_range (100,1000,2000)


#Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters

def number_upper_lower (s):
    u=0
    l=0
    for i in (s):
        if i.isupper():
            u+=1
        elif i.islower():
            l+=1
    print ("upper letters", u)
    print ("lower letters", l)
s=input("word")
number_upper_lower (s)

number_upper_lower ("Hi Welomehghk Y")

def Letter(s):
    c1,c2=0,0
    for i in s:
        if i.isupper():
            c1+=1
        elif i.islower():
            c2+=1
    print("Upper Case Letters:-",c1)
    print("Lower Case Letters:-",c2)
s=input("Enter Something:--")
Letter(s)



#Write a Python function that takes a list and returns a new list with unique elements

def unique_number(n):
    unique=[]
    for i in (n):
        if i not in unique:
            unique.append(i)
    return unique

unique_number ([1,1,2,3,4,2,2])

#Print multipication 12th table

def table (n1,n2):
    print(n2, "x 12 =", n1*n2)
    n2=n2+1
    if n2<=10:
        return table (n1,n2)
table (12,1)




#area of rectangle

def area_rectangle (l,b):
    return (l*b)

area_rectangle (10,4)


#parametre of rectangle

def parametre_rect (l,b):
    return (2*(l+b))

parametre_rect (10,4)


def power_number (a,b):
    return pow (a,b)

power_number (4,2)





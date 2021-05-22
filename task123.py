# check if the year is leap or not

x=int(input("Year to be checked: "))
if x%400==0:
    print("This is a leap year")
elif x%4==0 and x%100!=0:
    print("This is a leap year")
else:
    print("This is a non-leap year")


# given number is +ve or -ve or zero, check in posibble ways

# 1st way

x=int(input("number: "))
if x<=0:
    if x==0:
        print("zero")
    else:
        print("-ve number")
else:
    print("+ve number")

# 2nd way

x=int(input("number to be checked: "))
if x==0:
    print("zero")
if x>0:
    print("+ve")
if x<0:
    print("-ve")



# calculate the grade of 5 subjects

math=int(input("secured mark in math: "))
MIL=int(input("secured mark in MIL: "))
ENG=int(input("secured mark in ENG: "))
science=int(input("secured mark in science: "))
history=int(input("secured mark in history: "))
average=(math+MIL+ENG+science+history)/5
if average>=90 and average<=100:
    print("Grade is A+")
elif average>=80 and average<=89:
    print("Grade is A")
elif average>=70 and average<=79:
    print("Grade is B+")
elif average>=60 and average<=69:
    print("Grade is B ")
elif average>=50 and average<=59:
    print("Grade is C")
elif average>=40 and average<=49:
    print("Pass Only")
else:
    print("invalid marks/failed")
    
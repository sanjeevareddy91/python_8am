# Loopings or Iterations: Executing certain set of statements multiple no.of times..

# while loop(infinite loop)
# for loop

a=13

# if a>10:
#     print(a,'is greaterthan 10')

"""
while condition:
    statements
"""    

# while a>10:
#     print(a,'is greaterthan 10')
#     a = a-1


# for loop: It performing the iteration on sequences.. 

"""
for element in sequence:
    statements
"""

# str1 = input("Enter your string:")
# print(str1)

# for ele in str1: # python is programming language
#     print(ele,end=" ")

# list1 = ['naresh','suresh','mahesh','subash']

# for ele in list1:
#     print(ele)

# range() -- 

# print(range(50))

# for ele in range(50):
#     print(ele,end=" ")

# for ele in range(10,50):
#     print(ele,end=" ")

# for ele in range(10,50,3):
#     print(ele,end=" ")


# for ele in range(50,10,-1):
#     print(ele,end=" ")

# control flow statements

# break -- It will stop all the next iteration and will go directly outside of the loop..
# continue

list1 = ['venkat','suresh','ramesh','mahesh','mukesh','subash','pavan']

# for ele in list1:
#     if ele=='mahesh':
#         print(ele,"is found")
#         break
#     print(ele,"check failed")

# for ele in list1:
#     if ele=='mahesh':
#         print(ele,"is found")
#         break

# list1 = ['venkat','suresh','ramesh','mahesh','mukesh','subash','pavan']

# for ele in list1:
#     if ele=='mahesh':
#         continue
#         print("Hello")
#     print(ele,"your profile is shortlisted")

# Task1:

pin1 = 1234
account_type = 'current'
for ele in range(3):
    pin2 = int(input("Enter your pin:"))
    if pin2 == pin1:
        account_type1 = input("Enter account type:")
        if account_type1 == account_type:
            amount = input("ENter amount:")
            print(amount,"is debited form your account")
            break
        else:
            print("Account Type doesnot match")
    else:
        print("Pin incorrect")
    if ele == 2:
        print("Account Blocked!")
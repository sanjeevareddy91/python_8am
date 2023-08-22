# strings : Sequence of anything declared inside ' ' or " " or ''' ''' or """ """

# a="Python is a programming language"
# print(a)

# b='Python is a programming language'
# print(b)

# # c='''Python is a programming language
# # Django is a framework for python 
# # Django is used in webdevelopment'''
# # print(c)

# poem = 'Twinkle Twinkle Little" Star'

# print(poem)

slogan1 = "East or West Ballayya is the best"

# print(slogan1)

# Indexing :: Accessing inside the string is done using indexing.. 

# it is represented with [ ]. 
# indexing will start from 0.

# print(slogan1[0])

# print(slogan1[13])

# print(slogan1[50]) # This is an error as the index value is greaterthan length of string.

# print(slogan1[8:12])

# print(slogan1[4:16])

# print(slogan1[2:20:3])

# Negative Indexing:Performing the indexing with negative values.. 
    # negative indexing will start from -1. 

# slogan1 = "East or West Ballayya is the best"

# print(slogan1)

# print(slogan1[-1])

# print(slogan1[-10])

# print(slogan1[-13:-21:-1])

# print(len(slogan1))
# print(slogan1[-1:-(len(slogan1)+1):-1])

# print(slogan1[-1:-(len(slogan1)+1):-1])
# print(slogan1[-1:-(len(slogan1)+1):-2])


# Strings are immutable (Which doesnt allow us to make the chnages after the declaration).

# name = "ramesh"

# print(id(name))
# name[0] = 'R'

# name = 'R'+name[1:]

# print(name)
# 
# print(id(name))

# Concatenation(+)
# Repetition(*)

# print("Hello"+"world")

# print("Hello"*3)

# replace and format. 

# replace() -- Its for replacing a substring from the main string with someother string.. 

# dialogue = "Dont trouble the trouble if you trouble the trouble trouble troubles you i am not the trouble i am the truth."


# print(dialogue.replace('trouble','problem')) # this will replace all the occurence of trouble with problem inside the string.. 

# print(dialogue.replace('trouble','problem',3)) # this will replace first 3 occurence of trouble with problem inside the string.. 


# TASK - Replace the last occurence of trouble with problem inside the string.. 

# .format()

# {}
# .format()

"USE this OTP 847744 for your recent purchase at amazon.com with a worth of RS.534/-"

# str1 = "Use this OTP {} for your recent purchase at {} wiht a worth of RS.{}/-".format(848884,'amazon.com',5437)

# print(str1)

otp = input("Enter OTP:")
website = input("Enter Website:")
amount = input("Enter Amount:")

str1 = "Use this OTP {} for your recent purchase at {} with a worth of RS.{}/-".format(otp,website,amount)

print(str1)

str2 = "Use this OTP {} for your recent purchase at {} with a worth of RS.{}/-".format(website,amount,otp)

print(str2)

# f format syntax.

str3 = f'Use this OTP {otp} for your recent purchase at {website} with a worth of RS.{amount}/-'

print(str3)


# TASK2:

str1 = "Python programming language"

# enter your string : Python programming language
# enter your substring which you want to find : g
    # enter which occurence of g index you want: 3
        # 3rd occurence of g is at 19 index. 
    # G occurenced on 4 times, try with lesser occurence value:
# Substring G is not present in the main string.. 


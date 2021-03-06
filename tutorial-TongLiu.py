# Python from Zero.
# 
# This tutorial is intended for students without any programming background
#
# Author: Tong Liu, t.liu@unibo.it
# Date: Dec 11th 2018
# link: https://www.unibo.it/sitoweb/t.liu


# 1) Primitives in python 3
# ======

# a variable is an element that has a (arbitrary) name and a value.
# in Python a variable can be declared in two ways:

a = 10 # case 1, a simple statement
print("value of 'a':",a) 

for a in [1,2,3]: # case 2, a statement in a control flow
	print(a,end=",") 
print() # start a new line

# 'a' in both cases is the name of the variable.
# In the first case, 'a' takes the value 10.
# In the second case, 'a' takes the values from a list of numbers (1,2,3) in turn.
# ps: print(a,end=',') is used for printing the values of 'a' in one line.

# if you declare more variables, you can also use a Pythonic way which makes it more compact.
a,b,c,d = 2,0,1,8 # it is equivalent to say "a=2 b=0 c=1 d=8"
print('values of four variables:',a,b,c,d) #2 0 1 8

# When you introduce a variable, you should give it a value to make it meaningful,
# a variable value can be of the following types:

# # integer
a = 6 # a is an integer variable

# # float
a = 3.2 # a is a float variable 

# # string
a = 'Dear friends' # a is a string

# # boolean
a = True # a is a boolean
a = False 
# boolean is often used with the conditional keyword 'if'
# and they are often generated by verification statements:
# ==,!=, in, not in

# # list a.k.a. array
# list is a collection of 'meaningful' objects. 
# It facilitates you to execute some routine operations

a = [] # 'a' is an empty list, we also use this statement to erase a's elements.
a = [6,4,9] # 'a' is a list of numbers
a = [6,3.2,'hello',3] # the content of a list could be ANYTHING, 
a = [6,3.2,'hello',[3,1,0], a]  # even another list or a variable as long as it is meaningful
# a = [N] # this will give an error, because 'N' is not defined; it is not meaningful
print('value of a complex list:',a)

# List element is identified by an index; in Python, the index starts from 0.
print('read the first element of a ',a[0])
del a[1] # delete the second element of a
a[2] = 100 # change the third element to 100

# --- variable operators ----
# depending on the type of variable, the same operator may have different meanings.

a,b = 5,7.2
print('the meaning of + for integer and float',a,'+',b,'=',a+b)

a,b = 'hello ','my FRIEND'
print('the meaning of + for string variables',a,'+',b,'=',a+b)

a,b = True,False
print('the meaning of + for boolean variables',a,'+',b,'=',a+b)

a,b = [2,0,1],[8]
print('the meaning of + for lists',a,'+',b,'=',a+b)

# now you can check other operators, such as, -, %. /, and see what will happen!

# There are several fundamental list functions that you SHOULD know.

# 1 Get the length of a list
print('The length of ',a,'is',len(a))

# 2 Append an element to a list
a.append(10)

# 3 Concatenate two lists
a = a+b

# 4 Verify if an element is in a list
if 10 in a:
	print(10,'is inside',a)

# 5 Create a list of consecutive numbers
a = list(range(10)) # [0,1,2,3,4,5,6,7,8,9]
a = (list(range(2,10,2))) # [2, 4, 6, 8] create a list from 2 to 9 with a step of 2

# 6 Get element cardinality of a list
a = [2,2,0,0,0,1,8,8]
# print (set(a)) # {2,0,1,8}
b = [1,8,8] # difference of cardinality between two sets
print ('Card diff',set(a) - set(b)) # {2,0}

# --- conditional statement ----
# conditional statement instructs the computer to take proper action to handle different cases.

a,b = 2,0
if a < b:
	print (a,'is less than',b)
elif a==b:
	print (a,'equals to',b)
elif a==2 and b==2: # you can use the keyword 'and','or' to create more precise conditions.
	print ('a = b = 2')
else:
	print (a,'is bigger than',b)

# 2) Iterative Control Flows
# ======

# A computer is very good at doing the repetitive tasks, e.g., classifying a list of data;
# it checks each item and decides which group the item belongs to.
# If you are sure that some logic should be repeated to 
# each element of list, then you should use the control flow (CF).
# CF is a piece of logic that you call repeatedly, and it is controlled
# under some condition. A typical CF in Python is the statement "for _ in _:"
# where the logic segment can be applied to each element specified in the "for" statement.

# Example.
# You have a list of numbers, and you want to
# put the numbers which are less than 5 into the list A and others in the list B.

L = [8,5,3,8,1,6,3,0,6,3,2,7,1,3,9,6,4]
A = []
B = []

# you can address it easily with the CF 'for'
for num in L:
	if num < 5: A.append(num)
	else: B.append(num)

print(A,B) # [3, 1, 3, 0, 3, 2, 1, 3, 4] [8, 5, 8, 6, 6, 7, 9, 6]

# The logic segment here is 
#   if num < 5: A.append(num)
#   else: B.append(num)
# and this logic has been applied to each element of the list L.
# To visit the element of L we used the variable 'num' as a reference of the temporal 
# element that we are visiting.

# CF has the keywords, 'continue' and 'break', to make your logic more elaborated.
# For example, we only collect the numbers which are bigger than 5,
# and we stop when we encounter a 9.

A,B = [],[] # we erase the elements in A and B
for num in L:
	if num < 5:
		continue # skip the following instructions, and start with the next element of L
	elif num == 9:
		break # interrupt the CF, the remaining elements in L will not be visited
	B.append(num)
print(A,B) # [] [8, 5, 8, 6, 6, 7]

# Recall that L is a list, each element has an index and a value.
# one can access both of these information in a CF with the enumerate() function.
for idx,num in enumerate(L):
	print((idx,num),end=',') # (0, 8),(1, 5),(2, 3),(3, 8),(4, 1),(5, 6),(6, 3),(7, 0),(8, 6),(9, 3),(10, 2),(11, 7),(12, 1),(13, 3),(14, 9),(15, 6),(16, 4)

# 3) List Comprehension (LC)
# ======

# LC is a technique to generate a new list by elaborating 
# the elements of an existing list.
# 
# It has the following structure:
# new_list = [expression(i) for i in old_list if filter(i)]
# 
# This is equivalent to the following CF
# new_list = []
# for i in old_list:
#     if filter(i):
#         new_list.append(expressions(i))
#
# As you can see, LC is very powerful, it makes your 
# code more compact and easier to read!
# This is one of the most attractive features of Python

"""
Example 1: 
suppose a list of phrases extracted
from the book of Harry Potter, and you are interested to pick out 
the sentences which mention 'Harry'.
"""
A = ["That is because it is a monstrous thing, to slay a unicorn,", 
"said Firenze. Only one who has nothing to lose, and everything to gain",
"Harry stared at the back of Firenze's head",
"enough to drink something else -- some ..",
"Harry, do you know what is hidden in the school at this very moment?"
"The Sorcerer's Stone! Of course -- the Elixir of Life!"
"Can you think of nobody who has waited many years..."
"It was as though an iron fist had clenched suddenly around Harry's heart", 
"Over the rustling of the trees, he seemed ..."]

# you can address it with LC in just one line of code
print([phrase_with_harry for phrase_with_harry in A if 'Harry' in phrase_with_harry ])


"""
Example 2: 
suppose that you want to square a list of numbers, 
with the mathematic operator '**''
"""
A = [2,0,1,8]
print([elm**2 for elm in A]) # result: [4, 0, 1, 64]

"""
Example 3: 
suppose that you want to take out and square the numbers 
of A which do not appear in the list B
"""
A = [2,0,1,8,12,6]
B = [2,0,1,7,12,5,12,14]
print([elm**2 for elm in A if elm not in B]) # result: [64, 36]

# now you should have a clear idea of how powerful the LC is.

# 4) Function
# ======

# a function makes your code segment reusable, it helps you organize
# better your logic, and makes the your program more modularized.

# a function in Python has three parts; the keyword 'def', the function name and input parameters.
# for example,
def anArbitraryFunctionName(here,you,can,put,anynumber,of,parameters):
	# in the function body, you can do any operations you want
	youCanCreateAnyVariable = here+you+can-put+anynumber*of+parameters
	youCanDoWhateverYouWantInsideAFunction = can+you
	# and you can optionally choose to return something
	return youCanDoWhateverYouWantInsideAFunction

# you can call your function as many times as you want,
# instead of writing repeated code segments, you just call the name of your function as follows.
result = anArbitraryFunctionName(2,0,1,8,12,0,5)  + anArbitraryFunctionName(5,0,12,8,1,0,2) 

# 5) We now solve an interview question from FaceBook as an exercise.
# ======
# Find out a pair of different numbers with sum 
# as x from a given array A[].
#
# For example, 
# given a = [6,5,9,3,2,1,1] and x = 10,
# the resulting pair is 9 and 1 because their sum makes 10.
#
# There could be many solutions, a possible one is the following:
#

A = [6,5,9,3,2,1,1]

def findPair(A,x):
    for i in A: # check the each element of A
        counter_part = x - i # calculate its conter_part 
        if counter_part in A and counter_part != i : # check if the counter part is in A, and it is different from i.
            print ('Found a solution:',i,counter_part)
            return True
    print ('No solution found')
    return False

findPair(A,10) # please also try with other input, e.g. 0, 5, 200,  ...


# references:
# https://www.pythonforbeginners.com/basics/list-comprehensions-in-python
# https://docs.python.org/3/tutorial/controlflow.html
# https://www.pythonlearn.com/html-008/cfbook006.html
# https://python.swaroopch.com/problem_solving.html
# Chapter 2, A Crash Course in Python. Joel Grus. "Data Science from Scratch"



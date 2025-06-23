# Python programming language

python is a high-level and easy to understand and simple language , python is a interpreted language but technically it does both compiling and interpreting and it is object oriented (structring the code using objects ===> data means attributes and behaviour means methods / functions) programming language .

python can not used by mobile applications

Features :

1.easy to understand - less developement time

2.free and open source

3.high level language

4.portable - works on windows or linus or mac

5.Python has inbuilt library

Interpreter : An **interpreter** translates and executes the code  **line by line** , at  **runtime** .

compiler : A **compiler** translates the **entire code** (source code) into **machine code (binary)**  **at once** , before running the program.

# Chapter-1 (modules and comments and pip)

executing first python code -> print("hello world")

extenstion to same the file -> .py

how to execute the python code in vs code -> python filename.py

**Modules** (it is a code written by  somebody else that code we are using in our code)

types of modules :

1. Build in module -> preinstalled in python
2. external module -> need to install by pip

pip : pip is package manager for python, you need to us pip to install a module on your system

* python is used a calculator : open cmd and type python and then enter a expression it given the calculated value(REPL - read evaluate print loop)

Comments : writing something so that the programmer does not want to execute

types of comments :

1. Single line -> #
2. Multi line -> """ """

# Chapter -2 (datatypes and variables)

**variable : i**t is a name given to the memory location in the program

**rules for identifing a variable :**
 1.variable name can contain alphabet,digit and underscore

 2.variable name can only start with alphabet and underscore

 3.variable name can not start with digit

4. no white space is allowed to use inside a variable name

**datatypes :** (python automatically identifies the type of data for us)

1.integer

2.floating point numbers

3.strings

4.booleans

5.none

operators in python :

1.arithmetic operators => +,-,*,/,%,//

2.assignment operator => =,+=,-= etc

3.comparison operator=> ==,.,>=,<,!=

4.Logical operator => and , or , not

type() function : (use to find the datatype of a varaiable given , type takes only arg or parameter)) and typecasting:(converting one datatype to other)) :

input() function : function allows the user to take input from the keyboard in the form of string

# Chapter - 3 (Strings)

string is a datatype in python

string is a sequence of characters enclosed in quotes ====>  ' ' , '' '',''' '''

**String slicing :** string in python is sliced for getting a part of string

 **forward indexing :** indexing in a string starts from 0 to (len-1) in python ,

 **backward indexing :** indexing starts from left to right which is  , it starts with -1

name = "Meghana"

    s = name[start,end] end = end-1

    s[0:3]  returns "Meg"

    s[1:3] returns "eg"

**Slicing with skip value :** we can provide a skip value as a part of our slice

 ex: word = "amazing"

    word[1:6:2] --> 'mzn'

**advanced slicing techniques :** word = "amazing"

    word[:7] ----> 'amzing'

    word[0:]  ----> 'amazing'

**String funnctions :**

1. len()
2. string.endswith('g')
3. string.count('l')
4. string.capitalize()
5. string.find(word)
6. string.replace(oldword , newword)

# **Chapter - 4 : (Lists and tuples)**

lists are containers to store set of values of any datatype

fruits=['apple','banana',7,False]

**List indexing** : can be indexed just like a string

    name = [7 , 9 ,'Harry']

name[0] = 7

name[1] = 9

name[50] = error

name[0:2] = [7,9]

**List Methods :**

 list[1,8,7,2,21,15]

1. list.sort() : updates the list to [1,2,7,8,15,21]
2. list.reverse() : updates the list to [15,21,2,7,8,1]
3. list.append(8) : adds 8 at the end of the list
4. list.insert(3,8) : this will add 8 at 3rd index
5. list.pop(2) : will delete element at index 2 and returns its value
6. list.remove(21) : will remove 21 from the list
7. len(list) : gives the length of list
8. l

**Tuples :** tuple is an immuatable(can not be changed) data type

a = () ===> empty tuple

a = (1, ) ===> tuple with only one element needs a comma

a = (1,7,2) ===> tuple with more than one element

**once defined a tuple element cant be altered or manipulated**

**Tuple methods :**

    a = (1,7,2)

a.count(1) : it returns number of times 1 occures in a

a.index(1) : returns the index of first occurance of 1 in a

# **Chapter - 5 (Dictionary & Sets)**

**Dictionary :** collection of key value pairs

 syntax : a = {'key':'value','harry':'code','marks':'100','list':'[1,2,9]'}

a['key'] => print 'value'

a['list'] => print [1,2,9]

**properties in dictionaries :

1. it is unordered
2. it is mutable
3. it is indexed
4. cannot contain duplicate keys

methods in dictionary :

  ex : a = {'name':'harry' , 'from':'india' , 'marks' : [92,98,96]}

1. a.items() : returns a list of (key value) tuples
2. a.keys() : returns list containing dictionaries keys
3. a.update({'fruit':'sam'}) : updates dictionary with supplied key value pair
4. a.get('name') : returns the value of key ===> harry

**Sets in python :** collection of non repetative elements

s = set()

s.add(1)

s.add(2)

**properties of sets**

1. sets are unordered -> order does not matter
2. sets are unindexed -> cannot access elements by index
3. there is no way to change items in sets
4. sets can not contain duplicate values

**operations on sets**

   s = {1,8,2,3}

1. len(s) : returns 4
2. s.remove(8) : updates set and removes 8 from s
3. s.pop(): removes arbitrary element from set and returns element removed
4. s.clear(): empties the set s
5. s.union({8,11}) : returns new set with all items from both the sets ==> {1,8,2,3,11}
6. s.intersection({8,11}) : returns a set which contains only items in both sets ===> {8}

# **Chapter-6 Conditional Expressions** :

we must be able to execute instructions on a conditions being met

1. if else
2. elif
   syntax :
3. if(condition):
   print('yes')
   elif(condition):
   prit("no")
   else:
   print("Maybe")

**Relational Operators :  ( == , >= , <= )**   used to evaluate the conditions inside the if statement

**Logical Operators :**   (and or not)    these operate on conditional statements

**elif clause : [ else if ]** if stat can be chained together with a lot of these elif stat follwed by else

# **Chapter - 7 (loops in python)**

sometimes we need to repeat set of statements in our program for instance .

so loops make it easy for programmers to tell the computer which set of instructions to repeat and how

#### **Types of loops in python :**

primarily there are two types of loops in python :

1. while loop : condition is checked first , if it evaluates to true the body of loop is executed otherwise not , once the loop is entered process is continued until the condition becomes false
2. for loop : iterates through sequence like list , tuple,string

syntax of while loop : while condition :

    #body of loop

syntax of for loop : for list in i :

    print(list)

Range function in Python : used to generate a sequence of numbers

    range(start,stop,step)

ex: for i in range(0,7):

    print(i)

for loop with else :

ex: list = [1,2,3,4]

    for item in list :

    print(item)

    else :

    print("done")

**break stat** : used to come out  of loop when encountered

ex: for i  in range(0,80)

    print(i)

    if i ==3 :

    break

**continue stat :** used to stop current iteration of loop and continue with the next

ex : for i in range(0,4):
           print("new")

    if i==2:

    continue

    print(i)

**Pass stat :** null stat in python which means it does nothing

ex: for i in list :

    pass  ----> without pass the program will  give an error

# Python programming language

python is a high-level and easy to understand and simple language .

Features :

1.easy to understand - less developement time

2.free and open source

3.high level language

4.portable - works on windows or linus or mac

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

fruits['apple','banana',7,False]

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

**Tuples :** tuple is an immuatable(can not be changed) data type

a = () ===> empty tuple

a = (1, ) ===> tuple with only one element needs a comma

a = (1,7,2) ===> tuple with more than one element

**once defined a tuple element cant be altered or manipulated**

**Tuple methods :** 

    a = (1,7,2)

a.count(1) : it returns number of times 1 occures in a

a.index(1) : returns the index of first occurance of 1 in a

**Chapter - 5 (Dictionary & sets)**

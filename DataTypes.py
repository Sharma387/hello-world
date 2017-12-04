#Datatypes
#Integer - int 3, float 3.7 and complex 5j

#String datatype
string1 = 'sharma'
string2 = 'shyam'
print('Fulname =', string2+string1) #concatinate strings example
print('repeate the string 10 times',string1*10) #repeate string
print('slicing the string it is similar to trim',string1[2:4]) #trim feature
print('indexing the string its nothing by picking char from a string',string1[-2]+string1[1]) #pick char from string

#String type specific methods
string3 ="this is very interesting and going good so far and in fact easier than java"
#find()
print("find the and word in the string3 ",string3.find('and'))

#replace()
print("replace very word in the string3 ",string3.replace('very','very good'))

#split() - this will split the string value and stores it in an array or otherwise called tuples
print("split the string by space and store it in tuplese",string3.split(' '))

#Count()
print('count a character in the string',string3.count('a'))

#capitalize(0
print(string3.capitalize())
print(string3.upper())
print(string3.center(3))
print(string3.encode())
print(string3.isalpha())
print(string3.strip("java"))

# tuples - value cannot be changed kind of constant array
tuples1 = (1,2,3,4,6)
print(tuples1.count(3))


#Mutable strings

# list - similar to array values can be changed

list1 = [1,2,4,5]
#apped a value in the list1
list1.append(4)
print(list1)

#Dictionary - it is like storing value in Key:value pair

#empty dictionary - you can add value to it later
my_dict1 ={}

#dictionary with integer key
my_dict2 = {1:'sharma',2:'shyam', 3:'rajasekar', 4:'minty'}


#dictionary with mixed keys
my_dict3 = {1:'sharma',2:['a','b','c']}

#from sequence having each item as pair
my_dict4 = dict([(1,'apple'),(2,'pine')])

#lets what are functions we have it dictionary
print('keys from my_dict2',my_dict2.keys())
print('values from my_dict2',my_dict2.values())
print('values from key 2 in my_dict2',my_dict2.get(2))


#set - its a collection of elements but cannot have duplicate values init

my_set ={1,2,3,4,5,6,8,9,8,10}
print(my_set)

#operation you can perform are
#Union, intersection, differences.. lets see the examples

my_set1 = {1,2,3,'s','r','y','u'}
my_set2 = {'a','c',6,3,5,9,'d','s','y','r','x','u'}

print('Union', my_set1 | my_set2) #this is A Union B
print('Intersection', my_set1 & my_set2) #this is A intersection B
print('Difference', my_set1 - my_set2) #this is A difference B
#strings
#each element is a single character
#accessing range 
str='hi' ' hello' #automatic contatenaiton
str[2:3]#excludes the end point keep that in mind
str[:4]#starts from the beginning
str[4:]#goes till the end
#we can also step
str[::2]#here step is to and goes from the beginning to the end
raw=r'hi\nksjdksdj' #it prints it as it is
#IMP we can use an index that doesnt exist while slicing



#string methods
#.lower()   converts to lower case
#.upper()   converts to upper
#.count(substring) counts the frequency of substring
#.find(substring)  returns the starting index of the substring in the string if not in the string returns -1
#.replace(substr1,substr2) replaces substr1 with substr2 in the string

#formatting strings(basically place holding)
placeholder1='name'
placeholder2='hemang'
my_name='My {} is {}'.format(placeholder1,placeholder2)
#we can also number the placeholders
my_name= 'My {0} is {1} which is my {0}'.format(placeholder1,placeholder2) #my name is hemang which is my name
#using dictionaries
person={'name':'hemang','age':19}
intro='My {1} is {0[name]} and my age is {0[age]}'.format(person,placeholder1)#My name is hemang and my age is 19
#the same thing can be done with lists but instead of keys we use indexes
#doing the same thing with object
class person():
    def __init__(self,name,age):
        self.name=name
        self.age=age
person_hemang=person('Hemang','age')

intro='My {1} is {0.name} and age is {0.age}'.format(person_hemang,placeholder1)#My name is hemang and age is 19
#can also use a keyword argument format what we did above was index format ...dw ull see what i mean
my_name='my {} is {name}'.format(placeholder1,name='hemang')#my name is hemang


#f'string(makes formatting much simpler)
my_name=f'my {placeholder1} is {placeholder2}'

#old string formating
#just like in c
'''print("%s is my %s"%('hemang','name'))'''


#numbers
#abs() takes in an argument and return its absolute value
#round(arg1,arg2) arg1 is the number to be rounded arg2 is the number of decimal places
#to which it has to be rounded arg2 by default is 0(so integer)

#Lists
#IMP we can assign a section of the list by using list slicing
#.insert(pos,value)
#.extend(list)
#.append(value)
#.remove(value)
#.pop() removes the last value and returns it 
'''so print(list_name.pop()) will print out the last item'''
#.reverse()
#.sort(reverse=True)
#.sort(reverse=False)
#sorted(list_name)
#max(),min(),sum()
#.index(value) returns index of the value
#join and split methods
#'str'.join(list_name) returns a string withh all the elements seperated by whatever is there is the string
#for example l=[1,2,3] print('hey'.join(l)) will output 1hey2hey3
#split is the opposite list_name.split('str')
#tupples are basically immutable lists
#sets
#set1.intersection(set2) in both set1 and set2
#set1.difference(set2) in set1 but not in set2 
#.union()
#create empty lists [],list()
#create empty tupple (),tuple()
#BUT FOR SETS we cant use {} cause its then an empty dict
#.keys() returns a list of keys 
#.values() returns a list of value
#.items() returns a list of tuples of key value pairs

#Conditional statements
'''if condition :
    code_block'''
#is statements checks the equivalence of id
#what is id? id()gives u the memory location id of a particular variable
#false values
'''
False
None
zero of any numerical type
any empty sequence(list,tuple,set)
any empty mapping(dictionary)
'''
#loops and iterations
#range(start,stop,step) doesnt include stop
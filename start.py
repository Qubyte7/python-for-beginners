# x=2
# y=4
# print(x+y)
# x= input('What is your Name?')
# print(x)
# x=2
# if  2 == x:
#     print('x is ',x)
# elif x==12:
#     print('sorry you are not 2')
#     print('wewewewewe')

# def sum(a,b):
#     total = a+b 
#     print(total)

# q=input('enter the first number:')
# a = int(input('enter the first number:'))
# b=int(input('enter the second number:')) 
# z = a+b
# print(z)
# sum(5,6)
"""
fruits = ['banana', 'orange', 'waterMelon']
for fruit in fruits :
    print(fruit)
print('I love it')
"""
'''
name = "Mugisha"
print(len(name))#length of string 
print(name[0:4])
print(name[:2])
print(name[4:])

for letter in name :
    print(letter)
if 'gi' in name:
    print("tu es valide")
pos = name.find('gi')


name2 = "  innocent"

if name2 == 'innocent':
    print("innocent man")
elif name2 <'innocent':
    print("tu viens apres innocent man")
elif name2 > 'innocent':
    print("toi tu viens avant innocent man")
else:
    print("it's okay ")
print(pos)
replace = name2.replace('nnocent', 'moji')
print(replace)
#trimming a string 
print(name.strip())

#file handling
reader = open('read.txt')
for line in reader:
    line = line.strip()
    print(line)

inp = reader.read()
print(inp)


#dictionary

dictionary1 = dict()
dictionary1['money']= 200000
dictionary1['money']= 200000
dictionary1['fire']='assualt rifle'
dictionary1['boomb']='hand grenade'

print(dictionary1)
dictionary2 =dict()
names= ['innocent','ganza','Michael','sabrina','innocent']

for name in names:
    if name  not in dictionary2:
        dictionary2[name] =1
    else:
        dictionary2[name] = dictionary2[name] + 1

x = dictionary2.get('innocent',0)
print(x)

print(list(dictionary2))#prints the keys
print(dictionary2.keys())#prints the keys
print(dictionary2.values())#prints the values 


#tuples : they similar to list but the slite difference is that they are not modifiriable 
# to mean they are immutable & function that may seem to be changing the tuple can not be applied

dict = dict()
dict['leo']= 15 
dict['leopord']=17
dict['tigre']=8

print(dict.items()) # not  that this function prints items in group of tuples

tuple =  (12,13,23,45,56)
print(tuple)

(Innocent,Ganza) = (16,13)
print(Innocent)
 #sorting tuples
for (k,v) in sorted(dict.items()):
    print(k,v)

temporaryList = list()
for (k,v) in dict.items():
    temporaryList.append((v,k))
print(temporaryList)
temporaryList2 = sorted(temporaryList, reverse=True)
print(temporaryList2)
'''

#regular expressions
import re
read = open('read.txt')

for line in read:
    line=line.strip()
    if re.search('^w.\S+',line):#not that re.search returns true for the values that muches the exprection
        print(line)

x= "My GOD: What on earth : is this thIngs "
e="From mugiha@gmail.com huye disctrict"

y=re.findall('[AIUOE]+',x)
print(y)
      #GREED in  regular expression 
      #Greed
g=re.findall('^My.+:',x)#the greed will take the : which will be on the highest position
print(g)
    #Non Greed
ng = re.findall('^My.+?:',x)# the ? limits for the the shortest match of the  :
print(ng)

email = re.findall('^From \S+',e)
email = re.findall('^From (\S+)',e)
print(email)
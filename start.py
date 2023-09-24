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

atpos = x.find('') # find prints back the index of the specified character
print(atpos)

# ATTENTION : 1) [^ ]: means a set charcters without a blank spce
# when you want to search for $ you use :\$

#Printing ASCII CODE OF A CHARACTER
print(ord("a"))

#sockets
import socket
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    mysocket.connect(('data.pr4s.org',80))
    cmd='GET http://data.pr4s.org/romeo.txt HTTP/1.0\n\n'.encode()
    mysocket.send(cmd)
    print("connection established")
except socket.error:
    print("connection error")

while True:
    data = mysocket.recv(512)
    if(len(data)<1):
        break;
    print(data.decode())
mysocket.close();
#socket.AF_INET : means that we are going to make a socket that is going to goes across the internet
#socket.SOCK_STREAM : means that we made a stream socket which is a series of characters that comes one after another


#read web pages using urllib
#using beatiful soup  :  is used for parsing HTML documents and extracting data from HTML documents
import urllib.parse,urllib.request,urllib.error
from bs4 import BeautifulSoup
try:
    url = input("enter url : ") 
    html =urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html,'html.parser')
    tags =soup('a')
    for tag in tags:
        print(tag.get('href',None))
except urllib.error:
    print("Sorry error ocuured while fetching hypertext")
'''

#XML



#json
import json
input2 = ''' [
    {
    "id": "001",
    "x": "1",
    "name": "Shami"
    },
    {
    "id": "004",
    "x": "4",
    "name": "Michael"
    }
   ]'''


# info = json.loads(input2)
try:
    info = json.loads(input2)
except json.JSONDecodeError as e:
    print(f"JSON decoding error: {e}")

print('user count : ', len(info))
for item in info:
    print('Name : ', item['name'])
    print('ID :',item['id'])
    print('Attribute : ', item['x'])


# def mutli_add(a,b,/,*,c,d):
#     return a + b + c + d

# print(mutli_add(1,2,d=3,c=4))
# # mutli_add(b=1,a=2,c=3,d=7)
# # mutli_add(a=1,b=2,d=3,c=8)
# # # mutli_add(a=1,b=3,c=4,d=5)
# # mutli_add(2,4,5,d=6)
# # mutli_add(2,5,4,5)

# # arbitrary arguments
# def print_names(**args):
#     for key,value in args.items():
#         print(f"Hello, {value}!")

# # Call with varying numbers of arguments
# print_names(name="Alice",number=2)

# # set 
# my_set = [1,5,3,5]
# my_tuple = (1,5,3,5)

# print(set(my_set))
# print(my_tuple[0])

# # lambda function exercises

# x= lambda x: x*15
# y= lambda x,y: x*y

# print(x(5))
# print(y(4,5))

# # sorting using lambda function
# # sort 1
# tuple_list=[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

# # sort according lesson name
# sorted_list = sorted(tuple_list,key= lambda item:len(item[0]))

# # sort 2
# dictionary_list = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
# sorted_list_dic = sorted(dictionary_list, key=lambda item:len(item.values()))


# for item in sorted_list_dic:
#     print(item)

# checking that 
# check = lambda s,c: True if s.startswith(c) else False
# print(check('innocent','i'))    

# # extracting date , month and tome
# from datetime import datetime

# # getting current date
# now=datetime.now()
# print(now)

# year = lambda x: x.year
# month = lambda x: x.month
# day = lambda x: x.day
# hour = lambda x: x.hour

# print(day(now))

# # checking that a given input is a string or not
# string_check = lambda x:x.replace('.','',1).isdigit()
# # that 1 means that . will be replaced at the frst coccirence
# print(string_check('2.2'))

# from functools import reduce

# numbers = [1, 2, 3, 4, 5]

# sum_result = reduce(lambda x, y: x + y, numbers)
# print(sum_result)  # Output: 15


# date = '2021-06-05'


# print(date.month)


string_1 = "innocent"
count = 0
for i in string_1:
    count += 1
print(count)

# getting frequenyc of a character in a string

dictionary = {}
for i in string_1:
    keys = dictionary.keys()
    print(keys)
    if i in keys:
        dictionary[i] += 1
    else:
        dictionary[i] = 1

print(dictionary)
print(string_1.capitalize())
print(string_1.upper())
print(string_1,"what is this")
print(string_1+"it is a string")
replace = string_1.replace("n","d")
print(replace)

#tuples


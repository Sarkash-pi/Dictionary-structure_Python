# Dict items are key value pairs enclosed in curly brackets
# Dict is ordered as of python 3.7
# Dict is mutable
# Dict keys are unique, cannot have duplicates
# Elements can be of different data types


'''
Dict Attributies
'''

# print(dir(dict))
# print(help(dict.items))

'''
Creating python dictionary
'''

# dict_example = {}
# dict_example = {'name': 'Sarkash', 'age': 25}
# dict_example = dict([(1,'car'), (2, 'bicycle')])
# print(dict_example)
# print(dict_example.items())  # will get back tuples

'''
Access dictionary values
'''

# student = {'name': 'Sarkash', 'age': 25}
# print(student['age'])
# print(student.get('name'))
# print(student.keys())
# print(student.values())
# print(student.items())

# students = [{'name': 'Sarkash', 'age': 25}, {'name': 'Tina', 'age': 40}]

# print(students[1])
# print(students[1]['name'])

# for i in range(len(students)):
  # print(students[i]['name'])


'''
Changing dictionary Elements
'''

# student = {'name': 'Sarkash', 'age': 25}
# student['age'] = 35
# print(student)

# or we can use update method, basicly it is allowe you to update it entirly 
# student.update({'name': 'Tina', 'age': 35})
# print(student)

# default method. it doesn't change the value but it check the key if it isn't defalut it will add it 

# student = {'name': 'Sarkash', 'age': 25}
# student.setdefault('name', 'Steve')
# student.setdefault('subject', 'Python')
# print(student)

'''
Remove element from dictionary
'''

# student = {'name': 'Sarkash', 'age': 25}
# # student.pop('name') # remove specific item
# # student.popitem() # will remove last item
# # student.clear() # clear all items
# # or if we want delet the dictionary 
# # del student

# print(student)


'''
Dictionary membership test
'''

# student = {'name': 'Sarkash', 'age': 25}
# print('age' not in student)
# print('name' in student)




# clear()	      - Remove all items from dictionary
# copy()	      - Returns a shallow copy of dictionary
# fromkeys()	  - Returns a dictionary with the specified keys and value
# get()	        - Returns the value of the specified key
# items()	      - Returns a list containing a tuple for each key value pair
# keys()	      - Returns a list containing the dictionary's keys
# pop()	        - Removes the element with the specified key
# popitem()	    - Removes the last inserted key-value pair
# setdefault()	- Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	    - Updates the dictionary with the specified key-value pairs
# values()	    - Returns a list of all the values in the dictionary
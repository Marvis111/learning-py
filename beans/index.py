from __future__ import print_function

print('This is a string')
s = 13.3
name = 'Place my variable here: %s' %(s)

print(name)

print('First: %s ,  second : %s. third : %s' %('Hi','two', 4))

print("First : {x} second: {y} ".format(x = 'inserted', y ='name'))

students = [{"id": x } for x in range(5)] 

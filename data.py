animals = ['cat','dogs','hen',]

nums = [ num for num in range(4) ] 


print(len(nums * 3), 3 in nums, nums[2])


cat, *rest = animals

print(rest)

animals.append('Goat')

animals.insert(2,'elephant')

print(animals)

nums.sort(reverse=True)
print(nums)

#dictionary

details = {"name":'marvellous','age':'18','color':'blue'}

acopy = { det[0] : det[1] for det in details.items()}

print(acopy == details)


print('My fav food is '+str(details.get('food','Amala')))


#string

"""myname = 'Tony'

for i in myname:
    if i != "N":
        print('no N')"""
        
name = 'Hello world'

print(name[2]) 

print(name.split('l'))


greet = '''sua7
 hello word
 greet
'''
n = '\n'
print(greet.split(n))

def name(name):
    if name =='Tony':
        print('This is marvellous')
    elif name =='Marvellous':
        print('great guy, welcom')
    elif name == 'Okeke':
        print('wHAT IS John paul doing here...')
    else:
        print('Hello stranger')

name('Tony')

#while loop

def printspam(spam):
    if spam < 5 :
        print('hello world')
        spam += 1
        printspam(spam)

#printspam(0)

def printspams(spam):
    while spam < 5 :
        print('hello spam '+str(spam))
        spam += 1

#printspams(0)

#The above functions are actually the same 
#One is recursive and the other makes use of the while loop

"""while True :
    print('Please type your name')
    user = input()
    if user == 'Tony':
        print('Hello Marv')
        break
print('Thank you for learning...')
    """
#range

def findrange(num):
    for i in range(num):
        print(i)

#findrange(4)

def sum(num):
    total = 0
    for numbs in range(num + 1):
        total += numbs
    print(total)


#sum(100)

def ranges(start, end):
    for num in range(start, end+1):
        print(num)

#ranges(1,4)
for i in range(10,20,3):
    print(i)
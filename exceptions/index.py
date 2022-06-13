import logging

logging.basicConfig(filename='log.txt',level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

logging.debug('Start of Program')
#logging.disable(logging.CRITICAL)
name = 'Marvellous'

assert name == 'Marvellous', 'name is not equal to Marvellous'


assert 'a' in name, 'N not found in name'


if 'aj' not in name:
    logging.error('No a in name')
    

print(type(2)== int)

def hello(a):
    """
    INPUT : A number
    OUTPUT : A boolean
    """
    print(a)

print(type(hello) == object)

hello('hell','hey')
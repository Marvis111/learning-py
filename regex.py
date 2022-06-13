from re import compile,VERBOSE

regex = compile(r'(\d\d\d)-(\d\d\d)-\d\d\d\d')

mo = regex.search('My number is 123-323-3434 and my sis is 123-232-2133')

firstPart, lastPart = mo.groups()

print(firstPart,lastPart)

#count vowel and consoants

def countAlphabets(soundType:str,words : str):
    soundRegex =  r'[aeiouAEIOU]'
    if soundType.lower() == 'vowels':
        soundRegex = r'[aeiouAEIOU]'
    else:
        soundRegex = r'[^aeiouAEIOU0-9 ]'
    regex = compile(soundRegex)
    return len(regex.findall(words))


vowels  = countAlphabets('vowels','Vowels are 4 DDAs')
   

print(vowels)


#phone number regex without extension]

phoneNumberRegex = r'''
    (\d{3}|\(\d{3}\))?
    (\s|-|\.)?
    \d{3}
    (\s|-|\.)
    (\d{4}
'''

reg = compile(phoneNumberRegex,VERBOSE)

result = reg.findall('These are numbers 123-222-2323 , 1122323232,123.123.1334 ')

print(result)

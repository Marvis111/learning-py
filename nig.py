from re import compile, VERBOSE, IGNORECASE 

nigPhoneRexExpression = r'''(
    ([+]?[2][3][4])?    #country code
    0?[7-9][0-1][0-9]   #first 4 digits
    (\s|-|\.)?     #the number can have either space, hyphen or . as seperators
    \d{3}
    (\s|-|\.)?
    \d{4}
)
'''
regex = compile(nigPhoneRexExpression,VERBOSE | IGNORECASE)
text = 'In this text we have - 0913-395-0674, 706-920-0394, 08012342423 , +2349133950674 '
numbers =  regex.findall(text)
for phoneNum , *others in numbers:
    print(phoneNum)
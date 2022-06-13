import os
from zipfile import ZipFile,ZIP_DEFLATED

myFiles = ['account.txt','index.txt','index.py']

"""for files in myFiles:
    print(os.path.join(os.getcwd(),files))
"""

def getXfileSize(extension:str = 'py'):
    totalsize = 0
    for file in os.listdir(os.getcwd()):
        if file.lower().endswith(extension.lower()):
            totalsize += os.path.getsize(os.path.join(os.getcwd(),file))
    return totalsize


pyfiles = getXfileSize()
#ts files
tsFiles = getXfileSize('TS')
print(tsFiles)

if os.path.exists(os.path.join(os.getcwd(),'beans')):
    print('Folder already exist')
else:
    os.makedirs('beans')


#reading and writing in file...

file = open('./contents/index.txt')

print(file.read())

zipfiles = ZipFile('example.zip','w')

# zipfiles.write('index.js',compress_type= ZIP_DEFLATED)
# zipfiles.write('index.ts',compress_type= ZIP_DEFLATED)

'''print(os.unlink(os.path.join(os.getcwd(),'beans')))
print(zipfiles.namelist())'''
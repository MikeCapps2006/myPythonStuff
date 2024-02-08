import shutil
import os
import re
#import pdb

""" directory_to_unzip_to = '/Users/mike/myPythonStuff/advancedModules/advancedmodulespuzzle'
shutil.unpack_archive('unzip_me_for_instructions.zip', directory_to_unzip_to, 'zip') """

regex_phone = r'\d\d\d-\d\d\d-\d\d\d\d'

def search(file, pattern=r'\d{3}-\d{3}-\d{4}'):
    f = open(file, 'r')
    text = f.read()

    if re.search(pattern, text):
        return re.search(pattern, text)
    else:
        return ''
results = []
for folder, sub_folders, files in os.walk(os.getcwd()+'/extracted_content'):
    for file in files:
        full_path = folder + '/' + file

        results.append(search(full_path))

for r in results:
    if r != '':
        print(r.group())

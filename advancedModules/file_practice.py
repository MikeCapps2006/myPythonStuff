import os
import shutil
import send2trash

#f = open('practice.txt', 'w+') #Opens or creates a practice file and writes a test statement in it and then closes the file
#f.write('This is a test for Mike Capps')
#f.close()

#print(os.getcwd()) #prints the current working directory

#print(os.listdir()) #prints the contents inside of the current working directory
#print(os.listdir('/Users/mike')) #prints the contents inside of the passed in directory

#shutil.move('practice.txt', '/Users/mike') #Moves a file from current working directory to another directory
#shutil.move('/Users/mike/practice.txt', os.getcwd()) #Moves file from one spot to the current working directory


#send2trash.send2trash('practice.txt') #Uses the send2Trash module to send deleted files and folders to the trash besides permanantly deleting them

""" NOTE: The os module provides 3 methods for deleting files:

os.unlink(path) which deletes a file at the path your provide
os.rmdir(path) which deletes a folder (folder must be empty) at the path your provide
shutil.rmtree(path) this is the most dangerous, as it will remove all files and folders contained in the path. """


for folder, sub_folders, files in os.walk('complete-python-3-bootcamp-master'):
    print(f'Currently looking at folder - {folder} \n')
    
    print('Subfolders:')
    for folder in sub_folders:
        print(f'\t {folder}')

    print('\n')

    print('Files:')
    for file in files:
        print(f'\t {file}')


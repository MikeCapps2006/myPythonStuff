import zipfile
import shutil

#this just creates 2 text files
""" f = open('new_file.txt', 'w+')
f.write('This is a new file to zip')
f.close()

f = open('new_file2.txt', 'w+')
f.write('This is the second file to zip')
f.close()
 """

#this creates a compressed file and add 2 text files to it
""" comp_file = zipfile.ZipFile('comp_file.zip', 'w')
comp_file.write('new_file.txt', compress_type=zipfile.ZIP_DEFLATED)
comp_file.write('new_file2.txt', compress_type=zipfile.ZIP_DEFLATED)
comp_file.close() """


#Extracts the contents of comp_file.zip into a created file extracted_content
""" zip_obj = zipfile.ZipFile('comp_file.zip', )
zip_obj.extractall('extracted_content')
 """

#Zips folder with shutil
""" directory_to_zip = '/Users/mike/myPythonStuff/advancedModules'
new_archive = 'AdvancedModules'

shutil.make_archive(new_archive, 'zip', directory_to_zip) """

#Unzips folder
directory_to_unzip = '/Users/mike/myPythonStuff/advancedModules/advancedModules'
shutil.unpack_archive('AdvancedModules.zip', directory_to_unzip, 'zip')
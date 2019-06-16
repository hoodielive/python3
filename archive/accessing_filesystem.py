
import os

os.unlink('deleteme.txt') # remove deleteme.txt from disk 
os.rename('file.txt', 'newname.txt') # mv file.txt to newname.txt 
os.chdir(newdirectory) #change current/working directory
filelist = os.listdir(dirname) # creat list of files in a directory
curdir = os.getcwd() #obtain current directory 
os.mkdir(dirname) #create a directory 
os.rmdir(dirname) #remove a directory (requires it to be empty) 
exists = os.path.exists(path) #does the file/directory exist? 
isfile = os.path.isfile(filepathname) #does path name exist and is it a file?
isdir = os.path.isdir(filepath) #does path name exist  and is it directory?

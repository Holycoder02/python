"""
File handling in Python allows you to read, write, and manipulate files on your computer. You can use built-in functions to open files, read their contents, write data to them, and close them when you're done. Here's a basic overview of file handling in Python:
1. Opening a file: You can use the open() function to open a file. It takes two arguments: the file path and the mode (e.g., 'r' for reading, 'w' for writing, 'a' for appending).
2. Reading from a file: You can use methods like read(), readline(), or readlines() to read the contents of a file.
3. Writing to a file: You can use the write() method to write data to a file. If the file doesn't exist, it will be created. If it already exists, it will be overwritten (in 'w' mode) or appended to (in 'a' mode).
4. Closing a file: It's important to close a file after you're done with it using the
close() method to free up system resources.
 


open("file name".txt", "mode")


"""

file = open('C:/Users/gaura/Downloads/git repo/python/File Handling/files.txt', 'r')  #open the file in read mode
content = file.read() #read the content of the file
print(content) #print the content of the file
file.close() #close the file after use

file = open('C:/Users/gaura/Downloads/git repo/python/File Handling/file2.txt', 'w')  #open the file in write mode
content = input('enter a data to write : ')
file.write(content)
print('data written successfully')
file.close() #close the file after use
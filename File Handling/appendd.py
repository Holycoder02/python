with open('C:/Users/gaura/Downloads/git repo/python/File Handling/file2.txt', 'a') as file:  #open the file in append mode
    content = input('enter data to append = ')
    file.write(content)
    print('appended successfully')

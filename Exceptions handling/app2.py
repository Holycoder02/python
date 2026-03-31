try:
    with open('/path/to/file.txt', 'r') as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print('file not found')

finally:
    print('file operations completed')
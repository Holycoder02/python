start = int(input('enter start = '))
stop = int(input('enter stop = '))

skip = int(input('enter skip = '))

for i in range(start, stop):
    if i == skip:
        continue
    print(i)

    #make range function in this by yourself.....you moron uncertinity, define advanced program defin ?
print(list(range(0, 10, 3)))

print(list(range(-10, -100, -20)))

a = ['mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):    #to find the length of list for we use len() intger
  print(i, a[i])


print(sum(range(3, 10,)))


password = "12345@python"

if len(password) >= 5:
    print("login successful")

else:
    print("login failed")
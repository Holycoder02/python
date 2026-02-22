profile = {
    'name':'raju', 'age':100, 'salary':25000.00
}

all_items = profile.items()
print(list(all_items))

profile = {
    'name':'raju', 'age':100, 'salary':25000.00
}


#=====================
#popped method to remove or double check

popped = profile.pop('age')
print(popped)
print(profile)

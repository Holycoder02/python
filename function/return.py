def get_full_name(first_name, last_name):
    '''return the full name, in a neated format'''
    full_name = f'{first_name} {last_name}'
    return full_name ##or like '''return full_name.title()'''

name = get_full_name('raju', 'singh')
print(name)
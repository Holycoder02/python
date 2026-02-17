#chaper 4 control statement
#area of circle

pie = 3.147
radius = float(input('enter radius = '))

area_of_circle = pie * radius ** 2
print('area of circle is = ', area_of_circle)

#top to bottom flow control 
#statement suite...
# - condition, float run, other not run
#for while else suite
#infinite loop
#nested
#pass
#break
#assert return

"""
if condition:
    statements
    """
age = int(input('enterage = , '))
if age >= 18 and age <=100: #true 
    print('you are eligible for vote')
    #else: alyways comes after if statement otherwise it will give error
else:
    print('you are less than 18')





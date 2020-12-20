import secrets

days = ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday')

def food():
    Breakfast = ('akamu & akara', 'bacon & eggs', 'bread & tea', 'coffee', 'ogi')
    Lunch = ('yam & egg', 'rice & stew', 'jollof rice', 'yam & egg', 'beans')
    Dinner = ('yam & egg', 'rice & stew', 'jollof rice', 'yam & egg', 'beans & plaintain', 'fried rice', 'eba & soup')
    x,y,z = secrets.choice(Breakfast), secrets.choice(Lunch), secrets.choice(Dinner)
    print('Breakfast =', x)

    if y == z:
        y = secrets.choice(Lunch)
        print('Lunch =', y)
        print('Dinner =', z)
    else:
        print('Lunch =', y)
        print('Dinner =', z)

for day in days:
    print(day)
    food()
    print()




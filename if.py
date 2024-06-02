cars = ["audi", "bmw", "subaru", "toyota"]
cars_new = cars[:]
cars_new.append("limo")

for car in cars_new:
    # check for something in a list, can use not in too
    if(car in cars):
        if (car == 'bmw'):
            print(car.upper())
        # else if = elif, and can use cnditional with and / or
        elif (car != 'audi' and True == True or False == True):
            print(car.lower())
        else: 
            print(car.title())
    else:
        print(f'not in cars_new {car}')

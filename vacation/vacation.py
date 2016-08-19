





def hotel_cost(nigths):
    return 140 * nigths

def plane_ride_cost(city):
    if city == 'Charlotte':
        return 183
    elif city == 'Tampa':
        return 220
    elif city == 'Pittsburgh':
        return 222
    elif city == 'Los Angeles':
        return 475


def rental_car_cost(days):
    car = 40 * days
    if days >= 7:
        car -= 50
    elif days >= 3 and days < 7:
        car -= 20

    return car

def trip_cost(city, days):
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city)
import random
from city import City


cityList = []
CITY_NUMBERS = 25
for i in range(0, CITY_NUMBERS):
    cityList.append(City(x=int(random.random() * 200), y=int(random.random() * 200)))

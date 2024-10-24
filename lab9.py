from Cars.car_showroom import CarShowroom

# Создание первого экземпляра
showroom1 = CarShowroom("First Showroom")
print(showroom1.name)  # Output: First Showroom

# Создание второго экземпляра
showroom2 = CarShowroom("Second Showroom")
print(showroom2.name)  # Output: First Showroom

# Проверка, что оба экземпляра ссылаются на один и тот же объект
print(showroom1 is showroom2)  # Output: True

from Cars.car_showroom import Car, GasCarRentalStrategy
from Users.users import User


# Пример использования
if __name__ == "__main__":
    car = Car(1, "Toyota", "Camry", 3000, 2020, "Sedan", "New York")
    user = User(1, "JohnDoe", "1990-01-01", "71234567890", "password123")

    print(f"Initial state of car {car.model}: Free")
    car.set_strategy(GasCarRentalStrategy())
    car.rent(user, 5)  # Арендуем автомобиль

    car.rent(user, 5)  # Попытка арендовать автомобиль, который уже арендован

    car.return_car()  # Возвращаем автомобиль
    car.return_car()  # Попытка вернуть уже свободный автомобиль

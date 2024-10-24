from Cars.car_showroom import Car
from Cars.car_showroom import ElectricCarRentalStrategy, GasCarRentalStrategy
from Users.users import User


if __name__ == "__main__":
    # Создание электромобиля с соответствующей стратегией расчета аренды
    electric_car = Car(1,
                       "Tesla",
                       "Model S",
                       5000,
                       2022,
                       "Sedan",
                       "California")
    electric_car.set_strategy(ElectricCarRentalStrategy())
    gas_car = Car(2,
                  "Toyota",
                  "Camry",
                  3000,
                  2020,
                  "Sedan",
                  "New York")
    gas_car.set_strategy(GasCarRentalStrategy())

    user = User(1, "JohnDoe", "1990-01-01", "71234567890", "password123")

    # Аренда электромобиля на 5 часов
    electric_car.rent(user, 5)
    # Output: The rental fee for Tesla Model S for 5 hours is $500.00

    # Аренда бензинового автомобиля на 5 часов
    gas_car.rent(user, 5)
    # Output: The rental fee for Toyota Camry for 5 hours is $250.00

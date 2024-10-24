from lab11 import ElectricCarFactory, GasCarFactory
from Users.users import User
from Cars.car_showroom import GasCarRentalStrategy


class CarFlyweight:
    def __init__(self, model, fuel_type):
        self.model = model
        self.fuel_type = fuel_type


if __name__ == "__main__":
    # Создаем экземпляр фабрики для создания электромобилей
    electric_car_factory = ElectricCarFactory()
    electric_car = electric_car_factory.create_car(id=1,
                                                   brand="Tesla",
                                                   model="Model S",
                                                   price=80000,
                                                   year=2024,
                                                   car_class="Luxury",
                                                   location="New York",
                                                   battery_capacity=100)

    print("Created Electric Car:")
    print(f"ID: {electric_car.id}, Model: {electric_car.model}, "
          f"Available: {electric_car.get_status_rent}")
    print(f"Battery Capacity: {electric_car.battery_capacity} kWh")

    print()

    # Создаем экземпляр фабрики для создания автомобилей на бензине
    gas_car_factory = GasCarFactory()
    gas_car = gas_car_factory.create_car(id=2,
                                         brand="Toyota",
                                         model="Camry",
                                         price=25000,
                                         year=2024,
                                         car_class="Sedan",
                                         location="Los Angeles",
                                         fuel_type="Gasoline")

    print("Created Gas Car:")
    print(f"ID: {gas_car.id}, Model: {gas_car.model}, "
          f"Available: {gas_car.get_status_rent}")
    print(f"Fuel Type: {gas_car.fuel_type}")

    # Создаем клиента
    user = User(1, "JohnDoe", "1990-01-01", "71234567890", "password123")
    gas_car.set_strategy(GasCarRentalStrategy())
    # Пробуем арендовать и вернуть автомобиль
    gas_car.rent(user, 5)
    gas_car.return_car()

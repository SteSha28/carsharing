from Cars.car_showroom import Car


# Конкретные классы для разных типов автомобилей
class ElectricCar(Car):
    def __init__(self,
                 id: int,
                 brand: str,
                 model: str,
                 price: int,
                 year: int,
                 car_class: str,
                 location: str,
                 battery_capacity: int):
        super().__init__(id, brand, model, price, year, car_class, location)
        self.battery_capacity = battery_capacity

    def __str__(self):
        return f'''Electric Car: {self.brand} {self.model},
        Battery Capacity: {self.battery_capacity} kWh'''


class GasCar(Car):
    def __init__(self,
                 id: int,
                 brand: str,
                 model: str,
                 price: int,
                 year: int,
                 car_class: str,
                 location: str,
                 fuel_type: str):
        super().__init__(id, brand, model, price, year, car_class, location)
        self.fuel_type = fuel_type

    def __str__(self):
        return (f'Gas Car: {self.brand} {self.model},'
                f'Fuel Type: {self.fuel_type}')


# Абстрактная фабрика для создания автомобилей
class CarFactory:
    def create_car(self,
                   id: int,
                   brand: str,
                   model: str,
                   price: int,
                   year: int,
                   car_class: str,
                   location: str,
                   *args, **kwargs) -> Car:
        raise NotImplementedError('''This method should be
                                  overridden by subclasses''')


# Конкретная фабрика для создания электромобилей
class ElectricCarFactory(CarFactory):
    def create_car(self,
                   id: int,
                   brand: str,
                   model: str,
                   price: int,
                   year: int,
                   car_class: str,
                   location: str,
                   battery_capacity: int) -> ElectricCar:
        return ElectricCar(id,
                           brand,
                           model,
                           price,
                           year,
                           car_class,
                           location,
                           battery_capacity)


# Конкретная фабрика для создания автомобилей на бензине
class GasCarFactory(CarFactory):
    def create_car(self,
                   id: int,
                   brand: str,
                   model: str,
                   price: int,
                   year: int,
                   car_class: str,
                   location: str,
                   fuel_type: str) -> GasCar:
        return GasCar(id,
                      brand,
                      model,
                      price,
                      year,
                      car_class,
                      location,
                      fuel_type)


# Пример использования фабричного метода
def main():
    # Создаем фабрику электромобилей
    electric_car_factory = ElectricCarFactory()

    # Создаем электромобиль через фабрику
    electric_car = electric_car_factory.create_car(
        id=1,
        brand="Tesla",
        model="Model S",
        price=80000,
        year=2024,
        car_class="Luxury",
        location="New York",
        battery_capacity=100
    )

    print("Created Electric Car:")
    print(electric_car)

    print()

    # Создаем фабрику для автомобилей на бензине
    gas_car_factory = GasCarFactory()

    # Создаем автомобиль на бензине через фабрику
    gas_car = gas_car_factory.create_car(
        id=2,
        brand="Toyota",
        model="Camry",
        price=25000,
        year=2024,
        car_class="Sedan",
        location="Los Angeles",
        fuel_type="Gasoline"
    )

    print("Created Gas Car:")
    print(gas_car)


if __name__ == "__main__":
    main()

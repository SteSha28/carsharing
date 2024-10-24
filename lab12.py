from Users.users import User
from Cars.car_showroom import Car
from datetime import datetime
from abc import ABC, abstractmethod
from lab10 import Contract


class AbstractFactory(ABC):
    @abstractmethod
    def create_car(self,
                   id: int,
                   brand: str,
                   model: str,
                   price: int,
                   year: int,
                   car_class: str,
                   location: str) -> Car:
        pass

    @abstractmethod
    def create_user(self,
                    id: int,
                    username: str,
                    dob: datetime,
                    phone_number: str,
                    password: str) -> User:
        pass

    @abstractmethod
    def create_contract(self,
                        contract_id: int,
                        car: Car,
                        user: User,
                        rent_start: datetime,
                        rent_end: datetime,
                        price: float) -> Contract:
        pass


# Конкретная фабрика
class ConcreteFactory(AbstractFactory):
    def create_car(self,
                   id: int,
                   brand: str,
                   model: str,
                   price: int,
                   year: int,
                   car_class: str,
                   location: str) -> Car:
        return Car(id, brand, model, price, year, car_class, location)

    def create_user(self,
                    id: int,
                    username: str,
                    dob: datetime,
                    phone_number: str,
                    password: str) -> User:
        return User(id, username, dob, phone_number, password)

    def create_contract(self,
                        contract_id: int,
                        car: Car,
                        user: User,
                        rent_start: datetime,
                        rent_end: datetime, price: float) -> Contract:
        return Contract(contract_id, car, user, rent_start, rent_end, price)


# Пример использования абстрактной фабрики
def main():
    # Создаем фабрику
    factory = ConcreteFactory()

    # Создаем автомобиль через фабрику
    car = factory.create_car(1,
                             "Tesla",
                             "Model S",
                             80000, 2024,
                             "Luxury",
                             "New York")

    # Создаем пользователя через фабрику
    user = factory.create_user(1,
                               "JohnDoe",
                               '1985-05-15',
                               "71234567890",
                               "password123")

    # Создаем контракт через фабрику
    contract = factory.create_contract(1,
                                       car,
                                       user,
                                       '2024-06-01',
                                       '2024-06-10',
                                       car.price)

    # Выводим информацию о контракте
    print(contract)


if __name__ == "__main__":
    main()

from abc import ABC, abstractmethod
from Users.users import User
from Cars.car_showroom import Car, CarShowroom
from datetime import datetime


class InvalidClientException(Exception):
    def __init__(self, message="Invalid client specified"):
        super().__init__(message)


class IMediator(ABC):
    @abstractmethod
    def rent_car(self,
                 car: Car,
                 client: User,
                 rent_start: datetime,
                 rent_end: datetime):
        pass

    @abstractmethod
    def return_car(self, car: Car, user: User):
        pass


class Contract:
    def __init__(self,
                 contract_id,
                 car: Car,
                 user: User,
                 rent_start: datetime,
                 rent_end: datetime,
                 price: float):
        self.contract_id = contract_id
        self.car = car
        self.user = user
        self.rent_start = rent_start
        self.rent_end = rent_end
        self.price = price

    def __str__(self):
        return f'''
        Contract #{self.contract_id} -
        Car: {self.car.model}, User: {self.user.username},
        Rent from {self.rent_start} to {self.rent_end}, Price: {self.price}
        '''


class Employee:
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name
        self.contracts = []

    def notify_about_new_contract(self, contract: Contract):
        self.contracts.append(contract)
        print(f"Employee {self.name} notified about new contract: {contract}")

    def get_contracts(self):
        return self.contracts


class RentalMediator(IMediator):
    def __init__(self, car_showroom: CarShowroom, employee: Employee):
        self.car_showroom = car_showroom
        self.employee = employee
        self.contract_id = 0

    def rent_car(self,
                 car: Car,
                 user: User,
                 rent_start: datetime,
                 rent_end: datetime):
        if car.get_status_rent():
            print(f"Car {car.model} is already rented.")
            return

        if not user.get_driver_license():
            raise InvalidClientException('''User doesn't have a valid
                                         driver's license.''')

        car.set_status_rent(True)
        user.add_car_rental(car.id)
        contract = Contract(self.contract_id,
                            car,
                            user,
                            rent_start,
                            rent_end,
                            car.price)
        self.employee.notify_about_new_contract(contract)
        self.contract_id += 1
        print(f"Car {car.model} rented to {user.username}.")

    def return_car(self, car: Car, user: User):
        if car.get_status_rent():
            car.set_status_rent(False)
            user.get_cars_rental().remove(car.id)
            print(f"Car {car.model} returned by {user.username}.")
        else:
            print(f"Car {car.model} is not rented.")


# Пример использования
if __name__ == "__main__":
    showroom = CarShowroom("Super Cars")
    employee = Employee(1, "Alice")
    mediator = RentalMediator(showroom, employee)

    # Добавление машин в автосалон
    car1 = Car(1, "Toyota", "Corolla", 10000, 2020, "C", "NY")
    car2 = Car(2, "Honda", "Civic", 12000, 2019, "C", "LA")

    showroom.add_car(car1)
    showroom.add_car(car2)

    # Создание пользователя
    user1 = User(1, "JohnDoe", "1990-01-01", "71234567890", "password123")
    user1.add_driver_license(123456)

    # Аренда машины
    mediator.rent_car(car1, user1, datetime.now(), datetime(2024, 12, 1))

    # Возврат машины
    mediator.return_car(car1, user1)

    # Просмотр контрактов сотрудником
    contracts = employee.get_contracts()
    for contract in contracts:
        print(contract)

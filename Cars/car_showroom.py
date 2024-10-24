from typing import List
from abc import ABC, abstractmethod


class ICarState(ABC):
    @abstractmethod
    def handle_rent(self, car, user):
        pass

    @abstractmethod
    def handle_return(self, car):
        pass


# Состояние: автомобиль свободен
class FreeState(ICarState):
    def handle_rent(self, car, user):
        # Логика при аренде автомобиля, если он свободен
        car.set_status_rent(True)
        car.set_state(RentedState())  # Переводим в состояние "арендован"
        print(f"Car {car.model} has been rented by {user.username}.")

    def handle_return(self, car):
        # Если автомобиль свободен, возврат невозможен
        print(f"Car {car.model} is already free. No need to return.")


# Состояние: автомобиль арендован
class RentedState(ICarState):
    def handle_rent(self, car, user):
        # Если автомобиль уже арендован, аренда невозможна
        print(f"Car {car.model} is already rented. Cannot rent again.")

    def handle_return(self, car):
        # Логика возврата арендованного автомобиля
        car.set_status_rent(False)
        car.set_state(FreeState())  # Переводим в состояние "свободен"
        print(f"Car {car.model} has been returned and is now available.")


# Интерфейс стратегии расчета аренды
class IRentalCalculationStrategy(ABC):
    @abstractmethod
    def calculate_rental_fees(self, car, hours: int) -> float:
        pass


# Стратегия расчета для электромобилей
class ElectricCarRentalStrategy(IRentalCalculationStrategy):
    def calculate_rental_fees(self, car, hours: int) -> float:
        # Пример расчета для электромобиля, например, по количеству часов
        return 100 * hours


# Стратегия расчета для автомобилей на бензине
class GasCarRentalStrategy(IRentalCalculationStrategy):
    def calculate_rental_fees(self, car, hours: int) -> float:
        # Пример расчета для бензинового автомобиля
        return 50 * hours


class Car:
    def __init__(self,
                 id: int,
                 brand: str,
                 model: str,
                 price: int,
                 year: int,
                 car_class: str,
                 location: str,
                 ):
        self.id = id
        self.brand = brand
        self.model = model
        self.price = price
        self.year = year
        self.car_class = car_class
        self.location = location
        self.grade = 0
        self.reviews: List[str] = list()
        self.status_rent = False
        self.state: ICarState = FreeState()
        self.strategy: IRentalCalculationStrategy

    def set_strategy(self, stratagy: IRentalCalculationStrategy):
        self.strategy = stratagy

    def set_state(self, state: ICarState):
        self.state = state

    def get_grade(self):
        return self.grade

    def set_grade(self, grade: int):
        self.grade = grade

    def get_reviews(self):
        return self.reviews

    def add_reviews(self, reviews: str):
        self.reviews.append(reviews)

    def delete_review(self, reviews: str):
        self.reviews.remove(reviews)

    def get_status_rent(self):
        return self.status_rent

    def set_status_rent(self, status_rent: bool):
        self.status_rent = status_rent

    def rent(self, user, hours: int):
        # Передаем управление состоянию автомобиля
        if self.strategy:
            rental_fee = self.strategy.calculate_rental_fees(self, hours)
            print(f"The rental fee for {self.model}"
                  f" for {hours} hours is ${rental_fee:.2f}")
        else:
            print("Rental calculation strategy not set!")
        self.state.handle_rent(self, user)

    def return_car(self):
        # Передаем управление состоянию автомобиля
        self.state.handle_return(self)


# Паттерн Singleton
class CarShowroom:
    _instance = None  # Переменная класса для хранения единственного экземпляра

    def __new__(cls, *args, **kwargs):
        if CarShowroom._instance is None:  # Если экземпляр еще не создан
            # Создаем экземпляр
            CarShowroom._instance = super(CarShowroom, cls).__new__(cls)
        return CarShowroom._instance  # Возвращаем единственный экземпляр

    def __init__(self, name):
        if not hasattr(self, 'initialized'):
            self.name = name
            self.cars = list()
            self.initialized = True

    def get_cars(self):
        return self.cars

    def add_car(self, car: Car):
        self.cars.append(car)

    def delete_car(self, car: Car):
        self.cars.remove(car)

    def get_available_cars(self):
        return [car for car in self.cars if car.get_status_rent()]

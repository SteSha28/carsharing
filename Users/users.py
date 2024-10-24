from abc import ABC, abstractmethod
from datetime import datetime


class ABCUser(ABC):
    '''Абстрактный класс пользователя.'''
    def __init__(self, id, username, dob, phone_number, password):
        if not isinstance(id, int):
            raise Exception('Wrong ID')
        if not username.isalpha():
            raise Exception('Wrong name')
        if not (phone_number.isdigit() and len(phone_number) == 11):
            raise Exception('Wrong phone number')
        if not self.check_correction_password(password):
            raise Exception('Uncorrect password')

        self.id = id
        self.username = username
        self.phone_number = phone_number
        self.password = password

        # Инициализация даты рождения
        try:
            self.dob = datetime.strptime(dob, '%Y-%m-%d')
        except ValueError:
            raise Exception('Wrong date of birthday')

    @staticmethod
    def check_correction_password(passwd):
        return len(passwd) >= 8 and \
            passwd.isalnum() and \
            passwd.strip() == passwd

    @abstractmethod
    def change_password(self, new_password):
        if self.check_correction_password(new_password):
            self.password = new_password
        else:
            raise Exception("Uncorrect password")


class User(ABCUser):
    '''Базовый класс пользователя'''
    def __init__(self, id, username, dob, phone_number, password):
        super().__init__(id, username, dob, phone_number, password)
        self.driver_license = None
        self.cars_for_rent = set()
        self.cars_rental = set()
        self.grade = 0
        self.reviews = list()

    def get_driver_license(self):
        return self.driver_license

    def add_driver_license(self, driver_license: int):
        self.driver_license = driver_license

    def delete_driver_license(self):
        del self.driver_license

    def get_cars_for_rent(self):
        return self.cars_for_rent

    def add_car_for_rent(self, car_for_rent: int):
        self.cars_for_rent.add(car_for_rent)

    def delete_cars_for_rent(self):
        self.cars_for_rent.clear()

    def get_cars_rental(self):
        return self.cars_rental

    def add_car_rental(self, cars_rental: int):
        self.cars_rental.add(cars_rental)

    def delete_cars_rental(self):
        self.cars_rental.clear()

    def get_grade(self):
        return self.grade

    def set_grade(self, grade: int):
        self.grade = grade

    def get_reviews(self):
        return self.reviews

    def add_review(self, reviews: str):
        self.reviews.append(reviews)

    def delete_review(self, reviews: str):
        self.reviews.remove(reviews)

    def change_password(self, new_password):
        if User.check_correction_password(new_password):
            self.password = new_password
        else:
            raise Exception("Uncorrect password")

from Cars.car_showroom import Car
from Users.users import User


class CarRentalProxy:
    def __init__(self, real_car: Car):
        self._real_car = real_car

    def get_status_rent(self):
        # Проверка доступности автомобиля через прокси
        if self._real_car.get_status_rent():
            print(f"Car {self._real_car.model} is already rented.")
            return False
        else:
            return True

    def set_status_rent(self, status_rent: bool):
        # Дополнительная логика перед изменением статуса аренды
        if not self.get_status_rent() and status_rent:
            print(f"Car {self._real_car.model} is now rented.")
        self._real_car.set_status_rent(status_rent)

    def rent_car(self, user: User):
        # Дополнительная проверка, например, наличие прав у пользователя
        if not user.get_driver_license():
            raise Exception("User doesn't have a valid driver's license.")

        # Если автомобиль доступен, арендуем его
        if self.get_status_rent():
            self.set_status_rent(True)
            user.add_car_rental(self._real_car.id)
            print(f'Car {self._real_car.model} has '
                  f'been rented by {user.username}.')
        else:
            print(f"Car {self._real_car.model} is not available for rent.")

    def return_car(self, user: User):
        # Проверяем, арендован ли автомобиль и возвращаем его
        if self._real_car.get_status_rent():
            self._real_car.set_status_rent(False)
            user.get_cars_rental().remove(self._real_car.id)
            print(f"Car {self._real_car.model} returned by {user.username}.")
        else:
            print(f"Car {self._real_car.model} is not currently rented.")


# Пример использования прокси для класса Car
car = Car(id=1,
          brand="Toyota",
          model="Camry",
          price=100,
          year=2020,
          car_class="Sedan",
          location="New York")
user = User(id=1,
            username="JohnDoe",
            dob="1990-01-01",
            phone_number="71234567890",
            password="securepassword")
user.add_driver_license(34567)

car_proxy = CarRentalProxy(car)

# Попытка арендовать автомобиль через прокси
car_proxy.rent_car(user)

# Попытка вернуть автомобиль через прокси
car_proxy.return_car(user)

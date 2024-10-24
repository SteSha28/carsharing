import unittest
from Users.users import User
from Cars.car_showroom import CarShowroom, Car


class TestUser(unittest.TestCase):
    def test_create_user(self):
        """Проверка создания пользователя с корректными данными."""
        user = User(1,
                    "JohnDoe",
                    "1990-05-15",
                    "12345678901",
                    "password123")
        self.assertEqual(user.username, "JohnDoe")
        self.assertEqual(user.phone_number, "12345678901")
        self.assertEqual(user.get_grade(), 0)

    def test_change_password(self):
        """Проверка изменения пароля пользователя."""
        user = User(2,
                    "JaneDoe",
                    "1985-08-10",
                    "09876543210",
                    "password123")
        user.change_password("newpass456")
        self.assertEqual(user.password, "newpass456")

    def test_invalid_phone_number(self):
        """Проверка ошибки при неверном номере телефона."""
        with self.assertRaises(Exception) as context:
            User(3,
                 "Tom",
                 "1993-01-01",
                 "12345",
                 "password123")
        self.assertTrue("Wrong phone number" in str(context.exception))

    def test_review_management(self):
        """Проверка управления отзывами пользователя."""
        user = User(4,
                    "Alice",
                    "1995-10-20",
                    "12345678901",
                    "password123")
        user.add_review("Great service!")
        self.assertIn("Great service!", user.get_reviews())

    def test_add_multiple_reviews(self):
        """Проверка добавления нескольких отзывов."""
        user = User(5,
                    "Bob",
                    "1992-12-15",
                    "12345678901",
                    "password123")
        user.add_review("Good car!")
        user.add_review("Nice experience!")
        self.assertEqual(len(user.get_reviews()), 2)

    def test_change_password_invalid(self):
        """Проверка изменения пароля с неверным форматом."""
        user = User(6,
                    "Charlie",
                    "1988-02-10",
                    "12345678901",
                    "password123")
        with self.assertRaises(Exception) as context:
            user.change_password("short")
        self.assertTrue("Uncorrect password" in str(context.exception))


class TestCar(unittest.TestCase):
    def test_create_car(self):
        """Проверка создания автомобиля."""
        car = Car(1,
                  "Toyota",
                  "Camry",
                  25000,
                  2020,
                  "Business",
                  "NY")
        self.assertEqual(car.brand, "Toyota")
        self.assertEqual(car.model, "Camry")
        self.assertEqual(car.get_grade(), 0)

    def test_add_review_to_car(self):
        """Проверка добавления отзыва к автомобилю."""
        car = Car(2,
                  "Honda",
                  "Civic",
                  27000,
                  2021,
                  "Business",
                  "LA")
        car.add_reviews("Great car!")
        self.assertIn("Great car!", car.get_reviews())

    def test_add_car_to_showroom(self):
        """Проверка добавления автомобиля в автосалон."""
        showroom = CarShowroom("Luxury Cars")
        car = Car(3,
                  "Mercedes",
                  "S-Class",
                  80000,
                  2022,
                  "Luxury",
                  "NY")
        showroom.add_car(car)
        self.assertIn(car, showroom.get_cars())


if __name__ == '__main__':
    unittest.main()

from django.test import TestCase
from ..models import *


def run_field_parameter_test(
        model, self_,
        field_and_parameter_value: dict,
        parameter_name: str) -> None:
    """Тестирует значение параметра для всех объектов модели"""

    for instance in model.objects.all():
        for field, expected_value in field_and_parameter_value.items():
            parameter_real_value = getattr(
                instance._meta.get_field(field), parameter_name
            )

            self_.assertEqual(parameter_real_value, expected_value)


class TestVerboseNameMixin:
    """Миксин для проверки verbose_name"""

    def run_verbose_name_test(self, model):
        """Метод, тестирующий verbose_name"""

        run_field_parameter_test(
            model, self, self.field_and_verbose_name, 'verbose_name'
        )


class TestMaxLengthMixin:
    """Миксин для проверки max_length"""

    def run_max_length_test(self, model):
        """Метод, тестирующий max_length"""

        run_field_parameter_test(
            model, self, self.field_and_max_length, 'max_length'
        )


class AccountTests(TestCase, TestVerboseNameMixin, TestMaxLengthMixin):
    """Тесты для модели Account"""
    @classmethod
    def setUpTestData(cls):
        User.objects.create(id=1)
        cls.account = Account.objects.create(firstname='Роман', secondname='Фролов', user_id=1)
        cls.account_field = cls.account._meta.get_field('firstname')
        cls.field_and_verbose_name = {
            'firstname': 'Имя',
        }
        cls.field_and_max_length = {
            'firstname': 255,
        }

    def test_string_representation(self):
        """Тест строки"""

        self.assertEqual(str(self.account), str(self.account.secondname))

    def test_model_verbose_name(self):
        """Тест поля verbose_name модели Account"""

        self.assertEqual(Account._meta.verbose_name, 'Учетная запись')

    def test_model_verbose_name_plural(self):
        """Тест поля verbose_name_plural модели Account"""

        self.assertEqual(Account._meta.verbose_name_plural, 'Учётные записи')

    def test_verbose_name(self):
        """Тест параметра verbose_name"""

        super().run_verbose_name_test(Account)

    def test_max_length(self):
        """Тест параметра max_length"""

        super().run_max_length_test(Account)


class CarTests(TestCase, TestVerboseNameMixin, TestMaxLengthMixin):

    @classmethod
    def setUpTestData(cls):
        cls.car = Car.objects.create(name='БМВ', vin='ZFA22300005556777')
        cls.car_field = cls.car._meta.get_field('name')
        cls.field_and_verbose_name = {
            'name': 'Название',
        }
        cls.field_and_max_length = {
            'name': 255,
        }

    def test_string_representation(self):
        """Тест строки представления"""

        self.assertEqual(str(self.car), str(self.car.name))

    def test_model_verbose_name(self):
        """Тест поля verbose_name модели Car"""

        self.assertEqual(Car._meta.verbose_name, 'Автомобиль')

    def test_model_verbose_name_plural(self):
        """Тест поля verbose_name_plural модели Car"""

        self.assertEqual(Car._meta.verbose_name_plural, 'Автомобили')

    def test_verbose_name(self):
        """Тест параметра verbose_name"""

        super().run_verbose_name_test(Car)

    def test_max_length(self):
        """Тест параметра max_length"""

        super().run_max_length_test(Car)








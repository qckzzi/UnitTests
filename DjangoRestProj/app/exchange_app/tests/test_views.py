from django.test import TestCase
from ..views import *

EMAIL_AND_DOMAIN = {
    'test1@gmail.com': 'gmail.com',
    'test2@wrong_email': 'wrong_email',
    'test3@mail.ru': 'mail.ru',
    'test4@@wrong_email.com': '',
}


class MethodsTests(TestCase):
    """Класс с тестами функций"""

    def test_get_domain(self):
        """Тест функции get_domain"""

        for email, expected_doamin in EMAIL_AND_DOMAIN.items():
            with self.subTest(f'{email=}'):
                real_domain = get_domain(email)

                self.assertEqual(real_domain, expected_doamin)





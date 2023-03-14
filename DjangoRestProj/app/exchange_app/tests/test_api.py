from rest_framework.test import APITestCase
from rest_framework import status

DOMAIN = 'http://127.0.0.1:8000/'

URLS = (
    '',
    'api/v1/account/',
    'api/v1/cars/',
)

URLS = (DOMAIN + page for page in URLS)


class APITests(APITestCase):
    """Класс с тестами API"""

    def test_status_code(self):
        """Тест статус-кода"""

        for page in URLS:
            with self.subTest(f'{page=}'):
                response = self.client.get(page)
                self.assertEqual(response.status_code, status.HTTP_200_OK)

"""Модуль для валидации полей в json-схемах"""


class ValidationOfFields:

    @staticmethod
    def check_that_https_in_link(web_link):
        """Метод проверяет, что в заданном поле присутствует 'https://'

        Args:
            web_link: поле, содержащее веб-ссылку
        """

        if 'https://' in web_link:
            return web_link
        else:
            raise ValueError(f'Не валидное поле: {web_link}')

    @staticmethod
    def check_that_dog_presented_in_email_adress(email):
        """Метод проверяет, что в заданном поле присутствует символ '@'

        Args:
            email: поле, содержащее адрес электронной почты
        """

        if '@' in email:
            return email
        else:
            raise ValueError(f'Не валидное поле: {email}')

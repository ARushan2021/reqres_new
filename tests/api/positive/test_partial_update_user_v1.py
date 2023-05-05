"""Позитивный тест"""
import pytest
import allure

from api.reqres.common import Common
from schemas.put_patch import PutPatch


@pytest.mark.usefixtures('clear_test_reports_and_logs')
@allure.epic('Позитивное тестирование портала "https://reqres.in/"')
@pytest.mark.parametrize('id_user, body_request',
                         [('8', f'{Common.REQUEST_BODY_UPDATE}'),
                          ('9', f'{Common.REQUEST_BODY_UPDATE2}')])
def test_partial_update_user_v1(base, id_user, body_request):
    """Позитивный тест. Запрос информации о пользователе.

    Шаг 1. Отправка запроса. PATCH https://reqres.in/api/users/2
    Шаг 2. Проверка статус кода
    Шаг 3. Проверка тела ответа
    Шаг 4. Проверка времени ответа на запрос
    """

    response = base.api_v1.patch_api_users(id_user=id_user, body_request=body_request)
    base.asserts.assert_request(response=response, exp_status_code=200, json_schema=PutPatch)


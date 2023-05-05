"""Позитивный тест"""
import pytest
import allure

from api.reqres.common import Common
from schemas.put_patch import PutPatch


@pytest.mark.usefixtures('clear_test_reports_and_logs')
@allure.severity('CRITICAL')
@allure.feature('Positive keys')
@allure.epic('API Тестирование портала "https://reqres.in/"')
@pytest.mark.parametrize('id_user, body_request',
                         [('8', f'{Common.REQUEST_BODY_UPDATE}'),
                          ('9', f'{Common.REQUEST_BODY_UPDATE2}')])
@allure.title('Изменение всех параметров пользователя')
def test_partial_update_user_v1(base, id_user, body_request):

    response = base.api_v1.put_api(id_user=id_user, body_request=body_request, res_api=Common.RESOURCE_USERS)
    base.asserts.assert_request(response=response, exp_status_code=200, json_schema=PutPatch)


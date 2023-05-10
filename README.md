# Проект по тестированию reqres.ru
- API-запросы:
- 5 позитивных кейсов, по одноу запросу в каждом кейсе.
- 5 негативных кейсов, в 4-х по одному запросу и в одном два запроса.

- Во всех кейсах проверяется на json-схему в body response (если в body пусто, значит проверяется, что пусто).
- Некоторые поля в json-схеме проверяются на валидность значений.
- Проверяется статус код.
- Проверяется время response, должно быть не более 2-х сек.
- Пишутся логи по всем запросам.
- Формируется allure отчет.
*****
- Web тестирование reqres.ru:
- 5 позитивный кейсов, во всех кейсах проверяется:
- заголовок страницы
- статус код
- json-схема, некоторые поля в json-схеме проверяются на валидность значений.
*****
- Web тестирование swagger reqres.ru:
- один позитивный и один негативный кейс
- во всех кейсах проверяется:
- заголовок страницы
- статус код и тело ответа сравнивается с аналогичными api запросами
*****
- pytest 7.3.0
- requests 2.28.2
- pydantic 1.10.7
- allure-pytest 2.13.1
*****
- pytest tests/ --alluredir=./test_reports/

- pytest tests/api/negative/ -v -s --alluredir=./test_reports/
- pytest tests/api/positive/ -v -s --alluredir=./test_reports/
- pytest tests/web/reqres/ -v -s --alluredir=./test_reports/
- pytest tests/web/swagger/ -v -s --alluredir=./test_reports/

- allure serve test_reports - формирование allure в html
*****

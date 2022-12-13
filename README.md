Files
-----

[conftest.py](conftest.py) Код для перехвата неудачных тестов и создание скриншота страницы

[pages/base.py](pages/base.py) Шаблон для реализации страницы на Python

[pages/auth_page.py](pages/auth_page.py) Страница для авторизации работы с автотестами на Python

[pages/registration_page.py](pages/registration_page.py) Страница для авторизации работы с автотестами
w
[pages/elements.py](pages/elements.py) содержит вспомогательный класс для определения веб-элементов на веб-страницах.

[autotests_rostelecom.py](autotests_rostelecom.py) Тест веб-интерфейса (https://b2c.passport.rt.ru/)



How To Run Tests
----------------

1) Install all requirements:


    pip install -r requirements.txt


2) Download Selenium WebDriver from https://chromedriver.chromium.org/downloads (choose version which is compatible with your browser)

3) Run tests:

    pytest -v --driver Chrome --driver-path /chromedriver autotests_rostelecom.py

Autotests description
-----
**test_start_page_is_correct**

Тест-кейс 1 Корректное отображение "Стандартной страницы авторизации"


**test_location_of_page_blocks**

Тест-кейс 2  Проверка элементов в левом и правом блоке страницы
Тест не проходит (Bug-1).Причина - расположение элементов на странице не соответствует ТЗ


**test_phone_tab**

Тест-кейс 3 Проверка названия вкладки "Номер"
Тест не проходит (Bug-3).Причина - Вкладка 'Номер' не соответствует ТЗ (вкладка "Телефон" вместо "Номер")


**test_registration_page_and_continue_button**

Тест-кейс 4 Проверка названия кнопки "Продолжить" в форме "Регистрация"
Тест не проходит (Bug-4). Причина - Кнопка должна иметь текст 'Продолжить'


**test_registration_page_with_empty_name_field**

Тест-кейс 5 Регистрация пользователя с пустым полем "Имя", появления текста с подсказкой об ошибке


**test_registration_with_an_incorrect_value_in_the_name_field**

Тест-кейс 6 Регистрация пользователя со значением в поле "Имя" меньше 2 символов, появление текста с подсказкой об ошибке


**test_registration_with_an_incorrect_value_in_the_last_name_field**

Тест-кейс 7 Регистрация пользователя со значением в поле "Фамилия" превышающим 30 символов), появление текста с подсказкой об ошибке


**test_registration_of_an_already_registered_user**

Тест-кейс 8 Регистрация пользователя с уже зарегистрированным номером, появление оповещения


**test_notification_form**

 Тест-кейс 9 Проверка значка "х" - закрыть всплывающее окно оповещения
Тест не проходит (Bug-4). Причина - "Должна быть кнопка закрыть 'х'"


**test_incorrect_password_during_registration**

Тест-кейс 10  При регистрации пользователя введен пароль содержащий менее 8 символов, появление текста с подсказкой об ошибке


**test_instead_of_cyrillic_invalid_characters**

Тест-кейс 11 При регистрация пользователя в поле "Фамилия" введено значение, содержащее недопустимые символы вместо кириллицы



**test_password_and_password_confirmation_do_not_match**

Тест-кейс 12 Значения в поле ввода "Пароль" и поле ввода "Подтверждение пароля" в форме "Регистрация" не совпадают


**test_invalid_email_or_mobile_phone**

Тест-кейс 13 Не валидный email в поле ввода "Email или мобильный телефон" в форме регистрация


**test_authorization_of_a_user_with_an_invalid_password**

Тест-кейс 14 Вход по неправильному паролю в форме "Авторизация" уже зарегистрированного пользователя, надпись "Забыл пароль"
перекрашивается в оранжевый цвет


**test_authorisation_valid**

Тест-кейс 15 Тестирование аутентификации зарегистрированного пользователя

**test_authorisation_vk**

Тест-кейс 16 Тестирование аутентификации зарегистрированного пользователя через ВК

**test_authorisation_ok**

Тест-кейс 17 Тестирование аутентификации зарегистрированного пользователя через OK

**test_authorisation_mail**

Тест-кейс 18 Тестирование аутентификации зарегистрированного пользователя через Mail

**test_authorisation_google**

Тест-кейс 19 Тестирование аутентификации зарегистрированного пользователя через Google

**test_authorisation_ya**

Тест-кейс 20 Тестирование аутентификации зарегистрированного пользователя через Yandex



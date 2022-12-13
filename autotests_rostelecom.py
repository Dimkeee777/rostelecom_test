import pytest

from pages.auth_page import AuthPage
from pages.registration_page import RegPage


# Тест-кейс 1
# Корректное отображение "Стандартной страницы авторизации"
def test_start_page_is_correct(web_browser):
    page = AuthPage(web_browser)
    phone_tab_class = page.phone_tab.get_attribute("class")
    assert phone_tab_class == "rt-tab rt-tab--small rt-tab--active"
    assert page.phone.is_clickable()
    assert page.password.is_clickable()
    assert page.btn_login.is_clickable()
    assert page.registration_link.is_clickable()
    assert page.auth_title.get_text() == "Авторизация"
    assert page.logo_lk.get_text() == "Личный кабинет"


# Тест-кейс 2 (Bug-1)
# Проверка элементов в левом и правом блоке страницы
@pytest.mark.xfail(reason="Расположение элементов на странице не соответсвует ТЗ")
def test_location_of_page_blocks(web_browser):
    page = AuthPage(web_browser)
    assert page.auth_form.find(timeout=1)
    assert page.lk_form.find(timeout=1)


# Тест-кейс 3(Bug-2)
# Проверка названия вкладки "Номер"
@pytest.mark.xfail(reason="Название вкладки 'Номер' не соответствует ТЗ")
def test_phone_tab(web_browser):
    page = AuthPage(web_browser)
    assert page.phone_tab.get_text() == "Номер"


# Тест-кейс 4(Bug-3)
# Проверка названия кнопки "Продолжить" в форме "Регистрация"
@pytest.mark.xfail(reason="Кнопка должна иметь текст 'Продолжить'")
def test_registration_page_and_continue_button(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    assert reg_page.name_field_text.get_text() == "Имя"
    assert reg_page.last_name_field_text.get_text() == "Фамилия"
    assert reg_page.region_field_text.get_text() == "Регион"
    assert reg_page.email_or_mobile_phone_field_text.get_text() == "E-mail или мобильный телефон"
    assert reg_page.password_field_text.get_text() == "Пароль"
    assert reg_page.password_confirmation_field_text.get_text() == "Подтверждение пароля"
    assert reg_page.continue_button.get_text() == "Продолжить"


# Тест-кейс 5
# Регистрация пользователя с пустым полем "Имя", появления текста с подсказкой об ошибке
def test_registration_page_with_empty_name_field(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys('')
    reg_page.last_name_field.send_keys("Салихов")
    reg_page.email_or_mobile_phone_field.send_keys("lbtumatym1@gmai.com")
    reg_page.password_field.send_keys("1227341dD")
    reg_page.password_confirmation_field.send_keys("1227341dD")
    reg_page.continue_button.click()
    reg_page.error_message_name.is_visible()
    assert reg_page.error_message_name.get_text() == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."


# Тест-кейс 6
# Регистрация пользователя со значением в поле "Имя" меньше 2 символов, появление текста с подсказкой об ошибке
def test_registration_with_an_incorrect_value_in_the_name_field(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys('Н')
    reg_page.last_name_field.send_keys("Салихов")
    reg_page.email_or_mobile_phone_field.send_keys("lbtumatym1@gmai.com")
    reg_page.password_field.send_keys("1227341dD")
    reg_page.password_confirmation_field.send_keys("1227341dD")
    reg_page.continue_button.click()
    reg_page.error_message_name.is_visible()
    assert reg_page.error_message_name.get_text() == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."


# Тест-кейс 7
# Регистрация пользователя со значением в поле "Фамилия" превышающим 30 символов), появление текста с подсказкой об ошибке
def test_registration_with_an_incorrect_value_in_the_last_name_field(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys("Наталья")
    reg_page.last_name_field.send_keys("ловпоаплыоалваоывлоалвыоалоаловавлыо")
    reg_page.email_or_mobile_phone_field.send_keys("lbtumatym1@gmai.com")
    reg_page.password_field.send_keys("1227341dD")
    reg_page.password_confirmation_field.send_keys("1227341dD")
    reg_page.continue_button.click()
    reg_page.error_message_name.is_visible()
    assert reg_page.error_message_last_name.get_text() == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."


# Тест-кейс 8
# Регистрация пользователя с уже зарегистрированным номером, появление оповещения
def test_registration_of_an_already_registered_user(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys("Дмитрий")
    reg_page.last_name_field.send_keys("Салихов")
    reg_page.email_or_mobile_phone_field.send_keys("+79153218182")
    reg_page.password_field.send_keys("142536Hn")
    reg_page.password_confirmation_field.send_keys("142536Hn")
    reg_page.continue_button.click()
    assert reg_page.notification_form.is_visible


# Тест-кейс 9(Bug-4)
# Проверка значка "х" - закрыть всплывающее окно оповещения
@pytest.mark.xfail(reason="Должен быть значок закрыть 'х'")
def test_notification_form(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys("Дмитрий")
    reg_page.last_name_field.send_keys("Салихов")
    reg_page.email_or_mobile_phone_field.send_keys("+79153218182")
    reg_page.password_field.send_keys("1227341dD")
    reg_page.password_confirmation_field.send_keys("1227341dD")
    reg_page.continue_button.click()
    assert reg_page.login_button.get_text() == 'Войти'
    assert reg_page.recover_password_button.get_text() == 'Восстановить пароль'
    assert reg_page.close_button.get_text() == 'x'


# Тест-кейс 10
#  При регистрации пользователя введен пароль содержащий менее 8 символов, появление текста с подсказкой об ошибке
def test_incorrect_password_during_registration(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys("Олег")
    reg_page.last_name_field.send_keys("Никитин")
    reg_page.email_or_mobile_phone_field.send_keys("g.nikitin@mail.ru")
    reg_page.password_field.send_keys("Osm123")
    reg_page.password_confirmation_field.send_keys("Osm123")
    reg_page.continue_button.click()
    assert reg_page.error_message_password.get_text() == "Длина пароля должна быть не менее 8 символов"


# Тест-кейс 11
# При регистрация пользователя в поле "Фамилия" введено значение, содержащее недопустимые символы вместо кириллицы
def test_instead_of_cyrillic_invalid_characters(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys("Дмитрий")
    reg_page.last_name_field.send_keys("!!!@@@")
    reg_page.email_or_mobile_phone_field.send_keys("lbtumatym1@gmail.com")
    reg_page.password_field.send_keys("1227341dD")
    reg_page.password_confirmation_field.send_keys("1227341dD")
    reg_page.continue_button.click()
    assert reg_page.message_must_be_filled_in_cyrillic.get_text() == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."


# Тест-кейс 12
# Значения в поле ввода "Пароль" и поле ввода "Подтверждение пароля" в форме "Регистрация" не совпадают
def test_password_and_password_confirmation_do_not_match(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys("Дмитрий")
    reg_page.last_name_field.send_keys("Салихов")
    reg_page.email_or_mobile_phone_field.send_keys("lbtumatym1@gmail.com")
    reg_page.password_field.send_keys("Qwerty123")
    reg_page.password_confirmation_field.send_keys("Qwerty123456")
    reg_page.continue_button.click()
    assert reg_page.message_passwords_dont_match.get_text() == "Пароли не совпадают"


# Тест-кейс 13
# Не валидный email в поле ввода "Email или мобильный телефон" в форме регистрация
def test_invalid_email_or_mobile_phone(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys("Дмитрий")
    reg_page.last_name_field.send_keys("Салихов")
    reg_page.email_or_mobile_phone_field.send_keys("lbtumatym.gmail.com")
    reg_page.password_field.send_keys("Qwerty123")
    reg_page.password_confirmation_field.send_keys("Qwerty123")
    reg_page.continue_button.click()
    assert reg_page.message_enter_the_phone_in_the_format.get_text() == "Введите телефон в формате +7ХХХХХХХХХХ или" \
                                                                        " +375XXXXXXXXX, или email в формате example@email.ru"


# Тест-кейс 14
# Вход по неправильному паролю в форме "Авторизация" уже зарегистрированного пользователя, надпись "Забыл пароль"
# перекрашивается в оранжевый цвет
def test_authorization_of_a_user_with_an_invalid_password(web_browser):
    page = AuthPage(web_browser)
    page.phone.send_keys('+79777777777')
    page.password.send_keys("Test")
    page.btn_login.click()
    assert page.message_invalid_username_or_password.get_text() == "Неверный логин или пароль"
    assert "rt-link--orange" in page.the_element_forgot_the_password.get_attribute('class')


# Тест-кейс 15
# Тестирование аутентификации зарегестрированного пользователя
def test_authorisation_valid(web_browser):
    page = AuthPage(web_browser)
    page.phone.send_keys("+9153218182")
    page.password.send_keys("1227341dD")
    page.btn_login.click()

    assert 'https://b2c.passport.rt.ru/account_b2c/page?state=' in page.get_current_url() \
           and '&client_id=account_b2c#/' in page.get_current_url()

# Тест-кейс 16
# Открытие Регистрации через VK
def test_authorisation_vk(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link_vk.click()

# Тест-кейс 17
# Открытие Регистрации через Однаклассники
def test_authorisation_ok(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link_ok.click()

# Тест-кейс 18
# Открытие Регистрации через mail.ru
def test_authorisation_mail(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link_mail.click()

# Тест-кейс 19
# Открытие Регистрации через google
def test_authorisation_google(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link_google.click()

# Тест-кейс 20
# Открытие Регистрации через yandex
def test_authorisation_yandex(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link_yandex.click()
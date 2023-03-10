import pytest

from auth_page28 import AuthPage
from registration_page28 import RegPage

""" запуск тестов на моем компе из терминала PyCharm: pytest -v --driver Chrome --driver-path D:/chromedriver.exe tests/test_rostelecom.py"""

# Тест-кейс N-01
# Корректное отображение "Стандартной страницы авторизации"
def test_start_page_is_correct(web_browser):
    """ Make sure main auth page opens fine. """
    page = AuthPage(web_browser)
    phone_tab_class = page.phone_tab.get_attribute("class")
    assert phone_tab_class == "rt-tab rt-tab--small rt-tab--active"
    assert page.phone.is_clickable()
    assert page.password.is_clickable()
    assert page.btn_login.is_clickable()
    assert page.registration_link.is_clickable()
    assert page.auth_title.get_text() == "Авторизация"
    assert page.logo_lk.get_text() == "Личный кабинет"

# Тест-кейс N-02 (Bugs-01)
# Проверка названия таб выбора "Номер"
@pytest.mark.xfail(reason="Таб выбора 'Номер' не соответсвует ожидаемым требованиям (вместо 'номер' указан 'телефон') ")
def test_phone_tab(web_browser):
    """ Make sure phone tab name is correct. """
    page = AuthPage(web_browser)
    assert page.phone_tab.get_text() == "Номер"

# Тест-кейс N-03 (Bugs-02)
# Проверка название кнопки "Продолжить" в форме "Регистрация"
@pytest.mark.xfail(reason="Кнопка должна иметь текст 'Продолжить', вместо него указан текст - 'Зарегистрироваться' ")
def test_registration_page_and_continue_button(web_browser):
    """ Make sure Continue button name is correct. """
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

# Тест-кейс N-04
# Регистрация пользователя с пустым полем "Имя", появление текста с подсказкой об ошибке
def test_registration_page_with_empty_name_field(web_browser):
    """ Test Registration with an empty name field. """
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys('')
    reg_page.last_name_field.send_keys("Фамилия")
    reg_page.email_or_mobile_phone_field.send_keys("test123@mail.ru")
    reg_page.password_field.send_keys("Qazwsx1124")
    reg_page.password_confirmation_field.send_keys("Qazwsx1124")
    reg_page.continue_button.click()
    reg_page.error_message_name.is_visible()
    assert reg_page.error_message_name.get_text() == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."

# Тест-кейс N-05
# Регистрация пользователя с некорректным значением в поле "Имя"(< 2 символов), появление текста с подсказкой об ошибке
def test_registration_with_a_low_value_in_the_name_field(web_browser):
    """ Test Registration with a short text in the name field. """
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys('А')
    reg_page.last_name_field.send_keys("Фамилия")
    reg_page.email_or_mobile_phone_field.send_keys("test123@mail.ru")
    reg_page.password_field.send_keys("Qazwsx1124")
    reg_page.password_confirmation_field.send_keys("Qazwsx1124")
    reg_page.continue_button.click()
    reg_page.error_message_name.is_visible()
    assert reg_page.error_message_name.get_text() == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."

# Тест-кейс N-06
# Регистрация пользователя с некорректным значением в поле "Имя"(> 30 символов), появление текста с подсказкой об ошибке
def test_registration_with_a_long_value_in_the_name_field(web_browser):
    """ Test Registration with a long text in the name field. """
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys('Афывапролджфывапролджфывапролджфыва')
    reg_page.last_name_field.send_keys("Фамилия")
    reg_page.email_or_mobile_phone_field.send_keys("test123@mail.ru")
    reg_page.password_field.send_keys("Qazwsx1124")
    reg_page.password_confirmation_field.send_keys("Qazwsx1124")
    reg_page.continue_button.click()
    reg_page.error_message_name.is_visible()
    assert reg_page.error_message_name.get_text() == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."

# Тест-кейс N-07
# Регистрация пользователя с некорректным значением в поле "Имя"(латинские символы), появление текста с подсказкой об ошибке
def test_registration_with_a_latin_letters_in_the_name_field(web_browser):
    """ Test Registration with a latin text in the name field. """
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys('Jacob')
    reg_page.last_name_field.send_keys("Фамилия")
    reg_page.email_or_mobile_phone_field.send_keys("test123@mail.ru")
    reg_page.password_field.send_keys("Qazwsx1124")
    reg_page.password_confirmation_field.send_keys("Qazwsx1124")
    reg_page.continue_button.click()
    reg_page.error_message_name.is_visible()
    assert reg_page.error_message_name.get_text() == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."

# Тест-кейс N-08
# Регистрация пользователя с некорректным значением в поле "Имя"(спецсимволы), появление текста с подсказкой об ошибке
def test_registration_with_special_symbols_in_the_name_field(web_browser):
    """ Test Registration with special symbols in the name field. """
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys('~!@#$%^&*()')
    reg_page.last_name_field.send_keys("Фамилия")
    reg_page.email_or_mobile_phone_field.send_keys("test123@mail.ru")
    reg_page.password_field.send_keys("Qazwsx1124")
    reg_page.password_confirmation_field.send_keys("Qazwsx1124")
    reg_page.continue_button.click()
    reg_page.error_message_name.is_visible()
    assert reg_page.error_message_name.get_text() == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."

# Тест-кейс N-09
# Регистрация пользователя с некорректным значением в поле "Имя"(цифры), появление текста с подсказкой об ошибке
def test_registration_with_a_figures_in_the_name_field(web_browser):
    """ Test Registration with a figures in the name field. """
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys('1234567890')
    reg_page.last_name_field.send_keys("Фамилия")
    reg_page.email_or_mobile_phone_field.send_keys("test123@mail.ru")
    reg_page.password_field.send_keys("Qazwsx1124")
    reg_page.password_confirmation_field.send_keys("Qazwsx1124")
    reg_page.continue_button.click()
    reg_page.error_message_name.is_visible()
    assert reg_page.error_message_name.get_text() == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."

# Тест-кейс N-10
# Регистрация пользователя с пустым полем "Фамилия", появления текста с подсказкой об ошибке
def test_registration_page_with_empty_family_field(web_browser):
    """ Test Registration with an empty family field. """
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys('Сергей')
    reg_page.last_name_field.send_keys("")
    reg_page.email_or_mobile_phone_field.send_keys("test123@mail.ru")
    reg_page.password_field.send_keys("Qazwsx1124")
    reg_page.password_confirmation_field.send_keys("Qazwsx1124")
    reg_page.continue_button.click()
    reg_page.error_message_name.is_visible()
    assert reg_page.error_message_last_name.get_text() == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."

# Тест-кейс N-11
# Регистрация пользователя с некорректным полем "Фамилия" (< 2 знаков), появление текста с подсказкой об ошибке
def test_registration_page_with_short_family_field(web_browser):
    """ Test Registration with a short family field. """
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys('Сергей')
    reg_page.last_name_field.send_keys("А")
    reg_page.email_or_mobile_phone_field.send_keys("test123@mail.ru")
    reg_page.password_field.send_keys("Qazwsx1124")
    reg_page.password_confirmation_field.send_keys("Qazwsx1124")
    reg_page.continue_button.click()
    reg_page.error_message_name.is_visible()
    assert reg_page.error_message_last_name.get_text() == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."

# Тест-кейс N-12
# Регистрация пользователя с некорректным полем "Фамилия" (> 30 знаков), появление текста с подсказкой об ошибке
def test_registration_page_with_long_family_field(web_browser):
    """ Test Registration with a long family field. """
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys('Сергей')
    reg_page.last_name_field.send_keys("Афывапролджфывапролджфывапролджфыва")
    reg_page.email_or_mobile_phone_field.send_keys("test123@mail.ru")
    reg_page.password_field.send_keys("Qazwsx1124")
    reg_page.password_confirmation_field.send_keys("Qazwsx1124")
    reg_page.continue_button.click()
    reg_page.error_message_name.is_visible()
    assert reg_page.error_message_last_name.get_text() == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."

# Тест-кейс N-13
# Регистрация пользователя с некорректным полем "Фамилия" (латинские буквы), появление текста с подсказкой об ошибке
def test_registration_page_with_latin_letters_in_family_field(web_browser):
    """ Test Registration with a latin letters in family field. """
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys('Сергей')
    reg_page.last_name_field.send_keys("Steinitz")
    reg_page.email_or_mobile_phone_field.send_keys("test123@mail.ru")
    reg_page.password_field.send_keys("Qazwsx1124")
    reg_page.password_confirmation_field.send_keys("Qazwsx1124")
    reg_page.continue_button.click()
    reg_page.error_message_name.is_visible()
    assert reg_page.error_message_last_name.get_text() == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."

# Тест-кейс N-14
# Регистрация пользователя с некорректным полем "Фамилия" (спецсимволы), появление текста с подсказкой об ошибке
def test_registration_page_with_special_symbols_in_family_field(web_browser):
    """ Test Registration with special symbols in family field. """
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys('Сергей')
    reg_page.last_name_field.send_keys("~!@#$%^&*()")
    reg_page.email_or_mobile_phone_field.send_keys("test123@mail.ru")
    reg_page.password_field.send_keys("Qazwsx1124")
    reg_page.password_confirmation_field.send_keys("Qazwsx1124")
    reg_page.continue_button.click()
    reg_page.error_message_name.is_visible()
    assert reg_page.error_message_last_name.get_text() == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."

# Тест-кейс N-15
# Регистрация пользователя с некорректным полем "Фамилия" (цифры), появление текста с подсказкой об ошибке
def test_registration_page_with_figures_in_family_field(web_browser):
    """ Test Registration with figures in family field. """
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys('Сергей')
    reg_page.last_name_field.send_keys("1234567890")
    reg_page.email_or_mobile_phone_field.send_keys("test123@mail.ru")
    reg_page.password_field.send_keys("Qazwsx1124")
    reg_page.password_confirmation_field.send_keys("Qazwsx1124")
    reg_page.continue_button.click()
    reg_page.error_message_name.is_visible()
    assert reg_page.error_message_last_name.get_text() == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."

# Тест-кейс N-16
# Некорректный email/телефон в поле ввода "Email или мобильный телефон"
def test_invalid_email_or_mobile_phone(web_browser):
    """ Test Registration with an invalid email or phone field. """
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys("Сергей")
    reg_page.last_name_field.send_keys("Фамилия")
    reg_page.email_or_mobile_phone_field.send_keys("pochta123")
    reg_page.password_field.send_keys("Qwerty1234")
    reg_page.password_confirmation_field.send_keys("Qwerty1234")
    reg_page.continue_button.click()
    assert reg_page.message_enter_the_phone_in_the_format.get_text() == "Введите телефон в формате +7ХХХХХХХХХХ или" \
                                                                        " +375XXXXXXXXX, или email в формате example@email.ru"

# Тест-кейс N-17
# Поле ввода "Пароль" и поле ввода "Подтверждение пароля"  в форме "Регистрация" не совпадают
def test_password_and_password_confirmation_does_not_match(web_browser):
    """ Test Registration - password confirmation does not match. """
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys("Сергей")
    reg_page.last_name_field.send_keys("Фамилия")
    reg_page.email_or_mobile_phone_field.send_keys("test123@mail.ru")
    reg_page.password_field.send_keys("Qwerty1234")
    reg_page.password_confirmation_field.send_keys("Testy1234")
    reg_page.continue_button.click()
    assert reg_page.message_passwords_dont_match.get_text() == "Пароли не совпадают"

# Тест-кейс N-18
# В пароле нет ни одной заглавной буквы
def test_password_no_upper_case(web_browser):
    """ Test Registration - no upper case in the password. """
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys("Сергей")
    reg_page.last_name_field.send_keys("Фамилия")
    reg_page.email_or_mobile_phone_field.send_keys("test123@mail.ru")
    reg_page.password_field.send_keys("qwerty1234")
    reg_page.password_confirmation_field.send_keys("qwerty1234")
    reg_page.continue_button.click()
    assert reg_page.error_message_password.get_text() == "Пароль должен содержать хотя бы одну заглавную букву"

# Тест-кейс N-19
# Пароль короче 8 символов
def test_password_too_short(web_browser):
    """ Test Registration - too short password. """
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys("Сергей")
    reg_page.last_name_field.send_keys("Фамилия")
    reg_page.email_or_mobile_phone_field.send_keys("test123@mail.ru")
    reg_page.password_field.send_keys("Qwer1")
    reg_page.password_confirmation_field.send_keys("Qwer1")
    reg_page.continue_button.click()
    assert reg_page.error_message_password.get_text() == "Длина пароля должна быть не менее 8 символов"

# Тест-кейс N-20
# Регистрация пользователя с уже зарегистрированным номером, отображается оповещающая форма
def test_registration_of_an_already_registered_user(web_browser):
    """ Test Registration - already registered user. """
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys("Людмила")
    reg_page.last_name_field.send_keys("Чижик")
    reg_page.email_or_mobile_phone_field.send_keys("+79210916809")
    reg_page.password_field.send_keys("Test12345678")
    reg_page.password_confirmation_field.send_keys("Test12345678")
    reg_page.continue_button.click()
    assert reg_page.notification_form.is_visible

# Тест-кейс N-21
# Вход по неправильному паролю в форме "Авторизация" уже зарегистрированного пользователя, надпись "Забыл пароль"
# перекрашивается в оранжнвый цвет
def test_authorization_of_a_user_with_an_invalid_password(web_browser):
    """ Test Authorization - invalid password. """
    page = AuthPage(web_browser)
    page.phone.send_keys('+79210916809')
    page.password.send_keys("TestPass")
    page.btn_login.click()
    assert page.message_invalid_username_or_password.get_text() == "Неверный логин или пароль"
    assert "rt-link--orange" in page.the_element_forgot_the_password.get_attribute('class')

# Тест-кейс N-22
# Тестирование аутентификации зарегестрированного пользователя
def test_authorisation_valid(web_browser):
    """ Test Authorization - valid user. """
    page = AuthPage(web_browser)
    page.phone.send_keys('+79210916809')
    page.password.send_keys("Test12345678")
    page.btn_login.click()

    assert 'https://b2c.passport.rt.ru/account_b2c/page?state=' in page.get_current_url() \
           and '&client_id=account_b2c#/' in page.get_current_url()
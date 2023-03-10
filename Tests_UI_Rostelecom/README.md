Тестирование интерфейса регистрации и авторизации от Ростелеком.

Файлы
-----

[conftest.py](conftest.py) contains all the required code to catch failed test cases and make screenshot
of the page in case any test case will fail.

[tests/base.py](tests/base.py) содержит библиотеку Smart Page Object

[tests/auth_page28.py](tests/auth_page28.py) содержит класс для Авторизации

[tests/registration_page28.py](tests/registration_page28.py) содержит класс для Регистрации

[tests/elements.py](tests/elements.py) содержит класс для определения элементов на веб-страницах

[tests/test_rostelecom.py](tests/test_rostelecom.py) автотесты для проверки UI сайта Ростелеком (https://b2c.passport.rt.ru/)


Описание автотестов:
-----
**test_start_page_is_correct**
Тест-кейс N-01 Корректное отображение "Стандартной страницы авторизации"

**test_phone_tab**
Тест-кейс N-02 Проверка названия таб выбора "Номер"
Тест не проходит(Bugs-01). Причина - Таб выбора 'Номер' не соответсвует ожидаемым требованиям (вместо 'номер' указан 'телефон')

**test_registration_page_and_continue_button**
Тест-кейс N-03 Проверка название кнопки "Продолжить" в форме "Регестрация"
Тест не проходит(Bugs-02). Причина - Кнопка должна иметь текст 'Продолжить', вместо него указан текст - 'Зарегистрироваться'

**test_registration_page_with_empty_name_field**
Тест-кейс N-04 Регистрация пользователя с пустым полем "Имя", появление текста с подсказкой об ошибке

**test_registration_with_a_low_value_in_the_name_field**
Тест-кейс N-05 Регистрация пользователя с некорректным значением в поле "Имя"(< 2 символов), появление текста с подсказкой об ошибке

**test_registration_with_a_long_value_in_the_name_field**
Тест-кейс N-06 Регистрация пользователя с некорректным значением в поле "Фамилия"(>30 символов), появление текста с подсказкой об ошибке

**test_registration_with_a_latin_letters_in_the_name_field**
Тест-кейс N-07 Регистрация пользователя с некорректным значением в поле "Имя"(латинские символы), появление текста с подсказкой об ошибке

**test_registration_with_special_symbols_in_the_name_field**
Тест-кейс N-08 Регистрация пользователя с некорректным значением в поле "Имя"(спецсимволы), появление текста с подсказкой об ошибке

**test_registration_with_a_figures_in_the_name_field**
Тест-кейс N-09 Регистрация пользователя с некорректным значением в поле "Имя"(цифры), появление текста с подсказкой об ошибке

**test_registration_page_with_empty_family_field**
Тест-кейс N-10 Регистрация пользователя с пустым полем "Фамилия", появление текста с подсказкой об ошибке

**test_registration_page_with_short_family_field**
Тест-кейс N-11 Регистрация пользователя с некорректным полем "Фамилия" (< 2 знаков), появления текста с подсказкой об ошибке

**test_registration_page_with_long_family_field**
Тест-кейс N-12 Регистрация пользователя с некорректным полем "Фамилия" (> 30 знаков), появление текста с подсказкой об ошибке

**test_registration_page_with_latin_letters_in_family_field**
Тест-кейс N-13 Регистрация пользователя с некорректным полем "Фамилия" (латинские буквы), появление текста с подсказкой об ошибке

**test_registration_page_with_special_symbols_in_family_field**
Тест-кейс N-14 Регистрация пользователя с некорректным полем "Фамилия" (спецсимволы), появление текста с подсказкой об ошибке

**test_registration_page_with_figures_in_family_field**
Тест-кейс N-15 Регистрация пользователя с некорректным полем "Фамилия" (цифры), появление текста с подсказкой об ошибке

**test_invalid_email_or_mobile_phone**
Тест-кейс N-16 Некорректный email/телефон в поле ввода "Email или мобильный телефон

**test_password_and_password_confirmation_does_not_match**
Тест-кейс N-17 Поле ввода "Пароль" и поле ввода "Подтверждение пароля"  в форме "Регистрация" не совпадают

**test_password_no_upper_case**
Тест-кейс N-18 В пароле нет ни одной заглавной буквы

**test_password_too_short**
Тест-кейс N-19 Пароль короче 8 символов

**test_registration_of_an_already_registered_user**
Тест-кейс N-20 Регистрация пользователя с уже зарегистрированным номером, отображается оповещающая форма

**test_authorization_of_a_user_with_an_invalid_password**
Тест-кейс N-21 Вход по неправильному паролю в форме "Авторизация" уже зарегистрированного пользователя, надпись "Забыл пароль"
перекрашивается в оранжевый цвет

**test_authorisation_valid**
Тест-кейс N-22 Тестирование аутентификации зарегестрированного пользователя


Как запустить тесты
----------------

1) Установить все библиотеки:

    pip install -r requirements.txt


2) Скачать Selenium WebDriver https://chromedriver.chromium.org/downloads (выбрать версию, совместимую с вашим браузером)

3) Запус тестов (на примере вебдрайвера Chrome):

    pytest -v --driver Chrome --driver-path chromedriver.exe test_rostelecom.py
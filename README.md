# Приложение для расчета стоимости страховки
### Инструкция по использованию
По эндпоинтам `createMaterial`и `material` вы можете добавить/посмотреть материалы
По эндпоинту `calculate_insurance_cost` вы можете рассчитать стоимость страховки указав материал и тариф

###  Установка проекта на локальный сервер
 - Склонировать репозиторий `https://github.com/mexoil1/smitApp`
 - Создать и запустить виртуальное окружение `python -m venv venv` и `source venv/bin/activate`
 - Перейти в директорию с файлом requirements.txt и установить зависимости `pip install -r requirements.txt`
 - в файле .env прописать ваши настройки базы данных в виде: `PG_USER = <Ваше имя>`
 - Запустить сервер: `uvicorn main:app --reload`

### Автор
[Слукин Михаил](https://github.com/mexoil1)
# snippets

## Добро пожаловать!

### Установка проекта

```
1. Склонируйте репозиторий: 
    
    git clone https://github.com/Zavodsk0y/internetportal -b api-branch
   
2. Перейдите в директорию проекта

    cd .../tutorial
    
3. Установите необходимые зависимости из файла requirements.txt

    pip install -r requirements.txt
```

#### Поздравляю, проект установлен и готов к работе!

### Работа с проектом

Примечание: адреса будут предоставлены как для локального запуска, так и с сайта pythonanywhere.com

API использует ViewSets, что позволяет обновлять, удалять, создавать и получать данные

API предоставляет работу по следующим адресам:


```
    При использовании GET-метода мы можем получить весь список существующих сниппетов
    
    https://lordess.pythonanywhere.com/api/snippets/
    127.0.0.1:8000/api/snippets/
   
    Если мы хотим рассмотреть сниппет подробнее, то мы можем воспользоваться следующим адресом с GET-методом
    
    https://lordess.pythonanywhere.com/api/snippets/1.../
    127.0.0.1:8000/api/snippets/1.../
    
    Также при использовании методов PATCH/DELETE вы можете соответственно изменить/удалить сниппет
    
    Если мы хотим получить список пользователей с GET-методом:
    
    https://lordess.pythonanywhere.com/api/users/
    http://127.0.0.1:8000/api/users/
    
    Также можем детально увидеть пользователя через GET:
    Учтите, что данные адреса используются только для просмотра, удалить, создать и изменить здесь мы ничего не можем
    
    https://lordess.pythonanywhere.com/api/users/1/
    http://127.0.0.1:8000/api/users/1/
    
    Мы также можем увидеть хайлайтинг сниппета кода по адресу:
    
    https://lordess.pythonanywhere.com/api/snippets/1/highlight/
    127.0.0.1:8000/api/snippets/1/highlight/
```

#### Примечание:

В проект уже вшита база данных Sqlite с некоторыми данными, а также присутствуют миграции. Потому вам ничего не нужно
будет с ними делать.

#### Структура проекта

```
    README.md
    requirements.txt
    tutorial\
        snippets\  -- папка приложения
            migrations\   -- папка с миграциями базы данных
                migrationfiles.....
                __init.py__
            tests.py
            __init.py__
            admin.py
            apps.py
            serializers.py
            models.py
            urls.py
            views.py
        tutorial\ 
            __init.py__
            asgi.py
            settings.py
            urls.py
            wsgi.py
        db.sqlite3
        manage.py
            
```

#### Запуск проекта

```
1. Перейдите в корневую папку проекта DjangoREST

2. Впишите в терминал следующую команду для запуска сервера:

    python manage.py runserver
    
3. Далее вы можете перейти по адресу, на котором запустился сервер в браузере

```

Примечание: логин/пароль для входа в админку: 

admin/admin

### Автор

Работу выполнил студент Петренко Константин, 421 группа




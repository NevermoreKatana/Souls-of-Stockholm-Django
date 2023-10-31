# Проект "Анонимно-псевдонимный сетевой форум"
# Проект закрыт в связи переноса проекта на Django
## Описание
Souls of Stockholm - анонимный форум на котором люди могут анонимно обсжудать любые виды тем. Проект имеет 3 версии:

- Десктопное приложение - Сайт
- Мобильное приложение - Android App

Данный репозиторий содержит только серверную и десктопную часть, другие части выполняются

[Vladimir (Rukati)](https://github.com/Rukati)

## Установка 

```sh
make install
```

## Запуск сервера (WSGI)
```sh
make start
```
## Запуск сервера (Разработчика)
```sh
make dev
```
## Заполнение .env
```sh
SECRET_KEY= Секретный ключ для сервера(можно сделать с помощью make secretkey)
POSTGRES_DB= Имя БД для запуска Docker контейнера postgres
POSTGRES_USER= Имя пользователя для запуска Docker контейнера postgres
POSTGRES_PASSWORD= Пароль пользователя для запуска Docker контейнера postgres
DB_URL= Ссылка на URL базы данных
DEBUG=True\False в зависимости от среды разработка\Деплой
```
## Запуск контейнера(для разработки)
```sh
make docker-build
```
## Быстрое выполнение миграций 
```sh
make migration
```


## Результат можно посмотреть

[Souls of Stockholm](https://souls-of-stockholm.onrender.com/)

## Репозиторий мобильной части 
- Тут когда-то будет Android App


## Authors
- ### Сервер и десктоп
- [@KatanaNevermore](https://github.com/NevermoreKatana)
- [@KatanaNevermore(Tg)](https://t.me/nevermorekatana)
- ### Мобильная часть
- [@Rukati](https://github.com/Rukati)
- [@Rukati(Tg)](https://t.me/bubblessort)

## License

[MIT](https://github.com/NevermoreKatana/Souls-of-Stockholm/blob/main/LICENSE)



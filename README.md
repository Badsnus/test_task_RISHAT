Ссылка на развернутый проект
---
___
http://185.195.26.137/ (дебаг включен специально)

Данные от админки: admin:admin

Вопросы про реализацию
---
___
1)GET /buy/{id} - Вместо GET юзал POST, так как это создание сессии и мне кажется, что тут правильнее юзать POST

2)Модель Order - не совсем понял что это и зачем. Я так понимаю, что это грубо говоря
коризна айтемов, но так как на сайте нет авторизации, то смысл от таковой модели Order - нет.
Так как нам в любом случае придется это хранить где-то в сессии, поэтому проще будет просто выкинуть список товаров и
уже на жс их обрабатывать в данном случае.
Поэтому мне чет не очень захотелось это пилить.

3)Также как я понял, не нужно было вебхук делать на получение оплаты (ну если надо было то сори)) ) 


Инструкция по установке
---
___

#### 1)Клонируем репозиторий

    git clone https://github.com/Badsnus/test_task_RISHAT.git

#### 2)Заходим в директорию репозитория

    cd test_task_RISHAT

#### 3)  .env.example -> .env

    И выставить там настройки


#### 4) Поднимаем контейнер

    docker-compose up

Ссылка на тестовое
---
___
https://docs.google.com/document/d/1spNK2HhLEuzO3whKr7togZdwtdFiEbCKjOPfzleLz2c/edit?usp=sharing


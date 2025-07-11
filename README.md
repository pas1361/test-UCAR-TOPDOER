# test-UCAR-TOPDOER
Тестовое задание для UCAR&lt;>TOPDOER выполнил Первишко Александр

Установка зависимостей:

pip install fastapi uvicorn

Запуск:

uvicorn main:app --reload

Примеры запросов и результаты их выполнения в командной строке Windows - cmd.exe:

```
curl -X POST http://127.0.0.1:8000/reviews -H "Content-Type: application/json" -d "{\"text\": \"Мне не нравится интерфейс\"}"
{"id":1,"text":"Мне не нравится интерфейс","sentiment":"negative","created_at":"2025-07-09T11:27:19.247599"}

curl -X POST http://127.0.0.1:8000/reviews -H "Content-Type: application/json" -d "{\"text\": \"Очень хороший сервис, люблю его!\"}"
{"id":2,"text":"Очень хороший сервис, люблю его!","sentiment":"positive","created_at":"2025-07-09T11:28:44.762207"}

curl -X POST http://127.0.0.1:8000/reviews -H "Content-Type: application/json" -d "{\"text\": \"Хотел бы видеть больше функций\"}"
{"id":3,"text":"Хотел бы видеть больше функций","sentiment":"neutral","created_at":"2025-07-09T11:29:26.814838"}

curl -X POST http://127.0.0.1:8000/reviews -H "Content-Type: application/json" -d "{\"text\": \"Классный и супер удобный интерфейс\"}"
{"id":4,"text":"Классный и супер удобный интерфейс","sentiment":"positive","created_at":"2025-07-09T11:29:56.145895"}

curl -X POST http://127.0.0.1:8000/reviews -H "Content-Type: application/json" -d "{\"text\": \"Ужасный опыт, очень разочарован\"}"
{"id":5,"text":"Ужасный опыт, очень разочарован","sentiment":"negative","created_at":"2025-07-09T11:30:20.727865"}

curl -X POST http://127.0.0.1:8000/reviews -H "Content-Type: application/json" -d "{\"text\": \"\"}"
{"error":"Missing 'text'"}

curl -X POST http://127.0.0.1:8000/reviews -H "Content-Type: application/json" -d "{}"
{"error":"Missing 'text'"}


curl http://127.0.0.1:8000/reviews
[
{"id":1,"text":"Мне не нравится интерфейс","sentiment":"negative","created_at":"2025-07-09T11:27:19.247599"},
{"id":2,"text":"Очень хороший сервис, люблю его!","sentiment":"positive","created_at":"2025-07-09T11:28:44.762207"},
{"id":3,"text":"Хотел бы видеть больше функций","sentiment":"neutral","created_at":"2025-07-09T11:29:26.814838"},
{"id":4,"text":"Классный и супер удобный интерфейс","sentiment":"positive","created_at":"2025-07-09T11:29:56.145895"},
{"id":5,"text":"Ужасный опыт, очень разочарован","sentiment":"negative","created_at":"2025-07-09T11:30:20.727865"}
]

curl http://127.0.0.1:8000/reviews?sentiment=negative
[
{"id":1,"text":"Мне не нравится интерфейс","sentiment":"negative","created_at":"2025-07-09T11:27:19.247599"},
{"id":5,"text":"Ужасный опыт, очень разочарован","sentiment":"negative","created_at":"2025-07-09T11:30:20.727865"}
]

curl http://127.0.0.1:8000/reviews?sentiment=positive
[
{"id":2,"text":"Очень хороший сервис, люблю его!","sentiment":"positive","created_at":"2025-07-09T11:28:44.762207"},
{"id":4,"text":"Классный и супер удобный интерфейс","sentiment":"positive","created_at":"2025-07-09T11:29:56.145895"}
]

curl http://127.0.0.1:8000/reviews?sentiment=neutral
[{"id":3,"text":"Хотел бы видеть больше функций","sentiment":"neutral","created_at":"2025-07-09T11:29:26.814838"}]
```


Можно добавить в код следующие строки, чтобы запускать исполнение скрипта короче - python main.py:

```
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
```

Для тестирования API через встроенный в FastApi Swagger - необходимо использовать Pydantic-модели.

В нашем случаем нет возможности передать JSON в Swagger. 

Для тестирования и отправки запросов удобнее использовать Postman.

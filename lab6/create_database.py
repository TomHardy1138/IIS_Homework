from tinydb import TinyDB, Query

questions = [
    {
        "question": "Вы имеете научное звание? (да/нет)",
        "number": 1,
        "answer": [
            "Да",
            "Нет"
        ]
     },
    {
        "question": "У Вас есть научное открытие? (да/нет)",
        "number": 2,
        "answer": [
            "Да",
            "Нет"
        ]
    },
    {
        "question": "Ваш средний балл за время учебы? (число от 0 до 5)",
        "number": 3,
        "answer": [""]
    },
    {
        "question": "Ваш стаж работы по специальности? (полные года)",
        "number": 4,
        "answer": [""]
    }
]


def main() -> None:
    db = TinyDB("database.json")
    for question in questions:
        db.insert(question)

    a = Query()
    print(db.search(a.number == 2))
    db.close()


if __name__ == "__main__":
    main()
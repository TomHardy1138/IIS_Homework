import streamlit as st
from tinydb import TinyDB, Query


def position(answers) -> str:
    print(answers)
    degree = (answers[0] == "Да")
    discovery = (answers[1] == "Да")
    grade = answers[2]
    experience = int(answers[3])

    if not degree:
        return "Отказать"
    else:
        if discovery:
            return "Научный сотрудник"
        else:
            if grade >= 3.5:
                return "Инженер-конструктор"
            else:
                if experience > 2:
                    return "Лаборант"
    return "Отказать"


def main() -> None:
    st.header("Лабораторная работа №6. Продукционная система")
    database = TinyDB("lab6/database.json")

    answers = []
    for item in database:
        number = item["number"]
        question = f"{number}) {item['question']}"

        if number == 3:
            answers.append(
                st.slider(
                    question,
                    0.0, 5.0
                )
            )
        elif number == 4:
            answers.append(st.number_input(question))
        else:
            answers.append(st.radio(question, item["answer"]))

    if st.button("Подтвердить ответ"):
        result_message = f"Решение - {position(answers)}"
        st.text(result_message)


if __name__ == "__main__":
    main()

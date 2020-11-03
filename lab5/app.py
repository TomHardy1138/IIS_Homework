import streamlit as st
from tinydb import TinyDB, Query
import pandas as pd

task: str = "Консультационная система"


def main() -> None:
    st.title("Лабораторная работа №5")
    st.markdown(
        "<h3 style='margin-bottom: 50px'>"
        "{task}"
        "</h3>".format(task=task),
        unsafe_allow_html=True)

    database = TinyDB("database.json")

    answers = []
    for item in database:
        question = f"{item['number']}) {item['question']}"
        answers.append(st.radio(question, item["answer"]))

    if st.button("Рассчитать данные"):
        d, m, n = 0, 0, 0
        for idx, answer in enumerate(answers):
            id = idx + 1
            info = Query()
            result = database.search(info.number == id)[0]["answer"]
            case = result.index(answer)

            if id == 1:
                if case == 0:
                    d += 1
                if case == 1:
                    n += 1
                if case == 2:
                    m += 1
            if id == 2:
                if case == 0:
                    d += 1
                if case == 1:
                    n += 1
                if case == 2:
                    m += 1
            if id == 3:
                if case == 0:
                    m += 1
                if case == 1:
                    n += 1
                if case == 2:
                    d += 1
            if id == 4:
                if case == 0:
                    m += 1
                if case == 1:
                    d += 1
                if case == 2:
                    n += 1
            if id == 5:
                if case == 0:
                    n += 1
                if case == 1:
                    m += 1
                if case == 2:
                    d += 1
            if id == 6:
                if case == 0:
                    n += 1
                if case == 1:
                    d += 1
                if case == 2:
                    m += 1
            if id == 7:
                if case == 0:
                    d += 1
                if case == 1:
                    m += 1
                if case == 2:
                    n += 1
            if id == 8:
                if case == 0:
                    n += 1
                if case == 1:
                    d += 1
                if case == 2:
                    m += 1
            if id == 9:
                if case == 0:
                    n += 1
                if case == 1:
                    m += 1
                if case == 2:
                    d += 1
            if id == 10:
                if case == 0:
                    m += 1
                if case == 1:
                    n += 1
                if case == 2:
                    d += 1

        d = d / 10 * 100
        m = m / 10 * 100
        n = n / 10 * 100

        df = pd.DataFrame(
            data=[d, m, n],
            index=[
                "Делопроизводитель",
                "Менеджер",
                "Начальник"
            ],
            columns=["Вероятность"]
        )
        st.write(df)


if __name__ == "__main__":
    main()

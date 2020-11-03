import streamlit as st
import numpy as np
import pandas as pd
from typing import List, Dict, Any

default_choices: List[str] = ["Да", "Нет"]
dict_default_choices: Dict[str, Any] = dict(
    zip(
        default_choices,
        (True, False)
    )
)

seller_questions: List[str] = [
    "Продавец предлагает товар энергично и напористо?",
    "Продавец не настойчив с клиентом?",
    "Продавец не идёт на уступки в вопросах цены?",
    "Продавец старается избегать возможных осложнений при работе?",
    "Продавец уделяет полное внимание клиенту?",
    "Продавец компетентен, знает многое о товаре?",
    "Продавец испытывает чувство превосходства над клиентом?",
    "Продавец открыт и честен с клиентом?",
    "Продавец старается прислушиваться к мнению покупателя?",
    "Продавца можно назвать честолюбивым?",
    "Продавец во всём старается быть полезным покупателю?"
]
customer_questions: List[str] = [
    "Демонстрирует,что знает больше других?",
    "Мнением продавца не интересуется?",
    "Покупатель высокомерен в общении?",
    "Чрезвычайно придирчив при выборе товара?",
    "Покупатель часто меняет решения по вариантам покупки?",
    "Покупатель задаёт продацу неуместные вопросы?",
    "Покупатель не может чётко сформулировать, что его интересует?",
    "Продавец отдаёт инициативу при выборе товара продавцу?",
    "Всегда тщательно осматривает весь ассортимент?",
    "Покупатель внимательно выслушивает мнение продавца?",
    "Свободно излагает свои идеи и вопросы по товару?",
    "Покупатель обладает гибкостью в вопросах подбора товара?"
]

task: str = "Построение экспертной системы в области торговли"
result_messages: List[List[str]] = [
    [
        "Результат – средний. Взаимное соперничество.",
        "Результат низкий. Продавец не может убедить покупателя.",
        "Результат средний.Покупатель не доверяет продавцу."
    ],
    [
        "Результат высокий. Продавец доминирует, покупатель принимает предложение продавца.",
        "Результат средний. Покупатель и продавец не могут найти общий язык.",
        "Результат – средний. Продавец не может понять, чего хочет покупатель."
    ],
    [
        "Результат – средний. Покупатель получает информацию и трезво её оценивает.",
        "Результат – низкий. Продавец не может ответить покупателю на его вопросы.",
        "Результат – высокий. Взаимное уважение, четкое понимание цели."
    ]
]


def main() -> None:
    st.title("Лабораторная работа №2")
    st.markdown(
        "<h3 style='margin-bottom: 50px'>"
        "{task}"
        "</h3>".format(task=task),
        unsafe_allow_html=True)
    seller, customer = st.beta_columns(2)

    seller.text("Вопросы о продавце")
    customer.text("Вопросы о покупателе")
    seller_answers, customer_answers = [], []

    for question in seller_questions:
        seller_answers.append(seller.radio(question, default_choices))
    for question in customer_questions:
        customer_answers.append(customer.radio(question, default_choices))
    if st.button("Рассчитать результат сделки"):
        type_seller: Dict[int, int] = {k: 0 for k in range(1, 4)}
        type_customer: Dict[int, int] = {k: 0 for k in range(1, 4)}
        # Подсчёт баллов для всех типов продавцов
        for idx, answer in enumerate(seller_answers):
            # Если ответ "Нет", то вопрос нас не интересует
            # Если ответ "Да", то считаем коэффициенты
            if not dict_default_choices[answer]:
                continue
            if idx == 0:
                type_seller[1] += 5
                type_seller[3] += 2.5
            if idx == 1:
                type_seller[2] += 10
            if idx == 2:
                type_seller[1] += 10
            if idx == 3:
                type_seller[2] += 5
            if idx == 4:
                type_seller[2] += 2.5
                type_seller[3] += 5
            if idx == 5:
                type_seller[1] += 2.5
                type_seller[3] += 10
            if idx == 6:
                type_seller[1] += 5
            if idx == 7:
                type_seller[3] += 5
            if idx == 8:
                type_seller[2] += 5
                type_seller[3] += 2.5
            if idx == 9:
                type_seller[1] += 2.5
            if idx == 10:
                type_seller[2] += 2.5
        # Подсчёт баллов для всех типов покупателей
        for idx, answer in enumerate(customer_answers):
            if not dict_default_choices[answer]:
                continue
            if idx == 0:
                type_customer[1] += 6
            if idx == 1:
                type_customer[1] += 7
            if idx == 2:
                type_customer[1] += 4
            if idx == 3:
                type_customer[1] += 3
            if idx == 4:
                type_customer[2] += 7
            if idx == 5:
                type_customer[2] += 3
            if idx == 6:
                type_customer[2] += 6
            if idx == 7:
                type_customer[2] += 4
            if idx == 8:
                type_customer[3] += 7
            if idx == 9:
                type_customer[3] += 6
            if idx == 10:
                type_customer[3] += 4
            if idx == 11:
                type_customer[3] += 3

        seller_prob = list(type_seller.values())
        customer_prob = list(type_customer.values())

        seller_sum = sum(seller_prob)
        customer_sum = sum(customer_prob)

        seller_prob = [elem / seller_sum * 100 for elem in seller_prob]
        customer_prob = [elem / customer_sum * 100 for elem in customer_prob]

        probabilities = np.zeros((3, 3))
        for idx in range(3):
            for jdx in range(3):
                probabilities[idx][jdx] = seller_prob[idx] * customer_prob[jdx] / 100

        df = pd.DataFrame(
            data=probabilities,
            index=[
                f"{idx} тип покупателя" for idx in range(1, 4)
            ],
            columns=[
                f"{idx} тип продавца" for idx in range(1, 4)
            ]
        )
        st.write(df)
        row, col = np.unravel_index(probabilities.argmax(), probabilities.shape)
        st.text(result_messages[row][col])
        st.text(f"Вероятность сделки = {probabilities[row][col]:.1f}%")


if __name__ == "__main__":
    main()

import streamlit as st
from typing import (
    Tuple,
    Any,
    Dict
)

GENDER: Tuple[str, str] = ("Мужской", "Женский")
DEFAULT_CHOICES: Tuple[str, str] = ("Да", "Нет")
DICT_DEFAULT_CHOICES: Dict[str, int] = dict(zip(DEFAULT_CHOICES, [5, 0]))
MARK: str = "Дать оценку состояния"


def main() -> None:
    st.title("Лабораторная работа №1")
    st.subheader(
        "Построение простейшей медицинской экспертной системы"
    )
    FIO: str = st.text_input("ФИО:")
    GENDERS: str = st.selectbox("Пол:", GENDER)
    WEIGHT: str = st.text_input("Вес:")
    HEIGHT: str = st.text_input("Рост:")
    optimal_weight: int = 0

    if WEIGHT and HEIGHT:
        optimal_weight = int(WEIGHT) + 100 - int(HEIGHT)
        st.text(f"Превышение веса: {optimal_weight}")

    CIGARETTES: str = st.text_input("Пачек сигарет в день:", "0")
    ALCOHOL: str = st.text_input("Алкоголь, грамм в день:", "0")
    CHEST_PAIN: str = st.selectbox(
        "Боли в левой половине груди:",
        DEFAULT_CHOICES
    )
    HEADACHE: str = st.selectbox(
        "Боли в затылочной части:",
        DEFAULT_CHOICES
    )

    FILL_CONDITION: Any = FIO and HEIGHT and WEIGHT

    if st.button(MARK) and FILL_CONDITION:
        k: int = 0
        if GENDERS == "Мужской":
            k += 3

        optimal_weight //= 10
        optimal_weight = max(0, min(optimal_weight, 10))

        k += optimal_weight
        k += min(int(CIGARETTES) / .5, 5)
        k += min(int(ALCOHOL) // 100, 5)
        k += DICT_DEFAULT_CHOICES[CHEST_PAIN]
        k += DICT_DEFAULT_CHOICES[HEADACHE]

        result: Any = round(k / 33 * 100)

        if result <= 33:
            st.text(f"Низкая вероятность: {result}%")
        elif result >= 66:
            st.text(f"Высокая вероятность: {result}%")
        else:
            st.text(f"Средняя вероятность: {result}%")


if __name__ == "__main__":
    main()

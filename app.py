import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Модель хищник–жертва (Лотка–Вольтерра)")

# Форма ввода параметров
with st.form("params_form"):
    alpha = st.number_input("α (рост жертв)", value=0.1, step=0.01)
    beta = st.number_input("β (поедание)", value=0.02, step=0.001)
    gamma = st.number_input("γ (смертность хищников)", value=0.1, step=0.01)
    delta = st.number_input("δ (превращение жертв в хищников)", value=0.01, step=0.001)
    x0 = st.number_input("Начальное число жертв", value=40.0)
    y0 = st.number_input("Начальное число хищников", value=9.0)
    T = st.number_input("Время моделирования", value=200.0)
    dt = st.number_input("Шаг времени", value=0.1, step=0.01)
    submitted = st.form_submit_button("Запустить симуляцию")

def lotka_volterra(x, y, a, b, g, d):
    dx = a * x - b * x * y
    dy = d * x * y - g * y
    return dx, dy

if submitted:
    time = np.arange(0, T, dt)
    x = [x0]
    y = [y0]

    for _ in time[1:]:
        dx, dy = lotka_volterra(x[-1], y[-1], alpha, beta, gamma, delta)
        x.append(x[-1] + dx * dt)
        y.append(y[-1] + dy * dt)

    fig, ax = plt.subplots()
    ax.plot(time, x, label="Жертвы")
    ax.plot(time, y, label="Хищники")
    ax.set_xlabel("Время")
    ax.set_ylabel("Популяция")
    ax.set_title("Модель хищник–жертва (Лотка–Вольтерра)")
    ax.legend()
    st.pyplot(fig)

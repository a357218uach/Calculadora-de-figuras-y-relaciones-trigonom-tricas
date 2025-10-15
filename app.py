# app.py
# -----------------------------------------------------
# Calculadora de Figuras y Relaciones Trigonométricas
# Curso de Programación - UACH
# -----------------------------------------------------

import streamlit as st
import numpy as np



st.title("Calculadora de Figuras y Relaciones Trigonométricas 🤓")

tabs = st.tabs(["📐 Figuras geométricas", "📊 Funciones trigonométricas"])

# -----------------------------------------------------
# PARTE 1 y 2: FIGURAS GEOMÉTRICAS
# -----------------------------------------------------
with tabs[0]:
    st.header("Cálculo de área y perímetro")

    # Seleccionar figura
    figura = st.selectbox(
        "Selecciona una figura:",
        ["Círculo", "Triángulo", "Rectángulo", "Cuadrado"]
    )

    color = st.color_picker("Elige un color para la figura:", "#1f77b4")

    # Variables y cálculos según figura
    if figura == "Círculo":
        r = st.number_input("Radio (r)", min_value=0.0, value=1.0)
        area = np.pi * r**2
        perimetro = 2 * np.pi * r

    elif figura == "Triángulo":
        a = st.number_input("Lado a", min_value=0.0, value=3.0)
        b = st.number_input("Lado b (base)", min_value=0.0, value=4.0)
        c = st.number_input("Lado c", min_value=0.0, value=5.0)
        h = st.number_input("Altura (h)", min_value=0.0, value=4.0)
        area = 0.5 * b * h
        perimetro = a + b + c

    elif figura == "Rectángulo":
        b = st.number_input("Base (b)", min_value=0.0, value=4.0)
        h = st.number_input("Altura (h)", min_value=0.0, value=2.0)
        area = b * h
        perimetro = 2 * (b + h)

        fig, ax = plt.subplots()
        rect = plt.Rectangle((0, 0), b, h, color=color, fill=False, linewidth=2)
        ax.add_artist(rect)
        ax.set_xlim(-1, b + 1)
        ax.set_ylim(-1, h + 1)
        ax.set_aspect('equal')
        st.pyplot(fig)

    elif figura == "Cuadrado":
        l = st.number_input("Lado (l)", min_value=0.0, value=2.0)
        area = l**2
        perimetro = 4 * l

        fig, ax = plt.subplots()
        sq = plt.Rectangle((0, 0), l, l, color=color, fill=False, linewidth=2)
        ax.add_artist(sq)
        ax.set_xlim(-1, l + 1)
        ax.set_ylim(-1, l + 1)
        ax.set_aspect('equal')
        st.pyplot(fig)

    # Mostrar resultados
    st.success(f"Área = {area:.2f}")
    st.success(f"Perímetro = {perimetro:.2f}")

# -----------------------------------------------------
# 🟦 PARTE 3: FUNCIONES TRIGONOMÉTRICAS
# -----------------------------------------------------
with tabs[1]:
    st.header("Funciones trigonométricas")

    # Selección de función
    funcion = st.selectbox("Selecciona una función:", ["sin(x)", "cos(x)", "tan(x)"])
    amp = st.slider("Amplitud", 0.1, 2.0, 1.0)
    rango = st.slider("Rango (en múltiplos de π)", 1, 4, 2)

    # Crear eje x
    x = np.linspace(0, rango * np.pi, 400)

    # Evaluar función seleccionada
    if funcion == "sin(x)":
        y = amp * np.sin(x)
    elif funcion == "cos(x)":
        y = amp * np.cos(x)
    else:
        y = amp * np.tan(x)
        y[np.abs(y) > 10] = np.nan  # limitar valores grandes

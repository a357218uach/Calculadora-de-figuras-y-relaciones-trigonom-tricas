

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Calculadora de Figuras y Relaciones Trigonometricas")

# Crear pestañas
tabs = st.tabs(["Figuras geometrica", "Funciones trigonometricas"])

# PARTE 1 y 2: FIGURAS GEOMETRICAS
with tabs[0]:
    st.header("Calculo de area y perimetro")

    figura = st.selectbox(
        "Selecciona una figura:",
        ["Circulo", "Triangulo", "Rectangulo", "Cuadrado"]
    )

    color = st.color_picker("Elige un color para la figura:", "#1f77b4")

    # Circulo
    if figura == "Circulo":
        r = st.number_input("Radio (r)", min_value=0.0, value=1.0, format="%.4f")
        area = np.pi * r ** 2
        perimetro = 2 * np.pi * r

        # Dibujo
        fig, ax = plt.subplots()
        circle = plt.Circle((0, 0), r, color=color, fill=False, linewidth=2)
        ax.add_artist(circle)
        ax.set_aspect("equal")
        ax.set_xlim(-r * 1.2, r * 1.2)
        ax.set_ylim(-r * 1.2, r * 1.2)
        st.pyplot(fig)

    # Triangulo
    elif figura == "Triangulo":
        a = st.number_input("Lado a", min_value=0.0, value=3.0, format="%.4f")
        b = st.number_input("Lado b (base)", min_value=0.0, value=4.0, format="%.4f")
        c = st.number_input("Lado c", min_value=0.0, value=5.0, format="%.4f")
        h = st.number_input("Altura (h)", min_value=0.0, value=4.0, format="%.4f")
        area = 0.5 * b * h
        perimetro = a + b + c

        # Dibujo rapido (triangulo)
        fig, ax = plt.subplots()
        x = [0, b / 2, -b / 2, 0]
        y = [0, h, 0, 0]
        ax.plot(x, y, color=color, linewidth=2)
        ax.set_aspect("equal")
        st.pyplot(fig)

    # Rectangulo
    elif figura == "Rectangulo":
        base = st.number_input("Base (b)", min_value=0.0, value=4.0, format="%.4f")
        altura = st.number_input("Altura (h)", min_value=0.0, value=2.0, format="%.4f")
        area = base * altura
        perimetro = 2 * (base + altura)

        fig, ax = plt.subplots()
        rect = plt.Rectangle((0, 0), base, altura, color=color, fill=False, linewidth=2)
        ax.add_artist(rect)
        ax.set_xlim(-1, base + 1)
        ax.set_ylim(-1, altura + 1)
        ax.set_aspect("equal")
        st.pyplot(fig)

    # Cuadrado
    elif figura == "Cuadrado":
        l = st.number_input("Lado (l)", min_value=0.0, value=2.0, format="%.4f")
        area = l ** 2
        perimetro = 4 * l

        fig, ax = plt.subplots()
        sq = plt.Rectangle((0, 0), l, l, color=color, fill=False, linewidth=2)
        ax.add_artist(sq)
        ax.set_xlim(-1, l + 1)
        ax.set_ylim(-1, l + 1)
        ax.set_aspect("equal")
        st.pyplot(fig)

    # Mostrar resultados (asegurarse que area y perimetro existen)
    try:
        st.success("Area = {:.4f}".format(area))
        st.success("Perimetro = {:.4f}".format(perimetro))
    except NameError:
        st.error("No se calcularon area o perimetro: revisa los parametros de la figura.")

# PARTE 3: FUNCIONES TRIGONOMETRICAS
with tabs[1]:
    st.header("Funciones trigonometricas")

    funcion = st.selectbox("Selecciona una funcion:", ["sin(x)", "cos(x)", "tan(x)"])
    amp = st.slider("Amplitud", 0.1, 2.0, 1.0)
    rango = st.slider("Rango (en multiplos de pi)", 1, 4, 2)

    x = np.linspace(0, rango * np.pi, 400)

    if funcion == "sin(x)":
        y = amp * np.sin(x)
    elif funcion == "cos(x)":
        y = amp * np.cos(x)
    else:
        y = amp * np.tan(x)
        y[np.abs(y) > 10] = np.nan

    fig, ax = plt.subplots()
    ax.plot(x, y, linewidth=2)
    ax.set_title("{} con amplitud {}".format(funcion, amp))
    ax.set_xlabel("x (radianes)")
    ax.set_ylabel("y")
    ax.grid(True)
    st.pyplot(fig)

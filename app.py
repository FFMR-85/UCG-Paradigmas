import streamlit as st
import libreria_funciones as lf

st.title("Paradigmas de la programación")

st.sidebar.image("ucsg.png")

st.sidebar.title("Parametros")

st.write("Elaborado por Francisco Miranda")

capital = st.number_input("Ingrese el capital")
tasa_anual_pct = st.number_input("Ingrese la tasa anual")
dias_mora = st.number_input("Ingrese dias mora")

# resultado = lf.calcular_interes_mora()

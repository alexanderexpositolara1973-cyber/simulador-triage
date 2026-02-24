import streamlit as st
import random

st.title("🚑 Simulador Básico de Triage START")

def generar_paciente():
    return {
        "camina": random.choice(["Sí", "No"]),
        "respira": random.choice(["Sí", "No"]),
        "fr": random.randint(10, 45),
        "llenado": round(random.uniform(0, 4), 1),
        "obedece": random.choice(["Sí", "No"])
    }

def clasificacion_correcta(p):
    if p["camina"] == "Sí":
        return "VERDE"
    if p["respira"] == "No":
        return "NEGRO"
    if p["fr"] > 30:
        return "ROJO"
    if p["llenado"] > 2:
        return "ROJO"
    if p["obedece"] == "No":
        return "ROJO"
    return "AMARILLO"

if "paciente" not in st.session_state:
    st.session_state.paciente = generar_paciente()

p = st.session_state.paciente

st.write("### Datos del Paciente")
st.write(p)

opcion = st.radio(
    "Clasifique al paciente:",
    ["VERDE", "AMARILLO", "ROJO", "NEGRO"]
)

if st.button("Evaluar"):
    correcta = clasificacion_correcta(p)
    if opcion == correcta:
        st.success(f"Correcto ✅ - {correcta}")
    else:
        st.error(f"Incorrecto ❌ - Correcta: {correcta}")

if st.button("Nuevo Paciente"):
    st.session_state.paciente = generar_paciente()
    st.rerun()

import streamlit as st
import random

st.set_page_config(page_title="Simulador START Avanzado", layout="centered")

st.title("🚑 Simulador Académico de Triage START")
st.markdown("Entrenamiento para Medicina de Emergencias y Desastres")

# ---------------------------------
# Inicializar puntaje en sesión
# ---------------------------------

if "puntaje" not in st.session_state:
    st.session_state.puntaje = 0
    st.session_state.total = 0

# ---------------------------------
# Generador de paciente coherente
# ---------------------------------

def generar_paciente():

    camina = random.choice(["Sí", "No"])

    if camina == "Sí":
        return {
            "camina": "Sí"
        }, "🟢 Verde", "Paciente ambulatorio según START."

    # No camina → evaluar respiración
    respira = random.choice(["Sí", "No"])

    if respira == "No":
        via_aerea_responde = random.choice(["Sí", "No"])

        if via_aerea_responde == "No":
            return {
                "camina": "No",
                "respira": "No",
                "respuesta_apertura_via_aerea": "No"
            }, "⚫ Negro", "Apnea persistente tras apertura de vía aérea."

        else:
            return {
                "camina": "No",
                "respira": "No",
                "respuesta_apertura_via_aerea": "Sí"
            }, "🔴 Rojo", "Respira tras apertura de vía aérea."

    # Si respira
    fr = random.randint(10, 40)

    if fr > 30:
        return {
            "camina": "No",
            "respira": "Sí",
            "FR": fr
        }, "🔴 Rojo", "Frecuencia respiratoria mayor a 30."

    llenado = round(random.uniform(1, 3), 1)

    if llenado > 2:
        return {
            "camina": "No",
            "respira": "Sí",
            "FR": fr,
            "llenado_capilar_seg": llenado
        }, "🔴 Rojo", "Perfusión alterada (>2 seg)."

    obedece = random.choice(["Sí", "No"])

    if obedece == "No":
        return {
            "camina": "No",
            "respira": "Sí",
            "FR": fr,
            "llenado_capilar_seg": llenado,
            "obedece_ordenes": "No"
        }, "🔴 Rojo", "Alteración del estado mental."

    return {
        "camina": "No",
        "respira": "Sí",
        "FR": fr,
        "llenado_capilar_seg": llenado,
        "obedece_ordenes": "Sí"
    }, "🟡 Amarillo", "Paciente estable no ambulatorio."

# ---------------------------------
# Generar nuevo paciente
# ---------------------------------

if st.button("🔄 Generar nuevo paciente"):
    st.session_state.paciente, st.session_state.correcta, st.session_state.explicacion = generar_paciente()
    st.session_state.total += 1

# ---------------------------------
# Mostrar paciente si existe
# ---------------------------------

if "paciente" in st.session_state:

    st.subheader("📋 Datos del Paciente")
    st.json(st.session_state.paciente)

    st.subheader("🧠 Clasificación")

    respuesta = st.radio(
        "Seleccione la categoría:",
        ["🟢 Verde", "🟡 Amarillo", "🔴 Rojo", "⚫ Negro"]
    )

    if st.button("Evaluar"):
        if respuesta == st.session_state.correcta:
            st.success("✅ Clasificación correcta.")
            st.session_state.puntaje += 1
        else:
            st.error(f"❌ Incorrecto. La correcta era: {st.session_state.correcta}")

        st.info(f"Fundamento clínico: {st.session_state.explicacion}")

        st.write(f"📊 Puntaje actual: {st.session_state.puntaje} / {st.session_state.total}")

else:
    st.info("Presione 'Generar nuevo paciente' para comenzar la simulación.")

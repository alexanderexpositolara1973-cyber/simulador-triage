import streamlit as st
import random

st.title("🚑 Simulador de Triage START")

st.markdown("Simulación académica para Medicina de Emergencias y Desastres")

# -------------------------
# Generación coherente del paciente
# -------------------------

camina = random.choice(["Sí", "No"])

if camina == "Sí":
    categoria_real = "🟢 Verde"
    paciente = {
        "camina": camina
    }

else:
    respira = random.choice(["Sí", "No"])

    if respira == "No":
        fr = 0
        categoria_real = "⚫ Negro"
        paciente = {
            "camina": camina,
            "respira": respira,
            "fr": fr
        }

    else:
        fr = random.randint(10, 40)

        if fr > 30:
            categoria_real = "🔴 Rojo"
        else:
            llenado = round(random.uniform(1, 3), 1)

            if llenado > 2:
                categoria_real = "🔴 Rojo"
            else:
                obedece = random.choice(["Sí", "No"])

                if obedece == "No":
                    categoria_real = "🔴 Rojo"
                else:
                    categoria_real = "🟡 Amarillo"

            paciente = {
                "camina": camina,
                "respira": respira,
                "fr": fr,
                "llenado_capilar_seg": llenado,
                "obedece_ordenes": obedece
            }

        paciente = {
            "camina": camina,
            "respira": respira,
            "fr": fr
        }

# -------------------------
# Mostrar datos del paciente
# -------------------------

st.subheader("📋 Datos del Paciente")
st.json(paciente)

# -------------------------
# Respuesta del estudiante
# -------------------------

st.subheader("🧠 Clasifique al paciente")

respuesta = st.radio(
    "Seleccione la categoría de triage:",
    ["🟢 Verde", "🟡 Amarillo", "🔴 Rojo", "⚫ Negro"]
)

if st.button("Evaluar clasificación"):
    if respuesta == categoria_real:
        st.success("✅ Correcto. Clasificación adecuada según algoritmo START.")
    else:
        st.error(f"❌ Incorrecto. La clasificación correcta era: {categoria_real}")

  
    


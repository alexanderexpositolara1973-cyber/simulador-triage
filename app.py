import streamlit as st
import random

st.set_page_config(page_title="Plataforma de Simulación en Emergencias", layout="centered")

st.title("🚑 Plataforma Académica de Simulación Clínica")
st.markdown("Entrenamiento en Medicina de Emergencias")

# =====================================================
# 1️⃣ SIMULADOR DE VÍA AÉREA
# =====================================================

def simulador_via_aerea():

    st.header("🫁 Manejo Inicial de Vía Aérea")

    nivel_conciencia = random.choice(["Alerta", "Somnoliento", "Inconsciente"])
    saturacion = random.randint(75, 98)
    estridor = random.choice(["Sí", "No"])

    st.subheader("Datos del paciente")
    st.write(f"Nivel de conciencia: {nivel_conciencia}")
    st.write(f"Saturación O2: {saturacion}%")
    st.write(f"Estridor: {estridor}")

    respuesta = st.selectbox(
        "¿Cuál es la intervención inicial más adecuada?",
        [
            "Observación",
            "Cánula orofaríngea",
            "Oxígeno suplementario",
            "Intubación endotraqueal"
        ]
    )

    if st.button("Evaluar vía aérea"):

        if nivel_conciencia == "Inconsciente":
            correcta = "Intubación endotraqueal"
        elif saturacion < 90:
            correcta = "Oxígeno suplementario"
        else:
            correcta = "Observación"

        if respuesta == correcta:
            st.success("✅ Decisión adecuada.")
        else:
            st.error(f"❌ Respuesta esperada: {correcta}")

# =====================================================
# 2️⃣ SIMULADOR DE RCP
# =====================================================

def simulador_rcp():

    st.header("❤️ Reanimación Cardiopulmonar (RCP)")

    ritmo = random.choice(["FV/TV sin pulso", "Asistolia", "Actividad eléctrica sin pulso"])
    pulso = "No"

    st.subheader("Escenario")
    st.write(f"Paciente inconsciente, sin pulso.")
    st.write(f"Ritmo en monitor: {ritmo}")

    respuesta = st.selectbox(
        "¿Siguiente paso?",
        [
            "Desfibrilar",
            "Administrar adrenalina",
            "Iniciar compresiones torácicas",
            "Intubar inmediatamente"
        ]
    )

    if st.button("Evaluar RCP"):

        if ritmo == "FV/TV sin pulso":
            correcta = "Desfibrilar"
        else:
            correcta = "Iniciar compresiones torácicas"

        if respuesta == correcta:
            st.success("✅ Conducta correcta según algoritmo ACLS simplificado.")
        else:
            st.error(f"❌ Conducta esperada: {correcta}")

# =====================================================
# 3️⃣ SIMULADOR DE ESTADO DE SHOCK
# =====================================================

def simulador_shock():

    st.header("🩸 Reconocimiento de Shock")

    ta_sistolica = random.randint(70, 120)
    fc = random.randint(80, 140)
    piel = random.choice(["Fría", "Caliente"])

    st.subheader("Signos vitales")
    st.write(f"Tensión sistólica: {ta_sistolica} mmHg")
    st.write(f"Frecuencia cardíaca: {fc} lpm")
    st.write(f"Piel: {piel}")

    respuesta = st.selectbox(
        "Clasificación más probable:",
        [
            "Shock hipovolémico",
            "Shock distributivo",
            "Sin shock"
        ]
    )

    if st.button("Evaluar shock"):

        if ta_sistolica < 90 and piel == "Fría":
            correcta = "Shock hipovolémico"
        elif ta_sistolica < 90 and piel == "Caliente":
            correcta = "Shock distributivo"
        else:
            correcta = "Sin shock"

        if respuesta == correcta:
            st.success("✅ Clasificación adecuada.")
        else:
            st.error(f"❌ Respuesta correcta: {correcta}")

# =====================================================
# 4️⃣ SIMULADOR TCE
# =====================================================

def simulador_tce():

    st.header("🧠 Trauma Cráneo Encefálico (TCE)")

    glasgow = random.randint(3, 15)

    st.subheader("Evaluación neurológica")
    st.write(f"Escala de Glasgow: {glasgow}")

    respuesta = st.selectbox(
        "Clasificación del TCE:",
        [
            "Leve",
            "Moderado",
            "Grave"
        ]
    )

    if st.button("Evaluar TCE"):

        if glasgow >= 13:
            correcta = "Leve"
        elif 9 <= glasgow <= 12:
            correcta = "Moderado"
        else:
            correcta = "Grave"

        if respuesta == correcta:
            st.success("✅ Clasificación correcta.")
        else:
            st.error(f"❌ Clasificación correcta: {correcta}")

# =====================================================
# 5️⃣ SIMULADOR GASOMETRÍA
# =====================================================

def simulador_gasometria():

    st.header("🧪 Interpretación de Gasometría Arterial")

    ph = round(random.uniform(7.1, 7.5), 2)
    pco2 = random.randint(20, 60)
    hco3 = random.randint(15, 30)

    st.subheader("Valores")
    st.write(f"pH: {ph}")
    st.write(f"PaCO2: {pco2} mmHg")
    st.write(f"HCO3: {hco3} mEq/L")

    respuesta = st.selectbox(
        "Interpretación primaria:",
        [
            "Acidosis metabólica",
            "Acidosis respiratoria",
            "Alcalosis metabólica",
            "Normal"
        ]
    )

    if st.button("Evaluar gasometría"):

        if ph < 7.35 and hco3 < 22:
            correcta = "Acidosis metabólica"
        elif ph < 7.35 and pco2 > 45:
            correcta = "Acidosis respiratoria"
        elif ph > 7.45:
            correcta = "Alcalosis metabólica"
        else:
            correcta = "Normal"

        if respuesta == correcta:
            st.success("✅ Interpretación adecuada.")
        else:
            st.error(f"❌ Respuesta correcta: {correcta}")

# =====================================================
# MENÚ PRINCIPAL
# =====================================================

st.divider()

modulo = st.selectbox(
    "Seleccione el módulo de simulación:",
    [
        "Vía Aérea",
        "RCP",
        "Shock",
        "TCE",
        "Gasometría"
    ]
)

if modulo == "Vía Aérea":
    simulador_via_aerea()

elif modulo == "RCP":
    simulador_rcp()

elif modulo == "Shock":
    simulador_shock()

elif modulo == "TCE":
    simulador_tce()

elif modulo == "Gasometría":
    simulador_gasometria()
  
        

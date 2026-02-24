import streamlit as st
import random

st.set_page_config(page_title="Simulador Clínico Avanzado en Emergencias", layout="centered")

st.title("🚑 Plataforma Académica Avanzada de Simulación en Emergencias")
st.markdown("Entrenamiento clínico con coherencia fisiopatológica")

# =====================================================
# 1️⃣ SIMULADOR DE VÍA AÉREA (Mejorado)
# =====================================================

def simulador_via_aerea():

    st.header("🫁 Manejo Inicial de la Vía Aérea")

    nivel_conciencia = random.choice(["Alerta", "Somnoliento", "Inconsciente"])
    saturacion = random.randint(82, 98)
    estridor = random.choice(["Sí", "No"])
    trabajo_respiratorio = random.choice(["Normal", "Aumentado"])

    st.subheader("Datos del paciente")
    st.write(f"Nivel de conciencia: {nivel_conciencia}")
    st.write(f"Saturación O2: {saturacion}%")
    st.write(f"Estridor: {estridor}")
    st.write(f"Trabajo respiratorio: {trabajo_respiratorio}")

    respuesta = st.selectbox(
        "¿Conducta inicial más adecuada?",
        [
            "Observación",
            "Oxígeno suplementario",
            "Cánula orofaríngea",
            "Intubación endotraqueal"
        ]
    )

    if st.button("Evaluar vía aérea"):

        if estridor == "Sí" or (nivel_conciencia == "Inconsciente" and saturacion < 90):
            correcta = "Intubación endotraqueal"
        elif saturacion < 90 or trabajo_respiratorio == "Aumentado":
            correcta = "Oxígeno suplementario"
        elif nivel_conciencia == "Inconsciente":
            correcta = "Cánula orofaríngea"
        else:
            correcta = "Observación"

        if respuesta == correcta:
            st.success("✅ Conducta adecuada según evaluación ABC.")
        else:
            st.error(f"❌ Conducta esperada: {correcta}")

# =====================================================
# 2️⃣ SIMULADOR DE RCP (Basado en ACLS simplificado)
# =====================================================

def simulador_rcp():

    st.header("❤️ Reanimación Cardiopulmonar (RCP)")

    ritmo = random.choice(["FV/TV sin pulso", "Asistolia", "Actividad eléctrica sin pulso"])

    st.subheader("Escenario clínico")
    st.write("Paciente inconsciente, sin pulso.")
    st.write(f"Ritmo en monitor: {rito}")

    respuesta = st.selectbox(
        "¿Siguiente paso inmediato?",
        [
            "Iniciar compresiones torácicas",
            "Desfibrilar",
            "Administrar adrenalina",
            "Intubar inmediatamente"
        ]
    )

    if st.button("Evaluar RCP"):

        if ritmo == "FV/TV sin pulso":
            correcta = "Desfibrilar"
        else:
            correcta = "Iniciar compresiones torácicas"

        if respuesta == correcta:
            st.success("✅ Conducta acorde a algoritmo ACLS simplificado.")
        else:
            st.error(f"❌ Conducta correcta: {correcta}")

# =====================================================
# 3️⃣ SIMULADOR DE SHOCK (Integrando FC)
# =====================================================

def simulador_shock():

    st.header("🩸 Reconocimiento y Clasificación de Shock")

    ta_sistolica = random.randint(70, 120)
    fc = random.randint(80, 140)
    piel = random.choice(["Fría", "Caliente"])

    indice_shock = round(fc / ta_sistolica, 2)

    st.subheader("Signos vitales")
    st.write(f"Tensión sistólica: {ta_sistolica} mmHg")
    st.write(f"Frecuencia cardíaca: {fc} lpm")
    st.write(f"Piel: {piel}")
    st.write(f"Índice de shock (FC/TAS): {indice_shock}")

    respuesta = st.selectbox(
        "Clasificación más probable:",
        [
            "Shock hipovolémico",
            "Shock distributivo",
            "Sin shock"
        ]
    )

    if st.button("Evaluar shock"):

        if ta_sistolica < 90 and piel == "Fría" and indice_shock > 0.9:
            correcta = "Shock hipovolémico"
        elif ta_sistolica < 90 and piel == "Caliente":
            correcta = "Shock distributivo"
        else:
            correcta = "Sin shock"

        if respuesta == correcta:
            st.success("✅ Clasificación adecuada según fisiopatología.")
        else:
            st.error(f"❌ Clasificación correcta: {correcta}")

# =====================================================
# 4️⃣ SIMULADOR TCE (Con criterio clínico)
# =====================================================

def simulador_tce():

    st.header("🧠 Trauma Cráneo Encefálico (TCE)")

    glasgow = random.randint(3, 15)
    hipotension = random.choice(["Sí", "No"])
    hipoxia = random.choice(["Sí", "No"])

    st.subheader("Evaluación")
    st.write(f"Glasgow: {glasgow}")
    st.write(f"Hipotensión: {hipotension}")
    st.write(f"Hipoxia: {hipoxia}")

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
# 5️⃣ SIMULADOR GASOMETRÍA (Coherente)
# =====================================================

def simulador_gasometria():

    st.header("🧪 Interpretación de Gasometría Arterial")

    trastorno = random.choice([
        "Acidosis metabólica",
        "Acidosis respiratoria",
        "Alcalosis metabólica",
        "Normal"
    ])

    if trastorno == "Acidosis metabólica":
        ph = round(random.uniform(7.10, 7.30), 2)
        hco3 = random.randint(10, 20)
        pco2 = random.randint(25, 35)

    elif trastorno == "Acidosis respiratoria":
        ph = round(random.uniform(7.10, 7.30), 2)
        pco2 = random.randint(50, 70)
        hco3 = random.randint(24, 30)

    elif trastorno == "Alcalosis metabólica":
        ph = round(random.uniform(7.46, 7.55), 2)
        hco3 = random.randint(30, 40)
        pco2 = random.randint(45, 55)

    else:
        ph = round(random.uniform(7.36, 7.44), 2)
        pco2 = random.randint(35, 45)
        hco3 = random.randint(22, 26)

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

        if respuesta == trastorno:
            st.success("✅ Interpretación correcta.")
        else:
            st.error(f"❌ Diagnóstico correcto: {trastorno}")

# =====================================================
# MENÚ PRINCIPAL
# =====================================================

st.divider()

modulo = st.selectbox(
    "Seleccione módulo:",
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
         

   
        


  



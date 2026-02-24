import streamlit as st
import random

st.set_page_config(page_title="Simulador Clínico Avanzado", layout="centered")

st.title("🚑 Plataforma Académica de Simulación en Emergencias")

# =====================================================
# 1️⃣ VÍA AÉREA
# =====================================================

def simulador_via_aerea():

    st.header("🫁 Manejo Inicial de la Vía Aérea")

    if "via_aerea" not in st.session_state:
        st.session_state.via_aerea = {
            "nivel": random.choice(["Alerta", "Somnoliento", "Inconsciente"]),
            "sat": random.randint(82, 98),
            "estridor": random.choice(["Sí", "No"]),
            "trabajo": random.choice(["Normal", "Aumentado"])
        }

    p = st.session_state.via_aerea

    st.write(f"Nivel de conciencia: {p['nivel']}")
    st.write(f"Saturación O2: {p['sat']}%")
    st.write(f"Estridor: {p['estridor']}")
    st.write(f"Trabajo respiratorio: {p['trabajo']}")

    respuesta = st.selectbox(
        "Conducta inicial:",
        ["Observación", "Oxígeno suplementario", "Cánula orofaríngea", "Intubación endotraqueal"],
        key="resp_via"
    )

    if st.button("Evaluar vía aérea"):

        if p["estridor"] == "Sí" or (p["nivel"] == "Inconsciente" and p["sat"] < 90):
            correcta = "Intubación endotraqueal"
        elif p["sat"] < 90 or p["trabajo"] == "Aumentado":
            correcta = "Oxígeno suplementario"
        elif p["nivel"] == "Inconsciente":
            correcta = "Cánula orofaríngea"
        else:
            correcta = "Observación"

        if respuesta == correcta:
            st.success("✅ Conducta adecuada.")
        else:
            st.error(f"❌ Conducta correcta: {correcta}")

    if st.button("Nuevo paciente vía aérea"):
        del st.session_state["via_aerea"]
        st.rerun()


# =====================================================
# 2️⃣ RCP
# =====================================================

def simulador_rcp():

    st.header("❤️ Reanimación Cardiopulmonar")

    if "rcp" not in st.session_state:
        st.session_state.rcp = {
            "ritmo": random.choice(["FV/TV sin pulso", "Asistolia", "Actividad eléctrica sin pulso"])
        }

    p = st.session_state.rcp

    st.write("Paciente inconsciente, sin pulso.")
    st.write(f"Ritmo en monitor: {p['ritmo']}")

    respuesta = st.selectbox(
        "Siguiente paso:",
        ["Iniciar compresiones torácicas", "Desfibrilar", "Administrar adrenalina", "Intubar inmediatamente"],
        key="resp_rcp"
    )

    if st.button("Evaluar RCP"):

        if p["ritmo"] == "FV/TV sin pulso":
            correcta = "Desfibrilar"
        else:
            correcta = "Iniciar compresiones torácicas"

        if respuesta == correcta:
            st.success("✅ Manejo acorde a ACLS simplificado.")
        else:
            st.error(f"❌ Conducta correcta: {correcta}")

    if st.button("Nuevo paciente RCP"):
        del st.session_state["rcp"]
        st.rerun()


# =====================================================
# 3️⃣ SHOCK
# =====================================================

def simulador_shock():

    st.header("🩸 Evaluación de Shock")

    if "shock" not in st.session_state:
        ta = random.randint(70, 120)
        fc = random.randint(80, 140)
        st.session_state.shock = {
            "ta": ta,
            "fc": fc,
            "piel": random.choice(["Fría", "Caliente"]),
            "indice": round(fc / ta, 2)
        }

    p = st.session_state.shock

    st.write(f"Tensión sistólica: {p['ta']} mmHg")
    st.write(f"Frecuencia cardíaca: {p['fc']} lpm")
    st.write(f"Piel: {p['piel']}")
    st.write(f"Índice de shock: {p['indice']}")

    respuesta = st.selectbox(
        "Clasificación:",
        ["Shock hipovolémico", "Shock distributivo", "Sin shock"],
        key="resp_shock"
    )

    if st.button("Evaluar shock"):

        if p["ta"] < 90 and p["piel"] == "Fría" and p["indice"] > 0.9:
            correcta = "Shock hipovolémico"
        elif p["ta"] < 90 and p["piel"] == "Caliente":
            correcta = "Shock distributivo"
        else:
            correcta = "Sin shock"

        if respuesta == correcta:
            st.success("✅ Clasificación adecuada.")
        else:
            st.error(f"❌ Clasificación correcta: {correcta}")

    if st.button("Nuevo paciente shock"):
        del st.session_state["shock"]
        st.rerun()


# =====================================================
# 4️⃣ TCE
# =====================================================

def simulador_tce():

    st.header("🧠 Trauma Cráneo Encefálico")

    if "tce" not in st.session_state:
        st.session_state.tce = {
            "glasgow": random.randint(3, 15),
            "hipotension": random.choice(["Sí", "No"]),
            "hipoxia": random.choice(["Sí", "No"])
        }

    p = st.session_state.tce

    st.write(f"Glasgow: {p['glasgow']}")
    st.write(f"Hipotensión: {p['hipotension']}")
    st.write(f"Hipoxia: {p['hipoxia']}")

    respuesta = st.selectbox(
        "Clasificación:",
        ["Leve", "Moderado", "Grave"],
        key="resp_tce"
    )

    if st.button("Evaluar TCE"):

        if p["glasgow"] >= 13:
            correcta = "Leve"
        elif 9 <= p["glasgow"] <= 12:
            correcta = "Moderado"
        else:
            correcta = "Grave"

        if respuesta == correcta:
            st.success("✅ Clasificación correcta.")
        else:
            st.error(f"❌ Clasificación correcta: {correcta}")

    if st.button("Nuevo paciente TCE"):
        del st.session_state["tce"]
        st.rerun()


# =====================================================
# 5️⃣ GASOMETRÍA
# =====================================================

def simulador_gasometria():

    st.header("🧪 Gasometría Arterial")

    if "gaso" not in st.session_state:

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

        st.session_state.gaso = {
            "ph": ph,
            "pco2": pco2,
            "hco3": hco3,
            "trastorno": trastorno
        }

    p = st.session_state.gaso

    st.write(f"pH: {p['ph']}")
    st.write(f"PaCO2: {p['pco2']} mmHg")
    st.write(f"HCO3: {p['hco3']} mEq/L")

    respuesta = st.selectbox(
        "Interpretación:",
        ["Acidosis metabólica", "Acidosis respiratoria", "Alcalosis metabólica", "Normal"],
        key="resp_gaso"
    )

    if st.button("Evaluar gasometría"):

        if respuesta == p["trastorno"]:
            st.success("✅ Interpretación correcta.")
        else:
            st.error(f"❌ Diagnóstico correcto: {p['trastorno']}")

    if st.button("Nuevo paciente gasometría"):
        del st.session_state["gaso"]
        st.rerun()


# =====================================================
# MENÚ PRINCIPAL
# =====================================================

st.divider()

modulo = st.selectbox(
    "Seleccione módulo:",
    ["Vía Aérea", "RCP", "Shock", "TCE", "Gasometría"]
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

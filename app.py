```python
import os
import streamlit as st
import base64
from openai import OpenAI

# =========================================================
# CONFIGURACIÓN
# =========================================================

st.set_page_config(
    page_title="LUMEN • Visión Accesible",
    page_icon="👁️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# ESTILOS
# =========================================================

st.markdown("""
<style>

    /* ------------------------------
       FONDO GENERAL
    ------------------------------ */

    .stApp {
        background:
        radial-gradient(circle at 10% 10%, #242044 0%, transparent 30%),
        radial-gradient(circle at 90% 20%, #172a46 0%, transparent 30%),
        #090b12;
        color: white;
    }

    /* ------------------------------
       OCULTAR ELEMENTOS DE STREAMLIT
    ------------------------------ */

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    header {
        visibility: hidden;
    }

    /* ------------------------------
       TEXTO
    ------------------------------ */

    h1 {
        font-size: 55px !important;
        font-weight: 800 !important;
        letter-spacing: -2px;
    }

    h2 {
        color: #ffffff !important;
    }

    h3 {
        color: #b8b9ff !important;
    }

    p {
        color: #b8bac8;
        font-size: 17px;
    }

    /* ------------------------------
       HERO
    ------------------------------ */

    .hero {
        padding: 45px 50px;
        border-radius: 28px;
        background:
        linear-gradient(
            135deg,
            rgba(101, 85, 220, 0.25),
            rgba(33, 61, 105, 0.15)
        );

        border: 1px solid rgba(255,255,255,0.10);
        margin-bottom: 30px;
    }

    .hero-small {
        color: #8f91ff;
        font-size: 14px;
        font-weight: bold;
        letter-spacing: 3px;
        text-transform: uppercase;
    }

    .hero-title {
        font-size: 52px;
        font-weight: 800;
        color: white;
        line-height: 1.05;
        margin-top: 10px;
    }

    .hero-description {
        max-width: 700px;
        color: #b7b8c8;
        font-size: 18px;
        line-height: 1.6;
        margin-top: 15px;
    }

    /* ------------------------------
       TARJETAS
    ------------------------------ */

    .card {
        background: rgba(20, 22, 32, 0.85);
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 24px;
        padding: 28px;
        margin-bottom: 20px;
    }

    .card-title {
        font-size: 21px;
        font-weight: 700;
        color: white;
        margin-bottom: 8px;
    }

    .card-subtitle {
        color: #858797;
        font-size: 14px;
        margin-bottom: 20px;
    }

    /* ------------------------------
       UPLOADER
    ------------------------------ */

    [data-testid="stFileUploader"] {
        background: rgba(255,255,255,0.03);
        border: 2px dashed #5556a8;
        border-radius: 18px;
        padding: 15px;
    }

    [data-testid="stFileUploaderDropzone"] {
        background: transparent;
    }

    /* ------------------------------
       BOTONES
    ------------------------------ */

    .stButton > button {
        width: 100%;
        height: 58px;
        border-radius: 16px;
        border: 1px solid rgba(255,255,255,0.12);
        background: #171a27;
        color: white;
        font-size: 16px;
        font-weight: 700;
        transition: 0.2s;
    }

    .stButton > button:hover {
        border-color: #7778ff;
        background: #20243a;
        color: white;
    }

    /* ------------------------------
       BOTÓN PRINCIPAL
    ------------------------------ */

    .scan-button button {
        background: linear-gradient(
            135deg,
            #7067ff,
            #4f8cff
        ) !important;

        border: none !important;
        height: 65px !important;
        font-size: 18px !important;
        box-shadow: 0px 10px 35px rgba(86,82,255,0.25);
    }

    /* ------------------------------
       RESULTADO
    ------------------------------ */

    .result-box {
        background: linear-gradient(
            145deg,
            rgba(34,36,52,0.95),
            rgba(18,20,30,0.95)
        );

        border-radius: 25px;
        padding: 30px;
        border: 1px solid rgba(255,255,255,0.09);
        margin-top: 20px;
    }

    .result-label {
        color: #7f82ff;
        font-size: 13px;
        font-weight: bold;
        letter-spacing: 2px;
        text-transform: uppercase;
    }

    .result-text {
        color: #eeeeF5;
        font-size: 19px;
        line-height: 1.7;
        margin-top: 15px;
    }

    /* ------------------------------
       ESTADOS
    ------------------------------ */

    .status {
        display: inline-block;
        padding: 8px 14px;
        border-radius: 50px;
        background: rgba(88, 255, 170, 0.10);
        color: #70ffb1;
        font-size: 13px;
        font-weight: bold;
    }

    /* ------------------------------
       INFO CARDS
    ------------------------------ */

    .info-card {
        background: rgba(255,255,255,0.035);
        border: 1px solid rgba(255,255,255,0.07);
        padding: 22px;
        border-radius: 20px;
        min-height: 150px;
    }

    .info-icon {
        font-size: 28px;
    }

    .info-title {
        color: white;
        font-size: 17px;
        font-weight: bold;
        margin-top: 10px;
    }

    .info-text {
        color: #858797;
        font-size: 14px;
        line-height: 1.5;
        margin-top: 5px;
    }

    /* ------------------------------
       INPUT
    ------------------------------ */

    input {
        background-color: #131520 !important;
        color: white !important;
        border-radius: 12px !important;
    }

</style>
""", unsafe_allow_html=True)


# =========================================================
# FUNCIÓN PARA CODIFICAR IMAGEN
# =========================================================

def encode_image(image_file):

    return base64.b64encode(
        image_file.getvalue()
    ).decode("utf-8")


# =========================================================
# API
# =========================================================

ke = st.text_input(
    "API Key",
    type="password",
    placeholder="Ingresa tu API Key...",
)

os.environ["OPENAI_API_KEY"] = ke

api_key = os.environ.get("OPENAI_API_KEY")

if api_key:
    client = OpenAI(api_key=api_key)
else:
    client = None


# =========================================================
# HEADER
# =========================================================

st.markdown("""
<div class="hero">

    <div class="hero-small">
        LUMEN • VISIÓN ACCESIBLE
    </div>

    <div class="hero-title">
        Convierte imágenes<br>
        en información audible.
    </div>

    <div class="hero-description">
        Un scanner inteligente diseñado para describir el mundo
        a personas ciegas o con baja visión mediante inteligencia
        artificial y síntesis de voz.
    </div>

</div>
""", unsafe_allow_html=True)


# =========================================================
# ESTADO
# =========================================================

if "description" not in st.session_state:
    st.session_state["description"] = None


# =========================================================
# COLUMNAS PRINCIPALES
# =========================================================

left, right = st.columns([1.1, 0.9], gap="large")


# =========================================================
# COLUMNA IZQUIERDA
# =========================================================

with left:

    st.markdown("""
    <div class="card">

        <div class="card-title">
            📷 Escanear una imagen
        </div>

        <div class="card-subtitle">
            Sube una fotografía para que LUMEN
            pueda analizarla.
        </div>

    </div>
    """, unsafe_allow_html=True)

    uploaded_file = st.file_uploader(
        "Seleccionar imagen",
        type=["jpg", "jpeg", "png"],
        label_visibility="collapsed"
    )

    if uploaded_file:

        st.image(
            uploaded_file,
            use_container_width=True
        )

        st.markdown(
            '<div class="status">● IMAGEN LISTA</div>',
            unsafe_allow_html=True
        )

    else:

        st.markdown("""
        <div style="
            text-align:center;
            padding:40px;
            color:#777987;
        ">

            <div style="font-size:55px;">
                ◉
            </div>

            <div style="font-size:18px;">
                Esperando una imagen
            </div>

            <div style="font-size:13px;">
                JPG, JPEG o PNG
            </div>

        </div>
        """, unsafe_allow_html=True)


# =========================================================
# COLUMNA DERECHA
# =========================================================

with right:

    st.markdown("""
    <div class="card">

        <div class="card-title">
            ⚙️ Configuración del análisis
        </div>

        <div class="card-subtitle">
            Personaliza qué quieres conocer de la imagen.
        </div>

    </div>
    """, unsafe_allow_html=True)

    show_details = st.toggle(
        "Hacer una pregunta específica"
    )

    additional_details = ""

    if show_details:

        additional_details = st.text_area(
            "Pregunta",
            placeholder="Ej: ¿Qué texto aparece en la imagen?",
            height=110
        )

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        '<div class="scan-button">',
        unsafe_allow_html=True
    )

    analyze_button = st.button(
        "🔍  ESCANEAR IMAGEN",
        use_container_width=True
    )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )


# =========================================================
# ANALIZAR IMAGEN
# =========================================================

if uploaded_file is not None and api_key and analyze_button:

    with st.spinner("LUMEN está analizando la imagen..."):

        base64_image = encode_image(uploaded_file)

        prompt_text = """
        Describe esta imagen en español para una persona ciega
        o con baja visión.

        La descripción debe ser clara, natural y fácil de escuchar.

        Incluye:

        1. Qué tipo de lugar o escena aparece.
        2. Las personas presentes y qué están haciendo.
        3. Los objetos importantes y dónde están ubicados.
        4. Colores relevantes.
        5. Texto visible.
        6. Información que pueda ser importante para comprender
           la escena.

        Evita información innecesaria.
        No utilices lenguaje técnico.
        Imagina que la persona no puede ver absolutamente nada
        de la imagen.
        """

        if show_details and additional_details:

            prompt_text += f"""

            La persona también preguntó:

            {additional_details}

            Responde específicamente a esa pregunta.
            """

        messages = [
            {
                "role": "user",
                "content": [

                    {
                        "type": "text",
                        "text": prompt_text
                    },

                    {
                        "type": "image_url",
                        "image_url": {
                            "url":
                            f"data:image/jpeg;base64,{base64_image}"
                        }
                    }

                ]
            }
        ]

        try:

            response = client.chat.completions.create(
                model="gpt-4o",
                messages=messages,
                max_tokens=1200
            )

            st.session_state["description"] = (
                response.choices[0].message.content
            )

        except Exception as e:

            st.error(
                f"Error durante el análisis: {e}"
            )


# =========================================================
# RESULTADO
# =========================================================

if st.session_state["description"]:

    st.markdown("---")

    st.markdown("""
    <div class="result-box">

        <div class="result-label">
            ANÁLISIS COMPLETADO
        </div>

        <div class="card-title">
            👁️ Esto es lo que LUMEN encontró
        </div>

    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        f"""
        <div class="result-box">

            <div class="result-text">
                {st.session_state["description"]}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # =====================================================
    # BOTONES DE ACCIÓN
    # =====================================================

    col1, col2, col3 = st.columns(3)

    with col1:

        listen = st.button(
            "🔊 Escuchar",
            use_container_width=True
        )

    with col2:

        new_scan = st.button(
            "📷 Nuevo escaneo",
            use_container_width=True
        )

    with col3:

        clear = st.button(
            "✕ Limpiar",
            use_container_width=True
        )

    # =====================================================
    # TEXTO A VOZ
    # =====================================================

    if listen:

        try:

            with st.spinner("Preparando audio..."):

                speech_response = client.audio.speech.create(
                    model="gpt-4o-mini-tts",
                    voice="alloy",
                    input=st.session_state["description"]
                )

                audio_bytes = speech_response.read()

                st.audio(
                    audio_bytes,
                    format="audio/mp3"
                )

                st.success(
                    "Descripción lista para escuchar."
                )

        except Exception as e:

            st.error(
                f"No se pudo generar el audio: {e}"
            )

    if clear:

        st.session_state["description"] = None
        st.rerun()


# =========================================================
# SECCIÓN INFORMATIVA
# =========================================================

st.markdown("---")

st.markdown("""
<div style="
    text-align:center;
    padding:20px;
">

    <div style="
        color:#7779ff;
        font-size:13px;
        font-weight:bold;
        letter-spacing:3px;
    ">
        ¿CÓMO FUNCIONA?
    </div>

    <div style="
        color:white;
        font-size:30px;
        font-weight:bold;
        margin-top:8px;
    ">
        Tres pasos para entender tu entorno
    </div>

</div>
""", unsafe_allow_html=True)


info1, info2, info3 = st.columns(3)


with info1:

    st.markdown("""
    <div class="info-card">

        <div class="info-icon">📷</div>

        <div class="info-title">
            01 · Captura
        </div>

        <div class="info-text">
            Sube una fotografía del entorno,
            objeto o documento que quieras
            analizar.
        </div>

    </div>
    """, unsafe_allow_html=True)


with info2:

    st.markdown("""
    <div class="info-card">

        <div class="info-icon">🧠</div>

        <div class="info-title">
            02 · Comprende
        </div>

        <div class="info-text">
            La inteligencia artificial analiza
            los elementos importantes de la
            imagen.
        </div>

    </div>
    """, unsafe_allow_html=True)


with info3:

    st.markdown("""
    <div class="info-card">

        <div class="info-icon">🔊</div>

        <div class="info-title">
            03 · Escucha
        </div>

        <div class="info-text">
            Pulsa el botón de audio para
            escuchar una descripción
            del contenido.
        </div>

    </div>
    """, unsafe_allow_html=True)


# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<br><br>

<div style="
    text-align:center;
    color:#555866;
    font-size:13px;
    padding:20px;
">

    LUMEN • Proyecto de accesibilidad con IA

</div>
""", unsafe_allow_html=True)
```

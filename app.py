import os
import streamlit as st
import base64
from openai import OpenAI

# -----------------------------------
# CONFIGURACIÓN
# -----------------------------------

st.set_page_config(
    page_title="Visión Accesible",
    page_icon="👁️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.title("👁️ Visión Accesible")
st.subheader("Scanner de imágenes para personas ciegas")

st.write(
    "Sube una imagen y el sistema describirá lo que aparece en ella. "
    "Después podrás escuchar la descripción mediante voz."
)

# -----------------------------------
# API KEY
# -----------------------------------

ke = st.text_input(
    "Ingresa tu API Key",
    type="password"
)

os.environ["OPENAI_API_KEY"] = ke

api_key = os.environ.get("OPENAI_API_KEY")

if api_key:
    client = OpenAI(api_key=api_key)
else:
    client = None


# -----------------------------------
# FUNCIÓN PARA CONVERTIR IMAGEN
# -----------------------------------

def encode_image(image_file):
    return base64.b64encode(
        image_file.getvalue()
    ).decode("utf-8")


# -----------------------------------
# SUBIR IMAGEN
# -----------------------------------

st.markdown("### 📷 Escanear imagen")

uploaded_file = st.file_uploader(
    "Selecciona una imagen",
    type=["jpg", "png", "jpeg"]
)

if uploaded_file:

    st.image(
        uploaded_file,
        caption="Imagen escaneada",
        use_container_width=True
    )

    st.success("Imagen lista para analizar")


# -----------------------------------
# OPCIÓN DE CONTEXTO
# -----------------------------------

show_details = st.toggle(
    "¿Quieres hacer una pregunta específica?",
    value=False
)

additional_details = ""

if show_details:

    additional_details = st.text_area(
        "Escribe qué quieres saber de la imagen:",
        placeholder="Ejemplo: ¿Qué objetos hay sobre la mesa?"
    )


# -----------------------------------
# BOTÓN DE ESCANEAR
# -----------------------------------

analyze_button = st.button(
    "🔍 ESCANEAR IMAGEN",
    type="primary",
    use_container_width=True
)


# -----------------------------------
# ANÁLISIS
# -----------------------------------

if uploaded_file is not None and api_key and analyze_button:

    with st.spinner("Analizando imagen..."):

        base64_image = encode_image(uploaded_file)

        prompt_text = """
        Describe esta imagen en español para una persona ciega o con baja visión.

        Sé claro, directo y natural.

        Describe:
        - Las personas que aparecen.
        - Los objetos importantes.
        - El lugar o ambiente.
        - Los colores importantes.
        - Las acciones que están ocurriendo.
        - El texto visible en la imagen, si existe.
        - Cualquier elemento que pueda ser importante para comprender la escena.

        No describas cosas innecesarias.
        No uses lenguaje demasiado técnico.
        Organiza la descripción de manera que sea fácil de escuchar mediante voz.
        """

        if show_details and additional_details:

            prompt_text += f"""

            La persona también quiere saber específicamente:
            {additional_details}
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
                            "url": f"data:image/jpeg;base64,{base64_image}"
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

            full_response = response.choices[0].message.content

            # Guardamos la descripción para utilizarla
            # posteriormente con el botón de voz.
            st.session_state["description"] = full_response

        except Exception as e:

            st.error(
                f"No se pudo analizar la imagen: {e}"
            )


# -----------------------------------
# RESULTADO
# -----------------------------------

if "description" in st.session_state:

    st.markdown("---")

    st.markdown("### 📝 Descripción de la imagen")

    st.info(
        st.session_state["description"]
    )

    # -----------------------------------
    # TEXTO A VOZ
    # -----------------------------------

    st.markdown("### 🔊 Escuchar descripción")

    speech_button = st.button(
        "🔊 ESCUCHAR DESCRIPCIÓN",
        use_container_width=True
    )

    if speech_button:

        try:

            with st.spinner("Generando audio..."):

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

        except Exception as e:

            st.error(
                f"No se pudo generar el audio: {e}"
            )


# -----------------------------------
# MENSAJES DE AYUDA
# -----------------------------------

if analyze_button and not uploaded_file:

    st.warning(
        "📷 Primero debes subir una imagen."
    )

if analyze_button and not api_key:

    st.warning(
        "🔑 Primero debes ingresar tu API Key."
    )

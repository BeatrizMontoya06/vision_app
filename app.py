"""
👁️ OCULUS ARCHIVE // LABORATORIO DE VISION ARTIFICIAL
Estética: Cyberpunk Holo-Net / Terminal de Visión Cuántica Oscura y Neón
"""

import os
import streamlit as st
import base64
from openai import OpenAI

def encode_image(image_file):
    return base64.b64encode(image_file.getvalue()).decode("utf-8")

st.set_page_config(
    page_title="Oculus Archive // Vision Studio",
    page_icon="👁️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ── Estética Cyberpunk Holo-Net / Terminal Visual Oscuro ─────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Share+Tech+Mono&display=swap');

    .stApp {
        background: #050508;
        background-image: 
            radial-gradient(circle at 50% 10%, #120d21 0%, #050508 70%),
            linear-gradient(rgba(18, 13, 33, 0.1) 50%, rgba(0, 0, 0, 0.3) 50%);
        background-size: 100% 100%, 100% 4px;
        color: #00ffcc;
        font-family: 'Share Tech Mono', monospace;
    }

    header {visibility: hidden;}

    /* Cabecera Principal Tipo HUD Cibernético */
    .cyber-header {
        border: 1px solid #ff0055;
        background: rgba(15, 10, 25, 0.85);
        padding: 25px;
        text-align: center;
        box-shadow: 0 0 20px rgba(255, 0, 85, 0.25), inset 0 0 10px rgba(255, 0, 85, 0.1);
        margin-bottom: 30px;
        border-radius: 4px;
    }

    .cyber-header h1 {
        font-family: 'Orbitron', sans-serif;
        font-size: 2.2rem;
        color: #ff0055;
        letter-spacing: 3px;
        margin: 0;
        text-shadow: 0 0 10px rgba(255, 0, 85, 0.6);
    }

    .cyber-header p {
        font-family: 'Share Tech Mono', monospace;
        font-size: 0.85rem;
        color: #00ffcc;
        letter-spacing: 2px;
        margin-top: 8px;
        text-transform: uppercase;
    }

    /* Paneles Estilo Estación de Escaneo */
    .scan-panel {
        background: #0a0812;
        border: 1px solid #1f1835;
        border-left: 3px solid #00ffcc;
        padding: 25px;
        margin-bottom: 20px;
        box-shadow: 0 8px 32px rgba(0,0,0,0.8);
        border-radius: 2px;
    }

    .scan-panel h3 {
        font-family: 'Orbitron', sans-serif;
        font-size: 0.9rem;
        color: #00ffcc;
        letter-spacing: 1px;
        text-transform: uppercase;
        margin-top: 0;
        border-bottom: 1px dashed #1f1835;
        padding-bottom: 8px;
    }

    /* Consola de visualización de resultados tipo terminal */
    .terminal-stream {
        background: #030206;
        border: 1px solid #00ffcc;
        padding: 20px;
        font-family: 'Share Tech Mono', monospace;
        font-size: 1.1rem;
        color: #00ffcc;
        line-height: 1.6;
        min-height: 180px;
        box-shadow: inset 0 0 15px rgba(0, 255, 204, 0.15);
        border-radius: 2px;
    }

    /* Botones de Comando Estilo Neón */
    .stButton>button {
        background: transparent !important;
        color: #00ffcc !important;
        border: 1px solid #00ffcc !important;
        border-radius: 0px !important;
        font-family: 'Orbitron', sans-serif !important;
        font-size: 0.75rem !important;
        letter-spacing: 2px !important;
        text-transform: uppercase !important;
        padding: 12px 24px !important;
        width: 100% !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 0 10px rgba(0, 255, 204, 0.2);
    }

    .stButton>button:hover {
        background: #00ffcc !important;
        color: #050508 !important;
        box-shadow: 0 0 20px rgba(0, 255, 204, 0.6);
    }

    /* Estilización de Inputs y Controles */
    .stTextInput input, .stTextArea textarea {
        background: #030206 !important;
        border: 1px solid #1f1835 !important;
        color: #00ffcc !important;
        font-family: 'Share Tech Mono', monospace !important;
    }
    
    label {
        font-family: 'Share Tech Mono', monospace !important;
        font-size: 0.85rem !important;
        color: #8c82a8 !important;
    }
</style>
""", unsafe_allow_html=True)

# ── Cabecera de Interfaz Única ────────────────────────────────────────────────
st.markdown("""
<div class="cyber-header">
    <h1>oculus archive // neural vision</h1>
    <p>sistema de decodificación visual y análisis espectral por IA</p>
</div>
""", unsafe_allow_html=True)

# ── Distribución Asimétrica de Paneles ────────────────────────────────────────
col_net1, col_net2 = st.columns([1, 1], gap="large")

with col_net1:
    st.markdown('<div class="scan-panel">', unsafe_allow_html=True)
    st.markdown("### ⚡ 1. Enlace de Credenciales")
    ke = st.text_input('Clave de acceso OpenAI', type="password", placeholder="sk-...")
    if ke:
        os.environ['OPENAI_API_KEY'] = ke
        st.caption("[+] Núcleo criptográfico vinculado correctamente.")
    else:
        st.warning("[!] Ingrese su clave API para habilitar los circuitos de visión.")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="scan-panel">', unsafe_allow_html=True)
    st.markdown("### 👁️ 2. Ingesta de Muestra Visual")
    uploaded_file = st.file_uploader("Cargar archivo de imagen", type=["jpg", "png", "jpeg"])
    
    if uploaded_file:
        st.image(uploaded_file, caption=f"Muestra: {uploaded_file.name}", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col_net2:
    st.markdown('<div class="scan-panel">', unsafe_allow_html=True)
    st.markdown("### 🎛️ 3. Parámetros de Escaneo")
    show_details = st.toggle("Activar directrices de contexto específico", value=False)
    
    additional_details = st.text_area(
        "Parámetros o preguntas adicionales para la lectura:",
        disabled=not show_details,
        placeholder="Indique enfoques particulares, textos ocultos o patrones..."
    )
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="scan-panel">', unsafe_allow_html=True)
    st.markdown("### 🖥️ 4. Consola de Resultados Neurales")
    analyze_button = st.button("Iniciar escaneo de imagen")
    
    output_slot = st.empty()
    output_slot.markdown(
        '<div class="terminal-stream">> [ESTADO: SISTEMA EN ESPERA DE MUESTRA VISUAL]<br>> Cargue una imagen y configure los parámetros para iniciar la inferencia.</div>',
        unsafe_allow_html=True
    )
    st.markdown('</div>', unsafe_allow_html=True)

# ── Lógica de Procesamiento y Streaming ──────────────────────────────────────
api_key = os.environ.get('OPENAI_API_KEY', '')

if uploaded_file is not None and api_key and analyze_button:
    try:
        client = OpenAI(api_key=api_key)
        
        with st.spinner("Analizando espectro visual..."):
            base64_image = encode_image(uploaded_file)
            prompt_text = "Describe what you see in the image in spanish"
            
            if show_details and additional_details:
                prompt_text += f"\n\nAdditional Context Provided by the User:\n{additional_details}"
            
            messages = [
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt_text},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}"
                            }
                        },
                    ],
                }
            ]
            
            full_response = ""
            for completion in client.chat.completions.create(
                model="gpt-4o",
                messages=messages,
                max_tokens=1200,
                stream=True
            ):
                if completion.choices[0].delta.content is not None:
                    full_response += completion.choices[0].delta.content
                    output_slot.markdown(f'<div class="terminal-stream">{full_response}▌</div>', unsafe_allow_html=True)
            
            output_slot.markdown(f'<div class="terminal-stream">{full_response}</div>', unsafe_allow_html=True)

    except Exception as e:
        st.error(f"[!] Error crítico en el canal de visión: {e}")

elif analyze_button:
    if not uploaded_file:
        st.warning("[!] Alerta: Se requiere una muestra de imagen para procesar el análisis.")
    if not api_key:
        st.warning("[!] Alerta: Clave API de OpenAI no detectada en los circuitos.")

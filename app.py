import streamlit as st

# 1. Configuração da Página e Estética Visual
st.set_page_config(page_title="GM - Engenharia de Software", page_icon="❄️", layout="centered")

# --- CSS CUSTOMIZADO ---
st.markdown("""
    <style>
    /* Fundo da página */
    .stApp {
        background-color: #f0f2f6;
    }
    
    /* Cards brancos de entrada */
    [data-testid="stVerticalBlockBorderWrapper"] {
        background-color: white;
        padding: 30px !important;
        border-radius: 15px !important;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05) !important;
        border: none !important;
        margin-bottom: 20px !important;
    }

    /* Botão Cinza (conforme você confirmou que funcionou) */
    .stButton>button {
        width: 100%;
        background-color: #95a5a6 !important;
        color: white !important;
        border-radius: 10px;
        height: 3.5em;
        font-weight: bold;
        border: none !important;
    }

    /* ESTILO DO CARD AZUL DE RESULTADO */
    .card-resultado {
        background-color: #004aad !important;
        padding: 40px !important;
        border-radius: 25px !important;
        text-align: center !important;
        margin: 20px 0px !important;
        box-shadow: 0 10px 20px rgba(0, 74, 173, 0.2) !important;
    }
    
    /* Forçando a cor branca em todos os textos do card */
    .card-resultado h2, .card-resultado h1, .card-resultado p {
        color: white !important;
        font-family: 'sans serif' !important;
        margin: 0 !important;
    }
    
    .valor-btu {
        font-size: 3.5rem !important;
        font-weight: 800 !important;
        margin-top: 10px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- CABEÇALHO ---
col_logo_a, col_logo_b, col_logo_c = st.columns([1, 2, 1])
with col_logo_b:
    st.image("logo_gm.png", use_container_width=True)

st.markdown("<p style='text-align: center; color: gray; margin-top: -10px;'>Sistema Especialista em Dimensionamento Térmico</p>", unsafe_allow_html=True)

# --- ENTRADA DE DADOS ---

with st.container(border=True):
    st.markdown("#### 📏 Dimensões do Ambiente")
    opcao_medida = st.radio("Método:", ["Área total (m²)", "Comprimento x Largura"], horizontal=True)

    area = 0.0
    comprimento = 0.0
    largura = 0.0

    if opcao_medida == "Área total (m²)":
        area = st.number_input("Informe a área total (m²)", min_value=0.0, step=1.0)
    else:
        c1, c2 = st.columns(2)
        with c1: comprimento = st.number_input("Comprimento (m)", min_value=0.0, step=0.1)
        with c2: largura = st.number_input("Largura (m)", min_value=0.0, step=0.1)
        area = comprimento * largura
        if area > 0: st.info(f"Área calculada: **{area:.2f} m²**")

with st.container(border=True):
    st.markdown("#### 🔥 Fatores de Aquecimento")
    col_a, col_b = st.columns(2)
    with col_a:
        sol = st.selectbox("Incidência Solar:", ["Sombra/Manhã", "Sol o dia todo"])
        pessoas = st.number_input("Qtd. de Pessoas:", min_value=1, value=1)
    with col_b:
        eletronicos = st.number_input("Aparelhos Eletrônicos:", min_value=0, value=0)

# --- PROCESSAMENTO E EXIBIÇÃO ---

if st.button("CALCULAR E ANALISAR DISPOSIÇÃO"):
    if area <= 0:
        st.warning("⚠️ Informe as medidas do ambiente.")
    else:
        fator = 800 if sol == "Sol o dia todo" else 600
        carga_total = (area * fator) + ((pessoas - 1) * fator) + (eletronicos * fator)

        # CARD AZUL PERSONALIZADO
        st.markdown(f"""
            <div class="card-resultado">
                <p style="font-size: 1.2rem; opacity: 0.9;">✅ Dimensionamento Concluído</p>
                <p style="font-size: 1rem; opacity: 0.8; margin-top: 10px;">Carga Térmica Necessária</p>
                <h1 class="valor-btu">{carga_total:,.0f} BTUs</h1>
            </div>
            """.replace(',', '.'), unsafe_allow_html=True)
        
        # Sugestões
        st.markdown("### 🎯 Sugestões de Equipamentos")
        
        is_comprido = False
        if opcao_medida != "Área total (m²)" and largura > 0:
            if (comprimento / largura) > 1.8 or (comprimento / largura) < 0.5: is_comprido = True

        s1, s2 = st.columns(2)
        with s1:
            with st.container(border=True):
                st.markdown("**Alta Potência**")
                st.image("pisoteto.jpg")
                qtd_36 = int(carga_total / 36000) or 1
                if carga_total % 36000 > 6000: qtd_36 += 1
                st.info(f"📍 {qtd_36}x 36.000 BTUs")
        
        with s2:
            with st.container(border=True):
                st.markdown("**Distribuição Otimizada**")
                st.image("hiwall.jpg")
                qtd_12 = int(carga_total / 12000) or 1
                if carga_total % 12000 > 2000: qtd_12 += 1
                st.success(f"📍 {qtd_12}x 12.000 BTUs")
                if is_comprido: st.warning("💡 Recomendado para o formato do ambiente.")

# --- RODAPÉ ---
st.markdown("<br><hr><div style='text-align: center; color: gray; font-size: 0.8rem;'>Desenvolvido por <b>Glaudson Montenegro</b> | Projeto ADS</div>", unsafe_allow_html=True)
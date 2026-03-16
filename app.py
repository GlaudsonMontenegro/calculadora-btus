import streamlit as st

# 1. Configuração da Página e Estética Visual
st.set_page_config(page_title="GM - Engenharia de Software", page_icon="❄️", layout="centered")

# --- CSS CUSTOMIZADO (Identidade Visual GM - Total Azul) ---
st.markdown("""
    <style>
    /* Fundo da página */
    .stApp {
        background-color: #f0f2f6;
    }
    
    /* CARDS AZUIS (Entrada e Resultado) */
    [data-testid="stVerticalBlockBorderWrapper"] {
        background-color: #004aad !important;
        padding: 30px !important;
        border-radius: 20px !important;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1) !important;
        border: none !important;
        margin-bottom: 20px !important;
    }

    /* Forçando texto branco dentro dos cards azuis */
    [data-testid="stVerticalBlockBorderWrapper"] p, 
    [data-testid="stVerticalBlockBorderWrapper"] h4, 
    [data-testid="stVerticalBlockBorderWrapper"] label,
    [data-testid="stVerticalBlockBorderWrapper"] span {
        color: white !important;
    }

    /* Ajuste para os campos de entrada (Inputs) aparecerem bem no fundo azul */
    .stNumberInput input, .stSelectbox div, .stRadio label {
        background-color: rgba(255, 255, 255, 0.1) !important;
        color: white !important;
        border-radius: 8px !important;
    }

    /* Botão Principal Cinza */
    .stButton>button {
        width: 100%;
        background-color: #95a5a6 !important;
        color: white !important;
        border-radius: 10px;
        height: 3.5em;
        font-weight: bold;
        border: none !important;
    }

    /* Estilo específico para o valor do BTU no resultado */
    .valor-btu {
        font-size: 4rem !important;
        font-weight: 800 !important;
        color: white !important;
        text-align: center;
        margin-top: 10px !important;
    }
    
    .titulo-card {
        color: white !important;
        font-weight: 700 !important;
        text-align: center;
        margin-bottom: 15px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- CABEÇALHO ---
col_logo_a, col_logo_b, col_logo_c = st.columns([1, 2, 1])
with col_logo_b:
    st.image("logo_gm.png", use_container_width=True)

st.markdown("<p style='text-align: center; color: gray; margin-top: -10px;'>Sistema Especialista em Dimensionamento Térmico</p>", unsafe_allow_html=True)

# --- ENTRADA DE DADOS (AGORA EM CARDS AZUIS) ---

with st.container(border=True):
    st.markdown("<h4 class='titulo-card'>📏 Dimensões do Ambiente</h4>", unsafe_allow_html=True)
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
        if area > 0: st.write(f"**Área calculada: {area:.2f} m²**")

with st.container(border=True):
    st.markdown("<h4 class='titulo-card'>🔥 Fatores de Aquecimento</h4>", unsafe_allow_html=True)
    col_a, col_b = st.columns(2)
    with col_a:
        sol = st.selectbox("Incidência Solar:", ["Sombra/Manhã", "Sol o dia todo"])
        pessoas = st.number_input("Qtd. de Pessoas:", min_value=1, value=1)
    with col_b:
        eletronicos = st.number_input("Aparelhos Eletrônicos:", min_value=0, value=0)

# --- PROCESSAMENTO E EXIBIÇÃO ---

if st.button("CALCULAR E ANALISAR DISPOSIÇÃO"):
    if area <= 0:
        st.warning("⚠️ Por favor, informe as medidas do ambiente.")
    else:
        fator = 800 if sol == "Sol o dia todo" else 600
        carga_total = (area * fator) + ((pessoas - 1) * fator) + (eletronicos * fator)

        # CARD AZUL DE RESULTADO (Mesmo estilo dos outros)
        with st.container(border=True):
            st.markdown("<p style='text-align: center; font-size: 1.3rem;'>✅ Dimensionamento Concluído</p>", unsafe_allow_html=True)
            st.markdown("<p style='text-align: center; opacity: 0.8;'>Carga Térmica Necessária</p>", unsafe_allow_html=True)
            st.markdown(f"<h1 class='valor-btu'>{carga_total:,.0f} BTUs</h1>".replace(',', '.'), unsafe_allow_html=True)
        
        # SUGESTÕES DE EQUIPAMENTOS
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

        # ANÁLISE TÉCNICA (Custo-Benefício)
        with st.expander("📄 Ver Análise de Custo-Benefício"):
            st.write("""
            * **Redundância Técnica:** Dividir a carga em várias máquinas evita que o ambiente fique totalmente sem refrigeração em caso de falha de uma unidade.
            * **Manutenção Acessível:** Peças para máquinas de 12.000 BTUs são produzidas em larga escala, tornando a reposição 60% mais barata e rápida do que em sistemas centrais.
            * **Distribuição de Fluxo:** Em ambientes com geometria irregular, múltiplas unidades garantem que não existam 'pontos mortos' de calor.
            """)

# --- RODAPÉ ---
st.markdown("<br><hr><div style='text-align: center; color: gray; font-size: 0.8rem;'>Desenvolvido por <b>Glaudson Montenegro</b> | Projeto ADS - Portfólio Pessoal</div>", unsafe_allow_html=True)
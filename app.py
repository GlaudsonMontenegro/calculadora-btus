import streamlit as st

# 1. Configuração da Página e Estética Visual
st.set_page_config(page_title="GM - Engenharia de Software", page_icon="❄️", layout="centered")

# --- CSS CUSTOMIZADO (Identidade Visual GM) ---
st.markdown("""
    <style>
    /* Cor de fundo da página (Cinza Suave) */
    .stApp {
        background-color: #f0f2f6;
    }
    
    /* Estilização dos Containers brancos (Cards de entrada) */
    [data-testid="stVerticalBlockBorderWrapper"] {
        background-color: #blue !important; /* Aqui nasce o azul */
        padding: 30px !important;
        border-radius: 15px !important;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05) !important;
        border: none !important;
        margin-bottom: 20px !important;
    }

    /* Estilo do Botão Principal (Cinza para destaque) */
    .stButton>button {
        width: 100%;
        background-color: #95a5a6 !important; /* Cinza Profissional */
        color: white !important;
        border-radius: 10px;
        height: 3.5em;
        font-weight: bold;
        border: none !important;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #7f8c8d !important;
    }

    /* O NOVO CARD DE RESULTADO AZUL */
    .card-resultado {
        background-color: #004aad; /* Azul GM */
        padding: 40px;
        border-radius: 25px; /* Pontas bem arredondadas */
        color: white !important;
        box-shadow: 0 10px 20px rgba(0, 74, 173, 0.3);
        text-align: center;
        margin-top: 20px;
        margin-bottom: 30px;
    }
    .card-resultado h1, .card-resultado p {
        color: white !important;
        margin: 0;
    }
    .valor-btu {
        font-size: 3.8rem;
        font-weight: 800;
        margin-top: 10px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- CABEÇALHO ---
col_logo_a, col_logo_b, col_logo_c = st.columns([1, 2, 1])
with col_logo_b:
    # Certifique-se de que o arquivo logo_gm.png está na mesma pasta
    st.image("logo_gm.png", use_container_width=True)

st.markdown("<p style='text-align: center; color: gray; margin-top: -10px;'>Sistema Especialista em Dimensionamento Térmico</p>", unsafe_allow_html=True)

# --- FORMULÁRIO DE ENTRADA ---

# Bloco 1: Medição
with st.container(border=True):
    st.markdown("#### 📏 Dimensões do Ambiente")
    opcao_medida = st.radio(
        "Método de entrada:",
        ["Área total (m²)", "Comprimento x Largura"],
        horizontal=True
    )

    area = 0.0
    comprimento = 0.0
    largura = 0.0

    if opcao_medida == "Área total (m²)":
        area = st.number_input("Informe a área total (m²)", min_value=0.0, step=1.0)
    else:
        c1, c2 = st.columns(2)
        with c1:
            comprimento = st.number_input("Comprimento (m)", min_value=0.0, step=0.1)
        with c2:
            largura = st.number_input("Largura (m)", min_value=0.0, step=0.1)
        area = comprimento * largura
        if area > 0:
            st.info(f"Área calculada: **{area:.2f} m²**")

# Bloco 2: Carga de Calor
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
        st.warning("⚠️ Por favor, informe as medidas do ambiente.")
    else:
        # Cálculo Matemático
        fator = 800 if sol == "Sol o dia todo" else 600
        carga_total = (area * fator) + ((pessoas - 1) * fator) + (eletronicos * fator)

        # EXIBIÇÃO DO CARD AZUL (Seu novo layout)
        st.markdown(f"""
            <div class='card-resultado'>
                <p style='font-size: 1.2rem; opacity: 0.9;'>✅ Dimensionamento Concluído</p>
                <p style='font-size: 1rem; opacity: 0.8; margin-top: 10px;'>Carga Térmica Necessária</p>
                <h1 class='valor-btu'>{carga_total:,.0f} BTUs</h1>
            </div>
            """.replace(',', '.'), unsafe_allow_html=True)
        
        # Sugestões de Equipamentos
        st.markdown("### 🎯 Sugestões de Equipamentos")
        
        # Lógica de proporção para o ícone de aviso
        is_comprido = False
        if opcao_medida != "Área total (m²)" and largura > 0:
            if (comprimento / largura) > 1.8 or (comprimento / largura) < 0.5:
                is_comprido = True

        s1, s2 = st.columns(2)
        with s1:
            with st.container(border=True):
                st.markdown("**Opção Alta Potência**")
                st.image("pisoteto.jpg")
                qtd_36 = int(carga_total / 36000) or 1
                if carga_total % 36000 > 6000: qtd_36 += 1
                st.info(f"📍 {qtd_36}x 36.000 BTUs")
        
        with s2:
            with st.container(border=True):
                st.markdown("**Opção Distribuição**")
                st.image("hiwall.jpg")
                qtd_12 = int(carga_total / 12000) or 1
                if carga_total % 12000 > 2000: qtd_12 += 1
                st.success(f"📍 {qtd_12}x 12.000 BTUs")
                if is_comprido:
                    st.warning("💡 Recomendado para o formato deste ambiente.")

        with st.expander("📄 Ver Análise de Custo-Benefício"):
            st.write("- **Redundância:** O uso de múltiplas máquinas evita a parada total do sistema.")
            st.write("- **Manutenção:** Peças de 12k são mais baratas e de fácil reposição.")

# --- RODAPÉ ---
st.markdown("<br><hr>", unsafe_allow_html=True)
st.markdown(
    """
    <div style='text-align: center; color: gray; font-size: 0.8rem;'>
        Desenvolvido por <b>Glaudson Montenegro</b> | Projeto de Portfólio ADS
    </div>
    """, 
    unsafe_allow_html=True
)
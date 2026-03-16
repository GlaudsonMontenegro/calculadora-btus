import streamlit as st

# 1. Configuração da Página e Estética Visual
st.set_page_config(page_title="Natal Service - Consultoria Pro", page_icon="❄️", layout="centered")

# CSS Customizado para criar o efeito de "Cards" e profundidade
st.markdown("""
    <style>
    /* Cor de fundo da página */
    .stApp {
        background-color: #f0f2f6;
    }
    
    /* Estilização dos Containers para parecerem Cards */
    [data-testid="stVerticalBlockBorderWrapper"] {
        background-color: white;
        padding: 30px !important;
        border-radius: 15px !important;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08) !important;
        border: none !important;
        margin-bottom: 20px !important;
    }

    /* Título com gradiente */
    .titulo-pro {
        font-family: 'sans serif';
        color: #004aad;
        text-align: center;
        font-weight: 800;
        margin-bottom: 0px;
    }
    
    /* Botão Principal */
    .stButton>button {
        width: 100%;
        background-color: #004aad;
        color: white;
        border-radius: 10px;
        height: 3em;
        font-weight: bold;
        border: none;
    }
    </style>
    """, unsafe_allow_html=True)

# Cabeçalho
st.markdown("<h1 class='titulo-pro'>❄️ Natal Service</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Sistema Especialista em Dimensionamento Térmico</p>", unsafe_allow_html=True)

# --- INÍCIO DO FORMULÁRIO EM CONTAINERS ---

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
            st.info(f"Área total: **{area:.2f} m²**")

# Bloco 2: Carga de Calor
with st.container(border=True):
    st.markdown("#### 🔥 Fatores de Aquecimento")
    col_a, col_b = st.columns(2)
    with col_a:
        sol = st.selectbox("Incidência Solar:", ["Não (Sombra/Manhã)", "Sim (Sol o dia todo)"])
        pessoas = st.number_input("Qtd. de Pessoas:", min_value=1, value=1)
    with col_b:
        eletronicos = st.number_input("Aparelhos Eletrônicos:", min_value=0, value=0)
        st.caption("Considere computadores, TVs e motores.")

# --- PROCESSAMENTO ---

if st.button("CALCULAR E ANALISAR DISPOSIÇÃO"):
    if area <= 0:
        st.warning("⚠️ Por favor, informe as medidas do ambiente antes de calcular.")
    else:
        # Lógica de Cálculo
        fator = 800 if sol == "Sim (Sol o dia todo)" else 600
        carga_total = (area * fator) + ((pessoas - 1) * fator) + (eletronicos * fator)

        # Bloco de Resultado Principal
        with st.container(border=True):
            st.success("✅ **Resultado do Dimensionamento**")
            st.metric("Carga Térmica Total", f"{carga_total:,.0f} BTUs".replace(',', '.'))
            
            st.markdown("---")
            st.markdown("### 🎯 Sugestões Estratégicas")
            
            # Análise de Proporção
            is_comprido = False
            if opcao_medida != "Área total (m²)" and largura > 0:
                prop = comprimento / largura
                if prop > 1.8 or prop < 0.5: is_comprido = True

            # Colunas de Sugestão
            s1, s2 = st.columns(2)
            
            with s1:
                st.markdown("**Opção Alta Potência**")
                qtd_36 = int(carga_total / 36000) or 1
                if carga_total % 36000 > 6000: qtd_36 += 1
                st.info(f"📍 {qtd_36}x 36.000 BTUs\n(Piso Teto / Cassete)")
            
            with s2:
                st.markdown("**Opção Distribuição**")
                qtd_12 = int(carga_total / 12000) or 1
                if carga_total % 12000 > 2000: qtd_12 += 1
                st.success(f"📍 {qtd_12}x 12.000 BTUs\n(Hi-Wall)")
                if is_comprido:
                    st.warning("💡 *Indicado para este formato de ambiente.*")

            with st.expander("📄 Ver Análise de Custo-Benefício"):
                st.write("""
                - **Redundância Técnica:** Dividir a carga evita que o ambiente pare se uma máquina falhar.
                - **Manutenção:** Máquinas de 12k possuem peças 60% mais baratas.
                - **Estética:** Máquinas de 36k+ exigem menos furos, mas maior carga elétrica centralizada.
                """)

# --- RODAPÉ ---
st.markdown("<br>", unsafe_allow_html=True)
st.markdown(
    f"""
    <div style='text-align: center; color: #7f8c8d; font-size: 0.8rem;'>
        <hr>
        Desenvolvido por <b>Glaudson Montenegro</b><br>
        Projeto de Portfólio - Análise e Desenvolvimento de Sistemas
    </div>
    """, 
    unsafe_allow_html=True
)
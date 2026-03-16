import streamlit as st

# 1. Configuração da Página e Estética
st.set_page_config(page_title="GM - Tecnologia", page_icon="❄️", layout="centered")

# CSS para o efeito de Cards e Cores
st.markdown("""
    <style>
    .stApp { background-color: #f0f2f6; }
    [data-testid="stVerticalBlockBorderWrapper"] {
        background-color: white;
        padding: 30px !important;
        border-radius: 15px !important;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08) !important;
        border: none !important;
        margin-bottom: 20px !important;
    }
    .titulo-pro { color: #004aad; text-align: center; font-weight: 800; }
    </style>
    """, unsafe_allow_html=True)

# Cabeçalho com sua nova Logo
col_logo_a, col_logo_b, col_logo_c = st.columns([1, 2, 1])
with col_logo_b:
    st.image("logo_gm.png", use_container_width=True)

st.markdown("<p style='text-align: center; color: gray;'>Sistema de Cálculo Térmico para Portfólio ADS</p>", unsafe_allow_html=True)

# --- ENTRADA DE DADOS ---

with st.container(border=True):
    st.markdown("#### 📏 Dimensões do Ambiente")
    opcao_medida = st.radio("Método de entrada:", ["Área total (m²)", "Comprimento x Largura"], horizontal=True)

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
        if area > 0: st.info(f"Área total: **{area:.2f} m²**")

with st.container(border=True):
    st.markdown("#### 🔥 Fatores de Aquecimento")
    col_a, col_b = st.columns(2)
    with col_a:
        sol = st.selectbox("Incidência Solar:", ["Sombra/Manhã", "Sol o dia todo"])
        pessoas = st.number_input("Qtd. de Pessoas:", min_value=1, value=1)
    with col_b:
        eletronicos = st.number_input("Aparelhos Eletrônicos:", min_value=0, value=0)

# --- PROCESSAMENTO E RESULTADO ---

if st.button("CALCULAR E ANALISAR DISPOSIÇÃO"):
    if area <= 0:
        st.warning("⚠️ Informe as medidas do ambiente.")
    else:
        fator = 800 if sol == "Sol o dia todo" else 600
        carga_total = (area * fator) + ((pessoas - 1) * fator) + (eletronicos * fator)

        with st.container(border=True):
            st.success("✅ Dimensionamento Concluído")
            st.metric("Carga Térmica Total", f"{carga_total:,.0f} BTUs".replace(',', '.'))
            
            st.markdown("---")
            st.markdown("### 🎯 Sugestões de Equipamentos")
            
            # Lógica de proporção
            is_comprido = False
            if opcao_medida != "Área total (m²)" and largura > 0:
                if (comprimento / largura) > 1.8 or (comprimento / largura) < 0.5: is_comprido = True

            s1, s2 = st.columns(2)
            with s1:
                st.markdown("**Opção Alta Potência**")
                st.image("pisoteto.jpg", caption="Piso Teto / Cassete")
                qtd_36 = int(carga_total / 36000) or 1
                if carga_total % 36000 > 6000: qtd_36 += 1
                st.info(f"📍 {qtd_36}x 36.000 BTUs")
            
            with s2:
                st.markdown("**Opção Distribuição**")
                st.image("hiwall.jpg", caption="Modelo Hi-Wall")
                qtd_12 = int(carga_total / 12000) or 1
                if carga_total % 12000 > 2000: qtd_12 += 1
                st.success(f"📍 {qtd_12}x 12.000 BTUs")
                if is_comprido: st.warning("💡 Recomendado para ambientes estreitos.")

            with st.expander("📄 Ver Análise de Custo-Benefício"):
                st.write("* **Redundância:** Várias máquinas protegem o ambiente se uma falhar.")
                st.write("* **Manutenção:** Peças de 12k são mais baratas e fáceis de encontrar.")

# --- RODAPÉ ---
st.markdown("<br><hr><div style='text-align: center; color: gray; font-size: 0.8rem;'>Desenvolvido por <b>Glaudson Montenegro</b> | Projeto de Portfólio ADS</div>", unsafe_allow_html=True)
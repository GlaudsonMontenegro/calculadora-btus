import streamlit as st

# 1. Configuração da Página e Estilo
st.set_page_config(page_title="Natal Service - Calculadora Pro", page_icon="❄️")

st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stButton>button { width: 100%; background-color: #004aad; color: white; border-radius: 8px; }
    </style>
    """, unsafe_allow_html=True)

st.title("❄️ Calculadora de Carga Térmica")
st.subheader("Consultoria Técnica para Dimensionamento")
st.write("---")

# 2. Entrada de Dados: Medição do Ambiente
opcao_medida = st.radio(
    "Como deseja informar o tamanho do ambiente?",
    ["Área total (m²)", "Medir por Comprimento x Largura"]
)

area = 0.0
comprimento = 0.0
largura = 0.0

if opcao_medida == "Área total (m²)":
    area = st.number_input("Área total do ambiente (m²)", min_value=0.0, step=1.0)
else:
    col1, col2 = st.columns(2)
    with col1:
        comprimento = st.number_input("Comprimento (m)", min_value=0.0, step=0.1)
    with col2:
        largura = st.number_input("Largura (m)", min_value=0.0, step=0.1)
    area = comprimento * largura
    if area > 0:
        st.info(f"Área calculada: {area:.2f} m²")

# 3. Entrada de Dados: Variáveis de Calor
st.write("### Fontes de Calor")
col3, col4 = st.columns(2)
with col3:
    sol = st.radio("Incidência de Sol:", ["Sim (Tarde/Dia todo)", "Não (Manhã/Sombra)"])
with col4:
    pessoas = st.number_input("Total de Pessoas (Fixo + Rotativo)", min_value=1, value=1)
    eletronicos = st.number_input("Aparelhos Eletrônicos", min_value=0, value=0)

# 4. Processamento e Exibição do Resultado
if st.button("Calcular e Analisar Disposição", type="primary"):
    if area <= 0:
        st.error("Por favor, informe as medidas do ambiente.")
    else:
        # Lógica Matemática
        fator_btu = 800 if sol == "Sim (Tarde/Dia todo)" else 600
        
        btu_area = area * fator_btu
        btu_pessoas = (pessoas - 1) * fator_btu if pessoas > 0 else 0
        btu_eletronicos = eletronicos * fator_btu
        
        carga_total = btu_area + btu_pessoas + btu_eletronicos

        # Exibição da Métrica Principal
        st.success("Dimensionamento concluído!")
        st.metric("Carga Térmica Necessária", f"{carga_total:,.0f} BTUs".replace(',', '.'))

        # --- LÓGICA DE CONSULTORIA TÉCNICA (O Diferencial do seu Portfólio) ---
        st.markdown("---")
        st.markdown("### 🎯 Sugestões de Instalação")

        # Analisamos a geometria para o técnico
        is_comprido = False
        if opcao_medida != "Área total (m²)" and largura > 0:
            proporcao = comprimento / largura
            if proporcao > 1.8 or proporcao < 0.5:
                is_comprido = True

        col_opt1, col_opt2 = st.columns(2)

        with col_opt1:
            st.info("🏢 **Opção Alta Potência**")
            # Sugestão de máquinas de 36k
            qtd_36k = int(carga_total / 36000)
            if carga_total % 36000 > 5000: qtd_36k += 1
            if qtd_36k == 0: qtd_36k = 1
            
            st.write(f"Sugerido: **{qtd_36k:02d} máquina(s) de 36.000 BTUs**")
            st.caption("Indicado: Piso Teto ou Cassete para ambientes amplos.")

        with col_opt2:
            st.success("🌬️ **Distribuição Otimizada**")
            # Sugestão de máquinas de 12k
            qtd_12k = int(carga_total / 12000)
            if carga_total % 12000 > 2000: qtd_12k += 1
            
            st.write(f"Sugerido: **{qtd_12k:02d} máquinas de 12.000 BTUs**")
            
            if is_comprido:
                st.warning("⚠️ **Recomendado:** Local estreito/comprido. Use esta opção para o frio chegar ao fundo.")

        # Rodapé Técnico
        with st.expander("📂 Por que oferecemos essas opções? (Análise de Custo-Benefício)"):
            st.write("""
            * **Redundância:** Com várias máquinas de 12k, se uma quebrar, o ambiente não para.
            * **Manutenção:** Peças de 12k são 60% mais baratas que as de 36k/60k.
            * **Conforto:** Evita jatos de ar muito fortes em cima de uma única pessoa.
            """)

# 5. Assinatura do Desenvolvedor (Portfólio)
st.write("---")
st.markdown(
    """
    <div style='text-align: center;'>
        <p style='font-size: 0.8rem; color: gray;'>
            Desenvolvido por 
            <a href='https://github.com/GlaudsonMontenegro' target='_blank' style='text-decoration: none; color: #004aad; font-weight: bold;'>
                Glaudson Montenegro
            </a> | Projeto ADS - Soluções Reais
        </p>
    </div>
    """, 
    unsafe_allow_html=True
)
import streamlit as st

# 1. Configuração da Página
st.set_page_config(page_title="Calculadora BTU ", page_icon="❄️")

st.title("❄️ Calculadora de Btu's")
st.subheader("Dimensionamento de Carga Térmica.")
st.write("Preencha os dados abaixo para calcular o equipamento ideal.")
st.write("---")

# 2. Interface de Medição (Aplica Heurística de Flexibilidade)
opcao_medida = st.radio(
    "Como deseja informar o tamanho do ambiente?",
    ["Área total já calculada (m²)", "Medir por Comprimento x Largura"]
)

area = 0.0
if opcao_medida == "Área total já calculada (m²)":
    area = st.number_input("Área total do ambiente (m²)", min_value=0.0, value=0.0, step=1.0)
else:
    col1, col2 = st.columns(2) # Divide a tela em duas colunas
    with col1:
        comprimento = st.number_input("Comprimento (m)", min_value=0.0, value=0.0, step=0.5)
    with col2:
        largura = st.number_input("Largura (m)", min_value=0.0, value=0.0, step=0.5)
    
    area = comprimento * largura
    if area > 0:
        st.info(f"Área calculada automaticamente: {area:.2f} m²")

# 3. Interface das Variáveis de Calor
col3, col4 = st.columns(2)
with col3:
    sol = st.radio("O ambiente recebe sol da tarde ou o dia todo?", ["Sim", "Não"])
with col4:
    pessoas_fixas = st.number_input("Funcionários fixos", min_value=0, value=0, step=1)
    pessoas_rotativas = st.number_input("Clientes rotativos (Máx)", min_value=0, value=0, step=1)
    eletronicos = st.number_input("Equipamentos eletrônicos", min_value=0, value=0, step=1)

# 4. Botão de Ação e Processamento Matemático
if st.button("Calcular Carga Térmica", type="primary"):
    if area <= 0:
        st.error("Por favor, informe uma área ou medidas válidas maiores que zero.")
    else:
        # Lógica de cálculo que você já criou
        fator_btu = 800 if sol == "Sim" else 600
        total_pessoas = pessoas_fixas + pessoas_rotativas
        
        btu_area = area * fator_btu
        btu_pessoas = (total_pessoas - 1) * fator_btu if total_pessoas > 0 else 0
        btu_eletronicos = eletronicos * fator_btu
        
        carga_total = btu_area + btu_pessoas + btu_eletronicos
        
        # Lógica de distribuição de equipamentos comerciais
        capacidades_comerciais = [9000, 12000, 18000, 24000, 30000, 36000, 48000, 60000]
        sugestao = ""
        
        if carga_total <= 60000:
            for cap in capacidades_comerciais:
                if cap >= carga_total:
                    sugestao = f"01 equipamento de {cap:,.0f} BTUs".replace(',', '.')
                    break
        else:
            qtd_maquinas = int(carga_total // 60000)
            if carga_total % 60000 != 0:
                qtd_maquinas += 1
            carga_por_maquina = carga_total / qtd_maquinas
            
            for cap in capacidades_comerciais:
                if cap >= carga_por_maquina:
                    sugestao = f"{qtd_maquinas:02d} equipamentos de {cap:,.0f} BTUs (Distribuição otimizada)".replace(',', '.')
                    break

        # 5. Exibição do Resultado Visual
        st.success("Dimensionamento concluído!")
        st.markdown("### 📊 Relatório Final")
        st.write(f"**Carga Térmica Exata:** {carga_total:.0f} BTUs")
        st.markdown(f"#### 🎯 Sugestão de Instalação: **{sugestao}**")

st.write("---")
st.markdown(
    """
    <div style='text-align: center;'>
        <p style='font-size: 0.8rem; color: gray;'>
            Desenvolvido com ❤️ por 
            <a href='https://github.com/GlaudsonMontenegro' target='_blank' style='text-decoration: none; color: #004aad; font-weight: bold;'>
                Glaudson Montenegro
            </a>
        </p>
    </div>
    """, 
    unsafe_allow_html=True
)
print("=== SISTEMA : Cálculo de Carga Térmica Comercial ===")

# 1. Função de trava de segurança para números
def obter_numero(pergunta, tipo=int):
    while True:
        try:
            return tipo(input(pergunta))
        except ValueError:
            print("  -> ERRO: Por favor, digite apenas números válidos.\n")

# 2. Menu para escolha da forma de medição
while True:
    print("\nComo deseja informar o tamanho do ambiente?")
    print("[1] Área total já calculada (m²)")
    print("[2] Medir por Comprimento x Largura")
    opcao_medida = input("Escolha a opção (1 ou 2): ").strip()
    
    if opcao_medida in ['1', '2']:
        break
    print("  -> ERRO: Opção inválida.\n")

if opcao_medida == '1':
    area = obter_numero("\nQual a área total do ambiente (m²)? ", tipo=float)
else:
    comprimento = obter_numero("\nQual o comprimento do ambiente (em metros)? ", tipo=float)
    largura = obter_numero("Qual a largura do ambiente (em metros)? ", tipo=float)
    area = comprimento * largura
    print(f"  -> Área calculada: {area:.2f} m²\n")

# 3. Coletando os demais dados
while True:
    sol = input("O ambiente recebe sol da tarde ou o dia todo? (S/N): ").strip().upper()
    if sol in ["S", "N"]:
        break
    print("  -> ERRO: Digite apenas S ou N.\n")

pessoas_fixas = obter_numero("Quantos funcionários fixos no local? ")
pessoas_rotativas = obter_numero("Qual a capacidade máxima de clientes rotativos? ")
eletronicos = obter_numero("Quantos equipamentos eletrônicos geram calor? ")

# 4. Processando a matemática base
fator_btu = 800 if sol == "S" else 600
total_pessoas = pessoas_fixas + pessoas_rotativas

btu_area = area * fator_btu
btu_pessoas = (total_pessoas - 1) * fator_btu if total_pessoas > 0 else 0
btu_eletronicos = eletronicos * fator_btu

carga_total = btu_area + btu_pessoas + btu_eletronicos

# 5. NOVO: Lógica de Recomendação de Equipamentos Comerciais
# Lista das capacidades que existem no mercado
capacidades_comerciais = [9000, 12000, 18000, 24000, 30000, 36000, 48000, 60000]
sugestao = ""

if carga_total <= 60000:
    # Procura a máquina ideal para cargas normais
    for cap in capacidades_comerciais:
        if cap >= carga_total:
            sugestao = f"01 equipamento de {cap:,.0f} BTUs".replace(',', '.')
            break
else:
    # Descobre a quantidade mínima de máquinas necessárias dividindo pela maior capacidade (60k)
    qtd_maquinas = int(carga_total // 60000)
    
    # Se sobrar alguma carga de resto, adiciona mais uma máquina à conta
    if carga_total % 60000 != 0:
        qtd_maquinas += 1
        
    # Descobre qual deve ser a capacidade de cada máquina para ficar equilibrado
    carga_por_maquina = carga_total / qtd_maquinas
    
    for cap in capacidades_comerciais:
        if cap >= carga_por_maquina:
            sugestao = f"{qtd_maquinas:02d} equipamentos de {cap:,.0f} BTUs (Distribuição otimizada)".replace(',', '.')
            break
# 6. Exibindo o Relatório Final
print("\n" + "="*50)
print("             RELATÓRIO DE DIMENSIONAMENTO")
print("="*50)
print(f"Área do ambiente......: {area:.2f} m²")
print(f"Lotação máxima........: {total_pessoas} pessoas")
print(f"Equipamentos geradores: {eletronicos} itens")
print("-" * 50)
print(f">> CARGA TÉRMICA EXATA: {carga_total:.0f} BTUs")
print(f">> SUGESTÃO COMERCIAL.: {sugestao}")
print("="*50)

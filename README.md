#  Calculadora de Carga Térmica Comercial

> Uma ferramenta de linha de comando (CLI) desenvolvida em Python para dimensionamento rápido e preciso de equipamentos de ar-condicionado e refrigeração.

##  Sobre o Projeto

Este sistema foi construído para resolver um problema real de campo na rotina de serviços de refrigeração industrial e comercial. Ele automatiza o cálculo de BTUs necessários para climatizar um ambiente, levando em consideração variáveis críticas como exposição solar, lotação máxima e quantidade de equipamentos geradores de calor.

Além do cálculo matemático preciso, o algoritmo possui uma inteligência comercial que analisa a carga total e sugere automaticamente a melhor distribuição de equipamentos (ex: divisão de carga em múltiplas máquinas para ambientes acima de 60.000 BTUs).

##  Funcionalidades

- **Cálculo Flexível:** Opção de inserir a área total pronta ou calcular inserindo largura e comprimento.
- **Variáveis de Calor:** Contabiliza o fator de exposição ao sol (fator 600 ou 800).
- **Lotação e Equipamentos:** Adiciona carga térmica baseada em pessoas fixas, rotativas e eletrônicos no local.
- **Sugestão Comercial:** Algoritmo que varre uma lista de capacidades comerciais (9k a 60k) e indica a combinação ideal de compra/instalação.
- **Tratamento de Erros:** Prevenção contra falhas de digitação do usuário (letras no lugar de números).

##  Tecnologias Utilizadas

- **Python 3.x:** Linguagem principal para a lógica matemática e estruturação do algoritmo.

##  Como executar o projeto

Para rodar esta calculadora na sua máquina, siga os passos abaixo:

1. Certifique-se de ter o [Python](https://www.python.org/downloads/) instalado.
2. Clone este repositório:
   ```bash
   git clone [https://github.com/GlaudsonMontenegro/calculadora-btus.git](https://github.com/GlaudsonMontenegro/calculadora-btus.git)

3. Navegue até a pasta do projeto:

Bash

cd calculadora-btus

Execute o arquivo principal:

Bash

python main.py

Autor
Desenvolvido por Glaudson Montenegro Estudante de Análise e Desenvolvimento de Sistemas.

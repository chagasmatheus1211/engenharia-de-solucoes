
# 🏥 Sistema de Triagem de Glicemia (Diabetes Service)

[![Python](https://img.shields.io/badge/Python-3.10-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Projeto-Acadêmico-orange?style=for-the-badge)](https://github.com/chagasmatheus1211/portfolio-matheus-chagas-mauriz-coque)

## 📝 Descrição do Projeto

Este projeto consiste em um sistema desenvolvido em Python para simular a **triagem de pacientes com níveis elevados de glicose no sangue** em unidades de saúde.

O objetivo é demonstrar como a lógica de programação pode auxiliar na organização do fluxo de atendimento, identificando situações que exigem atenção prioritária de acordo com um limite de glicemia predefinido.

O sistema coleta os dados do paciente e analisa o valor informado para determinar qual fluxo de atendimento será indicado pelo algoritmo.

> ⚠️ **Aviso:** este projeto possui finalidade acadêmica e educacional. Seus resultados não substituem avaliação médica, protocolos clínicos oficiais ou atendimento profissional.

## 🚀 Tecnologias Utilizadas

- 🐍 **Linguagem:** Python
- 🧠 **Conceitos:** lógica de programação, estruturas condicionais `if/else` e entrada e saída de dados.
- 📊 **Documentação:** fluxogramas de processos e representação lógica da tomada de decisão.

## 📊 Regras de Negócio e Fluxo

O sistema segue um fluxo de decisão baseado nos dados informados pelo usuário.

### 📋 1. Coleta de Dados

O programa solicita as seguintes informações:

- 👤 Nome do paciente.
- 🎂 Idade do paciente.
- 🩸 Nível de glicose no sangue, informado em mg/dL.

### 🚨 2. Identificação de Valor Elevado

Quando o valor informado é **superior a 300 mg/dL**, o algoritmo exibe o alerta “Glicose muito alta!” e simula o encaminhamento prioritário para atendimento.

### 🏥 3. Fluxo Convencional

Quando o valor informado não ultrapassa o limite definido pelo programa, o sistema indica que o paciente deve aguardar o atendimento conforme o fluxo convencional da unidade.

**Importante:** o limite de 300 mg/dL é uma regra implementada para fins didáticos, não um critério suficiente para determinar sozinho a gravidade clínica ou a prioridade real de atendimento.

## 🔧 Como Executar

### 📋 Pré-requisitos

- Python instalado na máquina.
- Terminal ou editor de código compatível com Python.

### ▶️ Passo a Passo

**1. Clone o repositório**

```bash
git clone https://github.com/SEU-USUARIO/triagem-glicemia.git
```

**2. Acesse a pasta do projeto**

```bash
cd triagem-glicemia
```

**3. Execute o programa**

```bash
python triagem.py
```

**4. Informe os dados solicitados**

Preencha as informações do paciente no console e observe a resposta gerada pelo sistema de triagem.

## 📂 Estrutura do Projeto

```text
triagem-glicemia/
├── README.md
└── triagem.py
```

- 📘 `README.md`: documentação e instruções para execução.
- 🐍 `triagem.py`: script Python responsável pela coleta de dados e pela lógica de triagem.

## 💻 Acesse o Projeto

🐍 **[Visualizar código-fonte (main.py)](main.py)**

📁 **[Acessar portfólio no GitHub](https://github.com/chagasmatheus1211/portfolio-matheus-chagas-mauriz-coque/tree/main)**

## 👤 Autor

**Matheus Chagas Mauriz Coque**

🎓 Estudante de Engenharia de Software

- 💼 [LinkedIn](https://www.linkedin.com/in/matheus-chagas-coque-b190ba39b/)
- 🐙 [GitHub](https://github.com/chagasmatheus1211)
- 📧 [E-mail](mailto:chagasmatheus1211@gmail.com)

---

⭐ *Projeto acadêmico com foco em lógica de programação, estruturas condicionais, entrada e saída de dados e simulação de processos de triagem.*

⬅️ **[Voltar ao portfólio principal](https://github.com/chagasmatheus1211/portfolio-matheus-chagas-mauriz-coque/tree/main)**

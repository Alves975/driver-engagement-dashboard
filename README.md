# 📊 Driver Engagement Dashboard – 99

Dashboard interativo para análise do **engajamento de motoristas** da 99, desenvolvido em Streamlit.

## 📄 Demonstração do Dashboard

Você pode visualizar o PDF do dashboard clicando no link abaixo:

[Visualizar Dashboard (PDF)](docs/dashboard_demo.pdf)


## 🎯 Objetivo
Analisar o nível de engajamento dos motoristas com base na quantidade de corridas semanais,  
identificando padrões por nível de engajamento, cidade e atividade.  

Permite identificar **Top 10 motoristas mais engajados**, **piores 10 motoristas** e os **300 principais motoristas**, com destaque visual para os scores.

## ⚠️ Aviso de Uso

Este projeto é **apenas para fins educacionais** e de estudo.  
Os dados utilizados são **simulados ou fictícios** e não representam informações reais de motoristas da 99.  
Não deve ser usado para fins comerciais ou divulgação externa.


## 🧠 Métricas analisadas
- Corridas semanais  
- Horas ativas  
- Nível de engajamento (Alto, Médio, Baixo)  
- Score de engajamento  
- Média de corridas por cidade  

## 📈 Visualizações e Tabelas
- **Distribuição de motoristas por nível de engajamento** – gráfico de barras colorido  
- **Corridas semanais por engajamento** – gráfico de pizza  
- **Média de corridas semanais por nível de engajamento** – gráfico de barras  
- **Top 10 Motoristas** por score (maior score, ordenado por `driver_id`)  
- **Top 10 Motoristas Piores** por score (menor score, ordenado por `driver_id`)  
- **Top 300 Motoristas** por score (maior score, ordenado por `driver_id`)  

✅ **Destaque visual de score:**  
- Verde para o maior score dentro da tabela  
- Vermelho para o menor score dentro da tabela  

## 🛠️ Tecnologias
- Python 3.11+  
- Pandas – manipulação de dados  
- Matplotlib – gráficos  
- Streamlit – dashboard interativo  

## 🚀 Como executar
1. Clone o repositório:
2. Instale as dependências: 
- pip install -r requirements.txt
3. Execute o processamento de dados (opcional, se houver):
- python driver_engagement_analysis.py
4. Inicie o dashboard interativo:
- streamlit run app.py



```bash
git clone https://github.com/seu-usuario/driver-engagement-dashboard.git
cd driver-engagement-dashboard

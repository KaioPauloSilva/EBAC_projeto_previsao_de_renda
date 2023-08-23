import streamlit as st

st.set_page_config(
    page_title='Insights - Previsão de renda',
    page_icon='💲',
)

st.title('INSIGHTS')

st.header(' Insights com a análise de Univariada e Bivariada')

st.write('''
- Na analise renda x sexo percebemos que o sexo Masculino (M) tem uma media de renda acima do que o sexo Feminino (F).

- Na analise de renda x q_idade notamos que há uma renda menor em pessoas mais novas, entre 22 a 34 anos.

- Em renda x educacao percebesse que as pessoas com superior completo possuem uma renda maior que a maioria.

- Em renda x posse_de_veiculo as pessoas que possuem veiculo possuem uma renda maior que as pessoas sem veiculos

- Em renda x tipo_renda as pessoas que são servidores publicos possuem renda maior que as outras variaveis

- Na analise renda x q_tempo_emprego pessoas com um tempo de emprego maior possuem uma renda mais alta.''')



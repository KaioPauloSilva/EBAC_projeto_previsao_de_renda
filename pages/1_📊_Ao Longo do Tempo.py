import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(
     page_title='EBAC - Previsão de Renda',
     page_icon='',
     layout='wide',
     initial_sidebar_state='auto'
)

st.markdown('### Gráficos ao longo do tempo')
st.markdown('Selecione os Graficos ao lado ')
st.markdown('### ↙')
st.markdown('---')

sns.set(context='talk', style='ticks')

# carregando o dataframe
renda = pd.read_csv('./input/previsao_de_renda.csv')
renda = renda.drop(['Unnamed: 0'], axis=1)

#opcoes checkbox
with st.sidebar:
     st.header('Selecione os graficos:')
     opcao_pi = st.checkbox('Posse de imovel') #posse_de_imovel
     opcao_pv = st.checkbox('Posse de veiculo') #posse_de_veiculo
     opcao_qtd_fi = st.checkbox('Quantidade de filhos') #qtd_filhos
     opcao_tr = st.checkbox('Tipo renda') # tipo_renda
     opcao_edu = st.checkbox('Educação') # educacao
     opcao_ec = st.checkbox('Estado Civil') #estado_civil
     opcao_tipo_r = st.checkbox('Tipo de residência') #tipo_residencia

if opcao_pi:
     plt.close('all')
     plt.figure(figsize=[20, 10])
     st.write('Grafico posse_de_imovel x renda')
     sns.lineplot(x='data_ref', y='renda',hue='posse_de_imovel', data=renda)
     plt.tick_params(axis='x', rotation=45)
     sns.despine()
     st.pyplot(plt)

if opcao_pv:
     plt.close('all')
     plt.figure(figsize=[20, 10])
     st.write('Grafico posse_de_veiculo x renda')
     sns.lineplot(x='data_ref', y='renda', hue='posse_de_veiculo', data=renda)
     plt.tick_params(axis='x', rotation=45)
     sns.despine()
     st.pyplot(plt)

if opcao_qtd_fi:
     plt.close('all')
     plt.figure(figsize=[20,10])
     st.write('Grafico qtd_filhos x renda')
     sns.lineplot(x='data_ref', y='renda', hue='qtd_filhos', data=renda)
     plt.tick_params(axis='x', rotation=45)
     sns.despine()
     st.pyplot(plt)

if opcao_tr:
     plt.close('all')
     plt.figure(figsize=[20, 10])
     st.write('Grafico tipo_renda x renda')
     sns.lineplot(x='data_ref', y='renda', hue='tipo_renda', data=renda)
     plt.tick_params(axis='x', rotation=45)
     sns.despine()
     st.pyplot(plt)

if opcao_edu:
     plt.close('all')
     plt.figure(figsize=[20, 10])
     st.write('Grafico educacao x renda')
     sns.lineplot(x='data_ref', y='renda', hue='educacao', data=renda)
     plt.tick_params(axis='x', rotation=45)
     sns.despine()
     st.pyplot(plt)

if opcao_ec:
     plt.close('all')
     plt.figure(figsize=[20, 10])
     st.write('Grafico estado_civil x renda')
     sns.lineplot(x='data_ref', y='renda', hue='estado_civil', data=renda)
     plt.tick_params(axis='x', rotation=45)
     sns.despine()
     st.pyplot(plt)

if opcao_tipo_r:
     plt.close('all')
     plt.figure(figsize=[20, 10])
     st.write('Grafico tipo_residencia x renda')
     sns.lineplot(x='data_ref', y='renda', hue='tipo_residencia', data=renda)
     plt.tick_params(axis='x', rotation=45)
     sns.despine()
     st.pyplot(plt)

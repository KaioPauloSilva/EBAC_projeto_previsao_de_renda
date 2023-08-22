import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


st.set_page_config(
    page_title='Bivariada - Previsão de renda',
    page_icon='💲',
)


renda = pd.read_csv('./input/previsao_de_renda.csv')
renda['q_idade'] = pd.qcut(renda['idade'], 4)
renda['q_tempo_emprego'] =  pd.qcut(renda['tempo_emprego'], 3)


st.markdown('# Gráficos Bivariada')


opcao = st.selectbox('# Escolha a variável:',
                     ('Renda x Sexo', 'Renda x Idade',
                      'Renda x Educação', 'Renda x Posse de Imóvel',
                      'Renda x Posse de Veiculo', 'Renda x Tipo renda',
                      'Renda x Tempo emprego', 'Renda x Quantidade de filhos',
                      'Renda x Estado civil')
                     )


if opcao == 'Renda x Sexo':
    st.markdown('### Bivariada renda x sexo')
    st.markdown('- Esta analise com visualização se torna muito dificil pois há outlier em [`renda`].')
    st.markdown('- Nesta analise foi filtrado o grafico para renda abaixo de 20,000 pois ha um outlier acima.')
    fig, axs = plt.subplots(2, figsize=[10,10])
    sns.histplot(renda, x = 'renda', hue='sexo', multiple='stack', kde='True', ax = axs[0])
    sns.pointplot(renda, y = 'renda', x = 'sexo', ax = axs[1])
    axs[0].set_xlim(0, 20000)
    with st.spinner('Aguarde...'):
        st.pyplot(fig)


elif opcao == 'Renda x Idade':
    st.markdown('### Bivariada renda x idade')
    st.markdown('- As idades estão dividas por Categorias.')
    fig, axs = plt.subplots(2, figsize=[10,10])
    sns.histplot(renda, x='renda', hue='q_idade', multiple='stack', ax = axs[0])
    sns.pointplot(renda, y = 'renda', x = 'q_idade', ax = axs[1])
    axs[0].set_xlim(0, 20000)
    with st.spinner('Aguarde...'):
        st.pyplot(fig)


elif opcao == 'Renda x Educação':
    st.markdown('### Bivariada renda x educacao')
    fig, axs = plt.subplots(2, figsize=[15,10])
    sns.histplot(renda,x = 'renda',hue = 'educacao',multiple = 'stack',ax = axs[0])
    sns.pointplot(renda,y = 'renda',x = 'educacao',ax = axs[1])
    axs[0].set_xlim(0,20000)
    with st.spinner('Aguarde...'):
        st.pyplot(fig)

        
elif opcao == 'Renda x Posse de Imóvel':
    st.markdown('### Bivariada renda x posse_de_imovel')
    fig, axs = plt.subplots(2, figsize=[10, 10])
    sns.histplot(renda, x = 'renda', hue = 'posse_de_imovel',multiple = 'stack' ,ax = axs[0])
    sns.pointplot(renda, y = 'renda', x='posse_de_imovel', ax = axs[1])
    axs[0].set_xlim(0, 20000)
    with st.spinner('Aguarde...'):
        st.pyplot(fig)


elif opcao == 'Renda x Posse de Veiculo':
    st.markdown('### Bivariada renda x posse_de_veiculo')
    fig, axs = plt.subplots(2, figsize=[10, 10])
    sns.histplot(renda, x = 'renda', hue = 'posse_de_veiculo',multiple = 'stack' ,ax = axs[0])
    sns.pointplot(renda, y = 'renda', x='posse_de_veiculo', ax = axs[1])
    axs[0].set_xlim(0, 20000)
    with st.spinner('Aguarde...'):
        st.pyplot(fig)


elif opcao == 'Renda x Tipo renda':
    st.markdown('### Bivariada renda x tipo_renda')
    fig, axs = plt.subplots(2, figsize=[10,10])
    sns.histplot(renda, x = 'renda', hue = 'tipo_renda', multiple = 'stack', ax = axs[0])
    sns.pointplot(renda, y = 'renda', x = 'tipo_renda', ax = axs[1])
    axs[0].set_xlim(0,20000)
    with st.spinner('Aguarde...'):
        st.pyplot(fig)


elif opcao == 'Renda x Tempo emprego':
    st.markdown('### Bivariada renda x tempo_emprego')
    fig, axs = plt.subplots(2, figsize=[10,10])
    sns.histplot(renda, x='renda', hue='q_tempo_emprego', multiple='stack', ax = axs[0])
    sns.pointplot(renda, y = 'renda', x = 'q_tempo_emprego', ax = axs[1])
    axs[0].set_xlim(0, 20000)
    with st.spinner('Aguarde...'):
        st.pyplot(fig)


elif opcao == 'Renda x Quantidade de filhos':
    st.markdown('### Bivariada renda x qtd_filhos')
    fig, axs = plt.subplots(2, figsize=[10,10])
    sns.histplot(renda, x = 'renda', hue = 'qtd_filhos', multiple = 'stack', ax = axs[0])
    sns.pointplot(renda, y = 'renda', x = 'qtd_filhos', ax = axs[1])
    axs[0].set_xlim(0,20000)
    with st.spinner('Aguarde...'):
        st.pyplot(fig)


elif opcao == 'Renda x Estado civil':
    st.markdown('### Bivariada renda x estado_civil')
    fig, axs = plt.subplots(2, figsize=[10,10])
    sns.histplot(renda, x = 'renda', hue = 'estado_civil', multiple = 'stack', ax = axs[0])
    sns.pointplot(renda, y = 'renda', x = 'estado_civil', ax = axs[1])
    axs[0].set_xlim(0,20000)
    with st.spinner('Aguarde...'):
        st.pyplot(fig)
import streamlit as st
import pandas as pd

st.set_page_config(
     page_title="Previsão de renda",
     page_icon='💲',
     layout="wide",
)

renda = pd.read_csv('./input/previsao_de_renda.csv')
renda = renda.drop(['Unnamed: 0'], axis=1)

st.write('# Análise exploratória da previsão de renda')

st.write(''' Este é um projeto proposto pela EBAC, no curso de Cientista de Dados.

O objetivo deste projeto é com base nos dados fornecidos, analisar qual fator influenciara na renda da população e possibilitar predizer, qual será a **previsão de renda**.

Definição do Problema: Identificar os desafios específicos que a previsão de renda visa resolver. Isso pode envolver a identificação de padrões, variações de renda e fatores que influenciam as mudanças de renda ao longo do tempo.

Objetivos da modelagem: O objetivo está bem definido: desenvolver o melhor modelo preditivo de modo a auxiliar o mutuário a tomar suas próprias decisões referentes a renda.''')

st.write('---')

st.markdown('''### Dicionário de dados
Os dados estão dispostos em uma tabela com uma linha para cada cliente, e uma coluna para cada variável armazenando as características desses clientes.

| Variável                | Descrição                                           | Tipo         |
| ----------------------- |:---------------------------------------------------:| ------------:|
| data_ref                |  Data de coleta dos dados                           | object       |
| id_cliente              |  Id de identificação do cliente                     | int          |
| sexo                    |  M = Masculino / F = Feminino                       | object       |
| posse_de_veiculo        |  True = Possui Veiculo / False = Não possui Veiculo | bool         |
| posse_de_imovel         |  True = Possui Imovel / False = Não possui Imovel   | bool         |
| qtd_filhos              |  Quantidade de filhos do cliente                    | int          |
| tipo_renda              |  Tipo de renda (ex: Assalariado, Empresario e etc)  | object       |
| educacao                |  Nivel de educação(ex:Superior, Fundamental e etc)  | object       |
| estado_civil            |  Estado civil (ex:Casado, Solteiro e etc)           | object       |
| tipo_residencia         |  Tipo de residência (ex: casa/apartamento e etc)    | object       |
| idade                   |  Idade do cliente                                   | float        |
| tempo_emprego           |  Tempo de emprego com base em anos                  | float        |
| qt_pessoas_residencia   |  Quantidade de pessoas que residem na residencia    | float        |
| renda                   |  Renda do Cliente                                   | float        |
| q_idade                 |  Idades divididas em quarters                       | object       |''')

st.markdown('---')

st.markdown('## Dataframe ')
st.dataframe(renda)
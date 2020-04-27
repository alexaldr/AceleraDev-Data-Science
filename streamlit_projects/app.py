import streamlit as st
import pandas as pd


def main():
    st.markdown('![Codenation Logo](https://miro.medium.com/max/425/1*05vDjNRMACek8hWh1pnltA.png)')
    st.markdown('###### Essa aplicação faz parte do conteúdo estudado durante a aceleração da Codenation: **Aceleradev Data Science 2020**.')
    st.markdown('---')
    st.title('Análise Exploratória de Dados em Python')
    st.header('Use o menu lateral para escolher um arquivo csv.')

    f = st.sidebar.file_uploader('Escolha o arquivo do dataframe (csv):')
    if f:
        try:
            df = pd.read_csv(f)

            st.write('<span style="color:red">red</span>', unsafe_allow_html=True)
            st.markdown('#### Quantidade de colunas:')
            st.markdown(f'<span style="color:green">{df.shape[1]}</span>', unsafe_allow_html=True)

            st.markdown('#### Quantidade de linhas:')
            st.markdown(f'<span style="color:green">{df.shape[0]}</span>', unsafe_allow_html=True)

            st.markdown('#### df.head():')
            head_n = st.slider('número de linhas:', min_value=1,
                               max_value=15, value=5, step=1)
            st.dataframe(df.head(head_n))

            st.markdown('#### Escolha as colunas que deseja analisar:')
            colunas = st.multiselect(
                'Colunas do dataframe:', list(df.columns), default=None)

            if colunas:
                st.success(f'Colunas selecionadas: \n\n {colunas}')
                if st.button('Aplicar colunas ao dataframe'):
                    df = df[colunas]

            st.markdown('#### df.info():')
            st.table(df.info())

            st.markdown('#### df.describe():')
            st.dataframe(df.describe())

        except Exception as err:
            st.warning('Parece haver algum problema com o arquivo selecionado.')
            st.exception(err)


if __name__ == '__main__':
    main()

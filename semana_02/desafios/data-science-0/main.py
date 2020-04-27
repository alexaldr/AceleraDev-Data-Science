#!/usr/bin/env python
# coding: utf-8

# # Desafio 1
# 
# Para esse desafio, vamos trabalhar com o data set [Black Friday](https://www.kaggle.com/mehdidag/black-friday), que reúne dados sobre transações de compras em uma loja de varejo.
# 
# Vamos utilizá-lo para praticar a exploração de data sets utilizando pandas. Você pode fazer toda análise neste mesmo notebook, mas as resposta devem estar nos locais indicados.
# 
# > Obs.: Por favor, não modifique o nome das funções de resposta.

# ## _Set up_ da análise

# In[231]:


import pandas as pd
import numpy as np


# In[232]:


black_friday = pd.read_csv("black_friday.csv")


# ## Inicie sua análise a partir daqui

# In[233]:


black_friday.head()


# In[234]:


black_friday.info()


# In[235]:


black_friday.describe()


# ## Questão 1
# 
# Quantas observações e quantas colunas há no dataset? Responda no formato de uma tuple `(n_observacoes, n_colunas)`.

# Referências:
# - [pandas.DataFrame.shape](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.shape.html)

# In[236]:


def q1():
    return black_friday.shape

# visualização do retorno
q1()


# ## Questão 2
# 
# Há quantas mulheres com idade entre 26 e 35 anos no dataset? Responda como um único escalar.

# Referências:
# - [select a subset of a DataFrame](https://pandas.pydata.org/pandas-docs/stable/getting_started/intro_tutorials/03_subset_data.html)

# In[237]:


# quais são as idades das mulheres disponíveis no dataset?
black_friday[black_friday['Gender'] == 'F']['Age'].unique()


# In[238]:


# filtro de gênero e filtro de idade sobre gênero
black_friday_female = black_friday[black_friday['Gender'] == 'F']
black_friday_female_age_26_35 = black_friday_female[black_friday_female['Age'] == '26-35']


# In[239]:


def q2():
    return int(black_friday_female_age_26_35['Age'].count())

# visualização do retorno
q2()


# ## Questão 3
# 
# Quantos usuários únicos há no dataset? Responda como um único escalar.

# Referências:
# - [pandas.DataFrame.nunique](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.nunique.html)

# In[240]:


def q3():
    return black_friday['User_ID'].nunique()

# visualização do retorno
q3()


# ## Questão 4
# 
# Quantos tipos de dados diferentes existem no dataset? Responda como um único escalar.

# Referências:
# - [pandas.DataFrame.dtypes](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dtypes.html)
# - [pandas.DataFrame.nunique](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.nunique.html)

# In[241]:


def q4():
    return int(black_friday.dtypes.nunique()) 

# visualização do retorno
q4()


# ## Questão 5
# 
# Qual porcentagem dos registros possui ao menos um valor null (`None`, `ǸaN` etc)? Responda como um único escalar entre 0 e 1.

# Referências:
# - [pandas.DataFrame.dropna](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dropna.html)
# - [pandas.DataFrame.shape](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.shape.html)

# In[242]:


def q5():
    # (total - quantidade_nao_nulos) = quantidade_nulos
    # (total - quantidade_nao_nulos) / total = porcentagens_nulos
    return (black_friday.shape[0] - black_friday.dropna().shape[0]) / black_friday.shape[0]

# visualização do retorno
q5()


# ## Questão 6
# 
# Quantos valores null existem na variável (coluna) com o maior número de null? Responda como um único escalar.

# Referências: 
# - [pandas.DataFrame.isna](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.isna.html)
# - [pandas.DataFrame.sum](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sum.html)
# - [pandas.DataFrame.max](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.max.html)

# In[243]:


def q6():
    # Retorne aqui o resultado da questão 6.
    return int(black_friday.isna().sum().max())

# visualização do retorno
q6()


# ## Questão 7
# 
# Qual o valor mais frequente (sem contar nulls) em `Product_Category_3`? Responda como um único escalar.

# Referências: 
# - [pandas.Series.mode](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.mode.html)

# In[244]:


def q7():
    # basta retornar a moda da coluna
    return float(black_friday['Product_Category_3'].mode())

# visualização do retorno
q7()


# ## Questão 8
# 
# Qual a nova média da variável (coluna) `Purchase` após sua normalização? Responda como um único escalar.

# Referências: 
# - [pandas.Series.min](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.min.html)
# - [pandas.Series.max](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.max.html)
# - [pandas.Series.mean](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.mean.html)

# In[245]:


purchases_series = black_friday['Purchase'].copy()


# In[246]:


def q8():
    # normalização pelo mínimo e máximo
    normalized_purchases = (purchases_series - purchases_series.min())                         / (purchases_series.max() - purchases_series.min())
    return float(normalized_purchases.mean())

# visualização do retorno
q8()


# ## Questão 9
# 
# Quantas ocorrências entre -1 e 1 inclusive existem da variáel `Purchase` após sua padronização? Responda como um único escalar.

# Referências: 
# - [pandas.Series.mean](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.mean.html)
# - [pandas.Series.std](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.std.html)
# - [pandas.Series.between](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.between.html)

# In[247]:


def q9():
    # (valor - media) / desvio_padrao
    standardized_purchases = (purchases_series - purchases_series.mean()) / purchases_series.std()
    
    return int(standardized_purchases.between(-1, 1).sum())

# visualização do retorno
q9()


# ## Questão 10
# 
# Podemos afirmar que se uma observação é null em `Product_Category_2` ela também o é em `Product_Category_3`? Responda com um bool (`True`, `False`).

# Referências: 
# - [pandas.Series.isna](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.isna.html)
# - [pandas.Series.equals](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.equals.html)

# In[248]:


def q10():
    # basta comparar as duas séries de nan
    return black_friday['Product_Category_2'].isna().equals(black_friday['Product_Category_2'].isna())
    
# visualização do retorno
q10()


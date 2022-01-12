from random import uniform
import streamlit as st
import pdfkit
import datetime
import locale
from PIL import Image


def imagen_estrela(nota):
    if nota < 1 / 3:
        img = 'fill.png'
    elif nota >= 1 / 3 and nota < 2/3:
        img = 'half.png'
    else:
        img = 'full.png'
    return img

# Configuração da Pagina


st.set_page_config(page_title='Sistema de avaliação', page_icon='⭐', layout="wide",
                   initial_sidebar_state="auto", menu_items=None)
locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
# Configuração do sidebar

st.sidebar.title('Configurações')

nome = st.sidebar.text_input('Nome:')
inscrição = st.sidebar.text_input('Inscrição:')
funcao = st.sidebar.text_input('Função:')

# Inicia as variaveis de avaliação do funcionario
st.sidebar.subheader('Avaliação')
mes = st.sidebar.selectbox('Mês avaliado:', ['Janeiro', 'Fevereiro', 'Março', 'Abril',
                           'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'])
desempenho = st.sidebar.slider('Desempenho:', 0.0, 1.0, value=0.5, key=1)
manutencao = st.sidebar.slider('Manutenção:', 0.0, 1.0, value=0.5, key=2)
compromisso = st.sidebar.slider('Compromisso:', 0.0, 1.0, value=0.5, key=3)
pontualidade = st.sidebar.slider('Pontualidade:', 0.0, 1.0, value=0.5, key=4)
desenvolvimento = st.sidebar.slider(
    'Desenvolvimento:', 0.0, 1.0, value=0.5, key=5)

# Body principal

st.markdown(f'<h1 style="text-align: center">Sistema de Avaliação</h1>',
            unsafe_allow_html=True)
st.write('\n')
texto_html = f'<h3 style="text-align: center">O funcionário {nome.upper()} foi avaliado em {datetime.datetime.today().strftime("%d de %B de %Y")} e recebeu os seguintes resultados:</h3><br>'
st.markdown(texto_html, unsafe_allow_html=True)
st.write('\n')
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.markdown(
        f'<h4>Desempenho</h4><br><h5>Nota: {desempenho}</h5>', unsafe_allow_html=True)
    st.image(imagen_estrela(desempenho), width=60)
with col2:
    st.markdown(
        f'<h4>Manutenção</h4><br><h5>Nota: {manutencao}</h5>', unsafe_allow_html=True)
    st.image(imagen_estrela(manutencao), width=60)
with col3:
    st.markdown(
        f'<h4>Compromisso</h4><br><h5>Nota: {compromisso}</h5>', unsafe_allow_html=True)
    st.image(imagen_estrela(compromisso), width=60)
with col4:
    st.markdown(
        f'<h4>Pontualidade</h4><br><h5>Nota: {pontualidade}</h5>', unsafe_allow_html=True)
    st.image(imagen_estrela(pontualidade), width=60)
with col5:
    st.markdown(
        f'<h4>Desenvolvimento</h4><br><h5>Nota:{desenvolvimento}</h5>', unsafe_allow_html=True)
    st.image(imagen_estrela(desenvolvimento), width=60)
st.write('\n')
st.markdown(f'<br>', unsafe_allow_html=True)
st.markdown(f'<h1 style="text-align: center">O Resultado total da avaliação do mês de {mes} fico assim:</h1><br><br>',
            unsafe_allow_html=True)
scol1, scol2, scol3, scol4, scol5 = st.columns(5)

with scol1:
    st.write('\n')
with scol2:
    st.write(f'\n')
with scol3:
    st.text(f'\n')
    st.image(imagen_estrela(
        (desempenho+compromisso+pontualidade+desenvolvimento+manutencao)/5), width=90, caption=f'Nota: {round(desempenho+compromisso+pontualidade+desenvolvimento+manutencao,2)}')
with scol4:
    st.write('\n')
with scol5:
    st.write('\n')
if (desempenho+compromisso+pontualidade+desenvolvimento+manutencao)/5 == 1:
    st.balloons()

import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
import numpy as np


Dataframe=pd.read_csv('consulta.csv', sep=',', encoding='latin-1')
Dataframe = Dataframe.drop(['categoria'], axis=1)
Dataframe=Dataframe.drop(['ciudad'], axis=1)
Dataframe = pd.get_dummies(Dataframe, columns=['medio_de_pago'])
Dataframe=[['IdCategorias',
 'precio',
 'cuotas',
 'puntaje',
 'IdCiudad',
 'medio_de_pago_boleto',
 'medio_de_pago_credit_card',
 'medio_de_pago_debit_card',
 'medio_de_pago_voucher']]

with st.sidebar:

    selected= option_menu('Menú',
                          ['G4','Ventas'],
                          icons=['graph-up','flower3'],menu_icon='fontawesome',
                          default_index=0)
    

## --------------------------------------------------------------

if selected=='G4':
    
    #st.title("Información G4")
    # Titulo 
    st.markdown("<h1 style='text-align: center; color: white;'> G4</h1>", unsafe_allow_html=True)


# imagen G4

    from PIL import Image
    image = Image.open('G4.png')
    st.image(image, caption='G4',use_column_width=True)


# Objetivo principal y los otros objetivos

    st.markdown("<h3 style='text-align: center; color: white;'>Objetivo principal</h3>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: Left; color: white;'>El objetivo principal de este proyecto es realizar una predicción precisa de las ventas y llevar a cabo un análisis  de los métodos de pago más utilizados por los clientes. Además, se buscará comprender la distribución geográfica de los vendedores para asegurar tiempos de entrega predecibles y eficientes.</h4>", unsafe_allow_html=True)

    st.markdown("<h3 style='text-align: Center; color: white;'>Objetivos específicos</h3>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: left; color: white;'>- Análisis de los estados con mayores ventas</h4>", unsafe_allow_html=True)

    st.markdown("<h4 style='text-align: left; color: white;'>- Análisis de los métodos de pago más utilizados</h4>", unsafe_allow_html=True)

    st.markdown("<h4 style='text-align: left; color: white;'>- Análisis de la satisfacción del cliente</h4>", unsafe_allow_html=True)

    st.markdown("<h4 style='text-align: left; color: white;'>- Predicción de las ventas</h4>", unsafe_allow_html=True)

 

##--------------------------------------------------------------

if selected=='Ventas':

    st.title("Predicción de ventas ")

    st.text("Introduce los datos para predecir las ventas")

    st.header("Datos de entrada")

    col1,col2=st.columns(2)

    with col1:
        IdCategorias=st.number_input("IdCategorias",value=0.0,min_value=0.00, max_value=71.00,format="%.2f")
        precio=st.number_input("precio",value=0.0,min_value=0.00, max_value=1000000.00,format="%.2f")
        cuotas=st.number_input("cuotas",value=0.0,min_value=0.00, max_value=36.00,format="%.2f")
        puntaje=st.number_input("puntaje",value=0.0,min_value=0.00, max_value=5.00,format="%.2f")
        IdCiudad=st.number_input("IdCiudad",value=0.0,min_value=0.00, max_value=5.00,format="%.2f")
    
    with col2:
        medio_de_pago_boleto=st.number_input("medio_de_pago_boleto",value=0.0,min_value=0.00, max_value=1.00,format="%.2f")
        medio_de_pago_credit_card=st.number_input("medio_de_pago_credit_card",value=0.0,min_value=0.0, max_value=1.00,format="%.1f")
        medio_de_pago_debit_card=st.number_input("medio_de_pago_debit_card",value=0.0,min_value=0.0, max_value=1.00,format="%.1f")
        medio_de_pago_voucher=st.number_input("medio_de_pago_voucher",value=0.0,min_value=0.0, max_value=1.0,format="%.1f")

# Funcion para predecir valor con las columnas del modelo

    def predecir():
        model = joblib.load("model2.joblib")

        prediction=model.predict([[IdCategorias,precio,cuotas,puntaje,IdCiudad,medio_de_pago_boleto,medio_de_pago_credit_card,medio_de_pago_debit_card,medio_de_pago_voucher]])

        # mostrar el valor de la prediccion
        st.success("El valor de la predicción es: {}".format(prediction))
        
# crea boton para predecir
    
    trigger=st.button("predecir",on_click=predecir)
    if trigger:
       predecir()
       st.balloons()
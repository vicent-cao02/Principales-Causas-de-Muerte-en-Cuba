import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.title('Análisis de las Principales Causas de Muerte en Cuba')


with st.expander("Causas de Muerte"):
    st.write('Comprender las tendencias en las principales causas de muerte es crucial para desarrollar estrategias de prevención y promoción de la salud. Este proyecto se centra en una revisión exhaustiva de los datos proporcionados por el Anuario Estadístico de Cuba, que abarca desde el año 2000 hasta el 2022. ')
    
    st.write("Nuestro objetivo es analizar la evolución de las principales causas de muerte en Cuba durante más de dos décadas, desde el año 2000 hasta 2022. Utilizando una visualización interactiva y dinámica, exploraremos cómo estas causas han cambiado a lo largo de los años, identificando patrones, fluctuaciones y tendencias significativas.    Un aspecto particularmente notable es el comportamiento de los tumores malignos, que han sido la principal causa de muerte durante todo el período analizado. En particular, en 2021, los tumores malignos alcanzaron una tasa de mortalidad del 240.9 por cada 100,000 habitantes, un dato que destaca y merece una atención especial en nuestro análisis. Este aumento significativo subraya la importancia de entender las tendencias a largo plazo y de considerar las implicaciones para las políticas de salud pública y las estrategias de prevención.")
   
    def load_data():
        return pd.read_json('data/output.json')
    data = load_data()

    df = pd.DataFrame(data)

    df_long = df.melt(id_vars="enfermedades", var_name="Año", value_name="Número de Muertes")

    fig = go.Figure()

    for enfermedad in df['enfermedades']:
        df_enfermedad = df_long[df_long['enfermedades'] == enfermedad]
        fig.add_trace(go.Scatter(x=df_enfermedad['Año'], y=df_enfermedad['Número de Muertes'], mode='lines+markers',name=enfermedad))

                               
                 
    fig.update_layout(
        title='Principales Causas de Muerte en Cuba',
        xaxis_title='Año',
        yaxis_title='Número de Muertes',
        hovermode='x unified'
    )
    st.write("Este análisis no solo proporciona una perspectiva sobre el impacto histórico de estas enfermedades, sino que también ofrece información valiosa para la planificación de políticas de salud pública y la asignación de recursos. Al observar las tendencias y patrones en los datos, los responsables de la formulación de políticas y los profesionales de la salud podrán identificar áreas prioritarias para la intervención y mejorar las estrategias para abordar las principales causas de muerte en Cuba.")  
    # st.title('Análisis de Causas de Muerte')
    st.plotly_chart(fig)
    st.write("La visualización interactiva desarrollada en este proyecto permitirá a los usuarios explorar la evolución de estas causas de manera intuitiva, facilitando una comprensión más profunda de cómo han cambiado los perfiles de mortalidad en el país.")

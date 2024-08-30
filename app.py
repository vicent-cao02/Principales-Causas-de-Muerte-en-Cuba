import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit.components.v1 as components
import seaborn as sns
import matplotlib.pyplot as plt
import json
import streamlit_analytics
from streamlit_analytics import Analytics
from streamlit_authenticator import Authenticate

analytics = Analytics()

with streamlit_analytics.track():
    st.title('La Mortalidad en Cuba: Un estudio revelador')


    st.write('Cuba, como muchos países del mundo a pesar de su reconocido sistema de cobertura universal, enfrenta desafíos en la salud pública. Detrás de cada cifra de mortalidad hay una historia, preguntas como: ¿Qué factores están incidiendo en este panorama?, ¿será una concecuencia inevitable del envejecimiento de la población? o quizás la respuesta se encuentra en una combinación de factores que van más allá de las cifras oficiales.')

    def load_data():
        return pd.read_json('data/output.json')
    data = load_data()

    df = pd.DataFrame(data)

    df_long = df.melt(id_vars="enfermedades", var_name="Año", value_name="Número de Muertes")


    colores = {
        "Tumores malignos":'Red',
        'Enfermedades cardiovasculares': 'Blue',
        'Enfermedades cronicas respiratorias': 'green',
        'Enfermedades cerebrovasculares': 'Blue',
        "Influenza y neumonia": 'green',
        'Accidentes': 'orange',
        'Lesiones autoinflingidas accidentalmente': 'orange',
        'COVID-19': 'green',
        "Enfermedades de las arterias": "Blue",
        "Diabetes mellitus": "violet",
        "Cirrosis": "Brown",
    }

    fig = go.Figure()

    for enfermedad in df['enfermedades'].unique():  
        df_enfermedad = df_long[df_long['enfermedades'] == enfermedad]
        
        color = colores.get(enfermedad, 'black')
        
        fig.add_trace(go.Scatter(
            x=df_enfermedad['Año'],
            y=df_enfermedad['Número de Muertes'],
            mode='lines+markers',
            name=enfermedad,
            line=dict(color=color)  
        ))

    fig.update_layout(
        title='Principales Causas de Muerte en Cuba',
        xaxis_title='Año',
        yaxis_title='Número de Muertes',
        hovermode='x unified'
    )



    st.write("Las principales causas de defunción se agrupan en las siguientes categorías: enfermedades cardiovasculares (incluyendo cardiopatías isquémicas y accidentes cerebrovasculares), enfermedades respiratorias (como la enfermedad pulmonar obstructiva crónica e infecciones de las vías respiratorias inferiores, el Covid 19), las enfermedades hepáticas (Cirrosis), las enfermedades metabólicas (la Diabetes mellitus por tener un impacto significativo en la salud cardiovascular y estar relacionada con otras condiciones como la presión alterial alta, niveles elevados de colesterol, la obesidad entre otros.) las no intensionadas (como los accidentes de tránsito y las lesiones autoinflingida accidentalmente), y los tumores malignos (cáncer). En particular, el cáncer ha sido una de las principales causas de mortalidad a lo largo de los años, y experimentó un aumento significativo en el 2021, con una tasa de 240,9 muertes por cada 100,000 habitantes en un período afectado por la Covid-19. Este aumento subraya la necesidad de comprender la evolución a largo plazo y resaltar la importancia de desarrollar políticas de salud pública y estrategias de prevención adaptadas a estas realidades.")  
    st.plotly_chart(fig)



    def load_data():
        with open('data/output4.json') as f:
            data = json.load(f)
        return data

    data = load_data()

    def json_to_df(data):
        df_list = []
        for item in data:
            enfermedad = item['enfermedades']
            for key, value in item.items():
                if key != 'enfermedades':
                    df_list.append({'enfermedad': enfermedad, 'provincia': key, 'valor': float(value.replace(',', '.'))})
        
        df = pd.DataFrame(df_list)
        return df

    df = json_to_df(data)


    def load_geojson():
        with open('data/cuba.geojson') as f:
            geojson = json.load(f)
        return geojson

    geojson = load_geojson()

    def plot_map(df, geojson, selected_enfermedades):
        filtered_df = df[df['enfermedad'] == selected_enfermedades]
        
        provinces = filtered_df['provincia'].unique()
        print("Provincias disponibles en los datos:", provinces)
        
        fig = px.choropleth(
            filtered_df,
            geojson=geojson,
            locations='provincia',
            featureidkey="properties.province", 
            color='valor',
            color_continuous_scale="Viridis",
            labels={'valor': 'Incidencia'}
        )
        
        fig.update_geos(
            visible=True,
            fitbounds="locations", 
            projection=dict(
                type="mercator"  
            ),
            center={"lat": 20.5, "lon": -100.0},  
            
        )
        fig.update_layout(
            width=800,  
            height=600   
        )
        return fig

    enfermedades = df['enfermedad'].unique()
    selected_enfermedades = st.selectbox('Selecciona una enfermedad:', enfermedades)

    fig = plot_map(df, geojson, selected_enfermedades)
    st.plotly_chart(fig)

    st.write("El cáncer es un término genérico que designa un amplio grupo de enfermedades que pueden afectar a cualquier parte del organismo; también se utilizan los términos tumores malignos o neoplasias malignas. Constituyen un serio problema de salud para la humanidad y según el artículo publicado por la revista [Scielo](http://scielo.sld.cu/scielo.php?script=sci_arttext&pid=S1028-48182024000100005#:~:text=Los%20tumores%20malignos%20constituyen%20la,de%20muerte%20en%20el%20pa%C3%ADs.), 'Mortalidad por tumores malignos' se estima que se incremente en un 47% de los casos antes del 2040. Los hábitos, estilos de vida, el envejecimiento de la población y las enfermedades infecciosas, son factores fundamentales de este incremento. ")


    datas = pd.read_json('data/output2.json')
    df = pd.DataFrame(datas)
    for col in df.columns[1:]:  
        if df[col].dtype == 'object':
            df[col] = df[col].str.replace(',', '.').str.replace(' ', '').astype(float)

    df.set_index('Annos', inplace=True)
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(df, annot=True, cmap='YlGnBu', fmt=".1f", linewidths=0.5, ax=ax)
    ax.set_title('Tumores Malignos por Rango de Edad y Años(2021)')
    st.pyplot(fig)

    st.write("Se toma como referencia el año 2021 por ser este precisamente el que marcó el tope en cifras de mortalidad prevaleciendo la edad de la senectud por ser los principales vulnerables.")
    data = pd.read_json('data/output3.json')

    df = pd.DataFrame(data)
    for col in df.columns[1:]:  
        if df[col].dtype == 'object':  
            df[col] = df[col].str.replace(',', '.').str.replace(' ', '').astype(float)
    fig = px.pie(df[:-1], names='Localizacion', values='Tasa',
                title='Distribución de la Tasa de mortalidad de los tumores en el organismo (2022)',
                labels={'Tasa': 'Tasa de Mortalidad'},
                color_discrete_sequence=px.colors.sequential.Cividis)
    st.plotly_chart(fig)

    def load_data():
        return pd.read_json('data/output.json')
    data = load_data()

    df = pd.DataFrame(data)

    df_long = df.melt(id_vars="enfermedades", var_name="Año", value_name="Número de Muertes")

    for enfermedad in df['enfermedades'].unique():  
        df_enfermedad = df_long[df_long['enfermedades'] == enfermedad]
        
    df_enfermedad = pd.DataFrame(data)
    excluir_enfermedades = ["COVID-19", "Accidentes","Influenza y neumonia","Lesiones autoinflingidas accidentalmente"]

    df_2022 = df_enfermedad[~df_enfermedad['enfermedades'].isin(excluir_enfermedades)]
    df_2022 = df_2022[['enfermedades', '2022']].rename(columns={'2022': 'Número de Muertes'})

    enfermedades = df_2022['enfermedades']
    muertes_2022 = df_2022['Número de Muertes']

    st.write("La visualización interactiva desarrollada en este proyecto permitirá a los usuarios explorar de manera intuitiva la evolución de estas causas de mortalidad, facilitando una comprensión más profunda de cómo han cambiado los perfiles de mortalidad en el país a lo largo del tiempo. Resulta interesante resaltar que la mayoría de estas causas de muerte son no transmisibles, lo que sugiere una necesidad de abordar este tema causado en Cuba fundamentalmente por el alto consumo de tabaco en la población, lo que aumenta el riesgo de enfermedades cardiovasculares, cáncer y otras enfermedades no transmisibles.")
    st.title('Prevenir el riesgo de morir por Enfermedades No Transmisibles(ENT)')
    st.write("Las Enfermedades No Transmisibles (ENT) constituyen seis de las principales causas de mortalidad en Cuba. Estas incluyen tumores malignos, enfermedades cerebrovasculares, diabetes, cirrosis, enfermedades crónicas respiratorias y enfermedades de las arterias. En el 2022, estas enfermedades causaron un total de 423,3 muertes por cada 100,000 habitantes, representando el 40% de las principales causas de muerte en el país. Esta alta tasa de mortalidad destaca la magnitud del problema y subraya la necesidad urgente de estrategias de prevención y tratamiento efectivas.")
    fig1 = go.Figure(data=[go.Bar(x=enfermedades, y=muertes_2022, marker_color='blue')])

    fig1.update_layout(
        title='Tasas de Muertes en el 2022 por Enfermedades No Transmisibles (ENT)',
        xaxis_title='Enfermedades',
        yaxis_title='Número de Muertes',
        xaxis_tickangle=-45  
    )
    st.plotly_chart(fig1)
    st.write("Según el [artículo publicado por el Ministerio de Salud Pública de Cuba (MINSAP)](https://salud.msp.gob.cu/prevenir-el-riesgo-de-morir-prematuramente-por-enfermedades-no-transmisibles/), la prevención de la muerte prematura causada por enfermedades no transmisibles en Cuba se enfrenta a varios factores de riesgo significativos. Estos incluyen el tabaquismo y la exposición al humo de tabaco, una dieta poco saludable, la inactividad física, la obesidad y el consumo excesivo de alcohol. Recientemente, se ha añadido la contaminación del aire a esta lista, reconociéndose a nivel mundial como un factor de riesgo importante para las enfermedades cardiovasculares y respiratorias crónicas. Abordar estos factores es crucial para mejorar la salud pública y reducir la mortalidad prematura asociada con las enfermedades no transmisibles.")
    st.write("Las condiciones de vida, el empleo, el ambiente laboral, la educación, la globalización, así como las situaciones económicas y demográficas y la urbanización, son factores clave que determinan la prevalencia de enfermedades no transmisibles (ENT). Estos desafíos requieren un esfuerzo concertado tanto de los servicios de salud como de toda la sociedad, dado que se trata de un problema que afecta a nivel global, no solo a Cuba..")



    st.title("Enfermedades no Transmisibles con lentes de Género")
    st.write(" Las diferencias biológicas entre las mujeres y los hombres, los roles de género y la marginación social exponen de manera diferente a hombres y a mujeres a los factores de riesgo, y determinan su capacidad para modificar comportamientos de riesgo así como el éxito de las intervenciones frente a estas enfermedades. Un vistazo en los números muestran que estas enfermedades afectan más a hombres, esto estará dado seguro a que para obterner más estatus los hombres deben fumar y consumir bebidas alcohólicas frecuentemente, lo que provoca un aumento acelerado de estas enfermedades.")
    st.write("Las mujeres cubanas enfrentan un desafío creciente con el cáncer, especialmente cáncer de mama y cervical, que representan una alta tasa de mortalidad.Las mujeres tienen significativamente más probabilidad de ser obesas que los hombres, aumenta la vulnerabilidad de estas a padecer de enfermedades no transmisibles y especialmente diabetes.")
    def load_data():
        return pd.read_json('data/output1.json')
    data1 = load_data()

    df1 = pd.DataFrame(data1)
    excluir_enfermedades = ["COVID-19", "Accidentes ","Influenza y neumonia","Lesiones autoinflingidas accidentalmente","Influenza y neumonia ","Lesiones autoinfligidas intencionalmente "]
    df1 = df1[~df1['Enfermedades'].isin(excluir_enfermedades)]
    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=df1['Enfermedades'],
        y=df1['Tasas masculinas '],
        name='Tasas masculinas',
        marker_color='blue'
    ))

    fig.add_trace(go.Bar(
        x=df1['Enfermedades'],
        y=df1['Tasas femeninas'],
        name='Tasas femeninas',
        marker_color='#D81B60'
    ))

    fig.update_layout(
        title='Tasas de mortalidad por 100,000 habitantes por Enfermedad y Sexo en 2022',
        xaxis_title='Enfermedades',
        yaxis_title='Número de Tasas de mortalidad',
        barmode='group'
    )
    st.plotly_chart(fig)

    st.write("Este estudio ha proporcionado una visión importante sobre las causas de muerte en Cuba. Sin embargo es fundamental continuar la investigación para profundizar en la comprensión de las tendencias y los factores que contribuyen a la mortalidad por enfermedades no transmisibles. La aplicación de herramientas de ciencia de datos puede proporcionar información valiosa para el desarrollo de políticas públicas que aborden efectivamente los desafíos de la salud en Cuba.")



        
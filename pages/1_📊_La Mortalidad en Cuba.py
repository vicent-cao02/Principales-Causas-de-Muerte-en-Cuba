import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt
import json
import datetime
import streamlit_analytics


st.set_page_config(
    page_title="La Mortalidad en Cuba",
    page_icon="📊",
)
st.title('La Mortalidad en Cuba: Un estudio revelador.')


with streamlit_analytics.track():

    st.write('Cuba, como muchos países del mundo a pesar de su reconocido sistema de cobertura universal, enfrenta desafíos en la salud pública. Detrás de cada cifra de mortalidad hay una historia, preguntas como: ¿Qué factores están incidiendo en este panorama?, ¿será una consecuencia inevitable del envejecimiento de la población? o quizás la respuesta se encuentra en una combinación de factores que van más allá de las cifras oficiales.')

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



    st.write("Las principales causas de defunción se agrupan en las siguientes categorías: enfermedades cardiovasculares (incluyendo cardiopatías isquémicas y accidentes cerebrovasculares), enfermedades respiratorias (como la enfermedad pulmonar obstructiva crónica e infecciones de las vías respiratorias inferiores, el Covid 19), las enfermedades hepáticas (cirrosis), las enfermedades metabólicas (la diabetes mellitus por tener un impacto significativo en la salud cardiovascular y estar relacionada con otras condiciones como la presión arterial alta, niveles elevados de colesterol, la obesidad entre otros), las enfermedades no intensionadas (como los accidentes de tránsito y las lesiones autoinflingida accidentalmente), y los tumores malignos (cáncer). En particular, el cáncer ha sido una de las principales causas de mortalidad a lo largo de los años, y experimentó un aumento significativo en el 2021, con una tasa de 240,9 muertes por cada 100,000 habitantes en un período afectado por la Covid-19. Este aumento subraya la necesidad de comprender la evolución a largo plazo y resaltar la importancia de desarrollar políticas de salud pública y estrategias de prevención adaptadas a estas realidades.")  
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
        print(provinces)
        
        fig = px.choropleth(
            filtered_df,
            geojson=geojson,
            locations= provinces,
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

    data = pd.read_json('./data/output1.json')
    df = pd.DataFrame(data)

    df['Tasas masculinas '] = df['Tasas masculinas '].str.replace(',', '.').astype(float)
    df['Tasas femeninas'] = df['Tasas femeninas'].str.replace(',', '.').astype(float)
    df['Ambos sexos'] = df['Ambos sexos'].astype(float)

    años = df['Anos'].unique()
    año_seleccionado = st.selectbox("Selecciona el año:", años)

    sexo_seleccionado = st.selectbox("Selecciona el sexo:", ["Masculino", "Femenino", "Ambos sexos"])

    df_filtrado = df[df['Anos'] == año_seleccionado]

    if sexo_seleccionado == "Masculino":
        fig = px.scatter(
            df_filtrado,
            x='Enfermedades',
            y='Tasas masculinas ',
            size='Tasas masculinas ',
            color='Enfermedades',
            hover_name='Enfermedades',
            hover_data={'Tasas masculinas ': True},
            title=f'Tasas de Defunciones (Masculinos) en {año_seleccionado}',
            labels={'Tasas masculinas ': 'Tasa de Defunciones (Masculinos)'},
            size_max=60
        )
    elif sexo_seleccionado == "Femenino":
        fig = px.scatter(
            df_filtrado,
            x='Enfermedades',
            y='Tasas femeninas',
            size='Tasas femeninas',
            color='Enfermedades',
            hover_name='Enfermedades',
            hover_data={'Tasas femeninas': True},
            title=f'Tasas de Defunciones (Femeninos) en {año_seleccionado}',
            labels={'Tasas femeninas': 'Tasa de Defunciones (Femeninos)'},
            size_max=60
        )
    else:  
        fig = px.scatter(
            df_filtrado,
            x='Enfermedades',
            y='Ambos sexos',
            size='Ambos sexos',
            color='Enfermedades',
            hover_name='Enfermedades',
            hover_data={'Ambos sexos': True},
            title=f'Tasas de Defunciones (Ambos Sexos) en {año_seleccionado}',
            labels={'Ambos sexos': 'Tasa de Defunciones (Ambos Sexos)'},
            size_max=60
        )

    fig.update_layout(
        xaxis_visible=False,
        yaxis_visible=False,
        showlegend=False,
        margin=dict(l=0, r=0, t=30, b=0) 
    )

    fig.update_traces(marker=dict(line=dict(width=2, color='DarkSlateGrey')), selector=dict(mode='markers'))

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

    years = df["Annos"].unique()
    selected_year = st.selectbox("Selecciona un año", years)

    def clean_and_convert(column):
        column = column.str.replace(',', '.', regex=False).str.replace(' ', '', regex=False)
        return pd.to_numeric(column, errors='coerce')

    df['Tasa'] = clean_and_convert(df['Tasa'])

    filtered_df = df[df['Annos'] == selected_year]

    fig = px.pie(filtered_df[:-1], names='Localizacion', values='Tasa',
                title=f'Distribución de la Tasa de mortalidad de los tumores en el organismo {selected_year}',
                labels={'Tasa': 'Tasa de Mortalidad'},
                color_discrete_sequence=px.colors.sequential.Cividis
                )

    st.plotly_chart(fig)
    
    data = pd.read_json('./data/output7.json')
    df = pd.DataFrame(data)

    df["Defunciones Masculinas "] = pd.to_numeric(df["Defunciones Masculinas "].str.replace(" ", "").str.replace(",", ""), errors='coerce')
    df['Defunciones Femeninas '] = pd.to_numeric(df['Defunciones Femeninas '].str.replace(" ", "").str.replace(",", ""), errors='coerce')
    df['Tasa masculina'] = pd.to_numeric(df['Tasa masculina'].str.replace(",", "."), errors='coerce')
    df['Tasa femeninas'] = pd.to_numeric(df['Tasa femeninas'].str.replace(",", "."), errors='coerce')

    years = df['Annos'].unique()
    
    year_start = st.selectbox("Selecciona un año inicial", sorted(years))
    year_end = st.selectbox("Selecciona un año final", sorted(years), index=len(years)-1)

    sexo = st.selectbox("Selecciona el sexo", ["Masculino", "Femenino"])

    df_filtered = df[(df['Annos'] >= year_start) & (df['Annos'] <= year_end)].dropna()

    if sexo == "Masculino":
        suma_tasas = df_filtered.groupby('Localozaciones').agg(
            Suma_Tasa=('Tasa masculina', 'sum')
        ).reset_index()
        title = f"Tasa de defunciones masculinas de {year_start} a {year_end}"
    else:
        suma_tasas = df_filtered.groupby('Localozaciones').agg(
            Suma_Tasa=('Tasa femeninas', 'sum')
        ).reset_index()
        title = f"Tasa de defunciones femeninas de {year_start} a {year_end}"

    fig = px.treemap(
        suma_tasas,
        path=['Localozaciones'],
        values='Suma_Tasa',
        title=title,
        hover_data={'Suma_Tasa': True} 
    )

    fig.update_traces(hovertemplate='Localización: %{label}<br>Suma de tasas: %{value:.2f}')

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

    st.write("La visualización interactiva desarrollada en este proyecto permitirá a los usuarios explorar de manera intuitiva la evolución de estas causas de mortalidad, facilitando una comprensión más profunda de cómo han cambiado los perfiles de mortalidad en el país a lo largo del tiempo. Resulta interesante resaltar que la mayoría de estas causas de muertes son no transmisibles, lo que sugiere una necesidad de abordar este tema causado en Cuba fundamentalmente por el alto consumo de tabaco en la población, lo que aumenta el riesgo de enfermedades cardiovasculares, cáncer y otras enfermedades no transmisibles.")
    st.title('Prevenir el riesgo de morir por Enfermedades No Transmisibles (ENT).')
    st.write("Las Enfermedades No Transmisibles (ENT) constituyen seis de las principales causas de mortalidad en Cuba. Estas incluyen tumores malignos, enfermedades cerebrovasculares, diabetes, cirrosis, enfermedades crónicas respiratorias y enfermedades de las arterias. En el 2022, estas enfermedades causaron un total de 423,3 muertes por cada 100,000 habitantes, representando el 40% de las principales causas de muertes en el país. Esta alta tasa de mortalidad destaca la magnitud del problema y subraya la necesidad urgente de estrategias de prevención y tratamiento efectivas.")
    fig1 = go.Figure(data=[go.Bar(x=enfermedades, y=muertes_2022, marker_color='blue')])

    fig1.update_layout(
        title='Tasas de Muertes en el 2022 por Enfermedades No Transmisibles (ENT)',
        xaxis_title='Enfermedades',
        yaxis_title='Número de Muertes',
        xaxis_tickangle=-45  
    )
    st.plotly_chart(fig1)
    st.write("Según el [artículo publicado por el Ministerio de Salud Pública de Cuba (MINSAP)](https://salud.msp.gob.cu/prevenir-el-riesgo-de-morir-prematuramente-por-enfermedades-no-transmisibles/), la prevención de la muerte prematura causada por enfermedades no transmisibles en Cuba se enfrenta a varios factores de riesgos significativos. Estos incluyen el tabaquismo y la exposición al humo de tabaco, una dieta poco saludable, la inactividad física, la obesidad y el consumo excesivo de alcohol. Recientemente, se ha añadido la contaminación del aire a esta lista, reconociéndose a nivel mundial como un factor de riesgo importante para las enfermedades cardiovasculares y respiratorias crónicas. Abordar estos factores es crucial para mejorar la salud pública y reducir la mortalidad prematura asociada con las enfermedades no transmisibles.")
    st.write("Las condiciones de vida, el empleo, el ambiente laboral, la educación, la globalización, así como las situaciones económicas y demográficas y la urbanización, son factores claves que determinan la prevalencia de enfermedades no transmisibles (ENT). Estos desafíos requieren un esfuerzo concertado tanto de los servicios de salud como de toda la sociedad, dado que se trata de un problema que afecta a nivel global, no solo a Cuba..")



    st.title("Enfermedades no Transmisibles con lentes de género.")
    st.write(" Las diferencias biológicas entre las mujeres y los hombres, los roles de género y la marginación social exponen de manera diferente a hombres y mujeres a los factores de riesgo, y determinan su capacidad para modificar comportamientos de riesgos así como el éxito de las intervenciones frente a estas enfermedades. Un vistazo en los números muestran que estas enfermedades afectan más a hombres, esto se debe a que para obtener más estatus los hombres deben fumar y consumir bebidas alcohólicas frecuentemente, lo que provoca un aumento acelerado de estas enfermedades.")
    st.write("Las mujeres cubanas enfrentan un desafío creciente con el cáncer, especialmente cáncer de mama y cervical, lo cual representa una alta tasa de mortalidad.Las mujeres tienen significativamente más probabilidad de ser más obesas que los hombres, aumentando la vulnerabilidad de estas al padecer de enfermedades no transmisibles y especialmente diabetes.")

    # def load_data():
    #     return pd.read_json('data/output1.json')

    with open("data/output1.json") as f:
        data1 = json.load(f)

    # data1 = load_data()r
    df1 = pd.DataFrame(data1)

    excluir_enfermedades = [
        "COVID-19", 
        "Accidentes ", 
        "Influenza y neumonia", 
        "Lesiones autoinfligidas accidentalmente", 
        "Influenza y neumonia", 
        "Lesiones autoinfligidas intencionalmente "
    ]
    df1 = df1[~df1['Enfermedades'].isin(excluir_enfermedades)]

    years = df1["Anos"].unique()
    year_seleccionado = st.slider("Selecciona un año:", min_value=int(years.min()), max_value=int(years.max()), value=int(years.min()), key="sexo")

    df_filtered = df1[df1['Anos'] == year_seleccionado]

    df_filtered['Tasas masculinas '] = pd.to_numeric(df_filtered['Tasas masculinas '].str.replace(',', '.', regex=False).str.replace(' ', '', regex=False), errors='coerce')
    df_filtered['Tasas femeninas'] = pd.to_numeric(df_filtered['Tasas femeninas'].str.replace(',', '.', regex=False).str.replace(' ', '', regex=False), errors='coerce')

    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=df_filtered['Enfermedades'],
        y=df_filtered['Tasas masculinas '],
        name='Tasas masculinas',
        marker_color='blue'
    ))

    fig.add_trace(go.Bar(
        x=df_filtered['Enfermedades'],
        y=df_filtered['Tasas femeninas'],
        name='Tasas femeninas',
        marker_color='#D81B60'
    ))

    fig.update_layout(
        title=f'Tasas de mortalidad por 100,000 habitantes por Enfermedad y Sexo en {selected_year}',
        xaxis_title='Enfermedades',
        yaxis_title='Número de Tasas de mortalidad',
        barmode='group'
    )
    st.plotly_chart(fig)


    with open('./data/output8.json', 'r') as f:
        data = json.load(f)

    df = pd.DataFrame(data)

    df['Cantidad de defunciones '] = df['Cantidad de defunciones '].str.replace(" ", "").astype(int)
    df['Cantidad de especialistas'] = df['Cantidad de especialistas'].astype(int)

    enfermedades = df['enfermedades'].unique()
    enfermedad_seleccionada = st.selectbox("Selecciona una enfermedad:", enfermedades, key="selexbox")

    df_enfermedad = df[df['enfermedades'] == enfermedad_seleccionada]

    anios = df_enfermedad['Annos'].unique()

    anio_seleccionado = st.slider("Selecciona un año:", min_value=int(anios.min()), max_value=int(anios.max()), value=int(anios.min()), key="especialist")

    df_anio = df_enfermedad[df_enfermedad['Annos'] == anio_seleccionado]

    fig = px.bar(
        x=['Defunciones', 'Especialistas'],
        y=[df_anio['Cantidad de defunciones '].values[0], df_anio['Cantidad de especialistas'].values[0]],
        color=['Defunciones', 'Especialistas'],
        labels={'x': 'Categoría', 'y': 'Cantidad'},
        title=f'Cantidad de Defunciones y Especialistas en {enfermedad_seleccionada} ({anio_seleccionado})'
    )

    st.plotly_chart(fig)


    st.write("Este estudio propicia una visión importante sobre las causas de muerte en Cuba. Sin embargo es fundamental continuar la investigación para profundizar en la comprensión de las tendencias y los factores que contribuyen a la mortalidad por enfermedades no transmisibles. La aplicación de herramientas de ciencia de datos puede proporcionar información valiosa para el desarrollo de políticas públicas que aborden efectivamente los desafíos de la salud en Cuba.")


    def likes():
        st.subheader("¿Te gusta este artículo?")
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("👍 Me gusta"):
                st.success("¡Gracias por tu opinión positiva! 😊")

        with col2:
            if st.button("👎 No me gusta"):
                st.error("¡Gracias por tu opinión negativa! 😔")

    likes()
    def comentarios():
        with st.form(key='comment_form'):
            comment = st.text_area("Escribe tu comentario:")
            submit_button = st.form_submit_button("Enviar Comentario")

            if submit_button:
                if comment:
                    st.success("¡Gracias por tu comentario!")
                else:
                    st.error("Por favor, escribe un comentario antes de enviar.")

    comentarios()

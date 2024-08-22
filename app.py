import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit.components.v1 as components
import seaborn as sns
import matplotlib.pyplot as plt

GA_TRACKING_ID = 'G-E4PEX6Q6J0'  
ga_code = f"""
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id={GA_TRACKING_ID}"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', '{GA_TRACKING_ID}');
</script>
console.log('hello')
"""
components.html(ga_code, height=0, width=0)


st.title('Principales Causas de Muerte en Cuba')


st.write('')

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
st.write("En Cuba, las principales causas de defunción se agrupan en tres grandes categorías: enfermedades cardiovasculares (incluyendo cardiopatías isquémicas y accidentes cerebrovasculares), enfermedades respiratorias (como la enfermedad pulmonar obstructiva crónica e infecciones de las vías respiratorias inferiores), y tumores malignos (cáncer). En particular, el cáncer ha sido una de las principales causas de mortalidad a lo largo de los años, y experimentó un aumento significativo en 2021, con una tasa de 240,9 muertes por cada 100,000 habitantes. Este aumento subraya la necesidad de comprender las evolución a largo plazo y resaltar la importancia de desarrollar políticas de salud pública y estrategias de prevención adaptadas a estas realidades.")  
st.plotly_chart(fig)
st.write("La visualización interactiva desarrollada en este proyecto permitirá a los usuarios explorar de manera intuitiva la evolución de estas causas de mortalidad, facilitando una comprensión más profunda de cómo han cambiado los perfiles de mortalidad en el país a lo largo del tiempo. Resulta interesante resaltar que la mayoría de estas causas de muerte son no transmisibles, lo que sugiere una necesidad de abordar este tema causado en Cuba fundamentalmente por el alto consumo de tabaco en la población, lo que aumenta el riesgo de enfermedades cardeovasculares, cancer y otras enfermedades no transmisibles.")
df_enfermedad = pd.DataFrame(data)
excluir_enfermedades = ["COVID-19", "Accidentes","Influenza y neumonia","Lesiones autoinflingidas accidentalmente"]

df_2022 = df_enfermedad[~df_enfermedad['enfermedades'].isin(excluir_enfermedades)]
df_2022 = df_2022[['enfermedades', '2022']].rename(columns={'2022': 'Número de Muertes'})

enfermedades = df_2022['enfermedades']
muertes_2022 = df_2022['Número de Muertes']

st.title('Prevenir el riesgo de morir por Enfermedades No Transmisibles(ENT)')
st.write("Las Enfermedades No Transmisibles (ENT) constituyen seis de las principales causas de mortalidad en Cuba. Estas incluyen tumores malignos, enfermedades cerebrovasculares, diabetes, cirrosis, enfermedades crónicas respiratorias y enfermedades de las arterias. En 2022, estas enfermedades causaron un total de 423,3 muertes por cada 100,000 habitantes, representando el 40% de las principales causas de muerte en el país. Esta alta tasa de mortalidad destaca la magnitud del problema y subraya la necesidad urgente de estrategias de prevención y tratamiento efectivas.")
fig1 = go.Figure(data=[go.Bar(x=enfermedades, y=muertes_2022, marker_color='blue')])

fig1.update_layout(
    title='Número de Muertes en 2022 por Enfermedad No Transmisibles(ENT)',
    xaxis_title='Enfermedades',
    yaxis_title='Número de Muertes',
    xaxis_tickangle=-45  
)
st.plotly_chart(fig1)
st.write("Según un artículo publicado por el Ministerio de Salud Pública de Cuba (MINSAP) en febrero de 2020, la prevención de la muerte prematura causada por enfermedades no transmisibles (ENT) en Cuba se enfrenta a varios factores de riesgo significativos. Estos incluyen el tabaquismo y la exposición al humo de tabaco, una dieta poco saludable, la inactividad física, la obesidad y el consumo excesivo de alcohol. Recientemente, se ha añadido la contaminación del aire a esta lista, reconociéndose a nivel mundial como un factor de riesgo importante para las enfermedades cardiovasculares y respiratorias crónicas. Abordar estos factores es crucial para mejorar la salud pública y reducir la mortalidad prematura asociada con las ENT.")
st.write("Las condiciones de vida, el empleo, el ambiente laboral, la educación, la globalización, así como las situaciones económicas y demográficas y la urbanización, son factores clave que determinan la prevalencia de enfermedades no transmisibles (ENT). Estos desafíos requieren un esfuerzo concertado tanto de los servicios de salud como de toda la sociedad, dado que se trata de un problema que afecta a nivel global, no solo a Cuba..")

datas = pd.read_json('data/output2.json')
df = pd.DataFrame(datas)
for col in df.columns[1:]:  
    if df[col].dtype == 'object':  
        df[col] = df[col].str.replace(',', '.').str.replace(' ', '').astype(float)
df.set_index('Annos', inplace=True)
fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(df, annot=True, cmap='YlGnBu', fmt=".1f", linewidths=0.5, ax=ax)
ax.set_title('Tumores Malignos por Rango de Edad y Años(2021-2022)')
st.pyplot(fig)


data = pd.read_json('data/output3.json')

df = pd.DataFrame(data)
for col in df.columns[1:]:  
    if df[col].dtype == 'object':  
        df[col] = df[col].str.replace(',', '.').str.replace(' ', '').astype(float)
fig = px.pie(df[:-1], names='Localizacion', values='Tasa',
             title='Distribución de la Tasa de Mortalidad por Localización',
             labels={'Tasa': 'Tasa de Mortalidad'},
             color_discrete_sequence=px.colors.sequential.Cividis)
st.plotly_chart(fig)


st.title("Enfermedades no Transmisibles con lentes de Género")
st.write(" Las diferencias biológicas entre las mujeres y los hombres, los roles de género y la marginación social exponen de manera diferente a hombres y a mujeres a los factores de riesgo, y determinan su capacidad para modificar comportamientos de riesgo así como el éxito de las intervenciones frente a estas enfermedades. Un vistazo en los números muestan q estas enfermedades afectan más a hombres, esto estará dado seguro a que para obterner más estatus los hombres deben fumar y consumir bebidas alcohólicas mas frecuentementem, esto hace q tenga un aumento acelerado de estas enfermedades.")
st.write("las mujeres cubanas enfrentan un desafío creciente con el cáncer, especialmente cáncer de mama y cervical, que representan una alta tasa de mortalidad.Las mujeres tienen significativamente más probabilidad de ser obesas que los hombres, aumenta la vulnerabilidad de éstas a padecer (ENT) y especialmente diabetes.")
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


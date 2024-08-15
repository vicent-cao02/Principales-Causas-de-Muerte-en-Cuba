import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit.components.v1 as components

# # Reemplaza con tu ID de seguimiento de Google Analytics
# GA_TRACKING_ID = 'G-E4PEX6Q6J0'  # Para GA4

# # Código de seguimiento de Google Analytics
# ga_code = f"""
# <!-- Google tag (gtag.js) -->
# <script async src="https://www.googletagmanager.com/gtag/js?id={GA_TRACKING_ID}"></script>
# <script>
#   window.dataLayer = window.dataLayer || [];
#   function gtag(){{dataLayer.push(arguments);}}
#   gtag('js', new Date());
#   gtag('config', '{GA_TRACKING_ID}');
# </script>
# """

# # Agrega el código de seguimiento a la aplicación
# components.html(ga_code, height=0, width=0)
# Reemplaza con tu clave de escritura de Segment
SEGMENT_WRITE_KEY = 'GI7vYWHNmWwHbyFjBrvL0jOBA1TpZOXC'

# Código de seguimiento de Segment
segment_code = f"""
<!-- Segment Analytics.js -->
<script type="text/javascript">
  !function(){{
    var e=window.analytics=window.analytics||[];if(!e.initialize)
    if(e.invoked)window.console&&console.error&&console.error("Segment snippet included twice.");
    else{{
      e.invoked=!0,e.methods=["trackSubmit","trackClick","trackLink","trackForm","pageview","identify","reset","group","track","ready","alias","debug","page","once","off","on","addSourceMiddleware","addIntegrationMiddleware","setAnonymousId","addDestinationMiddleware"],
      e.factory=function(t){{return function(){var n=Array.prototype.slice.call(arguments);return n.unshift(t),e.push(n)}}};
      for(var t=0;t<e.methods.length;t++){{var n=e.methods[t];e[n]=e.factory(n)}}
      e.load=function(t,n){{var a=document.createElement("script");a.type="text/javascript",a.async=!0,a.src="https://cdn.segment.com/analytics.js/v1/"+t+"/analytics.min.js";var r=document.getElementsByTagName("script")[0];r.parentNode.insertBefore(a,r),e._loadOptions=n}},
      e.SNIPPET_VERSION="4.13.1",e.load("{SEGMENT_WRITE_KEY}")
    }}
  }}()
</script>
"""

# Agrega el código de seguimiento a la aplicación
components.html(segment_code, height=0, width=0)


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
st.write("La visualización interactiva desarrollada en este proyecto permitirá a los usuarios explorar de manera intuitiva la evolución de estas causas de mortalidad, facilitando una comprensión más profunda de cómo han cambiado los perfiles de mortalidad en el país a lo largo del tiempo.")

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


st.title("Disparidades de Género")
st.write("")

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
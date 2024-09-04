import streamlit as st
import streamlit_analytics
import plotly.express as px
import pandas as pd

st.set_page_config(
    page_title="La Mortalidad en Cuba",
    page_icon="📈",
)
with streamlit_analytics.track():
    st.title("Crisis en las Carreteras de Cuba: Un artículo sobre el Aumento de Accidentes de Tránsito.")
    st.image("data/bache.jpeg")
    st.write("En el vibrante panorama de la vida cubana, donde la movilidad es esencial para el desarrollo y la conectividad social, los accidentes de tránsito emergen como una crisis silenciosa pero devastadora. A pesar de los esfuerzos por mejorar la infraestructura y las políticas de seguridad vial, la isla enfrenta un aumento preocupante en la frecuencia y severidad de estos incidentes. Este artículo examina la alarmante realidad de los accidentes de tránsito en Cuba, desglosando las causas detrás del incremento, el impacto en la sociedad y las soluciones necesarias para revertir esta tendencia preocupante.")
    st.write("En el 2022, Cuba reportó aproximadamente 9848 accidentes de tránsito, un aumento del 13% en comparación con el año anterior. Estos accidentes resultaron en 705 muertes y 7 542 heridos, reflejando un incremento en la gravedad de las lesiones. La tasa de mortalidad por accidentes de tránsito en Cuba se sitúa en 51 por cada 100,000 habitantes, superando el promedio regional de América Latina que es de 10.5 por cada 100,000 habitantes.")
    st.write("El análisis revela que las principales arterias del país, como la Carretera Central y la Autopista Nacional, son las más propensas a accidentes, con un notable incremento en las zonas rurales y suburbios, donde la falta de mantenimiento adecuado es evidente.")
    df =pd.read_json("./data/output5.json")
    st.dataframe(df, width=900)

    st.subheader("Principales causas identificadas:")
    st.write("Infraestructura Deteriorada: Uno de los factores más críticos es el estado de las carreteras. Muchas vías en Cuba sufren de baches significativos, mala señalización y falta de iluminación. La carretera entre La Habana y Pinar del Río, por ejemplo, ha sido identificada como un punto caliente para los accidentes debido a su deterioro y diseño deficiente. El gobierno ha anunciado planes para reparar y actualizar estas rutas, pero los progresos han sido lentos.")
    st.write("Vehículos Obsoletos: La edad avanzada de la flota vehicular en Cuba también contribuye al problema. Muchos vehículos en circulación son antiguos y carecen de los estándares de seguridad modernos. Se estima que el 30% de los accidentes involucran vehículos que no han pasado las inspecciones técnicas necesarias. La falta de piezas de repuesto y mantenimiento adecuado exacerba este problema.")
    st.write("Comportamiento de los Conductor y los peatones: El comportamiento imprudente de los conductores es otra causa significativa. Los datos muestran que el 35% de los accidentes están relacionados con el exceso de velocidad, mientras que el 20% se deben a la conducción bajo los efectos del alcohol. Las infracciones comunes incluyen el uso del teléfono móvil mientras se conduce y la falta de respeto a las señales de tránsito.")
    st.write("Factores Climáticos: Las condiciones climáticas también juegan un papel importante. Las lluvias intensas, especialmente durante la temporada de huracanes, incrementan el riesgo de accidentes. En 2023, el 15% de los accidentes ocurrieron durante condiciones meteorológicas adversas, lo que subraya la necesidad de adaptar las infraestructuras y prácticas de conducción a estos desafíos.")

    st.subheader("Impacto en la Sociedad: Consecuencias y Desafíos")
    st.write("El aumento en los accidentes de tránsito tiene un profundo impacto en la sociedad cubana. Las familias afectadas enfrentan pérdidas trágicas y una carga emocional considerable. Los costos asociados con el tratamiento de lesiones y la rehabilitación afectan a los hospitales y al sistema de salud en general. La Red de Hospitales de Cuba ha informado un aumento del 20% en la demanda de servicios de emergencia relacionados con accidentes de tránsito.")
    st.write("Económicamente, los daños a vehículos y propiedades, junto con la pérdida de productividad laboral, representan una carga adicional para el país. El impacto también se refleja en la presión sobre los recursos del estado y la necesidad de inversiones urgentes en infraestructura y programas de prevención.")
    data = pd.read_json('data/output6.json')

    df = pd.DataFrame(data)
    for col in df.columns[1:]:  
        if df[col].dtype == 'object':  
            df[col] = df[col].str.replace(',', '.').str.replace(' ', '').astype(float)
    fig = px.pie(df[:-1], names='Principales violaciones', values='Accidentes',
                title='Distribución de la Tasa de mortalidad de los tumores en el organismo (2022)',
                labels={'Tasa': 'Tasa de Mortalidad'},
                color_discrete_sequence=px.colors.sequential.Cividis)
    st.plotly_chart(fig)
    st.subheader("Iniciativas y Soluciones: Caminos hacia la Mejora")
    st.write("Reparación y Modernización de Infraestructura: El gobierno ha lanzado un plan para reparar y modernizar las carreteras críticas, con una inversión estimada de $100 millones en los próximos tres años. Este plan incluye la repavimentación de rutas clave, mejora de la señalización y el fortalecimiento de la iluminación en áreas de alto riesgo.")
    st.write("Educación y Conciencia Vial: Las autoridades están intensificando las campañas de educación vial, enfocándose en el respeto a las normas de tránsito y los peligros del consumo de alcohol. Las campañas se están llevando a cabo a través de medios de comunicación, escuelas y comunidades, con el objetivo de cambiar el comportamiento de los conductores y peatones.")
    st.write("Aplicación de la Ley y Control: El refuerzo de la aplicación de las leyes de tránsito es crucial. Se están implementando controles más estrictos y sanciones más severas para infracciones relacionadas con el exceso de velocidad y la conducción bajo el efecto del alcohol. Además, se está aumentando la presencia de patrullas de tránsito en áreas identificadas como de alto riesgo.")

    st.subheader("Consideraciones finales")
    st.write("La crisis de los accidentes de tránsito en Cuba es un desafío urgente que requiere una acción concertada y efectiva. Con la combinación de infraestructura deteriorada, vehículos obsoletos y comportamientos imprudentes, el camino hacia una mayor seguridad vial es complejo pero necesario. Las iniciativas actuales son un paso en la dirección correcta, pero el éxito dependerá de la colaboración continua entre el gobierno, la comunidad y los ciudadanos.")
    st.write("Garantizar carreteras más seguras es una responsabilidad compartida. Es esencial que todos los involucrados tomen medidas proactivas para proteger la vida y la seguridad en las carreteras cubanas. La urgencia de abordar esta crisis no puede ser subestimada, y es imperativo que se tomen medidas decisivas para revertir esta tendencia preocupante y asegurar un futuro más seguro para todos.")


    def likes():
        st.subheader("¿Te gusta este artículo?")
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("👍 Me gusta"):
                st.success("¡Gracias por tu feedback positivo!")

        with col2:
            if st.button("👎 No me gusta"):
                st.error("¡Gracias por tu feedback negativo!")

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

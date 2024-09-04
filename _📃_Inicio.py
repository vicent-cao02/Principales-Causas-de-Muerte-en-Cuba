import streamlit as st
import streamlit_analytics 
import json
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="La Mortalidad en Cuba",
    page_icon="📃",
)
with streamlit_analytics.track():
    st.markdown("""<h1 class=titulo>Impactos en la salud cubana</h1> <style> .titulo { font-size: 55px; text-align: center; } </style>""", unsafe_allow_html=True)

    st.subheader("La Mortalidad en Cuba: Un Estudio Revelador")
    st.write("Cuba, a pesar de su sistema de salud universal, enfrenta serios desafíos en mortalidad. Las principales causas de muerte incluyen enfermedades cardiovasculares, respiratorias, hepáticas y metabólicas, así como el cáncer. En 2021, el cáncer tuvo un aumento notable en las tasas de mortalidad, resaltando la necesidad de mejores estrategias de prevención y políticas de salud adaptadas. Además, el consumo de tabaco es un factor crítico que contribuye a muchas de estas enfermedades. Las visualizaciones interactivas ayudarán a explorar mejor estos comportamientos y entender cómo han cambiado con el tiempo.")
    st.subheader("Crisis en las Carreteras de Cuba: Un artículo sobre el Aumento de Accidentes de Tránsito.")
    st.write("Los accidentes de tránsito son una crisis creciente en Cuba. En 2022, hubo casi 10,000 accidentes, con 705 muertes y más de 7,500 heridos. La infraestructura deteriorada, vehículos obsoletos, comportamientos imprudentes y condiciones climáticas adversas son las principales causas. El gobierno está trabajando en reparar carreteras, modernizar la flota vehicular, y mejorar la educación vial para reducir estos incidentes. A pesar de los esfuerzos, se necesita una acción continua y efectiva para mejorar la seguridad vial.")
    st.subheader("COVID-19 en Cuba: Un Podcast sobre la Pandemia")
    st.write("La pandemia de COVID-19 tuvo un impacto profundo en Cuba, convirtiéndose en una de las principales causas de muerte en 2022. Cuba respondió con confinamientos estrictos, uso obligatorio de mascarillas y el desarrollo de vacunas propias como Soberana 02, Abdala y Soberana Plus. Gracias a una campaña de vacunación efectiva, más del 90% de la población ha recibido al menos una dosis, ayudando a reducir la mortalidad y hospitalizaciones. El esfuerzo para controlar la pandemia demuestra la capacidad de Cuba para enfrentar grandes desafíos con estrategias adaptadas a sus necesidades.")
    st.write("Estos temas reflejan aspectos cruciales de la realidad en Cuba, desde desafíos en salud pública y seguridad vial hasta la respuesta a una pandemia global. Esperamos que esta visión general les haya sido útil y les animamos a profundizar en cada uno de estos temas para entender mejor las complejidades y sus soluciones en Cuba.")
    
    st.markdown(
        """<h1 class = 'universidad'>Universidad de la Habana</h1> 
            <style>
                .universidad{
                font-size: 35px;
                text-align: center;
                }
            </style>""",
        unsafe_allow_html=True,
    )
    st.markdown(
        """<h2 class = 'facultad'>Facultad: MATCOM </h2> <style>
                .facultad{
                font-size: 25px;
                text-align: center;
                }
            </style>""",
        unsafe_allow_html=True,
    )
    st.markdown(
        """<h2 class = 'carrera'>Carrera: Ciencia de Datos</h2> <style>
                .carrera{
                font-size: 25px;
                text-align: center;
                }
            </style>""",
        unsafe_allow_html=True,
    )
    st.markdown(
        """<h3 class = 'nombre'>Vicente Cao Tarrero</h3> <style>
                .nombre{
                font-size: 35px;
                text-align: center;
                }
            </style>""",
        unsafe_allow_html=True)

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

import streamlit as st
import streamlit_analytics 
st.set_page_config(
    page_title="La Mortalidad en Cuba",
    page_icon="📃",
)
with streamlit_analytics.track():
    
    st.markdown(
        """<h2 class = 'texto1'>En un mundo donde la salud pública es fundamental, el estudio de las causas de mortalidad nos proporciona una ventana vital hacia el bienestar de nuestras comunidades. Este proyecto de ciencia de datos se sumerge en las principales causas de muertes, un tema de gran relevancia que merece ser explorado a fondo. A través de un análisis meticuloso y la presentación de datos, buscamos iluminar los factores que influyen en la salud de la población cubana. Esta investigación se compone de tres elementos claves:</h2> <style>
                .texto1{
                font-size: 20px;
                }
            </style>""",
        unsafe_allow_html=True,
    )
    st.markdown(
        """<h2 class = 'texto1'>Data Product lo cual va a permitir a los lectores explorar de manera dinámica las estadísticas sobre mortalidad en Cuba. Con un enfoque en la claridad y el entendimiento, hemos utilizado gráficos para ofrecer una representación visual, atractiva y accesible, facilitando asi el conocimiento sobre las causas que afectan a nuestra sociedad.</h2> <style>
                .texto1{
                font-size: 20px;
                }
            </style>""",
        unsafe_allow_html=True,
    )
    st.markdown(
        """<h2 class = 'texto1'>Informe sobre los accidentes de tránsito: por ser precisamente este tema una principal causa de mortalidad en el país, en el informe analizamos los comportamientos y estadísticas explorando factores como la infraestructura vial y las políticas de seguridad.</h2> <style>
                .texto1{
                font-size: 20px;
                }
            </style>""",
        unsafe_allow_html=True,
    )
    st.markdown(
        """<h2 class = 'texto1'>Podcast sobre la covid 19. La pandemia de covid 19 ha dejado una marca significativa en la mortalidad global y Cuba no ha sido la excepción. En el podcast proporcionamos un panorama exhaustivo sobre el impacto del virus en la salud cubana, mostrando no solo las cifras, sino también la resiliencia del sistema de salud y las lecciones aprendidas en un momento sin precedentes.</h2> <style>
                .texto1{
                font-size: 20px;
                }
            </style>""",
        unsafe_allow_html=True,
    )
    st.markdown(
        """<h2 class = 'texto1'>A través de este proyecto no solo pretendemos informar, sino también inspirar a una reflexión profunda sobre las políticas de salud pública y la importancia de su prevención. Esperamos que los hallazgos presentados, sirvan como un recurso valioso para investigadores, profesionales de la salud, estudiantes de la carrera y cualquier persona interesada en el bienestar de la población cubana.</h2> <style>
                .texto1{
                font-size: 20px;
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
                text-align: center
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
            submit_button = st.form_submit_button("Enviar  Comentario")

            if submit_button:
                if comment:
                    st.success("¡Gracias por tu comentario!")
                else:
                    st.error("Por favor, escribe un comentario antes de enviar.")

    comentarios()

import streamlit as st
import streamlit_analytics


st.set_page_config(
    page_title="La Mortalidad en Cuba",
    page_icon="🦠",
)
st.title("COVID-19 en Cuba: Un Podcast sobre la Pandemia")
st.write("Hola y bienvenidos a nuestro podcast. En este episódio vamos a examinar cómo la COVID-19 ha afectado a Cuba, desde los primeros casos hasta las medidas de control implementadas. También discutiremos los avances en vacunas desarrolladas localmente y cómo estas han jugado un papel crucial en la lucha contra la pandemia. ¡Quédense con nosotros para una visión completa de esta crisis global y sus repercusiones en nuestra isla!")
with streamlit_analytics.track():
    audio_file = "./data/Podcats.mp3"
    st.audio(audio_file, format="audio/mp3")
    
    def likes():
        st.subheader("¿Te gusta este podcast?")
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

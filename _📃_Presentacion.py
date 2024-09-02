import streamlit as st
import streamlit_analytics 
import json
import matplotlib.pyplot as plt

with streamlit_analytics.track():

    
    def main():
        st.title("Sistema de Retroalimentación")

        # Crear botones para pulgar arriba y abajo
        st.subheader("¿Te gusta esta aplicación?")
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("👍 Me gusta"):
                st.success("¡Gracias por tu feedback positivo!")

        with col2:
            if st.button("👎 No me gusta"):
                st.error("¡Gracias por tu feedback negativo!")

    if __name__ == "__main__":
        main()
    def main():
        with st.form(key='comment_form'):
            comment = st.text_area("Escribe tu comentario:")
            submit_button = st.form_submit_button("Enviar Comentario")

            if submit_button:
                if comment:
                    st.success("¡Gracias por tu comentario!")
                else:
                    st.error("Por favor, escribe un comentario antes de enviar.")

    if __name__ == "__main__":
        main()

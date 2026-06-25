import streamlit as st
import random
import time


numeri_possibili = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

if "segreto" not in st.session_state:
    st.session_state.segreto = random.randint(1, 15)


st.title("Indovina il numero (da 1 a 15)")

risposta = st.selectbox("NUMERO SEGRETO:", numeri_possibili, index=None, placeholder="Scegli il numero...")

if risposta is not None:

    if risposta == st.session_state.segreto:

        st.success(f"Indovinato! Il numero era proprio {st.session_state.segreto}")
        st.balloons()

        time.sleep(3.0)

        del st.session_state.segreto

        st.rerun()

    elif risposta > st.session_state.segreto:

        st.write("Un po' di meno")

    elif risposta < st.session_state.segreto:

        st.write("Un po' di più")




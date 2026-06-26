import streamlit as st
import random
import time


numeri_possibili = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]

if "segreto" not in st.session_state:
    st.session_state.segreto = random.randint(1, 50)


st.title("Indovina il numero (da 1 a 100)")

risposta = st.selectbox("NUMERO SEGRETO:", numeri_possibili, index=None, placeholder="Scegli il numero...", key=st.session_state.segreto)

if risposta is not None:

    if risposta == st.session_state.segreto:

        st.success(f"Indovinato! Il numero era proprio {st.session_state.segreto}")
        st.balloons()

        time.sleep(3.0)

        st.session_state.clear()

        st.rerun()

    elif risposta > st.session_state.segreto:

        st.write("Un po' di meno")

    elif risposta < st.session_state.segreto:

        st.write("Un po' di più")




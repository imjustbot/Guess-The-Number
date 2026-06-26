import streamlit as st
import random
import time


numeri_possibili = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]

if "segreto" not in st.session_state:
    st.session_state.segreto = random.randint(1, 50)


st.title("Indovina il numero (da 1 a 50)")

risposta = st.selectbox("NUMERO SEGRETO:", numeri_possibili, index=None, placeholder="Scegli il numero...", key=st.session_state.segreto)

if st.session_state.segreto == 1:
    st.write("Il numero è dispari")

elif st.session_state.segreto == 2:
    st.write("Il numero è pari")

elif st.session_state.segreto == 3:
    st.write("Il numero è dispari")

elif st.session_state.segreto == 4:
    st.write("Il numero è pari")

elif st.session_state.segreto == 5:
    st.write("Il numero è dispari")

elif st.session_state.segreto == 6:
    st.write("Il numero è pari")

elif st.session_state.segreto == 7:
    st.write("Il numero è dispari")

elif st.session_state.segreto == 8:
    st.write("Il numero è pari")

elif st.session_state.segreto == 9:
    st.write("Il numero è dispari")

elif st.session_state.segreto == 10:
    st.write("Il numero è pari")

elif st.session_state.segreto == 11:
    st.write("Il numero è dispari")

elif st.session_state.segreto == 12:
    st.write("Il numero è pari")

elif st.session_state.segreto == 13:
    st.write("Il numero è dispari")

elif st.session_state.segreto == 14:
    st.write("Il numero è pari")

elif st.session_state.segreto == 15:
    st.write("Il numero è dispari")

elif st.session_state.segreto == 16:
    st.write("Il numero è pari")

elif st.session_state.segreto == 17:
    st.write("Il numero è dispari")

elif st.session_state.segreto == 18:
    st.write("Il numero è pari")

elif st.session_state.segreto == 19:
    st.write("Il numero è dispari")

elif st.session_state.segreto == 20:
    st.write("Il numero è pari")

elif st.session_state.segreto == 21:
    st.write("Il numero è dispari")

elif st.session_state.segreto == 22:
    st.write("Il numero è pari")

elif st.session_state.segreto == 23:
    st.write("Il numero è dispari")

elif st.session_state.segreto == 24:
    st.write("Il numero è pari")

elif st.session_state.segreto == 25:
    st.write("Il numero è dispari")

elif st.session_state.segreto == 26:
    st.write("Il numero è pari")

elif st.session_state.segreto == 27:
    st.write("Il numero è dispari")

elif st.session_state.segreto == 28:
    st.write("Il numero è pari")

elif st.session_state.segreto == 29:
    st.write("Il numero è dispari")

elif st.session_state.segreto == 30:
    st.write("Il numero è pari")

elif st.session_state.segreto == 31:
    st.write("Il numero è dispari")

elif st.session_state.segreto == 32:
    st.write("Il numero è pari")

elif st.session_state.segreto == 33:
    st.write("Il numero è dispari")

elif st.session_state.segreto == 34:
    st.write("Il numero è pari")

elif st.session_state.segreto == 35:
    st.write("Il numero è dispari")

elif st.session_state.segreto == 36:
    st.write("Il numero è pari")

elif st.session_state.segreto == 37:
    st.write("Il numero è dispari")

elif st.session_state.segreto == 38:
    st.write("Il numero è pari")

elif st.session_state.segreto == 39:
    st.write("Il numero è dispari")

elif st.session_state.segreto == 40:
    st.write("Il numero è pari")

elif st.session_state.segreto == 41:
    st.write("Il numero è dispari")

elif st.session_state.segreto == 42:
    st.write("Il numero è pari")

elif st.session_state.segreto == 43:
    st.write("Il numero è dispari")

elif st.session_state.segreto == 44:
    st.write("Il numero è pari")

elif st.session_state.segreto == 45:
    st.write("Il numero è dispari")

elif st.session_state.segreto == 46:
    st.write("Il numero è pari")

elif st.session_state.segreto == 47:
    st.write("Il numero è dispari")

elif st.session_state.segreto == 48:
    st.write("Il numero è pari")

elif st.session_state.segreto == 49:
    st.write("Il numero è dispari")

elif st.session_state.segreto == 50:
    st.write("Il numero è pari")



if risposta is not None:

    if risposta == st.session_state.segreto:

        st.success(f"Indovinato! Il numero era proprio {st.session_state.segreto}")
        st.balloons()

        time.sleep(3.0)

        st.session_state.clear()

        st.rerun()

    elif st.session_state.segreto > risposta:
        
        diffinpiù = abs(st.session_state.segreto - risposta)

        if diffinpiù <= 5:

            st.write("Ci sei quasi!")

        elif diffinpiù >= 6 and diffinpiù <= 20:

            st.write("Un po' di più")

        elif diffinpiù >= 21:

            st.write("Di più")

    elif risposta > st.session_state.segreto:

        diffinmeno = abs(risposta - st.session_state.segreto)

        if diffinmeno <= 5:

            st.write("Ci sei quasi!")

        elif diffinmeno >= 6 and diffinmeno <= 20:

            st.write("Un po' di meno")

        elif diffinmeno >= 21:

            st.write("Di meno")

    







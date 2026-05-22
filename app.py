import streamlit as st
import pandas as pd
import time
st.title ("Mon App streamlit")

col1,col2,col3= st.columns
with col1:
    st.header("Colonne 1")
    st.write("Contenu de la colonne 1")
with col2:
    st.header("Colonne 2")  
    st.write("Contenu de la colonne 2")
with col3:
    st.header("Colonne 3")
    st.write("Contenu de la colonne 3")

with st.sidebar:
    Option= st.selectbox("Choisir un page", ["Acceuil","A propos", "Contacts"])

data = [1,2,7,9,3]
tab1,tab2=st.tabs(["Grapghique","Données"])
with tab1:
    st.line_chart(data)
with tab2:
    st.dataframe(data)

with st.expander("Voir les details"):
    st.write("Entrer les details ...")
    st.code("print('Exemple')")
#Autres conteneur
#st.container
with st.container():
    st.header("Zone d'informations")
    st.write("Ce bloc regroupe plusieurs éléments")
#st.empty
placeholder=st.empty()
placeholder.Info('En attente ...')
#st.form
with st.form("Formulaire"):
    nom=st.text_input("Votre nom")
    age=st.number_input("Votre age",min_value=10,max_value=80)
    submit=st.form_submit_button("Envoyer")
    if submit:
        placeholder.warning("Traitement en cours...")
        time.sleep(2)
        placeholder.success(f"Bienvenu {nom}, vous avez {age} ans.")
df=pd.DataFrame({
    "Mois":["Jan","Fev","Mar","Avr","Mai"],
    "Ventes":[120,150,170,140,200]
})

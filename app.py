# HYGIENE_UPAC_CURIE_IA
import streamlit as st
import datetime
from PIL import Image

st.set_page_config(page_title="Recensement Pétri", page_icon="🧫")

if "historique" not in st.session_state:
    st.session_state.historique = []

st.title("🧫 Recensement des Boîtes de Petri")

col1, col2 = st.columns([1, 1])

with col1:
    st.header("📸 Scanner une boîte")
    uploaded_file = st.file_uploader("Glissez une photo ici...", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Photo reçue", use_container_width=True)
        
        if st.button("Lancer la détection AI 🚀"):
            nom_boite = f"Boîte-{len(st.session_state.historique) + 1}"
            date_actuelle = datetime.datetime.now().strftime("%d/%m/%Y à %H:%M")
            
            st.session_state.historique.append({
                "Identifiant": nom_boite,
                "Date": date_actuelle,
                "Statut": "Détectée ✅"
            })
            st.success(f"{nom_boite} enregistrée !")

with col2:
    st.header("📊 Historique")
    if not st.session_state.historique:
        st.info("Aucune boîte pour le moment.")
    else:
        st.dataframe(st.session_state.historique)

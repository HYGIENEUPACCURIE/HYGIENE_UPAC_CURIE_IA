import streamlit as st

# Configuration de la page principale
st.set_page_config(page_title="Hygène UPAC - IA Curie", page_icon="🧫", layout="wide")

# Titre Principal du Tableau de bord
st.title("🧫 Tableau de Bord - Suivi des Prélèvements")
st.markdown("Bienvenue sur l'application de recensement et d'analyse IA de l'UPAC Curie.")

st.divider()

# Chiffres clés (Simulés pour le moment)
col1, col2, col3, col4 = st.columns(4)
col1.metric(label="Total Boîtes Recensées", value="0")
col2.metric(label="Boîtes Positives (24h)", value="0")
col3.metric(label="Prélèvements aujourd'hui", value="0")
col4.metric(label="Précision actuelle de l'IA", value="-- %")

st.divider()

st.subheader("📋 Derniers prélèvements enregistrés")
st.info("Utilisez le menu latéral à gauche pour naviguer entre les différentes rubriques de votre application.")

import streamlit as st
import qrcode
from io import BytesIO
import datetime

st.set_page_config(page_title="Routine & QR Code", page_icon="📝", layout="wide")

st.title("📝 Création de la Routine & Génération de QR Codes")
st.markdown("Configurez votre session de prélèvement pour générer l'identifiant unique et le QR Code de la boîte.")

st.divider()

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("⚙️ Paramètres du prélèvement")
    
    # 1. Sélection de la ZONE
    zone_choisie = st.selectbox(
        "1. Sélectionnez la zone :",
        ["ZAC", "M4", "M5", "M6", "M7", "M10", "M11"]
    )
    
    # 2. Sélection du LIEU (Provisoire en attendant vos données de demain)
    lieu_choisi = st.selectbox(
        "2. Sélectionnez le lieu de prélèvement :",
        ["Sol", "Surface de travail", "Air ambiant", "Main opérateur", "Autre"]
    )
    
    # 3. NOUVEAU : Sélection du type de gélose / prélèvement
    type_gelose = st.selectbox(
        "3. Sélectionnez le type de gélose / prélèvement :",
        ["Écouvillon", "35 mm", "55 mm"]
    )
    
    # 4. Sélection de la date
    date_prelevement = st.date_input("4. Date du prélèvement :", datetime.date.today())
    
    # --- PRÉPARATION DES CODES POUR L'ID UNIQUE ---
    date_str = date_prelevement.strftime("%Y%m%d")
    lieu_clean = "".join(e for e in lieu_choisi if e.isalnum())[:4].upper()
    
    # Formatage propre du type de gélose pour l'ID (ex: ECOU, 35MM, 55MM)
    if "couvillon" in type_gelose.lower():
        gelose_code = "ECOU"
    else:
        gelose_code = type_gelose.replace(" ", "").upper()
    
    # --- CONSTRUCTION DE L'IDENTIFIANT UNIQUE ---
    id_unique = f"UPAC-{zone_choisie}-{date_str}-{lieu_clean}-{gelose_code}"
    
    st.info(f"**Identifiant unique généré :** `{id_unique}`")
    
    st.divider()
    
    # NOUVEAU : Bouton Enregistrer
    if st.button("💾 Enregistrer le prélèvement dans la base", variant="primary"):
        # Pour l'instant, on affiche une confirmation visuelle. 
        # Dès que notre base de données sera connectée, ce bouton l'écrira pour de vrai !
        st.success(f"✅ Le prélèvement `{id_unique}` a été enregistré avec succès dans le système !")

with col2:
    st.subheader("🔲 QR Code de traçabilité")
    
    # Génération du QR code basé sur le nouvel ID complet
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(id_unique)
    qr.make(fit=True)
    img_qr = qr.make_image(fill_color="black", back_color="white")
    
    buf = BytesIO()
    img_qr.save(buf, format="PNG")
    byte_im = buf.getvalue()
    
    st.image(byte_im, caption=f"QR Code pour {id_unique}", width=250)
    
    st.download_button(
        label="📥 Télécharger le QR Code (PNG)",
        data=byte_im,
        file_name=f"QR_{id_unique}.png",
        mime="image/png"
    )

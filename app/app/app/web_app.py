import streamlit as st
from youtube_extractor import get_transcript


def classify_content(text):
    sexual_keywords = ["kiss", "sex", "naked", "flirt"]
    violence_keywords = ["fight", "kill", "punch"]
    bad_words = ["fuck", "shit"]

    score = 0
    reasons = []

    for word in sexual_keywords:
        if word in text.lower():
            score += 2
            reasons.append(f"sexual/suggestive keyword detected: {word}")

    for word in violence_keywords:
        if word in text.lower():
            score += 2
            reasons.append(f"violence keyword detected: {word}")

    for word in bad_words:
        if word in text.lower():
            score += 1
            reasons.append(f"explicit language detected: {word}")

    if score >= 5:
        rating = "18+"
    elif score >= 3:
        rating = "16+"
    elif score >= 1:
        rating = "13+"
    else:
        rating = "7+"

    return rating, reasons


st.title("Age Content Classifier")
st.write("Analyse un lien YouTube et propose une catégorie d’âge.")

url = st.text_input("Colle un lien YouTube ici :")

if st.button("Analyser"):
    if url:
        try:
            transcript = get_transcript(url)
            rating, reasons = classify_content(transcript)

            st.subheader("Résultat")
            st.write("Catégorie d’âge proposée :", rating)

            st.subheader("Raisons")
            if reasons:
                for reason in reasons:
                    st.write("-", reason)
            else:
                st.write("Aucun signal sensible détecté.")
        except Exception as e:
            st.error(f"Erreur : {e}")
    else:
        st.warning("Veuillez entrer un lien YouTube.")

from craiyon import Craiyon
from PIL import Image 
from io import BytesIO
import streamlit as st
import translators.server as tts
from streamlit_disqus import st_disqus
import base64

def Generate(request):
	try:
		generator = Craiyon()
		result = generator.generate(request) 
		images = result.images
		return images
	except:
		return "Error"

generator = Craiyon()

st.set_page_config(layout="wide")

st.markdown("<center><h1>🤖Genera Immagini uniche con l'I.A.📸<small><br> Powered by INTELLIGENZAARTIFICIALEITALIA.NET </small></h1>", unsafe_allow_html=True)
st.write('<p style="text-align: center;font-size:15px;" > <bold>Divertiti a generare immagini uniche e irrecreabili, il tutto gratis, online e utilizzando input direttamente in italiano. Il tuo unico limite è la fantasia </bold><p><br>', unsafe_allow_html=True)

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            .css-12oz5g7 {
		    flex: 1 1 0%;
		    width: 100%;
		    padding: 0.3rem;
		    max-width: 46rem;
            }
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)


request = st.text_input("Sono in grado di disegnare tutto ciò che vuoi, se non ci credi provami🖌🤖","Un leone che suona il violino")

with st.expander("Esempi di input da dare 🎨"):
	st.markdown("🤖Esempi : \n- Una bicletta sulla Luna \n- Un gatto che gioca a calcio \n- Una mela dentro una galassia \n- Una borsa Rossa per eventi eleganti  \n- Un leone che suona il violino  \n- Un'auto che corre su una strada di ghiaccio  \n- Un topo che gioca a golf  \n- Un computer che dipinge quadri  \n- Una farfalla che gioca a scacchi  \n- Un uomo che cammina su un tappeto volante  \n 🤗 Non scordati di condividere gli output e il nostro sito con i tuoi amici o colleghi 🤗")

with st.expander("Consigli per ottenere risultati migliori 🎨"):
	st.markdown("🤖Consigli : \n- Usa parole chiave per ottenere risultati migliori \
		\n- Inserisci la parolola 'Foto' per immagini simili a Foto \
		\n- Inserisci la parolola 'Foto 4K HD' per simili a Foto di alta qualità \
		\n- Inserisci la parolola 'Disegno' per immagini simili a disegni \
		\n- inserisci la parolola 'Design' per immagini simili a disegni di design \
		\n- Inserisci la parolola 'Illustrazione' per immagini simili a illustrazioni \
		\n- Inserisci la parolola 'Logo' per immagini simili a loghi \
		\n- Inserisci la parolola 'Cartoon' per immagini simili a cartoni animati \
		\n- Inserisci la parolola 'Animazione' per immagini simili a animazioni \
		\n- Inserisci la parolola '3d' per immagini simili a 3d \
		\n- Inserisci la parolola 'Grafica' per immagini simili a grafica \
		\n 🤗 Non scordati di condividere gli output e il nostro sito con i tuoi amici o colleghi 🤗")

cola , colb, colc = st.columns(3)


if colb.button("Disegna le mie immagini 🖌"):
	with st.spinner("🧑‍🎨 Attendi un attimo ⏳ stiamo rapendo diversi artisti... ( circa 40 secondi ) 🧑‍🎨"):
		new_request = tts.google(request, from_language="it", to_language="en")
		image_files = Generate(new_request)
		if image_files != "Error":
			col1, col2, col3 = st.columns(3)
			with col1:
				st.image(Image.open(BytesIO(base64.decodebytes(image_files[0].encode("utf-8")))))
				st.image(Image.open(BytesIO(base64.decodebytes(image_files[1].encode("utf-8")))))
				st.image(Image.open(BytesIO(base64.decodebytes(image_files[2].encode("utf-8")))))
			with col2:
				st.image(Image.open(BytesIO(base64.decodebytes(image_files[3].encode("utf-8")))))
				st.image(Image.open(BytesIO(base64.decodebytes(image_files[4].encode("utf-8")))))
				st.image(Image.open(BytesIO(base64.decodebytes(image_files[5].encode("utf-8")))))
			with col3:
				st.image(Image.open(BytesIO(base64.decodebytes(image_files[6].encode("utf-8")))))
				st.image(Image.open(BytesIO(base64.decodebytes(image_files[7].encode("utf-8")))))
				st.image(Image.open(BytesIO(base64.decodebytes(image_files[8].encode("utf-8")))))
			st.balloons()
			st.info(" ☑️ Per scaricare le immagini clicca con il tasto destro del mouse e seleziona 'Salva immagine come...' ")
			st.success("🤖 Ecco le tue immagini, non sono meravigliose? ")
			st.warning("🤖 Se non ti piacciono, prova a cambiare input ")

		else:
			st.error("🤖Sembra che ci sia stato un errore, riprova più tardi🤖")

st_disqus("Condividi-le-immagini")
st.caption(" [© Intelligenza Artificiale Italia](https://www.intelligenzaartificialeitalia.net/)")

from craiyon import Craiyon
from PIL import Image 
from io import BytesIO
import streamlit as st
import translators.server as tts
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
	st.markdown("🤖Esempi : \n- Una bicletta sulla Luna \n- Un gatto che gioca a calcio \n- Una mela dentro una galassia \n- Una borsa Rossa per eventi eleganti  \n-Un leone che suona il violino  \n-Un'auto che corre su una strada di ghiaccio  \n-Un topo che gioca a golf  \n-Un computer che dipinge quadri  \n-Una farfalla che gioca a scacchi  \n-Un uomo che cammina su un tappeto volante  \n 🤗 Non scordati di condividere gli output e il nostro sito con i tuoi amici o colleghi 🤗")

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
			#appendi il nuovo input nel file input.txt
			with open("input.txt", "a") as file:
				file.write(new_request+"\n")
		else:
			st.error("🤖Sembra che ci sia stato un errore, riprova più tardi🤖")

with st.expander("👨‍👨‍👦‍👦 Lasciati ispirare dagli altri utenti"):
	#leggi il file input.txt riga per riga e fai un markdown 
	st.text("👨‍👨‍👦‍👦 Ecco alcuni esempi di input che altri utenti hanno dato:")
	with open("input.txt", "r") as file:
		for line in file:
			st.markdown("\n- "+line)
st.caption(" [© Intelligenza Artificiale Italia](https://www.intelligenzaartificialeitalia.net/)")

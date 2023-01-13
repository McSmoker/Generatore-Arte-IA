from craiyon import Craiyon
from PIL import Image 
from io import BytesIO
import streamlit as st
import translators.server as tts
import base64
def Generate(request):
    generator = Craiyon()
    result = generator.generate(request) 
    images = result.images
    return images

generator = Craiyon()
st.title("🤖Genera Immagini uniche con l' I.A.📸")

st.set_page_config(page_title="Genera Immagini uniche online by I.A. Italia", page_icon="📈")

st.markdown("<center><h1>🤖Genera Immagini uniche con l'I.A.📸<small><br> Powered by INTELLIGENZAARTIFICIALEITALIA.NET </small></h1>", unsafe_allow_html=True)
st.write('<p style="text-align: center;font-size:15px;" > <bold>Divertiti a generare immagini uniche e irrecreabili, il tutto gratis, online e utilizzando input direttamente in italiano.<bold>  </bold><p><br>', unsafe_allow_html=True)

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

request = st.text_input("Sono in grado di disegnare tutto ciò che vuoi, se non ci credi provami🖌🤖","Dimmi solo cosa disegnare e lo  farò!")
cola , colb, colc = st.columns(3)

if colb.button("Disegna le mie immagini 🖌"):
	with st.spinner("🧑‍🎨 Attendi un attimo stiamo rapendo diversi artisti... ( circa 40 secondi ) 🧑‍🎨"):
		new_request = tts.google(request, from_language="it", to_language="en")
		image_files = Generate(new_request)
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


st.caption(" [© Intelligenza Artificiale Italia](https://www.intelligenzaartificialeitalia.net/)")

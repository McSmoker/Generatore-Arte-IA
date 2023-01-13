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
st.title("Genera Immagini con l'IA")
st.header("Metti alla prova la mia IA generando immagini")
request = st.text_input("Sono in grado di disegnare tutto. Vuoi mettermi alla prova?","Dimmi solo cosa disegnare e lo farò!")
if st.button("Disegna le mie immagini"):
	with st.spinner("Attendi un attimo stiamo rapendo diversi artisti.."):
		new_request = tts.google(request, from_language="it", to_language="en")
		st.text("italiano : " + request + "\ninglese : " + new_request)
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

import streamlit as st
import PIL.Image
import spacy
from streamlit_option_menu import option_menu
from streamlit_extras.let_it_rain import rain
import whisper
from tempfile import NamedTemporaryFile





st.set_page_config(
    page_title="Herramientas AI - Qüid Lab",
    page_icon="random",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Parametros NLP
#nlp = spacy.load("en_core_web_lg")
nlp = spacy.load("en_core_web_sm")




# Funciones
def success():
	rain(
		emoji="🎈",
		font_size=54,
		falling_speed=5,
		animation_length=1, #'infinite'
	)





def adivinar_prompt(prompt_adivinado, prompt_real):
    frase1 = prompt_adivinado
    frase2 = prompt_real
    fra1 = nlp(frase1)
    fra2 = nlp(frase2)
    similitud_frases = fra1.similarity(fra2)
    puntaje_actual = similitud_frases
    return puntaje_actual


# Logo sidebar
image = PIL.Image.open('logo_blanco.png')
st.sidebar.image(image, width=None, use_column_width=None)

with st.sidebar:
    selected = option_menu(
        menu_title="Selecciona",  # required
        options=["Home", "Iniciar", "Créditos"],  # required
        icons=["house", "caret-right-fill", "caret-right-fill","caret-right-fill",
                        "caret-right-fill", "envelope"],  # optional
        menu_icon="upc-scan",  # optional
        default_index=0,  # optional
    )



if selected == "Home":
	st.title("Experimenta con IA - Pasando de audio a texto")
	st.write("Esta herramienta te permitirá experimentar con IA haciendo uso de un modelo que convierte de audio a texto.\n \n Recuerda que puedes transcribir máximo audios de 3 minutos y/o 2MB de tamaño.\n\n\n\n")
	st.write(' ')
	st.write("**Instrucciones:** \n ")
	"""
	* Selecciona iniciar en el menú de la izquierda.
	* Selecciona el botón "Browse files" para cargar un archivo de audio que se recomienda sea en formato .mp3 (máximo 2MB/3 minutos)
    * Se cargará el audio y podrás escucharlo haciendo clic en el botón "play"
	* Selecciona el botón "Transcribir audio" para iniciar la transcripción. Se demorará unos minutos dependiendo de la longitud del audio.
	* Espera a que salga el mensaje "Modelo cargado" esto indicará que ya se cargó el modelo de IA y que se está procesando tu audio
	* Al terminar de procesar saldrán 2 cosas:
		* Botón para descargar la transcripción: si haces clic se generará un archivo de texto en formato .txt
		* Texto de la transcripción: recuerda revisar qué tal funcionó, puede que tengas que mejorar la grabación para que el modelo pueda reconocer mejor las palabras.
	* Recuerda que estas experimentando y lo importante más que el resultado es reconocer las ventajas de la IA 

	

	\n \n \n NOTA: Esta herramienta es un demo experimental y está sujeta a la demanda de uso. 

	"""


if selected == "Iniciar":
		st.title(f"Herramienta para la transcripción de audio")
		audio_file = st.file_uploader("Subir audio de máximo 3 minutos", type=["wav", "mp3", "m4a"])
		st.audio(audio_file)
		if st.button("Transcribir audio"):
			if audio_file is not None:
				model=whisper.load_model("base")
				st.success("Modelo cargado")

				with NamedTemporaryFile(suffix="mp3", delete=False) as temp:
					temp.write(audio_file.getvalue())
					temp.seek(0)
					model = whisper.load_model("base")
					result = model.transcribe(temp.name, fp16=False)
					st.success("Transcripción completada")
					st.download_button('Descargar archivo de texto .txt con la transcripción', result["text"], file_name='transcripcion.txt')
					st.write(result["text"])


			else:
				st.error("Por favor subir el archivo de audio")




if selected == "Créditos":
	st.title(f"Seleccionaste la opción {selected}")
	st.write(' ')
	st.write(' ')
	st.subheader("Qüid Lab")
	body = '<a href="https://www.quidlab.co">https://www.quidlab.co</a>'
	linkedin = 'Linkedin: <a href="https://www.linkedin.com/in/jorgecif/">https://www.linkedin.com/in/jorgecif/</a>' 
	twitter = 'Twitter (X): <a href="https://twitter.com/jorgecif/">https://twitter.com/jorgecif/</a>' 
	st.markdown(body, unsafe_allow_html=True)
	st.write('Creado por: *Jorge O. Cifuentes* :fleur_de_lis:')
	st.markdown(linkedin, unsafe_allow_html=True)
	st.markdown(twitter, unsafe_allow_html=True)

	st.write('Email: *jorge@quidlab.co* ')
	st.write("Quid Lab AI tools")
	st.write("Version 1.0")
	st.text("")








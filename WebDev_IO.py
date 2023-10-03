import streamlit as st
import streamlit.components.v1 as components
import random
from audiorecorder import audiorecorder
# from selenium import webdriver
# from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup
from playsound import playsound
import speech_recognition as sr
from deep_translator import GoogleTranslator
from streamlit_option_menu import option_menu
from gtts import gTTS
import os
#import wikipedia
from streamlit_chat import message
import requests
import bs4
import base64
from langdetect import detect
import toml
flag = 0

st.set_page_config(
    page_title="Memories",
	# Toggle sidebar state between 'expanded' and 'collapsed'.
    initial_sidebar_state="expanded",
    page_icon="🎙️",
)
# Hide Streamlit footer
hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# def get_LinkYT_lama(cari_pidio):
# 	driver = webdriver.Chrome()
# 	driver.implicitly_wait(5)

# 	#search_query = input().split()
# 	search_query = cari_pidio.split(	)
# 	print(search_query)
# 	final_query = ''
# 	link = []
# 	for word in search_query:
# 		final_query += word + "+"
		
# 	driver.get('https://www.youtube.com/results?search_query={}'.format(final_query))
# 	select = driver.find_element(By.CSS_SELECTOR, 'div#contents ytd-item-section-renderer>div#contents a#thumbnail')
# 	link += [select.get_attribute('href')]

# 	print(link)
# 	linked = link[0]
# 	try:
# 		linked = linked.split("/")[4]
# 	except :
# 		linked = linked.split("/")[3]
# 		linked = linked.split("=",1)[1]
# 		linked = linked.split("&",1)[0]
# 	linked = "https://www.youtube.com/embed/" + linked
# 	print(linked)

# 	return linked

def get_LinkYT(cari_pidio):
	from youtube_search import YoutubeSearch
	results = YoutubeSearch(cari_pidio, max_results=1).to_dict()
	for v in results:
		print('https://www.youtube.com' + v['url_suffix'])
		linked = 'https://www.youtube.com' + v['url_suffix']

	try:
		linked = linked.split("/")[4]
	except :
		linked = linked.split("/")[3]
		linked = linked.split("=",1)[1]
		linked = linked.split("&",1)[0]

	print(linked)
	linked = "https://www.youtube.com/embed/" + linked
	print(linked)

	return linked

def get_LinkFirstImage(cari_poto):
	word = cari_poto
	url = 'https://www.google.com/search?q={0}&tbm=isch'.format(word)
	content = requests.get(url).content
	soup = BeautifulSoup(content,'lxml')
	images = soup.findAll('img')

	print(images[1].get('src'))
	return images[1].get('src')


st.markdown("<h1 style='text-align: center; color: grey;'>Memories</h1>", unsafe_allow_html=True)

st.markdown("<h3 style='text-align: center; color: grey;'><br></h1>", unsafe_allow_html=True)
#st.write("""
# Memories
#""")
#st.title("Anggap aja chat")






from streamlit_custom_notification_box import custom_notification_box

styles = {'material-icons':{'color': 'red'},
		'text-icon-link-close-container': {'box-shadow': '#3896de 0px 4px'},
		'notification-text': {'':''},
		'close-button':{'':''},
		'link':{'':''}}



#with st.container():
# input_user = ''
# input_user = st.text_input("User Input:", on_change=on_input_change, key="user_input")
# if input_user != '':
# 	message(input_user)
####################################
query = ''
			
def chatgpt4free(pencarian):
	import os
	import sys
	sys.path.append(os.path.join(os.path.dirname(__file__), os.path.pardir))
	import streamlit as st
	#from gpt4free import you,deepai
	def get_answer(question: str) -> str:
		# Set cloudflare clearance cookie and get answer from GPT-4 model
		try:
			openai.api_key = open("key.txt", "r").read().strip("\n")
			messages = [ {"role": "system", "content": "Jadilah pemandu museum, kamu dikenal sebagai mories, kamu sangat mengerti tentang museum terutama museum konferensi asia afrika (KAA) apabila diluar konteks tersebut kamu akan menjawabnya dengan 'Maaf Mories belum bisa menjawab' disertai alasannya. Usahakan menjawab sebisanya sebagai guru kepada muridnya dengan waktu 30 detik, jika tidak cukup jawab seringkas mungkin dan memberikan saran menanyakan bagian spesifik"}, ]
			#while True:
			#message = input("User : ")
			message = question  
			if message:
			    messages.append(
				{"role": "user", "content": message},
			    )
			    chat = openai.ChatCompletion.create(
				model="gpt-3.5-turbo", messages=messages
			    )
			reply = chat.choices[0].message.content
			print(f"ChatGPT: {reply}")
			messages.append({"role": "assistant", "content": reply})
			return reply

		except Exception as e:
			# Return error message if an exception occurs
			return (
				f'An error occurred: {e}. Please make sure you are using a valid cloudflare clearance token and user agent.'
			)

	answer = get_answer(pencarian)
	escaped = answer.encode('utf-8').decode('unicode-escape')
	while '[[' in escaped:
		link = find_between(escaped,'[[',')')
		escaped = escaped.replace('[['+link+')','')
	return escaped

def chatgpt4free_Lama(pencarian):
	import os
	import sys
	sys.path.append(os.path.join(os.path.dirname(__file__), os.path.pardir))
	import streamlit as st
	#from gpt4free import you,deepai
	def get_answer(question: str) -> str:
		# Set cloudflare clearance cookie and get answer from GPT-4 model
		try:
			result = ''
			import g4f
			message = [
				#{"role": "system", "content": "Act as Museum Guide dan namamu adalah is Mories. Museum ini adalah museum konferensi asia afrika. Perkenalkan dirimu sebelum menjawab.Jika pertanyaan keluar dari tema konferensi asia afrika jawab dengan maaf mories belum bisa bantu jawab dan jangan jawab pertanyaan itu. Jika masih berhubungan dengan museum jawablah seperti guru mengajar muridnya"},
				{"role": "system", "content": "Jadilah pemandu museum, kamu dikenal sebagai mories, kamu sangat mengerti tentang museum terutama museum konferensi asia afrika (KAA) apabila diluar konteks tersebut kamu akan menjawabnya dengan 'Maaf Mories belum bisa menjawab' disertai alasannya. Usahakan menjawab sebisanya sebagai guru kepada muridnya dengan waktu 30 detik, jika tidak cukup jawab seringkas mungkin dan memberikan saran menanyakan bagian spesifik"},
				{"role": "user", "content": question}
				]
			response = g4f.ChatCompletion.create(
					model="gpt-3.5-turbo",
					provider=g4f.Provider.DeepAi,
					#messages=[{"role": "user", "content": "Apa itu lumba lumba"}],
					messages=message,
					stream=True,
				)
			for message in response:
				result = result + message
			print(result)
			return result

		except Exception as e:
			# Return error message if an exception occurs
			return (
				f'An error occurred: {e}. Please make sure you are using a valid cloudflare clearance token and user agent.'
			)

	answer = get_answer(pencarian)
	escaped = answer.encode('utf-8').decode('unicode-escape')
	while '[[' in escaped:
		link = find_between(escaped,'[[',')')
		escaped = escaped.replace('[['+link+')','')
	return escaped

def gpt5(pencarian):
	import os
	import sys
	sys.path.append(os.path.join(os.path.dirname(__file__), os.path.pardir))
	import streamlit as st
	#from gpt4free import you,deepai
	def get_answer(question: str) -> str:
		# Set cloudflare clearance cookie and get answer from GPT-4 model
		try:
			messages = [ {"role": "system", "content": 
		                    "Perkenalkan dirimu dengan nama lisa."} ]
		        #while True:
		        #message = input("User : ")
		        message = question  
		        if message:
		            messages.append(
		                {"role": "user", "content": message},
		            )
		            chat = openai.ChatCompletion.create(
		                model="gpt-3.5-turbo", messages=messages
		            )
		        reply = chat.choices[0].message.content
		        print(f"ChatGPT: {reply}")
		        messages.append({"role": "assistant", "content": reply})
		        return reply

		except Exception as e:
			# Return error message if an exception occurs
			return (
				f'An error occurred: {e}. Please make sure you are using a valid cloudflare clearance token and user agent.'
			)

	answer = get_answer(pencarian)
	escaped = answer.encode('utf-8').decode('unicode-escape')
	while '[[' in escaped:
		link = find_between(escaped,'[[',')')
		escaped = escaped.replace('[['+link+')','')
	return escaped


def scrap_Lama(pencarian):
	text= pencarian
	url = 'https://google.com/search?q=' + text

	# Fetch the URL data using requests.get(url),
	# store it in a variable, request_result.
	request_result=requests.get( url )


	# Creating soup from the fetched request
	soup = bs4.BeautifulSoup(request_result.text,"html.parser")


	# soup.find.all( h3 ) to grab
	# all major headings of our search result,
	summary=soup.find_all( 'h3' )
	hasil = []
	for info in summary:
		print(info)
		print("---------")
		hasil.append(info.getText())

	print(hasil)
	return hasil

def scrap(pencarian):
	import requests
	import urllib
	import pandas as pd
	from requests_html import HTML
	from requests_html import HTMLSession

	def get_source(url):
		"""Return the source code for the provided URL. 

		Args: 
			url (string): URL of the page to scrape.

		Returns:
			response (object): HTTP response object from requests_html. 
		"""

		try:
			session = HTMLSession()
			response = session.get(url)
			return response

		except requests.exceptions.RequestException as e:
			print(e)    

	def get_results(query):
		
		query = urllib.parse.quote_plus(query)
		response = get_source("https://www.google.co.uk/search?q=" + query)
		
		return response

	def parse_results(response):
		
		css_identifier_result = ".tF2Cxc"
		css_identifier_title = "h3"
		css_identifier_link = ".yuRUbf a"
		css_identifier_text = ".VwiC3b"
		
		results = response.html.find(css_identifier_result)

		output = []
		
		for result in results:
			try:
				item = {
					'title': result.find(css_identifier_title, first=True).text,
					'link': result.find(css_identifier_link, first=True).attrs['href'],
					'text': result.find(css_identifier_text, first=True).text
				}
			
				output.append(item)
			except:
				pass
			
		return output

	def google_search(query):
		response = get_results(query)
		return parse_results(response)

	hasil = google_search(pencarian)
	output = []
	panjang = 0
	for values in hasil :
		#print(len(list(values.values())[2].split()))
		if len(list(values.values())[2].split()) > panjang:
			output = list(values.values())
			panjang = len(list(values.values())[2])
		#print(list(values.values()))
	if output[2][0:2].isdigit() and output[2][9].isdigit() :
		s = output[2]
		s = s[s.find(' — '):]
		s = s[3:]
		output[2] = s

	#print(output)

	return output

def testModelGpt4all(pencarian):
	from gpt4all import GPT4All
	model = GPT4All("A:\Program\GPT4All\Dwnld\ggml-model-gpt4all-falcon-q4_0.bin")
	pencarian = pencarian+" in three sentence"
	output = model.generate(pencarian, max_tokens=200)
	print(output)
	return output

def DisplayJwbBot(jawaban):
	with st.chat_message("assistant"):
		st.markdown(jawaban, unsafe_allow_html=True)

def play_audio_chat(file_path: str):
	with open(file_path, "rb") as f:
		data = f.read()
		b64 = base64.b64encode(data).decode()
		md = f"""
			<audio controls>
			<source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
			</audio>
			"""
		
		st.markdown(
				md,
				unsafe_allow_html=True,
			)
		
def play_audio(file_path: str):
	with open(file_path, "rb") as f:
		data = f.read()
		b64 = base64.b64encode(data).decode()
		md = f"""
			<audio controls>
			<source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
			</audio>
			"""
		with st.chat_message("assistant"):
			st.markdown(
				md,
				unsafe_allow_html=True,
			)

def autoplay_audio(file_path: str):
	with open(file_path, "rb") as f:
		data = f.read()
		b64 = base64.b64encode(data).decode()
		md = f"""
			<audio controls autoplay="true">
			<source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
			</audio>	
			"""
		with st.chat_message("assistant"):
			st.markdown(
			md,
			unsafe_allow_html=True,
		)

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""	


menu_selected = option_menu(None, ["Chat", "Home", 'History', 'Json','Audio?'], 
    icons=['chat', 'house', 'clock-history', 'filetype-json', 'mic'], 
    menu_icon="cast", default_index=0, orientation="horizontal",manual_select=False)



if menu_selected == "Home" :
	import os
	import numpy as np
	import streamlit as st
	from io import BytesIO
	import streamlit.components.v1 as components

	from st_custom_components import st_audiorec

	
	import base64
	file_ = open("mic_gif.gif", "rb")
	contents = file_.read()
	data_url = base64.b64encode(contents).decode("utf-8")
	file_.close()

	from PIL import Image
	image = Image.open('0==true.jpg')

	col1, col2, col3 = st.columns([1,6,1])
	with col1:
		st.write(' ')

	with col2:
		st.markdown(
		f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
		unsafe_allow_html=True,)

		wav_audio_data = st_audiorec()
		import wave
		if wav_audio_data is not None:
			# display audio data as received on the backend
			st.audio(wav_audio_data, format='audio/wav')
			import wave, struct, math, random
			sampleRate = 44100.0 # hertz
			duration = 1.0 # seconds
			frequency = 440.0 # hertz
			obj = wave.open('sound.wav','w')
			obj.setnchannels(1) # mono
			obj.setsampwidth(2)
			obj.setframerate(sampleRate)
			for i in range(99999):
				value = random.randint(-32767, 32767)
				data = struct.pack('<h', value)
				obj.writeframesraw( data )
			obj.close()
			r = sr.Recognizer()
			harvard = sr.AudioFile('s1.wav')
			with harvard as source:
				audio = r.record(source)
			st.text(r.recognize_google(audio))
	with col3:
		st.write(' ')

if menu_selected == 'Chat':
		
		col1, col2= st.columns([1,1])
		with col1:
			Gambar = st.checkbox('Dengan Foto ?')
		with col2:
			Video = st.checkbox('Dengan Video ?')
			
			

		if "messages" not in st.session_state:
			st.session_state.messages = []

		

		for message in st.session_state.messages:
			with st.chat_message(message["role"]):
				if "<audio" in message["content"] :
					audio_path = find_between(message["content"], "./", ".mp3" )
					print("./"+audio_path+".mp3")
					play_audio_chat("./"+audio_path+".mp3")
					print(f"Kamu Ngomong {query}\n")
					# st.text(f"Kamu Ngomong {query}\n")
				else:
					st.markdown(message["content"], unsafe_allow_html=True)
				

		# if "messages" in st.session_state:	
		# 	try:
		# 		#playsound('captured_voice.mp3')
		# 		#os.remove('captured_voice.mp3')
		# 	except:
		# 		pass

		# Gambar = st.checkbox('Dengan Foto ?')
		# Video = st.checkbox('Dengan Video ?')
		
		if prompt := st.chat_input("Silakan ketik pertanyaan anda?"):
			# Display user message in chat message container
			st.chat_message("user").markdown(prompt)
			# Add user message to chat history
			st.session_state.messages.append({"role": "user", "content": prompt})

			#response = f"Echo: {prompt}"
			# Display assistant response in chat message container
			# with st.chat_message("assistant"):
			# 	st.markdown(response)
			# Add assistant response to chat history
			#st.session_state.messages.append({"role": "assistant", "content": response})
			if "?" in prompt :
				prompt = prompt.replace("?","")
			if 'kaa' in prompt:
				prompt = prompt.replace("kaa","Konferensi Asia Afrika")
			if 'KAA' in prompt:
				prompt = prompt.replace("KAA","Konferensi Asia Afrika")
			query = prompt
			to_lang = 'en'
			list_hasil = []
			try:
				list_hasil = scrap(query)
			except:
				list_hasil = ['Hasil Tidak ditemukan','','Artikel Tidak tersedia']
			hasil = list_hasil[0]

			print(query + '?')

			#message(query + '?', is_user=True)

			st.session_state.messages.append({"role": "user", "content": query + '?'})

			#hasil = GoogleTranslator(source='auto', target='id').translate(hasil)

			print(list_hasil)
			img_path = get_LinkFirstImage(query)


			#message(list_hasil[0])

			#st.session_state.messages.append({"role": "assistant", "content": list_hasil[0]})



			deskripsi = list_hasil[2] + " baca Selengkapnya "+ list_hasil[1]
			kodeSuara = str(random.randint(10000000000,1000000000000000000))
			kodeSuara2 = str(random.randint(10000000000,1000000000000000000))
			deskripsi = list_hasil[0] + "\n" + deskripsi
			#st.session_state.messages.append({"role": "assistant", "content": deskripsi})
			#hasilgpt = GoogleTranslator(source='auto', target='id').translate(chatgpt4free(query)) # kalau mau translate dulu
			#prompt = "Act as Museum Guide with name memories. Museum ini adalah museum Hewan. Perkenalkan dirimu sebelum menjelaskan.Jika pertanyaan keluar dari tema hewan jawab dengan minta maaf tidak dapat menjawab pertanyaan tersebut "
			#prompt = "answer in one paragraph"
			hasilgpt = chatgpt4free(prompt + query)
			# coba 1
			if detect(hasilgpt) != 'id':
				hasilgpt = hasilgpt.replace("Memories","Alice")
				hasilgpt = GoogleTranslator(source='auto', target='id').translate(hasilgpt)
				hasilgpt = hasilgpt.replace("Alice","Memories")
			# coba 2
			if "Tidak dapat mengambil tanggapan, Coba lagi." == hasilgpt:
				hasilgpt = chatgpt4free(query)
			# coba 3
				if "Tidak dapat mengambil tanggapan" in hasilgpt or "Unable to fetch the response" in hasilgpt :
					hasilgpt = deskripsi
			
			#speak = gTTS(text="Menurut Google Search" + list_hasil[2] + "Klik Link untuk membaca selengkapnya", lang="id", slow=False)
			speak2 = gTTS(text="" + hasilgpt, lang="id", slow=False)
			audio_path = "./suara/captured_voice"+kodeSuara+".mp3"
			audio_path2 = "./suara/captured_voice"+kodeSuara2+".mp3"
			
			from elevenlabs import clone, generate, play, set_api_key, save
			from elevenlabs.api import History

			set_api_key("d4fded21f109859d8532af143c1bf443")

			# voice = clone(
			#     name="Voice Name",
			#     description="An old American male voice with a slight hoarseness in his throat. Perfect for news.",
			#     files=["./sample1.mp3", "./sample2.mp3"],
			# )

			#try:
			#	speak2 = generate(
			#	text=hasilgpt[:200],
			#	voice="Bella",
			#	model="eleven_multilingual_v2"
			#	)
			#except:
			#	speak2 = generate(
			#	text=hasilgpt,
			#	voice="Bella",
			#	model="eleven_multilingual_v2"
			#	)
			#print("menggunkan api voice")
			#save(speak2, audio_path2)

			#speak.save(audio_path)
			speak2.save(audio_path2)
			

			# message(
			# 			f'<img width="100%" height="200" src="{img_path}"/>', 
			# 			key=f"{random.randint(100,1000)}", 
			# 			allow_html=True
			# 		)

			#st.session_state.messages.append({"role": "assistant", "content": f'<audio controls src="{audio_path}"></audio>'})
			if Gambar :
				st.session_state.messages.append({"role": "assistant", "content": f'<img width="100%" height="200" src="{img_path}"/>'})


			#DisplayJwbBot(f'<audio controls src="{"https://docs.google.com/uc?export=open&id=1JZLGiYiguorOkIi53zYKHGEz5o6z-Im0"}"></audio>')


			linkYT = get_LinkYT(query)
			# message(
			# 			f'<iframe width="400" height="215" src={linkYT} title="YouTube video player" frameborder="0" allow="accelerometer; encrypted-media;"></iframe>', 
			# 			key=f"{random.randint(100,1000)}",
			# 			allow_html=True
			# 		)
			if Video :
				st.session_state.messages.append({"role": "assistant", "content": f'<iframe width="400" height="215" src={linkYT} title="YouTube video player" frameborder="0" allow="accelerometer; encrypted-media;"></iframe>'})

			#hasilgpt = GoogleTranslator(source='auto', target='id').translate(testModelGpt4all(GoogleTranslator(source='auto', target='english').translate(query)))
			st.session_state.messages.append({"role": "assistant", "content": hasilgpt})
			st.session_state.messages.append({"role": "assistant", "content": f'<audio controls src="{audio_path2}"></audio>'})
			import datetime

			with open("Link_gambar.txt", "w") as file:
				file.write(img_path)

			with open("Deskripsi.txt", "w") as file:
				file.write(hasilgpt)

			with open('History.txt', 'a') as f:
					f.writelines("\n\n\nWaktu : " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
					f.writelines("\nPertanyaan : " + query + ' ?')
					f.writelines("\nJawaban : " + hasilgpt)
					f.writelines("\nLokasi Suara : " + audio_path2)
					f.writelines("\nLink Gambar : " + img_path)
					f.writelines("\nLink Youtube : " + linkYT)
					f.close()


			with open('FineTune.txt', 'a') as f:
					
					sistemfirstprom = "Jadilah pemandu museum, kamu dikenal sebagai mories, perkenalkan dirimu sebelum menjawab, kamu sangat mengerti tentang museum terutama museum konferensi asia afrika (KAA) apabila diluar konteks tersebut kamu akan menjawabnya dengan 'Maaf Mories belum bisa menjawab' disertai alasannya. Usahakan menjawab sebisanya sebagai guru kepada muridnya"
					isi = "\n{'messages': [{'role': 'system', 'content': '" + sistemfirstprom+"'}, {'role': 'user', 'content':'"+ query + " ?' }, {'role': 'assistant', 'content':'"+ hasilgpt+"'}]}"
					isi = isi.replace("'",'"')
					f.writelines(isi)
					f.close()



			DisplayJwbBot(query + '?')
			#DisplayJwbBot(list_hasil[0])
			#DisplayJwbBot(deskripsi)
			#play_audio(audio_path)
			if Gambar :
				DisplayJwbBot(f'<img width="100%" height="400" src="{img_path}"/>')
			if Video:
				DisplayJwbBot(f'<iframe width="400" height="400" src={linkYT} title="YouTube video player" frameborder="0" allow="accelerometer; encrypted-media;"></iframe>')
			DisplayJwbBot(hasilgpt)
			play_audio(audio_path2)


		def takecommand():
				r = sr.Recognizer()
				with sr.Microphone() as source:
					playsound('sfxgoogle.mp3')
					#custom_notification_box(icon='info', textDisplay='listening.....', externalLink='more info', url='#', styles=styles, key="foo")
					print("listening.....")
					st.text("listening.....")
					r.pause_threshold = 1
					audio = r.listen(source)
				try:
					print("Recognizing.....")
					#custom_notification_box(icon='info', textDisplay='Recognizing.....', externalLink='more info', url='#', styles=styles, key="fo2")
					st.text("Recognizing.....")
					query = r.recognize_google(audio, language='id')
					print(f"Kamu Ngomong {query}\n")
					#custom_notification_box(icon='info', textDisplay=f"Kamu Ngomong {query}\n", externalLink='more info', url='#', styles=styles, key="fo21")
					#st.text(f"Kamu Ngomong {query}\n")
				except Exception as e:
					print("Tolong ulangi.....")
					#custom_notification_box(icon='info', textDisplay='Tolong ulangi.....', externalLink='more info', url='#', styles=styles, key="fo3")
					st.text("say that again please.....")
					speak = gTTS(text="Please repeat the question", lang='id', slow=False)
					speak.save("captured_voice.mp3")
					playsound('captured_voice.mp3')
					os.remove('captured_voice.mp3')
					return "None"
				return query
		
		def on_btn_click():
			del st.session_state.messages[:]
		def on_btn_mic():
				# Display user message in chat message container
				prompt = takecommand()
				while (prompt == "None"):
					prompt = takecommand()
				#st.chat_message("user").markdown(prompt)
				# Add user message to chat history
				st.session_state.messages.append({"role": "user", "content": prompt})
				
				query = prompt
				to_lang = 'en'
				list_hasil = []
				try:
					list_hasil = scrap(query)
				except:
					list_hasil = ['Hasil Tidak ditemukan','','Artikel Tidak tersedia']
				hasil = list_hasil[0]

				print(query + '?')

				#message(query + '?', is_user=True)

				#st.session_state.messages.append({"role": "user", "content": query + '?'})

				#hasil = GoogleTranslator(source='auto', target='id').translate(hasil)

				print(list_hasil)
				img_path = get_LinkFirstImage(query)


				#message(list_hasil[0])

				#st.session_state.messages.append({"role": "assistant", "content": list_hasil[0]})



				deskripsi = list_hasil[2] + " baca Selengkapnya "+ list_hasil[1]
				kodeSuara = str(random.randint(10000000000,1000000000000000000))
				kodeSuara2 = str(random.randint(10000000000,1000000000000000000))
				deskripsi = list_hasil[0] + "\n" + deskripsi
				#st.session_state.messages.append({"role": "assistant", "content": deskripsi})
				#hasilgpt = GoogleTranslator(source='auto', target='id').translate(chatgpt4free(query)) # kalau mau translate dulu
				#prompt = "Act as Museum Guide with name memories. Museum ini adalah museum Hewan. Perkenalkan dirimu sebelum menjelaskan.Jika pertanyaan keluar dari tema hewan jawab dengan minta maaf tidak dapat menjawab pertanyaan tersebut "
				#prompt = "answer in one paragraph"
				hasilgpt = chatgpt4free(prompt + query)
				# coba 1
				if detect(hasilgpt) != 'id':
					hasilgpt = hasilgpt.replace("Memories","Alice")
					hasilgpt = GoogleTranslator(source='auto', target='id').translate(hasilgpt)
					hasilgpt = hasilgpt.replace("Alice","Memories")
				# coba 2
				if "Tidak dapat mengambil tanggapan, Coba lagi." == hasilgpt:
					hasilgpt = chatgpt4free(query)
				# coba 3
					if "Tidak dapat mengambil tanggapan" in hasilgpt or "Unable to fetch the response" in hasilgpt :
						hasilgpt = deskripsi
				
				speak = gTTS(text="Menurut Google Search" + list_hasil[2] + "Klik Link untuk membaca selengkapnya", lang="id", slow=False)
				speak2 = gTTS(text="" + hasilgpt, lang="id", slow=False)
				audio_path = "./suara/captured_voice"+kodeSuara+".mp3"
				audio_path2 = "./suara/captured_voice"+kodeSuara2+".mp3"
				
				# from elevenlabs import clone, generate, play, set_api_key, save
				# from elevenlabs.api import History

				# set_api_key("6b5b2cfbb952aff99001c460c4355b5c")

				# voice = clone(
				#     name="Voice Name",
				#     description="An old American male voice with a slight hoarseness in his throat. Perfect for news.",
				#     files=["./sample1.mp3", "./sample2.mp3"],
				# )

				# speak2 = generate(
				# text=hasilgpt,
				# voice="Bella",
				# model="eleven_multilingual_v2"
				# )
				
				# save(speak2, audio_path2)

				# speak.save(audio_path)
				speak2.save(audio_path2)
				

				# message(
				# 			f'<img width="100%" height="200" src="{img_path}"/>', 
				# 			key=f"{random.randint(100,1000)}", 
				# 			allow_html=True
				# 		)
				with open('readme.txt', 'w') as f:
					f.write(img_path)
				#st.session_state.messages.append({"role": "assistant", "content": f'<audio controls src="{audio_path}"></audio>'})
				st.session_state.messages.append({"role": "assistant", "content": f'<img width="100%" height="200" src="{img_path}"/>'})

				#DisplayJwbBot(f'<audio controls src="{"https://docs.google.com/uc?export=open&id=1JZLGiYiguorOkIi53zYKHGEz5o6z-Im0"}"></audio>')


				linkYT = get_LinkYT(query)
				# message(
				# 			f'<iframe width="400" height="215" src={linkYT} title="YouTube video player" frameborder="0" allow="accelerometer; encrypted-media;"></iframe>', 
				# 			key=f"{random.randint(100,1000)}",
				# 			allow_html=True
				# 		)

				st.session_state.messages.append({"role": "assistant", "content": f'<iframe width="400" height="215" src={linkYT} title="YouTube video player" frameborder="0" allow="accelerometer; encrypted-media;"></iframe>'})

				#hasilgpt = GoogleTranslator(source='auto', target='id').translate(testModelGpt4all(GoogleTranslator(source='auto', target='english').translate(query)))
				st.session_state.messages.append({"role": "assistant", "content": hasilgpt})
				st.session_state.messages.append({"role": "assistant", "content": f'<audio controls src="{audio_path2}"></audio>'})

		def coba():
			st.write("halo")
			DisplayJwbBot("hai")

		def on_refresh():
			from streamlit_js_eval import streamlit_js_eval
			streamlit_js_eval(js_expressions="parent.window.location.reload()")	
		def on_btn_warning():
			st.warning('Maaf Pertanyaan anda diluar konteks', icon="⚠️")\
	
	

		st.button("Clear message", on_click=on_btn_click)
		#st.button("Ini Tombol buat Mic", on_click=mic)
		st.button("Ini Tombol buat Test warning", on_click=on_btn_warning)
		st.button("Ini Tombol buat Test Refresh", on_click=on_refresh)
		c=st.container()
		with c:
			audio = audiorecorder("Anggap aja ini simbol mic","Stop")

		if len(audio) > 0:
			# To play audio in frontend:
			#st.audio(audio.tobytes())
			
			# To save audio to a file:
			wav_file = open("input.mp3", "wb")
			wav_file.write(audio.tobytes())

			import time
			t = time.localtime()
			waktu = time.strftime("%H_%M_%S", t)
			current_time = waktu 
			filesuara = "./suara/"+current_time+".wav"
			import subprocess
			subprocess.call(['ffmpeg', '-i', 'input.mp3',
							filesuara]) 
			r = sr.Recognizer()
			harvard = sr.AudioFile(filesuara)
			with harvard as source:
				audio = r.record(source)
				output = r.recognize_google(audio, language='id')
				output = output.title()
				#st.text(output + " ?")

		# 	#st.write(scrap(output))
		# 	if gpt:
		# 		hasil = gpt5(output)
		# 		st.markdown(hasil)

		# 		speak = gTTS(text=output+ ". /n" + hasil, lang="id", slow=False)
		# 		audio_path = "./suara/"+current_time+".mp3"
		# 		speak.save(audio_path)
		# 		st.audio(audio_path)
		# else:
		# 	pass
			prompt = output
			
			#st.chat_message("user").markdown(prompt)
			# Add user message to chat history
			st.session_state.messages.append({"role": "user", "content": prompt})
			
			query = prompt
			to_lang = 'en'
			list_hasil = []
			try:
				list_hasil = scrap(query)
			except:
				list_hasil = ['Hasil Tidak ditemukan','','Artikel Tidak tersedia']
			hasil = list_hasil[0]

			print(query + '?')

			#message(query + '?', is_user=True)

			#st.session_state.messages.append({"role": "user", "content": query + '?'})

			#hasil = GoogleTranslator(source='auto', target='id').translate(hasil)

			print(list_hasil)
			img_path = get_LinkFirstImage(query)


			#message(list_hasil[0])

			#st.session_state.messages.append({"role": "assistant", "content": list_hasil[0]})



			deskripsi = list_hasil[2] + " baca Selengkapnya "+ list_hasil[1]
			kodeSuara = str(random.randint(10000000000,1000000000000000000))
			kodeSuara2 = str(random.randint(10000000000,1000000000000000000))
			deskripsi = list_hasil[0] + "\n" + deskripsi
			#st.session_state.messages.append({"role": "assistant", "content": deskripsi})
			#hasilgpt = GoogleTranslator(source='auto', target='id').translate(chatgpt4free(query)) # kalau mau translate dulu
			#prompt = "Act as Museum Guide with name memories. Museum ini adalah museum Hewan. Perkenalkan dirimu sebelum menjelaskan.Jika pertanyaan keluar dari tema hewan jawab dengan minta maaf tidak dapat menjawab pertanyaan tersebut "
			#prompt = "answer in one paragraph"
			hasilgpt = chatgpt4free(prompt + query)
			# coba 1
			if detect(hasilgpt) != 'id':
				hasilgpt = hasilgpt.replace("Memories","Alice")
				hasilgpt = GoogleTranslator(source='auto', target='id').translate(hasilgpt)
				hasilgpt = hasilgpt.replace("Alice","Memories")
			# coba 2
			if "Tidak dapat mengambil tanggapan, Coba lagi." == hasilgpt:
				hasilgpt = chatgpt4free(query)
			# coba 3
				if "Tidak dapat mengambil tanggapan" in hasilgpt or "Unable to fetch the response" in hasilgpt :
					hasilgpt = deskripsi
			
			speak = gTTS(text="Menurut Google Search" + list_hasil[2] + "Klik Link untuk membaca selengkapnya", lang="id", slow=False)
			speak2 = gTTS(text="" + hasilgpt, lang="id", slow=False)
			audio_path = "./suara/captured_voice"+kodeSuara+".mp3"
			audio_path2 = "./suara/captured_voice"+kodeSuara2+".mp3"
			
			from elevenlabs import clone, generate, play, set_api_key, save
			from elevenlabs.api import History

			set_api_key("6b5b2cfbb952aff99001c460c4355b5c")

			# voice = clone(
			#     name="Voice Name",
			#     description="An old American male voice with a slight hoarseness in his throat. Perfect for news.",
			#     files=["./sample1.mp3", "./sample2.mp3"],
			# )
			# try:
			# 	speak2 = generate(
			# 	text=hasilgpt[:200],
			# 	voice="Bella",
			# 	model="eleven_multilingual_v2"
			# 	)
			# except:
			# 	speak2 = generate(
			# 	text=hasilgpt,
			# 	voice="Bella",
			# 	model="eleven_multilingual_v2"
			# 	)
			
			#save(speak2, audio_path2)

			# speak.save(audio_path)
			speak2.save(audio_path2)
			

			# message(
			# 			f'<img width="100%" height="200" src="{img_path}"/>', 
			# 			key=f"{random.randint(100,1000)}", 
			# 			allow_html=True
			# 		)
			with open('readme.txt', 'w') as f:
				f.write(img_path)
			#st.session_state.messages.append({"role": "assistant", "content": f'<audio controls src="{audio_path}"></audio>'})
			st.session_state.messages.append({"role": "assistant", "content": f'<img width="100%" height="200" src="{img_path}"/>'})

			#DisplayJwbBot(f'<audio controls src="{"https://docs.google.com/uc?export=open&id=1JZLGiYiguorOkIi53zYKHGEz5o6z-Im0"}"></audio>')


			linkYT = get_LinkYT(query)
			# message(
			# 			f'<iframe width="400" height="215" src={linkYT} title="YouTube video player" frameborder="0" allow="accelerometer; encrypted-media;"></iframe>', 
			# 			key=f"{random.randint(100,1000)}",
			# 			allow_html=True
			# 		)

			st.session_state.messages.append({"role": "assistant", "content": f'<iframe width="400" height="215" src={linkYT} title="YouTube video player" frameborder="0" allow="accelerometer; encrypted-media;"></iframe>'})

			#hasilgpt = GoogleTranslator(source='auto', target='id').translate(testModelGpt4all(GoogleTranslator(source='auto', target='english').translate(query)))

			st.session_state.messages.append({"role": "assistant", "content": hasilgpt})
			st.session_state.messages.append({"role": "assistant", "content": f'<audio controls src="{audio_path2}"></audio>'})
			import datetime

			with open("Link_gambar.txt", "w") as file:
				file.write(img_path)

			with open("Deskripsi.txt", "w") as file:
				file.write(hasilgpt)

			with open('History.txt', 'a') as f:
					f.writelines("\n\n\nWaktu : " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
					f.writelines("\nPertanyaan : " + query + ' ?')
					f.writelines("\nJawaban : " + hasilgpt)
					f.writelines("\nLokasi Suara : " + audio_path2)
					f.writelines("\nLink Gambar : " + img_path)
					f.writelines("\nLink Youtube : " + linkYT)
					f.close()

			with open('FineTune.txt', 'a') as f:
					
					sistemfirstprom = "Jadilah pemandu museum, kamu dikenal sebagai mories, perkenalkan dirimu sebelum menjawab, kamu sangat mengerti tentang museum terutama museum konferensi asia afrika (KAA) apabila diluar konteks tersebut kamu akan menjawabnya dengan 'Maaf Mories belum bisa menjawab' disertai alasannya. Usahakan menjawab sebisanya sebagai guru kepada muridnya"
					isi = "\n{'messages': [{'role': 'system', 'content': '" + sistemfirstprom+"'}, {'role': 'user', 'content':'"+ query + " ?' }, {'role': 'assistant', 'content':'"+ hasilgpt+"'}]}"
					isi = isi.replace("'",'"')
					f.writelines(isi)
					f.close()
			
			DisplayJwbBot(query + '?')
			#DisplayJwbBot(list_hasil[0])
			#DisplayJwbBot(deskripsi)
			#play_audio(audio_path)
			if Gambar :
				DisplayJwbBot(f'<img width="100%" height="400" src="{img_path}"/>')
			if Video:
				DisplayJwbBot(f'<iframe width="400" height="400" src={linkYT} title="YouTube video player" frameborder="0" allow="accelerometer; encrypted-media;"></iframe>')
			DisplayJwbBot(hasilgpt)
			play_audio(audio_path2)
		
if menu_selected == "History" :
	st.markdown("<h1 style='text-align: center; color: white;'>History</h1>", unsafe_allow_html=True)
	#st.info('Ini inpo', icon="ℹ️")
	import time
	while True:
		# Refresh the container using st.empty
		st.empty()
		f = open('History.txt')
		for line in f:
			st.write(line)
		f.close()
		time.sleep(20)
		st.empty()
	
if menu_selected == "Json" :
	st.markdown("<h1 style='text-align: center; color: white;'>Semi Fine Tuning</h1>", unsafe_allow_html=True)

	def displayPDF(file):
		with open(file, "r") as f:
			st.download_button('Ini Tombol Download File', f,"Semi-Fine_Tuning.txt")

		# Opening file from file path
		with open(file, "r") as f:
			for i in f:
				st.text(i)
	displayPDF("FineTune.txt")
		
if menu_selected == "Audio?" :
	st.markdown("<h1 style='text-align: center; color: white;'>AI Menjawab</h1>", unsafe_allow_html=True)
	
	col1, col2, col3 = st.columns(3)
	with col1:
		st.text("")
	with col2:
		st.image("Krusty_Towers_019.png",caption="Kami tidak meragukan tamu meskipun pertanyaannya aneh - aneh")
		gpt = st.checkbox("Dengan AI ?")
		c=st.container()
		with c:
			audio = audiorecorder("Start","Recognizer ...")
			
	with col3:
		st.text("")

	if len(audio) > 0:
		# To play audio in frontend:
		#st.audio(audio.tobytes())
		
		# To save audio to a file:
		wav_file = open("input.mp3", "wb")
		wav_file.write(audio.tobytes())

		import time
		t = time.localtime()
		waktu = time.strftime("%H_%M_%S", t)
		current_time = waktu 
		filesuara = "./suara/"+current_time+".wav"
		import subprocess
		subprocess.call(['ffmpeg', '-i', 'input.mp3',
						filesuara]) 
		r = sr.Recognizer()
		harvard = sr.AudioFile(filesuara)
		with harvard as source:
			audio = r.record(source)
			output = r.recognize_google(audio, language='id')
			output = output.title()
			st.text(output + " ?")

		#st.write(scrap(output))
		if gpt:
			hasil = gpt5(output)
			st.markdown(hasil)

			speak = gTTS(text=output+ ". /n" + hasil, lang="id", slow=False)
			audio_path = "./suara/"+current_time+".mp3"
			speak.save(audio_path)
			st.audio(audio_path)
	else:
		pass
	
import time
with st.sidebar:
	
	import streamlit as st
	from audiorecorder import audiorecorder
	
	#st.markdown("<h1 style='text-align: center; color: white;'> </h1>", unsafe_allow_html=True)
	#st.markdown("<h1 style='text-align: center; color: white;'> </h1>", unsafe_allow_html=True)
	#st.markdown("<h1 style='text-align: center; color: white;'> </h1>", unsafe_allow_html=True)
	st.markdown("<h1 style='text-align: center; color: white;'>Voice Recognizer</h1>", unsafe_allow_html=True)
	st.markdown("<h1 style='text-align: center; color: white;'> </h1>", unsafe_allow_html=True)
	st.markdown("<h1 style='text-align: center; color: white;'> </h1>", unsafe_allow_html=True)
	col1, col2, col3 = st.columns([1,6,1])

	with col1:
		st.text("")
		
	with col2:
		st.write("\n\n\n\n\n")
		
		
		css_example = '''                                                                                                                                            
		<div class="box">
			<div class="object">
				<div class="outline">
				</div>
				<div class="outline" id="delayed">
					</div>
					<div class="button">
					</div>
					,
					<div class="button" id="circlein">
							<svg class="mic-icon" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 1000 1000" enable-background="new 0 0 1000 1000" xml:space="preserve" style="fill:#1E2D70">
			<g><path d="M500,683.8c84.6,0,153.1-68.6,153.1-153.1V163.1C653.1,78.6,584.6,10,500,10c-84.6,0-153.1,68.6-153.1,153.1v367.5C346.9,615.2,415.4,683.8,500,683.8z M714.4,438.8v91.9C714.4,649,618.4,745,500,745c-118.4,0-214.4-96-214.4-214.4v-91.9h-61.3v91.9c0,141.9,107.2,258.7,245,273.9v124.2H346.9V990h306.3v-61.3H530.6V804.5c137.8-15.2,245-132.1,245-273.9v-91.9H714.4z"/></g>
			</svg>
					</div>
			</div>
		</div>      
        <style>
		body {
			background: #222032;
		}

		.box {
			position: absolute;
		top: 50%;
		left: 50%;
		}

		.object {
		display: flex;
			flex: 0 1 100%;
		justify-content: center;
		align-items: center;
		align-content: stretch;
		}

		.outline {
			width: 60px;
			height: 60px;
			border-radius: 50%;
			border: 8px solid #B5A4A4;
		animation: pulse 3s;
			animation-timing-function: ease-out;
			animation-iteration-count: infinite;
			position: absolute;
		}

		.button {
			width: 120px;
			height: 120px;
			border-radius: 50%;
			background: #50CDDD;
			box-shadow: 0px 0px 80px #0084F9;
			position: absolute;
		}

		@keyframes pulse {
		0% {
			transform: scale(0);
			opacity: 0;
				border: 65px solid #0B3082;
		}
		50% {
				border: solid #A3FFC2;		
				opacity: 0.8;
		}
			
			90% {
			transform: scale(3.2);
				opacity: 0.2;
				border: 3px solid #2E3CFF;
		}
		100% {
			transform: scale(3.3);
				opacity: 0;
				border: 1px solid #7A89FF;
		}
		}

		#delayed {
			animation-delay: 1.5s;
		}

		#circlein {
			width: 100px;
			height: 100px;
			border-radius: 50%;
			background: #6BD6E1;
			box-shadow: 0px -2px 15px #E0FF94;
			position: absolute;
		}

		.mic-icon {
			height: 60px;
			position: absolute;
			margin: 21px;
		}
		</style>                                                                                                                                                   
		'''
		st.write(css_example, unsafe_allow_html=True)
		st.markdown("<h1 style='text-align: center; color: white;'> </h1>", unsafe_allow_html=True)
		st.markdown("<h1 style='text-align: center; color: white;'> </h1>", unsafe_allow_html=True)
		st.markdown("<h1 style='text-align: center; color: white;'> </h1>", unsafe_allow_html=True)
		

	with col3:
		st.text("")

	#while True:
	#Refresh the container using st.empty
	st.empty()
	with open("Link_gambar.txt", "r") as file:
		img_path = file.read()
	with open("Deskripsi.txt", "r") as file:
		img_doc = file.read()
	st.image(img_path, caption=img_doc)
	file.close()
	time.sleep(20)
	#st.empty()
	

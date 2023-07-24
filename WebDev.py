import streamlit as st
import string
import pandas as pd
import numpy as np
import streamlit.components.v1 as components
import random
#from selenium import webdriver
#from selenium.webdriver.common.by import By



# def get_LinkYT(cari_pidio):
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

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             #background-image: url("https://images.pexels.com/photos/7235085/pexels-photo-7235085.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
add_bg_from_url() 

st.write("""
# Test Voice
""")
st.title("Anggap aja chat")


#import speech_recognition as sr
#from deep_translator import GoogleTranslator
from gtts import gTTS
import os
import sys 
#import wikipedia
from streamlit_chat import message
import requests
import bs4
flag = 0

#with st.container():
# input_user = ''
# input_user = st.text_input("User Input:", on_change=on_input_change, key="user_input")
# if input_user != '':
# 	message(input_user)
####################################
dic = ('afrikaans', 'af', 'albanian', 'sq',
	'amharic', 'am', 'arabic', 'ar',
	'armenian', 'hy', 'azerbaijani', 'az',
	'basque', 'eu', 'belarusian', 'be',
	'bengali', 'bn', 'bosnian', 'bs', 'bulgarian',
	'bg', 'catalan', 'ca', 'cebuano',
	'ceb', 'chichewa', 'ny', 'chinese (simplified)',
	'zh-cn', 'chinese (traditional)',
	'zh-tw', 'corsican', 'co', 'croatian', 'hr',
	'czech', 'cs', 'danish', 'da', 'dutch',
	'nl', 'english', 'en', 'esperanto', 'eo',
	'estonian', 'et', 'filipino', 'tl', 'finnish',
	'fi', 'french', 'fr', 'frisian', 'fy', 'galician',
	'gl', 'georgian', 'ka', 'german',
	'de', 'greek', 'el', 'gujarati', 'gu',
	'haitian creole', 'ht', 'hausa', 'ha',
	'hawaiian', 'haw', 'hebrew', 'he', 'hindi',
	'hi', 'hmong', 'hmn', 'hungarian',
	'hu', 'icelandic', 'is', 'igbo', 'ig', 'indonesian',
	'id', 'irish', 'ga', 'italian',
	'it', 'japanese', 'ja', 'javanese', 'jw',
	'kannada', 'kn', 'kazakh', 'kk', 'khmer',
	'km', 'korean', 'ko', 'kurdish (kurmanji)',
	'ku', 'kyrgyz', 'ky', 'lao', 'lo',
	'latin', 'la', 'latvian', 'lv', 'lithuanian',
	'lt', 'luxembourgish', 'lb',
	'macedonian', 'mk', 'malagasy', 'mg', 'malay',
	'ms', 'malayalam', 'ml', 'maltese',
	'mt', 'maori', 'mi', 'marathi', 'mr', 'mongolian',
	'mn', 'myanmar (burmese)', 'my',
	'nepali', 'ne', 'norwegian', 'no', 'odia', 'or',
	'pashto', 'ps', 'persian', 'fa',
	'polish', 'pl', 'portuguese', 'pt', 'punjabi',
	'pa', 'romanian', 'ro', 'russian',
	'ru', 'samoan', 'sm', 'scots gaelic', 'gd',
	'serbian', 'sr', 'sesotho', 'st',
	'shona', 'sn', 'sindhi', 'sd', 'sinhala', 'si',
	'slovak', 'sk', 'slovenian', 'sl',
	'somali', 'so', 'spanish', 'es', 'sundanese',
	'su', 'swahili', 'sw', 'swedish',
	'sv', 'tajik', 'tg', 'tamil', 'ta', 'telugu',
	'te', 'thai', 'th', 'turkish',
	'tr', 'ukrainian', 'uk', 'urdu', 'ur', 'uyghur',
	'ug', 'uzbek', 'uz',
	'vietnamese', 'vi', 'welsh', 'cy', 'xhosa', 'xh',
	'yiddish', 'yi', 'yoruba',
	'yo', 'zulu', 'zu')
query = ''

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

			item = {
				'title': result.find(css_identifier_title, first=True).text,
				'link': result.find(css_identifier_link, first=True).attrs['href'],
				'text': result.find(css_identifier_text, first=True).text
			}
			
			output.append(item)
			
		return output

	def google_search(query):
		response = get_results(query)
		return parse_results(response)

	hasil = google_search(pencarian)

	output = []
	for values in hasil[0].values() :
		output.append(values) 
	#print(output)

	return output


def DisplayJwbBot(jawaban):
	with st.chat_message("assistant"):
		st.markdown(jawaban, unsafe_allow_html=True)

if "messages" not in st.session_state:
	st.session_state.messages = []

for message in st.session_state.messages:
	with st.chat_message(message["role"]):
		st.markdown(message["content"], unsafe_allow_html=True)

if prompt := st.chat_input("What is up?"):
	# Display user message in chat message container
	st.chat_message("user").markdown(prompt)
	# Add user message to chat history
	st.session_state.messages.append({"role": "user", "content": prompt})

	response = f"Echo: {prompt}"
	# Display assistant response in chat message container
	# with st.chat_message("assistant"):
	# 	st.markdown(response)
	# Add assistant response to chat history
	st.session_state.messages.append({"role": "assistant", "content": response})
	
	query = prompt
	to_lang = 'en-in'
	list_hasil = []
	list_hasil = scrap(query)
	hasil = list_hasil[0]

	print(query + '?')
	
	#message(query + '?', is_user=True)
	DisplayJwbBot(query + '?')
	st.session_state.messages.append({"role": "user", "content": query + '?'})
	
	#hasil = GoogleTranslator(source='auto', target='id').translate(hasil)

	print(list_hasil)
	#img_path = get_LinkFirstImage(query)


	#message(list_hasil[0])
	DisplayJwbBot(list_hasil[0])
	st.session_state.messages.append({"role": "assistant", "content": list_hasil[0]})
	


	deskripsi = list_hasil[2] + "baca Selengkapnya "+ list_hasil[1]
	#message(deskripsi)
	DisplayJwbBot(deskripsi)
	st.session_state.messages.append({"role": "assistant", "content": deskripsi})
	speak = gTTS(text="Menurut Google Search" + list_hasil[2] + "Klik Link untuk membaca selengkapnya", lang=to_lang, slow=False)
	speak.save("captured_voice.mp3")
	#playsound('captured_voice.mp3')
	os.remove('captured_voice.mp3')

	# message(
	# 			f'<img width="100%" height="200" src="{img_path}"/>', 
	# 			key=f"{random.randint(100,1000)}", 
	# 			allow_html=True
	# 		)
	#DisplayJwbBot(f'<img width="100%" height="400" src="{img_path}"/>')
	#st.session_state.messages.append({"role": "assistant", "content": f'<img width="100%" height="200" src="{img_path}"/>'})

	#DisplayJwbBot(f'<audio controls src="{"https://docs.google.com/uc?export=open&id=1JZLGiYiguorOkIi53zYKHGEz5o6z-Im0"}"></audio>')

	#linkYT = get_LinkYT(query)
	# message(
	# 			f'<iframe width="400" height="215" src={linkYT} title="YouTube video player" frameborder="0" allow="accelerometer; encrypted-media;"></iframe>', 
	# 			key=f"{random.randint(100,1000)}",
	# 			allow_html=True
	# 		)
	#DisplayJwbBot(f'<iframe width="400" height="215" src={linkYT} title="YouTube video player" frameborder="0" allow="accelerometer; encrypted-media;"></iframe>')
	#st.session_state.messages.append({"role": "assistant", "content": f'<iframe width="400" height="215" src={linkYT} title="YouTube video player" frameborder="0" allow="accelerometer; encrypted-media;"></iframe>'})

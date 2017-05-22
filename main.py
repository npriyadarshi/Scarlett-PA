import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
	print("Say something!")
	audio = r.listen(source)

try:
	recognized_speech = r.recognize_google(audio, key=" AIzaSyBFWL5ySjW4FpUsjC3VMi5XeyvUO7eEhKU")
except sr.UnknownValueError:
	print("Couldn't recognize audio")
except sr.RequestError as e:
	print("Couldn't request resuls from Google speech service : {}".format(e))


with open("recording.wav", "wb") as f:
	f.write(audio.get_wav_data())
from tkinter import *
import googletrans
import textblob
from tkinter import ttk, messagebox
import langid
import speech_recognition as sr
import pyttsx3

# Inisialisasi root window
root = Tk()
root.title('AI Translator')
root.configure(background="white")
root.geometry("1250x500")
root.resizable(width=False, height=False)

# Frame untuk bagian atas
Tops = Frame(root, background="white", width=1750, height=100, relief="ridge")
Tops.grid(row=0, column=1)

# Label judul aplikasi
headlabel = Label(Tops, font=('arial', 20, 'bold'), background="white", text='Languages Translator')
headlabel.grid(row=0, column=0, sticky=W)

# Fungsi untuk mendeteksi bahasa asli Menggunakan langid
def detect_language():
    try:
        text = original_text.get(1.0, END)
        lang, _ = langid.classify(text)  # 
        
        # Set combobox bahasa asli berdasarkan hasil deteksi
        for key, value in languages.items():
            if key == lang:
                original_combo.set(value)
                break
    except Exception as e:
        messagebox.showerror("Translator Error", str(e))

# Fungsi untuk menerjemahkan teks
def translate_it():
    try:
        from_language_key = None
        to_language_key = None

        for key, value in languages.items():
            if value == original_combo.get():
                from_language_key = key
                break

        for key, value in languages.items():
            if value == translated_combo.get():
                to_language_key = key
                break

        if not from_language_key:
            messagebox.showerror("Translator Error", "Original language not selected or not found")
            return

        if not to_language_key:
            messagebox.showerror("Translator Error", "Target language not selected or not found")
            return

        words = textblob.TextBlob(original_text.get(1.0, END))
        words = words.translate(from_lang=from_language_key, to=to_language_key)

        translated_text.delete(1.0, END)
        translated_text.insert(1.0, words)

    except Exception as e:
        messagebox.showerror("Translator Error", str(e))

# Fungsi untuk menghapus teks
def clear():
    original_text.delete(1.0, END)
    translated_text.delete(1.0, END)

# Fungsi untuk melakukan speech-to-text
def recognize_speech():
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)
            original_text.delete(1.0, END)
            original_text.insert(1.0, text)
        except sr.UnknownValueError:
            messagebox.showwarning("Speech Recognition", "Could not understand audio")
        except sr.RequestError:
            messagebox.showerror("Speech Recognition", "Could not request results; check your internet connection")
    except Exception as e:
        messagebox.showerror("Speech Recognition Error", str(e))

# Fungsi untuk text-to-speech
def speak_text():
    engine = pyttsx3.init()
    text = translated_text.get(1.0, END)
    engine.say(text)
    engine.runAndWait()

# Inisialisasi daftar bahasa
languages = googletrans.LANGUAGES
language_list = list(languages.values())

# Text widget untuk input teks asli
original_text = Text(root, height=15, width=50, font=("Arial", 12))
original_text.grid(row=1, column=0, pady=20, padx=10)

# Text widget untuk hasil terjemahan
translated_text = Text(root, height=15, width=50, font=("Arial", 12))
translated_text.grid(row=1, column=2, pady=20, padx=10)

# Button untuk menerjemahkan
translated_button = Button(root, text="Translate", font=("Helvetica", 20), command=translate_it)
translated_button.grid(row=1, column=1, padx=10)

# Combobox untuk memilih bahasa asli
original_combo = ttk.Combobox(root, width=20, values=language_list)
original_combo.grid(row=2, column=0)
original_combo.set('Choose Language')

# Combobox untuk memilih bahasa tujuan
translated_combo = ttk.Combobox(root, width=20, values=language_list)
translated_combo.grid(row=2, column=2)
translated_combo.set('Choose Language')

# Button untuk membersihkan teks
clear_button = Button(root, text="Clear", command=clear)
clear_button.grid(row=2, column=1)

# Button untuk mendeteksi bahasa asli
detect_button = Button(root, text="Detect Language", command=detect_language)
detect_button.grid(row=3, column=0, pady=10)

# Button untuk speech-to-text
speech_button = Button(root, text="Speech to Text", command=recognize_speech)
speech_button.grid(row=3, column=1, pady=10)

# Button untuk text-to-speech
speak_button = Button(root, text="Listen to Translation", command=speak_text)
speak_button.grid(row=3, column=2, pady=10)

# Menjalankan mainloop untuk aplikasi tkinter
root.mainloop()
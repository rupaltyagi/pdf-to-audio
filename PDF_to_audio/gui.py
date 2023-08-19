import tkinter as tk
from tkinter import filedialog
import os
import pygame
import PyPDF2
from gtts import gTTS

class PDFToAudioConverterApp:
    def __init__(self, window):
        self.window = window
        self.window.geometry('400x200')
        self.window.title('PDF to Audio Converter')
        self.window.configure(bg='#FFFAFF')

        self.heading = tk.Label(window, text='PDF to AUDIO', font=('Helvetica', 18, "bold"), bg='#FFFAFF', fg='#B10F2E')
        self.heading.grid(row=0, column=2, columnspan=3, pady=30, padx=10)

        self.button = tk.Button(window, text="Browse", command=self.browse_file)
        self.button.grid(row=1, column=1, padx=40)

        self.file_path = tk.Text(window, height=1, width=30, bg='#FAFFFF')
        self.file_path.grid(row=1, column=4)

        self.audio_button = tk.Button(window, text="PDF to audio", command=self.pdf_to_speech)
        self.audio_button.grid(row=2, column=4, pady=10)
        self.init_audio()

    def init_audio(self):
        pygame.mixer.init()

    def browse_file(self):
        path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        if path:
            self.file_path.delete("1.0", tk.END)
            self.file_path.insert(tk.END, path)
        else:
            self.file_path.delete("1.0", tk.END)
            self.file_path.insert(tk.END, "No PDF selected")

    def pdf_to_speech(self):
        pdf_path = self.file_path.get("1.0", tk.END).strip()
        if pdf_path.lower().endswith('.pdf'):
            file = open(pdf_path, 'rb')
            pdf_reader = PyPDF2.PdfReader(pdf_path)

            full_text = ''
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                full_text += page.extract_text()
                print(full_text)

            file.close()

            speech = gTTS(full_text)
            pdf_name = os.path.basename(pdf_path)
            audio_filename = pdf_name.replace('.pdf', '_output.mp3')

            audio_filename = str(audio_filename)

            speech.save(audio_filename)

            pygame.mixer.music.load(audio_filename)
            print(audio_filename)
            pygame.mixer.music.play()

        else:
            self.file_path.delete("1.0", tk.END)
            self.file_path.insert(tk.END, "Invalid PDF file")

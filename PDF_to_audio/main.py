import tkinter as tk
from gui import PDFToAudioConverterApp


if __name__ == '__main__':
    window = tk.Tk()
    app = PDFToAudioConverterApp(window)
    window.mainloop()



from tkinter import *
import tkinter as tk
import tkinter
import numpy as np
import pyaudio
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from PIL import Image, ImageTk
from io import BytesIO
import base64

logo = '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'

class WaveGeneratorApp:
    def __init__(self,win):

        window.title('Wave Generator Applet')
        window.geometry("800x400+10+20")

        brown = ImageTk.PhotoImage(Image.open(BytesIO(base64.b64decode(logo))))

        self.brownlogo = Label(image=brown)
        self.brownlogo.image = brown
        self.brownlogo.place(x = 110, y = 260)

        self.title = Label(win, text = 'Wave Generator App', font = ("Arial",25))
        self.title.place(x = 180, anchor = "center", y=25)
        self.course = Label(win, text = 'ENGN 1735: Vibrations')
        self.course.place(x = 180, anchor = "center", y=50)
        # self.authors = Label(win, text = 'Jack-William Barotta, Johnny Boustany, Maya Lewis, and Joshua Neronha')
        # self.authors.place(x = 300, anchor = "center", y=70)
        self.btn=Button(win, text="Go")
        self.btn.bind('<Button-1>', self.generate_tone)
        self.btn.place(x=180, y=210, anchor = "center")

        self.freqfld=Entry(win, text="Frequency")
        self.freqfld.place(x=80, y=110, width = 80, anchor = "center")
        self.freqlabel = Label(win, text = "Right (Hz)")
        self.freqlabel.place(x=80, y=140, anchor = "center")

        self.freqfld1=Entry(win, text="Frequency1")
        self.freqfld1.place(x=180, y=110, width = 80, anchor = "center")
        self.freqlabel1 = Label(win, text = "Left(Hz)")
        self.freqlabel1.place(x=180, y=140, anchor = "center")
        self.optionallabel = Label(win, text = "--optional--")
        self.optionallabel.place(x=180, y=160, anchor = "center")

        self.durfld=Entry(win, text="Duration")
        self.durfld.place(x=280, y=110, width = 80, anchor = "center")
        self.durlabel = Label(win, text = "Duration (s)")
        self.durlabel.place(x=280, y=140, width = 100, anchor = "center")

        #self.course = Label(win, text = 'RIGHT')
        #self.course.place(x = 250, anchor = "center", y=110)

        self.fig, self.ax = plt.subplots(figsize = (3,3))
        self.canvas = FigureCanvasTkAgg(self.fig, master = window)
        self.canvas.get_tk_widget().pack(side = tkinter.RIGHT,fill=tkinter.Y)
        NavigationToolbar2Tk(self.canvas, win)


    def generate_tone(self,win):

        self.ax.clear()

        p = pyaudio.PyAudio()

        volume = 1     # range [0.0, 1.0]
        self.fs = 41000       # sampling rate, Hz, must be integer

        try:
            self.f = int(self.freqfld.get())      # sine frequency, Hz, may be float
            self.f1 = int(self.freqfld1.get())      # sine frequency, Hz, may be float

            self.flist = [self.f, self.f1]

        except:
            self.f = int(self.freqfld.get())      # sine frequency, Hz, may be float

            self.flist = [self.f]

        if len(self.durfld.get()) != 0:
            self.duration = int(self.durfld.get())   # in seconds, may be float

            if len(self.freqfld.get()) != 0:
                self.time_array = np.arange(self.fs*self.duration)
                self.wave = np.sin(2*np.pi*self.time_array*self.f/self.fs).astype(np.float32)
                self.waveplot = np.sin(2*np.pi*self.time_array*self.f/self.fs).astype(np.float32)
                self.plot_function(self.fig, self.ax, self.waveplot, self.time_array, self.canvas,self.flist)

            if len(self.freqfld1.get()) != 0:
                self.time_array1 = np.arange(self.fs*self.duration)
                self.wave1 = np.sin(2*np.pi*self.time_array1*self.f1/self.fs).astype(np.float32)
                self.waveplot1 = np.sin(2*np.pi*self.time_array1*self.f1/self.fs).astype(np.float32)
                self.plot_function(self.fig, self.ax, self.waveplot1, self.time_array1, self.canvas, self.flist)

            signal = 0
            channels = 1

            if len(self.freqfld.get()) != 0 and len(self.freqfld1.get()) != 0:
                signal = volume*self.wave
                signal1 = volume*self.wave1
                length = len(signal)
                stereo_signal = np.zeros([length, 2])
                stereo_signal[:, 1] = signal[:]
                stereo_signal[:, 0] = signal1[:]
                signal = stereo_signal
                channels = 2

            elif len(self.freqfld.get()) != 0 and len(self.freqfld1.get()) == 0:
                signal = volume*self.wave

            elif len(self.freqfld.get()) == 0 and len(self.freqfld1.get()) != 0:
                signal = volume*self.wave1

            if len(self.freqfld.get()) != 0 or len(self.freqfld1.get()) != 0:
                stream = p.open(format=pyaudio.paFloat32,
                                channels=channels,
                                rate=self.fs,
                                output=True)
                chunks = []
                chunks.append(signal)
                chunk = np.concatenate(chunks)*0.1
                stream.write(chunk.astype(np.float32).tobytes())
                stream.stop_stream()
                stream.close()
        p.terminate()

    def plot_function(self, fig, ax, waveplot, time_array, canvas, flist):

        # fig, ax = plt.subplots(figsize = (2,1))
        # ax.set_xlim([0, 1000])

        # fig.clf()

        maxf = max(flist)

        ax.plot(time_array / self.fs, waveplot)

        ax.set_xlim(0, 5/maxf)

        ax.legend(['Right', 'Left'],loc = 'upper right')
        ax.set_title('Frequency Plot')
        ax.set_xlabel('Time')

        canvas.draw()

        # canvas = FigureCanvasTkAgg(fig, master = window)
        # # canvas.draw()
        # # placing the canvas on the Tkinter window
        # canvas.get_tk_widget().pack(side = tkinter.RIGHT,fill=tkinter.Y)

    def close_plot(self,pfig):
        pfig.close()


window = Tk()
instance = WaveGeneratorApp(window)
window.mainloop()

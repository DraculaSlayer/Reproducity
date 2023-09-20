"""
=================================================
                Por: DraculaSlayer
=================================================

"""
import tkinter as tk
from tkinter import Button, Label, Entry, Listbox, messagebox
from pygame import mixer
import os
from pytube import YouTube
import time

#inicio del codigo
root = tk.Tk()
mixer.init()

#variable que se van a usar mas tardes
mpr = None
q = None
a = None

def convertir(t, b):
	os.system(f"ffmpeg.exe -i {t} .\\{b}.mp3")

#funcion de buscar la musica en la misma carpeta
def buscar(): 
	global mpr, q
	files = os.listdir(".")

	mpr = [file for file in files if file.endswith((".mp3", ".wav"))]
	q = [nombre[:-4] for nombre in mpr]

buscar()

#La funcion de descargar
def descargar(a, b):

	yt = YouTube(a)

	video = yt.streams.filter(only_audio=True).first()

	out_file = video.download(output_path=".")

	cambio = os.rename(out_file, f".\\{b}.wav")

	t = f".\\{b}.wav"

	time.sleep(5)

	convertir(t,b)

	os.system(f"del {t}")

#Segunda Ventana
def vs():
	vs1 = tk.Toplevel(root)
	
	vs1.geometry("400x100")

	text1 = Label(vs1, text="Url:")
	text1.place(y=0,x=110)

	text2 = Label(vs1, text="Nombre del mp3:")
	text2.place(y=20,x=35)

	uno = Entry(vs1)
	uno.pack()

	dos = Entry(vs1)
	dos.pack()

	impor = Button(vs1, text="download", command=lambda: {descargar(uno.get(), dos.get())})
	impor.pack()

	uno.delete(0, tk.END)
	dos.delete(0, tk.END)

#el tamañio de la ventana
root.geometry("800x600")
root.title("Reproducity 2.0")

#el input de la ventana
entrada = Entry(root, text="elije")
entrada.pack()

#funciones mas importantes
class funciones():
		
	def mp3(a):
		if entrada.get() in q:
			mixer.music.load(f".\\{entrada.get()}.mp3")
			mixer.music.play()
			entrada.delete(0, tk.END)
		else:
			entrada.delete(0, tk.END)
			mensaje = messagebox.showerror("Error", "Esa cancion no existe, revise la lista")
		despausa.place_forget()
		pausa.place(y=150,x=450)
		sm.place_forget()
		detener.place(y=150,x=550)
	def wav(a):
		if entrada.get() in q:
			mixer.music.load(f".\\{entrada.get()}.wav")
			mixer.music.play()
			entrada.delete(0, tk.END)
		else:
			entrada.delete(0, tk.END)
			mensaje = messagebox.showerror("Error", "Esa cancion no existe, revise la lista")
		despausa.place_forget()
		pausa.place(y=150,x=450)
		sm.place_forget()
		detener.place(y=150,x=550)
			
#Aqui la funciones si importancia
def salir():
	exit()
def detener():
	mixer.music.stop()
	detener.place_forget()
	sm.place(y=150,x=550)
def seguir():
	mixer.music.play()
	sm.place_forget()
	detener.place(y=150,x=550)
def pausar():
	mixer.music.pause()
	pausa.place_forget()
	despausa.place(y=150,x=450)
def despausar():
	mixer.music.unpause()
	despausa.place_forget()
	pausa.place(y=150,x=450)

#las teclas de para reproducir musica
entrada.bind("<Return>", funciones.mp3)
entrada.bind("w", funciones.wav)

barra_menu = tk.Menu()

contenido = tk.Menu(barra_menu, tearoff=False)

contenido.add_command(label="Convertir", accelerator="Ctrl+N", command=lambda: [])

barra_menu.add_cascade(menu=contenido, label="Buscar")

root.config(menu=barra_menu)

#Las letras
texto = Label(root, text="Por: DraculaSlayer")
texto.pack()

version = Label(root, text="Version: 2.0")
version.pack()

#Los botones
boton = Button(root, text="Mp3",width=12,height=3, command=lambda: [funciones.mp3(a)])
boton.place(y=150,x=50)

boton = Button(root, text="Wav",width=12,height=3, command=lambda: [funciones.wav(a)])
boton.place(y=150,x=150)

rese = Button(root, text="Reset",width=12,height=3, command=lambda: [buscar(),porsi()])
rese.place(y=150,x=250)

salir = Button(root, text="Exit",width=12,height=3, command=salir)
salir.place(y=150,x=350)

despausa = Button(root, text="Despausar",width=12,height=3, command=despausar)

pausa = Button(root, text="Pausar",width=12,height=3, command=pausar)
pausa.place(y=150,x=450)

sm = Button(root, text="Seguir", width=12, height=3, command=seguir)

detener = Button(root, text="Stop", width=12,height=3, command=detener)
detener.place(y=150,x=550)

des = Button(root, text="Download", width=12,height=3, command=vs)
des.place(y=150,x=650)

#Esta es la lista
lit = Listbox(root, width=58,height=18)
lit.place(y=220, x=400)

def porsi():
	#este el codigo del listado
	lit.delete(0, tk.END)
	for i, a in enumerate(mpr):
		lit.insert(tk.END, str(i + 1) + ". " + a)
	
#aqui abajo esta el codigo del scroll 
barra = tk.Scrollbar(root, orient=tk.VERTICAL)
barra.config(command=lit.yview, orient=tk.VERTICAL, repeatinterval=0)

barra.pack(side=tk.LEFT, fill=tk.Y)
porsi()

entrada.delete(0, tk.END)

root.mainloop()
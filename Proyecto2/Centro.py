#Proyecto final de Fundamentos de Sistemas Embebidos 
#Candia Marcial Uriel
#Martin Desceano Jose Antonio	
#Reyes Luna Luis Ernesto 	
#
#	Licencia: MIT License
#Copyright <2023> <Equipo9>
#
#Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import webbrowser
import os
import vlc
import time
from getpass import getuser
import pathlib
import math

def tam_pant(root,boton,x,y):
	root.update_idletasks()
	altura=root.winfo_height()
	anchura=root.winfo_width()
	alt=math.ceil(altura/100)
	anch=math.ceil(anchura/100)
	boton.place(x=(anch*x), y=(alt*y))




#Funcion para abrir la pagina principal de streaming
def abrir_principal():
	#abrimos el navegador con el archivo html 
	navegador=webbrowser.get("chromium-browser")
	navegador.open("file:///home/uriel/Documentos/Proyecto2/centro-multimedia-main/user_interface.html",new=2, autoraise=True)
	time.sleep(1)
	#seleccionamos la ventana chromium
	cmd1="wmctrl -a Chromium"
	os.system(cmd1)
	time.sleep(0.1)
	#enviamos la entrada por teclado de la tecla f11 para entrar en pantalla completa dentro de chromium 
	cmd2="xdotool key F11"
	os.system(cmd2)
	

#Funcion para leer USB 
def lectura_usb(root): 
	root.destroy()
	#Inicializamos una nueva ventana tkinter 
	vent_usb = Tk()
	vent_usb.title("Dispositivos USB disponibles: ")
	#Ponemos la ventana en patalla completa 
	vent_usb.attributes('-fullscreen', True) 
	vent_usb.config(bg = "white")
	#Agregamos una imagen de fondo para la ventana 
	imagenL = ImageTk.PhotoImage(Image.open('Pro_img/fondo1.jpg'))
	lblImagen = Label(vent_usb, image = imagenL).pack()
	#Agregamos el texto 
	titulo=Label(vent_usb,text="USB disponibles:")
	#Enviamos la ventana y el titulo para colocarlos dentro de la ventana 
	tam_pant(vent_usb,titulo,10,10)
	

	#Con la funcion geuser obtenemos el usuario 
	user=getuser()
	#Asignamos a las variable dir_user la direccion de la mem
	dir_user="/media/"+user+"/"
	
	#Obtenemos el nombre de archivos dentro de la usb 
	Num_usbs = os.listdir(dir_user)
	#Contamos la usb disponibles 
	total_usbs = len(Num_usbs)
	botonUsb = []
	#Si existe una usb se crea un boton para mostrar el contenido de la usb 
	if total_usbs > 0:
		if total_usbs >= 1:
			boton1=Button(vent_usb,text=Num_usbs[0],bg="#212529",fg="white", command=lambda:cont_usb(vent_usb,Num_usbs[0]))
			tam_pant(vent_usb,boton1,10,15)

			if total_usbs >=2:
				boton2=Button(vent_usb,text=Num_usbs[1],bg="#212529", command=lambda:cont_usb(vent_usb,Num_usbs[1]))
				tam_pant(vent_usb,boton2,10,20)

				if total_usbs >= 3:
					boton3=Button(vent_usb,text=Num_usbs[2],bg="#212529", command=lambda:cont_usb(vent_usb, Num_usbs[2]))
					tam_pant(vent_usb,boton1,10,25)
					
					if total_usbs >= 4:
						boton4=Button(vent_usb,text=Num_usbs[3],bg="#212529", command=lambda:cont_usb(vent_usb, Num_usbs[3]))
						tam_pant(vent_usb,boton1,10,30)
	else:
		titulo=Label(vent_usb,text="No existen dispositivos usb disponibles").place(x=50,y=150)

	#Creamos un boton para regresar al menu anterior 
	boton_atras=Button(vent_usb,text="Atras",command=lambda:pant_prin(vent_usb))
	tam_pant(vent_usb,boton_atras,90,90)
	
	#Con la funcion try estamos bucando nuevas usb o en su caso la desconeccion de alguna usb 
	try:
		while True:
			detecta_usb = os.listdir(dir_user)
			#Si no existen nuevos usb
			if total_usbs == len(detecta_usb):
				vent_usb.update_idletasks()
				vent_usb.update()
			else:
				lectura_usb(vent_usb)
	except:
		print("Ocurrio un error inesperado")
	
	
	vent_usb.mainloop()

#Funcion para mostrar el contenido de una usb
def cont_usb(root,nombre_usb):
	#Se elimina la ventana anterior
	root.destroy()
	#Creamos una nueva ventana 
	vent_infousb = Tk()
	titulo = "Informacion de USB " + nombre_usb
	vent_infousb.title(titulo)
	#Ponemos la ventana en patalla completa
	vent_infousb.attributes('-fullscreen', True) 
	vent_infousb.config(bg = "white")
	#Agregamos una imagen de fondo para la ventana 
	imagenL = ImageTk.PhotoImage(Image.open('Pro_img/fondo1.jpg'))
	lblImagen = Label(vent_infousb, image = imagenL).place(x = 0, y = 0, relwidth = 1, relheight = 1)
	titulo=Label(vent_infousb,text="Contenido de la USB:")
	tam_pant(vent_infousb,titulo,10,10)
	#Se obtiene el directorio de la usb
	user=getuser()
	dir1="/media/"+user+"/" + nombre_usb+"/"
	#Obtenemos el directorio de la usb 
	directorio = pathlib.Path(dir1)


	#Obtenemos el nombre de archivos dentro de la usb  
	archivos=[]
	for fichero in directorio.iterdir():
		nom_file=str(fichero)
		archivos.append(nom_file[len(dir1):])
	
	archivos_ext=[]
	for extension in archivos:
		nomb,ext=os.path.splitext(extension)
		archivos_ext.append(ext)

	
	pos_y=15
	
	#Mostramos en la ventana todos los nombres de los archivos dentro de la usb 
	for archi in archivos:
			titulo=Label(vent_infousb,text=archi)
			tam_pant(vent_infousb,titulo,10,pos_y)
			pos_y=pos_y+2
	#Banderas para conocer si existe contenido de cierto tipo dentro de la usb
	band_music=False
	band_img=False
	band_vid=False
	
	#Obtenemos la extension de los archivos en la usb 
	for extens in archivos_ext:
		if extens == ".mp3" or extens == ".wav" :
			band_music=True
		elif extens == ".bmp" or extens == ".gif" or extens == ".jpg" or extens == ".png" or extens == ".jpeg":
			band_img=True
		elif extens == ".mp4" or extens == ".mov" or extens == ".mkv" or extens == ".wmv" or extens == ".flv":
			band_vid=True

	pos_y=610		
	
	#Si encontramos contenido creamos un boton a la ventana para poder visualizarlo 
	if band_music==True and band_img==False and band_vid==False:
		
		boton_music=Button(vent_infousb,text="Reproducir musica",command=lambda:rep_music(vent_infousb,archivos,dir1,nombre_usb))
		tam_pant(vent_infousb,boton_music,80,85)
		
	elif band_music==False and band_img==True and band_vid==False:
		
		boton_img=Button(vent_infousb,text="Reproducir imagenes",command=lambda:rep_img(archivos,dir1))
		tam_pant(vent_infousb,boton_img,80,80)
		
	elif band_music==False and band_img==False and band_vid==True:
		rep_vid()
		boton_vid=Button(vent_infousb,text="Reproducir video",command=lambda:rep_vid(archivos,dir1))
		tam_pant(vent_infousb,boton_vid,80,75)
		
	elif band_music==True and band_img==True and band_vid==True:
		boton_music=Button(vent_infousb,text="Reproducir musica",command=lambda:rep_music(vent_infousb,archivos,dir1,nombre_usb))
		tam_pant(vent_infousb,boton_music,80,85)
		
		boton_img=Button(vent_infousb,text="Reproducir imagenes",command=lambda:rep_img(archivos,dir1))
		tam_pant(vent_infousb,boton_img,80,80)
		
		boton_vid=Button(vent_infousb,text="Reproducir video",command=lambda:rep_vid(archivos,dir1))
		tam_pant(vent_infousb,boton_vid,80,75)
	
	
	#Boton para regresar a el menu anterior 
	boton_atras=Button(vent_infousb,text="Atras",command=lambda:lectura_usb(vent_infousb))
	tam_pant(vent_infousb,boton_atras,80,90)

	vent_infousb.mainloop()
	
	
#Funcion para reproducir musica
def rep_music(root,archivos,dir1,nombre_usb):
	#Elima la ventana anterior 
	root.destroy()
	vent_music = Tk()
	vent_music.title("Musica")
	vent_music.attributes('-fullscreen', True) 
	imagenL = ImageTk.PhotoImage(Image.open('Pro_img/fondo1.jpg'))
	lblImagen = Label(vent_music, image = imagenL).pack()
	titulo=Label(vent_music,text="Reproductor de musica")
	tam_pant(vent_music,titulo,45,1)


	#Crea una copia de la lista con los nombres de los archivos 
	archivos=archivos[:]
	#Crea una instancia vlc para una nueva lista de reproduccion
	list_player=vlc.MediaListPlayer()
	music=vlc.Instance()
	music_list=music.media_list_new()
	music_dir=[]
	#Obtenemos la extension de los arhcivos y separamos aquellas que sean musica 
	for extension in archivos:
		nomb,ext=os.path.splitext(extension)
		if ext == ".mp3" or ext == ".wav" :
			music_dir.append(extension)
	
	#Agregamos a la lista de reproduccion todas las canciones que encontremos 
	for arch_music in music_dir: 
		media=music.media_new(dir1+arch_music)
		music_list.add_media(media)
	
	#Reproducimos la lista de reproduccion 
	list_player.set_media_list(music_list)
	list_player.play() 
	
	boton_anterior=Button(vent_music,text="Anterior",command=lambda:ant(list_player))
	tam_pant(vent_music,boton_anterior,20,70)
	
	boton_play=Button(vent_music,text="Play",command=lambda:pau(list_player,0))
	tam_pant(vent_music,boton_play,40,70)
	
	boton_pau=Button(vent_music,text="Pause",command=lambda:pau(list_player,1))
	tam_pant(vent_music,boton_pau,60,70)
	
	boton_sig=Button(vent_music,text="Siguiente",command=lambda:sig(list_player))
	tam_pant(vent_music,boton_sig,80,70)
	
	boton_cerrar=Button(vent_music,text="X",command=lambda:cerrar(vent_music,list_player,nombre_usb))
	tam_pant(vent_music,boton_cerrar,85,20)
	
	time.sleep(0.5)

#Funciones para manipular la cancion en reproduccion 
def sig (list_player):
	list_player.next()
	
def ant (list_player):
	list_player.previous()
	
def pau(list_player,a):
	list_player.set_pause(a)
	
def cerrar(root,list_player,nombre_usb):
	list_player.stop()
	cont_usb(root,nombre_usb)
	
	
	

#Funcion para reproducir imagenes 
def rep_img(archivos,dir1):
	#Crea una copia de la lista con los nombres de los archivos 
	archivos=archivos[:]
	#Creamos una nueva instancia vlc 
	img=vlc.Instance()
	img_dir=[]
	#Obtenemos la extension de los archivos y separamos todas las imagenes 
	for extension in archivos:
		nomb,ext=os.path.splitext(extension)
		if ext == ".bmp" or ext == ".gif" or ext == ".jpg" or ext == ".png" or ext == ".jpeg":
			img_dir.append(extension)
		
	#Creamos un ciclo for para mostrar todas las imagenes en tipo presentacion con 5 segundos par cada imagen 	
	for nu_img in img_dir:
		player=img.media_player_new()
		media=img.media_new(dir1+nu_img)
		player.set_media(media)
		player.set_fullscreen(True)
		player.play()
		time.sleep(5)
		player.stop()

#Funcion para reproducir video 
def rep_vid(archivos,dir1):
	#Crea una copia de la lista con los nombres de los archivos 
	archivos=archivos[:]
	#Creamos una nueva instancia vlc
	vid=vlc.Instance()
	vid_dir=[]
	#Obtenemos la extension de los archivos y separamos todas los videos
	for extension in archivos:
		nomb,ext=os.path.splitext(extension)
		if ext == ".mp4" or ext == ".mov" or ext == ".mkv" or ext == ".wmv" or ext == ".flv":
			vid_dir.append(extension)
	
	#Creamos un ciclo for para mostrar todas los videos 
	for arch_vid in vid_dir: 
		player=vid.media_player_new()
		media=vid.media_new(dir1+arch_vid)
		player.set_media(media)
		player.set_fullscreen(True)
		player.play()
		time.sleep(0.5)
	
	
	
#Creamos una ventana principal 
def pant_prin(root):
	root.destroy()
	inicio_men = Tk()
	inicio_men.title("Menu")
	inicio_men.attributes('-fullscreen', True) #Maximiza la pantalla
	inicio_men.config(bg = "white")
	imagenL = ImageTk.PhotoImage(Image.open('Pro_img/fondo1.jpg'))
	lblImagen = Label(inicio_men, image = imagenL).place(x = 0, y = 0, relwidth = 1, relheight = 1)
	#Crea etiqueta y se asigna la ventana y el texto a mostrar
	titulo1=Label(inicio_men,text="Bienvenido")
	tam_pant(inicio_men,titulo1,49,1)
	

	#Crea botón que llama al menu principal y se envia la ventana actual.
	
	titulo2=Label(inicio_men,text="Ver medios usb disponibles:")
	tam_pant(inicio_men,titulo2,20,20)
	titulo3=Label(inicio_men,text="Abrir centro de streaming: ")
	tam_pant(inicio_men,titulo3,50,20)
	
		
	img_usb=PhotoImage(file='Pro_img/usb.png')
	boton_usb=Button(inicio_men,image=img_usb,command=lambda:lectura_usb(inicio_men))
	tam_pant(inicio_men,boton_usb,20,25)
	
	img_str=PhotoImage(file='Pro_img/streaming_boton.png')
	boton_streming=Button(inicio_men,image=img_str,command=lambda:abrir_principal())
	tam_pant(inicio_men,boton_streming,50,25)


	inicio_men.mainloop()


if __name__ == "__main__":
		#Inicializa ventana de bienvenida
	inicio = Tk()
	inicio.title("Menu")
	inicio.attributes('-fullscreen', True) #Maximiza la pantalla
	inicio.config(bg = "white")
	imagenL = ImageTk.PhotoImage(Image.open('Pro_img/fondo1.jpg'))
	lblImagen = Label(inicio, image = imagenL).place(x = 0, y = 0, relwidth = 1, relheight = 1)
	#Crea etiqueta y se asigna la ventana y el texto a mostrar
	titulo=Label(inicio,text="Bienvenido")
	tam_pant(inicio,titulo,49,1)
	

	#Crea botón que llama al menu principal y se envia la ventana actual.
	titulo2=Label(inicio,text="Ver medios usb disponibles:")
	tam_pant(inicio,titulo2,20,20)
	titulo3=Label(inicio,text="Abrir centro de streaming: ")
	tam_pant(inicio,titulo3,50,20)
	
	
	img_usb=PhotoImage(file='Pro_img/usb.png')
	boton_usb=Button(inicio,image=img_usb,command=lambda:lectura_usb(inicio))
	tam_pant(inicio,boton_usb,20,25)
	
	img_str=PhotoImage(file='Pro_img/streaming_boton.png')
	boton_streming=Button(inicio,image=img_str,command=lambda:abrir_principal())
	tam_pant(inicio,boton_streming,50,25)


	inicio.mainloop()

from tkinter import *
from tkinter import filedialog
from tkinter import font


root=Tk()
root.title('WordProccessor')
root.geometry('1200x660')
#Açık dosya adı için değişken ayarla
global open_status_name
open_status_name=False


#Yeni dosya oluşturma
def new_file():
    #Bir önceki texti siler
    my_text.delete('1.0',END)
    root.title('New File')
    #Statu barını güncelle
    status_bar.config(text='New File       ')
    global open_status_name
    open_status_name=False

#Dosya aç
def open_file():
    #Bi önceki texti sil
    my_text.delete('1.0',END)
    #Dosya ismini yakala
    text_file=filedialog.askopenfilename(title='Open File',filetypes=(('Text Files','*.txt'),('All Files','*.*')))
    #Dosya ismi var mı diye kontrol et
    if text_file:
     #Dosya ismini global yapıp sonradan erişim sağlama
     global open_status_name
     open_status_name=text_file
    #Status barı güncelle
    name=text_file
    status_bar.config(text=name)
    #Dosyayı aç
    text_file=open(text_file,'r')
    stuff=text_file.read()
    #Dosyayı textboxa ekleme
    my_text.insert(END,stuff)
    #Açılan dosyayı kapat
    text_file.close()

#Farklı Kaydet 
def save_as_file():
    text_file=filedialog.asksaveasfilename(defaultextension='.*',title='Save File',filetypes=(('Text Files','*.txt'),('All Files','*.*')))
    if text_file:
        #Status barı güncelleme
        name=text_file
        status_bar.config(text=name)
        #Dosyayı Kaydet
        text_file=open(text_file,'w')
        text_file.write(my_text.get(1.0,END))
        #Dosyayı Kapat
        text_file.close()

#Dosya kaydetme
def save_file():
   global open_status_name
   #Eğer dosya varsa
   if open_status_name:
     text_file=open(open_status_name,'w')
     text_file.write(my_text.get(1.0,END))
     #Dosyayı Kapat
     text_file.close()
     status_bar.config(text='Saved       ')
    #Eğer dosyayı ilk defa kaydediyorsak
   else:
      save_as_file()
        
   
#MainFrame Oluşturma
my_frame=Frame(root)
my_frame.pack(pady=5)

#Text box için scroll bar 
text_scroll=Scrollbar(my_frame)
text_scroll.pack(side=RIGHT,fill=Y)


#Text box oluşturma
my_text=Text(my_frame, width=97,height=25, font=('Helvetica',16),selectbackground='yellow',selectforeground='black',undo=True,yscrollcommand=text_scroll.set)
my_text.pack()

#Scroll barı configure et
text_scroll.config(command=my_text.yview)

#Menu oluştur
my_menu=Menu(root)
root.config(menu=my_menu)

#File menu oluştur
file_menu=Menu(my_menu,tearoff=False)
my_menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='New',command=new_file)
file_menu.add_command(label='Open',command=open_file)
file_menu.add_command(label='Save',command=save_file)
file_menu.add_command(label='Save as',command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label='Exit',command=root.quit)

#Edit menu oluştur
edit_menu=Menu(my_menu,tearoff=False)
my_menu.add_cascade(label='Edit',menu=edit_menu)
edit_menu.add_command(label='Cut')
edit_menu.add_command(label='Copy')
edit_menu.add_command(label='Paste')
edit_menu.add_command(label='Undo')
edit_menu.add_command(label='Redo')

#Sağ alta Statu Bar ekle
status_bar=Label(root, text='Ready       ',anchor=E)
status_bar.pack(fill=X,side=BOTTOM,ipady=5)


root.mainloop()
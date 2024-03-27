from tkinter import *
from tkinter import filedialog
from tkinter import font


root=Tk()
root.title('WordProccessor')
root.geometry('1200x680')
#Açık dosya adı için değişken ayarla
global open_status_name
open_status_name=False
global selected
selected=False


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


#Yazı kes
def cut_text(e):
   global selected
   #Klavyeden kısa yol(ctr+x) kullanılmış mı kontrol
   if e:
      selected=root.clipboard_get()
   else:
      if my_text.selection_get():
        #Textboxtaki seçilen metni yakala
         selected=my_text.selection_get()
        #Textboxtaki seçilen metni sil
         my_text.delete('sel.first','sel.last')
         root.clipboard_clear()
         root.clipboard_append(selected)
      
      
#Yazı kopyalama
def copy_text(e):
   global selected
   #Klavyeden kısa yol(ctr+c) kullanılmış mı kontrol
   if e:
      selected=root.clipboard_get()
   if my_text.selection_get():
      selected=my_text.selection_get()
      root.clipboard_clear()
      root.clipboard_append(selected)


#Yazı yapıştır
def paste_text(e):
   global selected
   #Klavyeden kısa yol(ctr+v) kullanılmış mı kontrol
   if e:
      selected=root.clipboard_get()
   else:
      if selected:
         position=my_text.index(INSERT)
         my_text.insert(position, selected)


#Yazı Kalınlaştırma
def bold_it():
   #Fontu oluştur
   bold_font=font.Font(my_text,my_text.cget('font'))
   bold_font.configure(weight='bold')
   #Tagi configure et 
   my_text.tag_configure('bold',font=bold_font)
   current_tags=my_text.tag_names('sel.first')
   #Tagin seçildiğini kontrol
   if 'bold' in current_tags:
      my_text.tag_remove('bold','sel.first','sel.last')
   else:
      my_text.tag_add('bold','sel.first','sel.last')
      


#Yazıyı İtalic Hale Getirme
def italics_it():
    #Fontu oluştur
   italic_font=font.Font(my_text,my_text.cget('font'))
   italic_font.configure(slant='italic')
   #Tagi configure et 
   my_text.tag_configure('italic',font=italic_font)
   current_tags=my_text.tag_names('sel.first')
   #Tagin seçildiğini kontrol
   if 'italic' in current_tags:
      my_text.tag_remove('italic','sel.first','sel.last')
   else:
      my_text.tag_add('italic','sel.first','sel.last')

#Yazının altını çizme
def underlines_it():
   #Fontu oluştur
   underline_font=font.Font(my_text,my_text.cget('font'))
   underline_font.configure(underline=True)
   #Tagi configure et 
   my_text.tag_configure('underline',font=underline_font)
   current_tags=my_text.tag_names('sel.first')
   #Tagin seçildiğini kontrol
   if 'underline' in current_tags:
      my_text.tag_remove('underline','sel.first','sel.last')
   else:
      my_text.tag_add('underline','sel.first','sel.last')


#Toolbar Oluşturma
toolbar_frame=Frame(root)
toolbar_frame.pack(fill=X)
   

#MainFrame Oluşturma
my_frame=Frame(root)
my_frame.pack(pady=5)


#Text box için scroll bar 
text_scroll=Scrollbar(my_frame)
text_scroll.pack(side=RIGHT,fill=Y)


#Yanlamasına Scroll Bar
hor_scroll=Scrollbar(my_frame,orient='horizontal')
hor_scroll.pack(side=BOTTOM,fill=X)


#Text box oluşturma
my_text=Text(my_frame, width=97,height=25, font=('Helvetica',16),selectbackground='yellow',selectforeground='black',undo=True,yscrollcommand=text_scroll.set,wrap="none",xscrollcommand=hor_scroll.set)
my_text.pack()


#Scroll barı configure et
text_scroll.config(command=my_text.yview)
#Yan Scrollbarı configure et
hor_scroll.config(command=my_text.xview)


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
edit_menu.add_command(label='Cut', command=lambda: cut_text(False),accelerator='Ctrl+X')
edit_menu.add_command(label='Copy', command=lambda: copy_text(False),accelerator='Ctrl+C')
edit_menu.add_command(label='Paste', command=lambda: paste_text(False),accelerator='Ctrl+V')
edit_menu.add_separator()
edit_menu.add_command(label='Undo',command=my_text.edit_undo,accelerator='Ctrl+Z')
edit_menu.add_command(label='Redo',command=my_text.edit_redo,accelerator='Ctrl+Y')


#Sağ alta Statu Bar ekle
status_bar=Label(root, text='Ready       ',anchor=E)
status_bar.pack(fill=X,side=BOTTOM,ipady=15)


#Kısayol Tuşlarını Düzenleme
root.bind('<Control-Key-x>', cut_text)
root.bind('<Control-Key-c>', copy_text)
root.bind('<Control-Key-v>', paste_text)


#Butonlar
bold_button=Button(toolbar_frame,text='Bold',command=bold_it)
bold_button.grid(row=0,column=0,sticky=W,padx=5)
italic_button=Button(toolbar_frame,text='Italic',command=italics_it)
italic_button.grid(row=0,column=1,padx=5)
underline_button=Button(toolbar_frame,text='Underline',command=underlines_it)
underline_button.grid(row=0,column=2,padx=5)


root.mainloop()
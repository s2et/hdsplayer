import os
from tkinter import * 
from tkinter.ttk import *
# importing askopenfile function 
# from class filedialog 
from tkinter import filedialog
root = Tk() 
root.wm_iconbitmap('@/home/s2/Documents/hds/favicon.xbm')
root.wm_title('SET SEQUENCE')
root.geometry('350x250') 
global var
global doc
doc=[]
global lb
global btn
var=0

def open_file():
	global var
	global doc
	file = filedialog.askopenfile(mode ='r', filetypes =[('Videos & Images', '*.*')])
	if file is not None:
		f=file.name
		print(file,f)
		doc.append(f)
		fn=os.path.basename(f)
		print(fn)
		var+=1
		cnr()

def change(da,ta):
	global doc
	global var
	docx=[]
	x=i=0
	print("Change",da,ta)
	print("doc",doc)
	file = filedialog.askopenfile(mode ='r', filetypes =[('Videos & Images', '*.*')])
	tb=ta-1
	if file is not None:
		print(ta,tb,file.name)
		fp=file.name
		for dx in doc:
			print(x,dx)
			if x==tb:
				docx.append(fp)
			else:
				docx.append(dx)
			x+=1
		print("docx",docx)
		doc=[]
		var=0
		clear()
		for dy in docx:
			doc.append(dy)
			var+=1
			cnr()

def clear():
	global var
	list = root.grid_slaves()
	for l in list:
		l.destroy()
	tab()
	
def remove(da,ta):
	global doc
	global lb
	global var
	print("Remove")
	docx=docy=[]
	i=0
	for dx in doc:
		if dx is not da:
			docx.append(dx)
			#var=1-i-ta	
	print(docx) 
	tb=ta-1
	doc=[]
	var=0
	clear()
	for dy in docx:
		doc.append(dy)
		var+=1
		cnr()
			
'''def rnd(d,t):
	print("rnd")
	if ".mp4"in d:
		print("Video",d)
	if ".mkv" in d:
		print("Video",d)
	if ".jpg" in d:
		print("Image",d)
	if ".jpg" in d:
		print("Image",d)
	if ".png"in d:
		print("Image",d)'''
	  
def cnr():
	global var
	global lb
	global btn
	t=0
	for d in doc:
		t+=1
		dt=os.path.basename(d)
		lb=Label(root, text = (" "+str(t)+"."), font =('Times New Roman', 12))
		lb.grid(row=t,column=0,columnspan=1)
		lb=Label(root, text = (dt), font =('Times New Roman', 12))
		lb.grid(row=t,column=1,columnspan=8)
		btn = Button(root, text ='CHANGE', command = lambda:change(d,t))
		btn.grid(row=var,column=15)
		btn = Button(root, text ='REMOVE', command = lambda:remove(d,t))
		btn.grid(row=var,column=18)
		#btn = Button(root, text ='Repeat/Duration', command = lambda:rnd(d,t))
		#btn.grid(row=var,column=20)	
	print(var)
	with open('/home/s2/Documents/hds/var1.txt', 'w') as filehandle:
		for listitem in doc:
			filehandle.write('%s\n' % listitem)
	#tab(var)	
	#var+=1
def tab():
	lb=Label(root, text = ("S.No. "),font =('Georgia',14))
	lb.grid(row=0,column=0,columnspan=1)
	lb=Label(root, text = ("File Name"),font =('Georgia', 14))
	lb.grid(row=0,column=1,columnspan=6)
	lb=Label(root, text = ("Edit Buttons"),font =('Georgia', 14))
	lb.grid(row=0,column=10,columnspan=10)
	btn=Button(root, text ='ADD FILE', command = lambda:open_file())
	btn.grid(row=100,column=1)	
	
with open('/home/s2/Documents/hds/var1.txt', 'r') as filehandle:
	for line in filehandle:
		currentPlace = line[:-1]
		doc.append(currentPlace)
		var+=1
		cnr()
tab()
print(doc)
  
mainloop() 
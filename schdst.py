import os,subprocess
from tkinter import * 
from tkinter.ttk import *
import tkinter as tk
from tkinter import filedialog
root = Tk() 
root.wm_iconbitmap('@/home/s2/Documents/hds/favicon.xbm')
root.wm_title("X=10Hrs to 22Hrs <::Set Schedule::> Y=0Mins to 59Mins")
root.geometry('1175x650') 
global doc
doc=[]
global btn
#f=open("/home/s2/Documents/hds/choda.txt","r")
#fn=f.read()
#f.close()
fpt="/home/s2/Documents/hds/"
fN="schd"
fn1=fpt+fN+".txt"
print(fn1)     
LABEL_BG = "#ccc"
ROWS, COLS = 1050, 650
ROWS_DISP = 400
COLS_DISP = 650
master_frame = tk.Frame(bg="Light Blue", bd=3, relief=tk.RIDGE)
master_frame.grid(sticky=tk.NSEW)
master_frame.columnconfigure(0, weight=1)
frame2 = tk.Frame(master_frame)
frame2.grid(row=3, column=0, sticky=tk.NW)
canvas = tk.Canvas(frame2, bg="white")
canvas.grid(row=0, column=0)
vsbar = tk.Scrollbar(frame2, orient=tk.VERTICAL, command=canvas.yview)
vsbar.grid(row=0, column=1, sticky=tk.NS)
canvas.configure(yscrollcommand=vsbar.set)
buttons_frame = tk.Frame(canvas, bg="gray", bd=2)
def open_file(h,m):
        print(h,m)
        global doc
        tp=0
        doc1=[]
        doc2=[]
        file = filedialog.askopenfile(mode ='r', filetypes =[('Videos & Images', '*.*')])
        if file is not None:
                f=file.name
                if ".mp4" in f or ".vlc" in f:
                       dur = subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","default=noprint_wrappers=1:nokey=1",f],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
                       dr1=dur.stdout.decode('utf-8')
                       print("dr1",dr1)
                       dr=str(round(float(dr1)))
                else:
                       dr="60"
                f1=str(h+10)+"="+str(m)+"="+f+"="+dr
                doc[h*60+m]=f1
                k=round(int(dr)/60)
                while tp<(k-1):
                     doc[h*60+m+tp+1]=str(h+10)+"="+str(m+tp+1)+"="+"n"+str(h+10)+str(m+tp+1)+"="+"0"
                     tp+=1 
                print(file,f1)
                print("doc[h*m]",doc[h*m])
                #print(doc)
                cnr0() 
         
                

def clear():
	global var
	list = buttons_frame.grid_slaves()
	for l in list:
                l.destroy()

def cnr0():
        with open(fn1, 'w+') as filehandle:
                   for listitem in doc:
                          filehandle.write('%s\n' % listitem)
        cnr1()
        
    	  
def cnr1():
        da=[]
        dh=[]
        dm=[]
        dp=[]
        dx=[]
        for d in doc:
          da=d.split("=")
          #print(len(da),da[0],da[1],da[2],da[3])
          du=float(da[3])/60
          #print(du,round(du))
          dt=os.path.basename(da[2])
          da0=int(da[0])-10
          #print(da0)
          dh.append(int(da[0])-10)
          dm.append(int(da[1]))
          dp.append(dt)
          dx.append(round(du))
        print(dp)
        clear()
        t=0
        vh=0
        vm=0
        vx=0#print("dh",dh,"dm",dm)
        while t<(len(doc)):
              vm=dm[t]
              vh=dh[t]
              print(vh,vm)
              if vx-2>0:
                 btn=Button(buttons_frame, text ="Disable", state='disabled').grid(row=dm[t],column=dh[t],columnspan=1)
                 vx-=1
              else:
                 btn=Button(buttons_frame, text =dp[t], command = lambda vh=vh,vm=vm:open_file(vh,vm)).grid(row=dm[t],column=dh[t],columnspan=1)
                 vx=dx[t]
              t+=1
        for g in range(10,23,1):
                 Label(buttons_frame, text = (str(g)+"Hrs"),font =('Times New Roman', 12)).grid(row=60,column=g-10,columnspan=1)
        for h in range(0,60,1):
                 Label(buttons_frame, text = (str(h)+"Mins"),font =('Times New Roman', 12)).grid(row=h,column=24,columnspan=1)  
              

        	
	

with open(fn1,'r+') as filehandle:
       for line in filehandle:
                currentPlace = line[:-1]
                doc.append(currentPlace)


if len(doc)>0:
       cnr1()

canvas.create_window((0,0), window=buttons_frame, anchor=tk.NW)
buttons_frame.update_idletasks()
bbox = canvas.bbox(tk.ALL)
w, h = bbox[2]-bbox[1], bbox[3]-bbox[1]
dw, dH = int((w/COLS) * COLS_DISP), int((h/ROWS) * ROWS_DISP)
canvas.configure(scrollregion=bbox, width=dw, height=dH)        
mainloop() 
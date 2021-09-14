import ftplib,urllib
import io,tkinter
from tkinter import *
root = Tk() 
root.wm_title('HRV')
root.geometry('150x50')
def browse_button(text):
    ft=ftplib.FTP("ftp.s2ecotech.com","gftp@guc.s2ecotech.com","0863s2ecotech")
    cmd=io.BytesIO(text)
    n=io.StringIO()
    print(cmd)
    ft.storlines("STOR fn.txt",cmd)
    while 1:
        ft.retrlines("RETR ack.txt",n.write)
        t=n.getvalue()
        if len(t)!= 0:
            if len(t)>10:
                open("statlog.txt","w").write(t)
            Label(root, text = "Done",font=('Verdana', 15)).pack(side=TOP,pady=10)
            sp=io.BytesIO(b'')
            ft.storlines("STOR fn.txt",sp)
            ft.storlines("STOR ack.txt",sp)
            break
        print("Not")
        
btn = Button(root,text="Update", command=lambda:browse_button(b"Update"))
btn.pack(side='left')
btn = Button(root,text="Test", command=lambda:browse_button(b"Play"))
btn.pack(side='left')
btn = Button(root,text="Stop", command=lambda:browse_button(b"Stop"))
btn.pack(side='left')
btn = Button(root,text="Stat", command=lambda:browse_button(b"Stat"))
btn.pack(side='left')

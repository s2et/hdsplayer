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
    ft.retrlines("RETR ack.txt",r.write)
    if len(r.getvalue())==0:
        Label(root, text = "Not Running",font=('Verdana', 15)).grid(row=3,column=2)
        ft.storlines("STOR ack.txt",io.BytesIO(b'NotRunning'))
    while 1:
        ft.retrlines("RETR ack.txt",n.write)
        t=n.getvalue()
        if len(t)!= 0:
            if len(t)>10:
                open("statlog.txt","w").write(t)
            Label(root, text = "Done",font=('Verdana', 15)).grid(row=4,column=2)
            sp=io.BytesIO(b'')
            ft.storlines("STOR fn.txt",sp)
            ft.storlines("STOR ack.txt",sp)
            break
        print("Not")
        
btn = Button(root,text="Update", command=lambda:browse_button(b"Update"))
btn.grid(row=1,column=3)
btn = Button(root,text="Test", command=lambda:browse_button(b"Test"))
btn.grid(row=1,column=1)
btn = Button(root,text="Stop", command=lambda:browse_button(b"Stop"))
btn.grid(row=1,column=4)
btn = Button(root,text="Stat", command=lambda:browse_button(b"Stat"))
btn.grid(row=1,column=5)

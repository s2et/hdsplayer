import os,subprocess,time,io,sys,signal
from ftplib import FTP
         
def loop():
         ft=FTP("ftp.s2ecotech.com","gftp@guc.s2ecotech.com","0863s2ecotech")
         n=io.StringIO()
         ft.retrlines("RETR fn.txt",n.write)
         nt=n.getvalue()
         re=open("/home/firefly/Documents/altareto/tmp.txt","r")
         pid=re.read()
         re.close()
         print(pid)
         ft.storlines("STOR ack.txt",io.BytesIO(b'Running'))
         if nt=="Stat":
             subprocess.run(["top","-p",pid," -b"," -n"," 1",">","st.txt"])
             fl=open("/home/firefly/Documents/altareto/st.txt","r")
             statz=fl.read()
             fl.close()
             da=io.BytesIO(statz.encode('utf-8'))
             ft.storlines("STOR ack.txt",da)
             #open("/home/firefly/Documents/altareto/st.txt","w+")
         if nt=="Stop":
             subprocess.run(["kill",pid])
             da=io.BytesIO(b'stopped')
             ft.storlines("STOR ack.txt",da)
             #open("/home/firefly/Documents/altareto/st.txt","w+")
             exit()
         if nt=="Update":
             subprocess.run(["kill",pid])
             subprocess.Popen("python3 /home/firefly/Documents/altareto/module1.py",shell = True)
             da=io.BytesIO(b'Updated')
             ft.storlines("STOR ack.txt",da)
             #open("/home/firefly/Documents/altareto/st.txt","w+")
            	   
while 1:
         loop()
             

     

import requests, os,subprocess,time
import vlc
playa=vlc.MediaPlayer()
playa.set_fullscreen(True)
url = 'https://guc.s2ecotech.com/gftp/links.txt'
re = requests.get(url,stream=True)
print(re.text)
doc = [ ]
i=0
t=re.text
tt=t.split(";")
pid=os.getpid()
li=open("/home/firefly/Documents/altareto/tmp.txt","w")
li.write(str(pid))
li.close()
print("tt",tt,len(tt))
def ply(tt):
  for data in tt:
      media=vlc.Media(data)
      playa.set_media(media)
      playa.play()
      time.sleep(15)
def stp():
      playa.stop()
while 1:
      ply(tt)
      i+=1
stp()     

      

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
print("tt",tt,len(tt))
def ply(tt):
  for data in tt:
      media=vlc.Media(data)
      playa.set_media(media)
      playa.play()
      time.sleep(15)
def stp():
      playa.stop()
while i<5:
      ply(tt)
      i+=1
stp()     

      

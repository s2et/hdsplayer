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
for data in tt:
      duration = subprocess.check_output(['ffprobe', '-i', data, '-show_entries', 'format=duration', '-v', 'quiet', '-of', 'csv=%s' % ("p=0")])
      doc.append(duration)
print("doc",doc)

def ply(tt):
  i=0
  while i<len(tt):
      media=vlc.Media(tt[i[)
      playa.set_media(media)
      playa.play()
      if doc[i]==b'N/A\n':
         time.sleep(20)
      else:
         dur=float(doc[i].decode().split('\n')[0])
         time.sleep(dur)
     i+=1
                           
def stp():
      playa.stop()
while 1:
      ply(tt)
      i+=1
stp()     

      

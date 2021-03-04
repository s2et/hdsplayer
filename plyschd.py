import subprocess, datetime, os,sys 
doc=[]
vd=[".mp4",".mkv",".flv"]
id=[".jpg",".jpeg",".png",".ico"]

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
          dt=da[2]
          da0=int(da[0])-10
          #print(da0)
          dh.append(da[0])
          dm.append(da[1])
          dp.append(dt)
          dx.append(float(da[3]))
        #print(dp)
        t=0
        vh=0
        vm=0
        vx=0
        #print("dh",dh,"dm",dm)
        while t<(len(doc)):
                  vm=dm[t]
                  vh=dh[t]
                  vx=dx[t]
                  nw=datetime.datetime.now()
                  #print(vh,vm)
                  if vx>0 :
                      if vh== nw.strftime("%H"):
                             if vm==nw.strftime("%M"):
                                    for pt in vd:
                                           if pt in dp[t]:
                                               subprocess.run(["mpv","--fullscreen",dp[t]])
                                               print(dp[t])
                                    for pt in id:
                                           if pt in dp[t]:
                                               subprocess.run(["mpv","--fullscreen","--image-display-duration",str(vx),dp[t]])
                                               print(dp[t]) 

                  t+=1

with open('/home/s2/Documents/hds/schd.txt', 'r') as filehandle:
             for line in filehandle:
                 currentPlace = line[:-1]
                 doc.append(currentPlace)
             print(doc)
             cnr1()
subprocess.Popen("python3 /home/s2/Documents/hds/plmpv.py", shell = True, preexec_fn=os.setsid)
while (1):
   cnr1()
 
	
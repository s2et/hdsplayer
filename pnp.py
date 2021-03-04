import os,sys,subprocess
import signal
#os.killpg(os.getpgid(pro.pid),signal.SIGTERM)
p1=subprocess.Popen(['xdotool','search','--class','mpv'],stdout=subprocess.PIPE)
out,err=p1.communicate()
ot=out.decode("utf-8")
print("ot",ot,"p1",p1)
if ot>str(0):
      subprocess.run(["xdotool","key","--window",ot,"p"])
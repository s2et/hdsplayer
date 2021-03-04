import os,sys,subprocess
import signal
#os.killpg(os.getpgid(pro.pid),signal.SIGTERM)
p=subprocess.Popen(['ps','-A'],stdout=subprocess.PIPE)
out,err=p.communicate()
ot=out.decode("utf-8")
print(ot)
for line in ot.splitlines():
      for j in ["mpv","python3"]:
               if j in line:
                     pid=int(line.split(None,1)[0])
                     os.kill(pid, signal.SIGKILL)    
#os.system("killall -9 iChat")
import subprocess, os, signal, time
subprocess.Popen("python3 /home/firefly/Documents/altareto/module0ext.py", shell = True)
time.sleep(2)
subprocess.Popen("python3 /home/firefly/Documents/altareto/module1.py", shell = True)
time.sleep(5)
subprocess.Popen("python3 /home/firefly/Documents/altareto/module2.py", shell = True)

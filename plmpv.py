import subprocess, time
doc=[]
vd=[".mp4",".mkv",".flv"]
id=[".jpg",".jpeg",".png",".ico"]
with open('/home/s2/Documents/hds/var1.txt', 'r+') as filehandle:
	for line in filehandle:
		t = line[:-1]
		print(t)
		print(line)
		doc.append(t)
		for ty in vd:
			if ty in t:
				t1=subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","default=noprint_wrappers=1:nokey=1",t],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
				print(t1.stdout)
				subprocess.run(["mpv","--fullscreen",t])
				dur=t1.stdout
				ti=float(dur)
				#time.sleep(ti)
		for ty in id:
			if ty in t:
				ti="59"
				subprocess.run(["mpv","--fullscreen","--image-display-duration",ti,t])
				#time.sleep(ti)


	
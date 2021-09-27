# hdsplayer
HRV Digital Signage Player
Runs on python3
depnedencies: python3-tk(),ffmpeg,mpv

**#hdsplayer: altareto version modules** 

#module0.py

Executes module0ext, module1 and module2 in pipe

#module0ext.py

Tkinter gui with functions to start and stop signage locally on display-end

#module1.py

depndencies: python3-vlc, ffmpeg

Extracts urls and plays in vlc

the pid of the module is written to local tmp.txt

#module2.py

communication module, continuously hits ftp file fn.txt for remote commands and delivers the responses to ftp file ack.txt

functions: Update,Status,Stop

reads pid from local tmp.txt, executes top command, reads top results written to st.txt and stores to ftp file ack.txt

#remotely.py (admin end)

dependencies: tkinter, ftplib

writes to ftp file fn.txt as per the button input, and recieves responses from ftp file ack.txt.

For stat response top command response is written to statlog.txt



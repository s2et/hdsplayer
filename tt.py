import csv
doc=[]
i=0
tp=''

filna=["10","11","12","13","14","15","16","17","18","19","20","21","22"]
for t in filna:
        for n in range(0,60,1):
                  t1=str(t)+"="+str(n)+"="+"n"+str(t)+str(n)+"="+"0"
                  doc.append(t1+"\n")

with open("/home/s2/Documents/hds/schd.txt","w+") as file_d:
         for d in doc:
               file_d.write(d)
               print(doc,len(doc))
    
#wt.writerow({"10":t,"11":t,"12":t,"13":t,"14":t,"15":t,"16":t,"17":t,"18":t,"19":t,"20":t,"21":t,"22":t})
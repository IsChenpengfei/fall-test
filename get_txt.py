import os

from os import getcwd
abs_path = os.getcwd()
print(abs_path)
paths='png'
f=open('val.txt','r+')
filenames=os.listdir(paths)
abs_path +'/images/%s.png\n'
for filename in filenames:
    if os.path.splitext(filename)[1]=='.png':
        out_path="data" +'/images/'+filename
        print(out_path)
        #f.writable(out_path+'\n')
        f.write(out_path+'\n')
f.close()
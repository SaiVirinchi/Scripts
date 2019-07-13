import os

classes = input()
imgList = os.listdir()
for name in imgList:
    file = os.path.splitext(name)[0]
    text=file+'.txt.'
    textFile=open(text,'w')
    imgtxt=classes+ ' 0.500000 0.500000 1.00000 1.00000'
    textFile.write(imgtxt)

#print(imgList)

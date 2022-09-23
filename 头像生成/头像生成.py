from PIL import Image,ImageDraw,ImageFont
import numpy

#因为这个需要不断调试，网上的算法千篇一律，出处https://blog.csdn.net/dpengwang/article/details/79076188
ascii_char  =list("MWN@QB%G$&8#ROgDKCH5S0EmdUAX693PZ2qVb4ewahkpF*Yosy[]cJ7un?f{LTx|}t<z)>v(1j=\+!Il/ri~-^;\",:`'._ ")
imgname = "input.jpg" #需要处理的文件名
fontsize=15      #几个像素缩成像素点 fontsize*fontsize为一个像素点为一个字符
backspace=-1    #文字负间距，因为没有这个文字间距离太远
zoom=2
#网上千篇一律的算法，也找不到出处了，可能是图像处理的一个算法
def get_char(r,g,b,alpha= 256):
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unitcount  = (256.0+1)/length
    return  ascii_char[int(gray/unitcount)]
img  = Image.open(imgname)#打开文件
width=int(img.width/zoom)#缩放图片宽度
height=int(img.height/zoom)#缩放图片高度
img  = img.resize((width,height),Image.NEAREST)#进行缩放
fontnumx=int(img.width/fontsize)#一行几个字符
fontnumy=int(img.height/fontsize)#一列几个字符
temp=img
temp=temp.convert("L")#暂存文件二值化
output = Image.new("RGB", (img.width,img.height), (255, 255, 255))#新建空白画布
drawBrush = ImageDraw.Draw(output)#绑定画刷
font=ImageFont.truetype("simkai.ttf",fontsize)#定义字体

#循环处理缩放后input的每一个像素
for i in range(fontnumx):
    for j in range(fontnumy):
        #统计字符块区域的特征值
        rgb=numpy.array((0,0,0))
        for k in range(fontsize):
            for l in range(fontsize):
                rgb+=numpy.array(img.getpixel((i*fontsize+k,j*fontsize+l)));
        rgb=(int(rgb[0]/fontsize/fontsize),int(rgb[1]/fontsize/fontsize),int(rgb[2]/fontsize/fontsize))
        drawBrush.text((i*(fontsize-backspace),j*(fontsize-backspace)), get_char(*rgb), (0,0,0),font=font)#在output画布上写字
outdata = numpy.array(output)#输出化为矩阵
r,g,b=outdata.T#获取rgba矩阵
needreplace=(r != 255) & (g != 255) & (b != 255)#进行条件矩阵运算
outdata[...][needreplace.T] = numpy.zeros((output.width,output.height,3))[needreplace.T]#替换字体部分
output =Image.fromarray(outdata)#写入输出图片
r, g, b = output.split()
g = g.point(lambda i: i>0 and 204)#白色不画
output = Image.composite(output,temp.convert("RGB"),g)
#output = Image.blend(output,temp.convert("RGB"),0.1)#方法二
output.show()#使用默认工具打开图片
output.save("output.jpg")#保存生成的图片到当前路径的output.jpg
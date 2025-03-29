from PIL import Image
import math
from tkinter.filedialog import askopenfilename,asksaveasfilename

flag=Image.open(askopenfilename(title='打开滤镜文件',filetypes=(('png文件(*.png)','png'),)))
file=askopenfilename(title='打开目标文件',filetypes=(('png文件(*.png)','png'),))
if file:
    head=Image.open(file)
    width,height=flag.size
    flag2=flag.crop((66,0,height+66,height))
    for i in range(height):
        for j in range(height):
            color=flag2.getpixel((i,j))
            distance=int(math.sqrt(i**2+j**2))
            alpha=255-distance//4
            if alpha<0:
                alpha=0
            new_color=color[0:-1]+(alpha,)
            flag2.putpixel((i,j),new_color)
    flag_new=flag2.resize(head.size)
    head.paste(flag_new,(0,0),flag_new)
    file=asksaveasfilename(title='保存到',filetypes=(('png文件(*.png)','png'),))
    head.save(file + ".png")
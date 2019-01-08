from PIL import Image
import os

# složka s obrázky
IMG_DIR = "obrazky"

# jména souborů v takovém uspořádání, jak se budou spojovat
names = [["Praha_4_0_13_rgb.jpg","Praha_4_0_14_rgb.jpg"],
         ["Praha_4_0_31_rgb.jpg","Praha_4_0_32_rgb.jpg"]]


images = []
for row in names:
    imgrow = []
    for name in row:
        imgrow.append(Image.open(os.path.join(IMG_DIR,name)))
    images.append(imgrow)

width = len(images[0])*images[0][0].width
height = len(images)*images[0][0].height

out_img = Image.new("RGB",(width,height))

# ve vnějším seznamu jsou uložené jednotlivé řádky,
# číslo řádku je y-ová souřadnice
for (y,row) in enumerate(images):
    for (x,img) in enumerate(row):
        out_img.paste(img,(x*img.width,y*img.height))

out_img.save("out.jpg")



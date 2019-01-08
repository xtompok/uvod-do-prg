from PIL import Image,ImageMath

im = Image.open("Beroun_0_7_42_cir.jpg")
# Oříznutí obrázku, aby postup 1) netrval moc dlouho
im = im.crop((0,im.height-1000,1000,im.height))
im.show()

# 1) Přístup přes getpixel / putpixel, pomalé
out_im = Image.new("L",(im.width,im.height))
for x in range(im.width):
    for y in range(im.height):
        nir,r,g = im.getpixel((x,y))
        ndwi = (g-nir)/(g+nir)
        out_im.putpixel((x,y),int((ndwi+1)*127))
out_im.show()

# 2) Využití třídy ImageMath, rychlé
(nir,r,g) = im.split()
out_im = ImageMath.eval("(float(g-nir)/float(g+nir)+1)*127",g=g,nir=nir)
out_im.show()

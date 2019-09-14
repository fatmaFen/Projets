"""
Author: SAAL Fatma

"""
import sys
from PIL import Image
import colors
import mathtools
def binarize(im,treeshold):
        """ This function is use to put a colour image to a white and black image
        :param im : Image to convert
        :type im: str
        :param treeshold:value to compare with the somme of value r,g,b
        :type treeshold: int
        """
        image=Image.open(im)
        im2=image.copy()
        xsize,ysize=im2.size
        for x in range(xsize):
                for y in range(ysize):
                        couleur=im2.getpixel((x,y))
                        r,g,b=couleur
                        somme=r+g+b
                        if somme<=treeshold :
                                im2.putpixel((x,y),colors.black)
                        else:
                                im2.putpixel((x,y),colors.white)


        return im2

"""
def voisin(im,pix):
"""
"""This function is use to determinate the neighberhood of pix
        :param im : an image
        :type im : image
        :param pix : a pixel
        :type pix : tuple
        :Example:
        """
"""
        voisin=[]
        size=im.size

        voisin.append((pix[0]-1,pix[1]))
        voisin.append((pix[0],pix[1]-1))
        voisin.append((pix[0],pix[1]+1))
        voisin.append((pix[0]+1,pix[1]))
        liste=[]
        for elt in voisin:
                if 0<=elt[0]<size[0] and 0<=elt[1]<size[1]:
                      liste.append(elt)

        return liste

"""
"""
def remplir(im,coords):
        im2=im.copy()
        l=[coords]
        while len(l)!=0:
                coords=l.pop()
                pixel=im2.getpixel(coords)
                if pixel==colors.white:
                        im2.putpixel(coords,colors.red)
                        vois1=voisin(im,coords)
                        for elt in vois1:
                                pix=im2.getpixel(elt)
                                if pix==colors.white:
                                        l=l+[elt]
        im2.show()
"""

def remplir(im,coords):

        im2=im.copy()
        l=[coords]
        size=im2.size
        while len(l)!=0:
                print(len(l))
                coords=l.pop()

                pixel=im2.getpixel(coords)
                if pixel==colors.white:
                        im2.putpixel(coords,colors.red)
                        q=[-1,1]
                        for elt in q :
                                if  0<=coords[0]+elt<size[0] and 0<=coords[1]<size[1]:
                                                pix=im2.getpixel((coords[0]+elt,coords[1]))
                                                if pix==colors.white:
                                                        l=l+[(coords[0]+elt,coords[1])]
                                if 0<=coords[0]<size[0] and 0<=coords[1]+elt<size[1]:
                                                pix=im2.getpixel((coords[0],coords[1]+elt))
                                                if pix==colors.white:
                                                        l=l+[(coords[0],coords[1]+elt)]

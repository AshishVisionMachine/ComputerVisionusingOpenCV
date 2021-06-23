from mask import Imagemask 
from Display import Display
from transform import transform
from ImageFilter import ImageFilter
import cv2

import numpy as np
Input_image="Input"
height=1024
width=1024
imagelist=[]
imagetitle=['ïnput','HUGH']
#input_with_filte="filter2D.jpg"
filer_size_bl=7
kheight=5
kwidth=5
std_dev=0
ksize=5

def circle_draw(image,circles):
    
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            center = (i[0], i[1])
            # circle center
            img_src=cv2.circle(image, center, 1, (0, 100, 100), 3)
            # circle outline
            radius = i[2]
            img_src=cv2.circle(image, center, radius, (255, 0, 255), 3)
    return image
    
def main():
    
    transform_o=transform(True)
    
    print("mask operation")
    dis_obj=Display(Input_image,height,width)
    im=dis_obj.Image_read()
    imagelist.append(im)

    image_mask=Imagemask(Input_image,height,width)
    #kernel_2d=image_mask.twodfilter(im)
    height_i, width_i,ch_i = im.shape
    
    #print("image height is {} image width is {} image channel is {}".format(height_i,width_i,ch_i))

    #imsat=image_mask.Image_Saturation_conversion(im)
    #img_re=np.reshape(imsat,(height_i,width_i,ch_i))
    
    imgfilter=ImageFilter(Input_image,height,width)

        
    
    img_out=cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    
    im_out=imgfilter.MedianFiler(img_out,ksize)
    #imagelist.append(im_out)
    img_cricles=image_mask.Huge_transform(im_out)
    
    #img_re=image_mask.bilateral_filter(im_out,filer_size_bl)
    #img_re=image_mask.image_border(img_re)
    img_x,img_y=transform_o.remapping_image(im,height_i,width_i)
    dst_img = cv2.remap(im, img_x, img_y, cv2.INTER_LINEAR)
    imagelist.append(dst_img)
    
    dis_obj.Display_plot(imagetitle,imagelist,len(imagetitle))
   
    





if __name__ == "__main__":
    main()
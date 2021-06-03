from mask import Imagemask 
from Display import Display
import numpy as np
Input_image="Input"
height=1024
width=1024
imagelist=[]
imagetitle=['ïnput','output']
#input_with_filte="filter2D.jpg"
filer_size_bl=7

sobel_param={
    "scale": "1",
    "depth": "3",
    "delta": "0",
    "bordertype": "cv.BORDER_DEFAULT"

}


if __name__ == "__main__":
    
    print("mask operation")
    dis_obj=Display(Input_image,height,width)
    im=dis_obj.Image_read()
    imagelist.append(im)

    image_mask=Imagemask(Input_image,height,width)
    #kernel_2d=image_mask.twodfilter(im)
    height_i, width_i,ch_i = im.shape

    #imsat=image_mask.Image_Saturation_conversion(im)
    #img_re=np.reshape(imsat,(height_i,width_i,ch_i))
    
    img_re=image_mask.bilateral_filter(im,filer_size_bl)
    #img_re=image_mask.image_border(img_re)
    im=image_mask.sobelfilter(img_re,sobel_param)
    imagelist.append(im)
    
    dis_obj.Display_plot(imagetitle,imagelist,len(imagetitle))
    
    
    
    
    
    
    
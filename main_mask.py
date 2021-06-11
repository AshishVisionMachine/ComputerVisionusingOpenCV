from mask import Imagemask 
from Display import Display
from ImageFilter import ImageFilter

import numpy as np
Input_image="Input"
height=1024
width=1024
imagelist=[]
imagetitle=['ïnput','sobel','Laplacian']
#input_with_filte="filter2D.jpg"
filer_size_bl=7
kheight=5
kwidth=5
std_dev=0

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
    #height_i, width_i,ch_i = im.shape
    
    #print("image height is {} image width is {} image channel is {}".format(height_i,width_i,ch_i))

    #imsat=image_mask.Image_Saturation_conversion(im)
    #img_re=np.reshape(imsat,(height_i,width_i,ch_i))
    
    imgfilter=ImageFilter(Input_image,height,width)

        
    
        
    im_out=imgfilter.GaussianFilter(im,kheight,kwidth,std_dev)
    #imagelist.append(im_out)
    
    img_re=image_mask.bilateral_filter(im_out,filer_size_bl)
    #img_re=image_mask.image_border(img_re)
    im=image_mask.sobelfilter(img_re,sobel_param)
    imagelist.append(im)
    
    
    im=image_mask.cannyedge(img_re)
    imagelist.append(im)
    
    dis_obj.Display_plot(imagetitle,imagelist,len(imagetitle))
    
    
    
    
    
    
    
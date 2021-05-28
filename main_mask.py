from mask import Imagemask 
from Display import Display
Input_image="Input"
height=1024
width=1024
imagelist=[]
imagetitle=['ïnput','output']
#input_with_filte="filter2D.jpg"


if __name__ == "__main__":
    
    print("mask operation")
    dis_obj=Display(Input_image,height,width)
    im=dis_obj.Image_read()
    imagelist.append(im)

    image_mask=Imagemask(Input_image,height,width)
    #kernel_2d=image_mask.twodfilter(im)
    imsat=image_mask.Image_Saturation_conversion(im)
    
    imagelist.append(imsat)
    
    dis_obj.Display_plot(imagetitle,imagelist,len(imagetitle))
    
    
    
    
    
    
    
from mask import Imagemask 
from Display import Display
Input_image="Input"
height=320
width=240
imagelist=[]
imagetitle=['ïnput','output']


if __name__ == "__main__":
    
    print("mask operation")
    dis_obj=Display(Input_image,height,width)
    im=dis_obj.Image_read()
    imagelist.append(im)

    image_mask=Imagemask(Input_image,height,width)
    kernel_2d=image_mask.twodfilter(im)
    
    imagelist.append(kernel_2d)
    
    dis_obj.Display_plot(imagetitle,imagelist,len(imagetitle))
    
    
    
    
    

from Display import Display
from ImageFilter import ImageFilter
from morpho import morplological
char="Tophat"
Input_image="Input"
testfunt="Tophat"
height=380
width=240
kheight=5
kwidth=5
std_dev=0
imagelist=[]
imagetitle=['ïnput','output']
imagetitleall=['Input','Gaussian','Median','bilateral']
ksize=5
bwidth=9
sigmacolor=75
sigmaspace=75
kernal=5
iteration=1

if __name__ == "__main__":
    print("Select option from below functions")
    if "input" in char:
        print("morpho operation")
        dis_obj=Display(Input_image,height,width)
        im=dis_obj.Image_read()
        dis_obj.display_image(im)
        
    elif "Gassian" in char :
        imgfilter=ImageFilter(Input_image,height,width)
        print("gauusian filter ") 

        
        dis_obj=Display(Input_image,height,width)
        im=dis_obj.Image_read()
        imagelist.append(im)
        
        im_out=imgfilter.GaussianFilter(im,kheight,kwidth,std_dev)
        imagelist.append(im_out)
        print("size of title \t" , len(imagetitle)) 
        dis_obj.Display_plot(imagetitle,imagelist,len(imagetitle))
    
    elif "median" in char:
        imgfilter=ImageFilter(Input_image,height,width)
        print("median filter ") 

        
        dis_obj=Display(Input_image,height,width)
        im=dis_obj.Image_read()
        imagelist.append(im)
        
        im_out=imgfilter.MedianFiler(im,ksize)
        imagelist.append(im_out)
        print("median e \t" , len(imagetitle)) 
        dis_obj.Display_plot(imagetitle,imagelist,len(imagetitle))
        
    elif "bilateral" in char:
        imgfilter=ImageFilter(Input_image,height,width)
        print("bilateral filter ") 

        
        dis_obj=Display(Input_image,height,width)
        im=dis_obj.Image_read()
        imagelist.append(im)
        
        im_out=imgfilter.bilateralFilter(im,bwidth,sigmacolor,sigmaspace)
        imagelist.append(im_out)
        print("bilateral e \t" , len(imagetitle)) 
        dis_obj.Display_plot(imagetitle,imagelist,len(imagetitle))    
        
    elif "all" in char:
        imgfilter=ImageFilter(Input_image,height,width)
        print("median filter ") 

        
        dis_obj=Display(Input_image,height,width)
        im=dis_obj.Image_read()
        imagelist.append(im)
        
        im_out1=imgfilter.GaussianFilter(im,kheight,kwidth,std_dev)
        imagelist.append(im_out1)
        
        im_out=imgfilter.MedianFiler(im,ksize)
        imagelist.append(im_out)
        
        im_out=imgfilter.bilateralFilter(im,bwidth,sigmacolor,sigmaspace)
        imagelist.append(im_out)
        
        
        print("median e \t" , len(imagetitleall)) 
        dis_obj.Display_plot(imagetitleall,imagelist,len(imagetitleall))    
        
    elif "Erosion" in char:
        imgfilter=ImageFilter(Input_image,height,width)
        print("morpho operation")
        
        dis_obj=Display(Input_image,height,width)
        im=dis_obj.Image_read()
        imagelist.append(im)
        
        
        morpho_obj=morplological(im,kernal,iteration)
        im=morpho_obj.Erosion()
        imagelist.append(im)
        
        print("Erosion e \t" , len(imagetitle)) 
        dis_obj.Display_plot(imagetitle,imagelist,len(imagetitle))

    elif "Dialation" in char:
        imgfilter=ImageFilter(Input_image,height,width)
        print("morpho operation")
        
        dis_obj=Display(Input_image,height,width)
        im=dis_obj.Image_read()
        imagelist.append(im)
        
        
        morpho_obj=morplological(im,kernal,iteration)
        im=morpho_obj.Dialation()
        imagelist.append(im)
        
        print("Dialation e \t" , len(imagetitle)) 
        dis_obj.Display_plot(imagetitle,imagelist,len(imagetitle))
        
    elif "opening" in char:
        imgfilter=ImageFilter(Input_image,height,width)
        print("morpho operation")
        
        dis_obj=Display(Input_image,height,width)
        im=dis_obj.Image_read()
        imagelist.append(im)
        
        
        morpho_obj=morplological(im,kernal,iteration)
        im=morpho_obj.Opening()
        imagelist.append(im)
        
        print("Dialation e \t" , len(imagetitle)) 
        dis_obj.Display_plot(imagetitle,imagelist,len(imagetitle))
        
    elif "Closing" in char:
        imgfilter=ImageFilter(Input_image,height,width)
        print("morpho operation")
        
        dis_obj=Display(Input_image,height,width)
        im=dis_obj.Image_read()
        imagelist.append(im)
        
        
        morpho_obj=morplological(im,kernal,iteration)
        im=morpho_obj.Closing()
        imagelist.append(im)
        
        print("Dialation e \t" , len(imagetitle)) 
        dis_obj.Display_plot(imagetitle,imagelist,len(imagetitle))
        
    elif "Morpgradient" in char:
        imgfilter=ImageFilter(Input_image,height,width)
        print("morpho operation")
        
        dis_obj=Display(Input_image,height,width)
        im=dis_obj.Image_read()
        imagelist.append(im)
        
        
        morpho_obj=morplological(im,kernal,iteration)
        im=morpho_obj.Morphogradient()
        imagelist.append(im)
        
        print("Dialation e \t" , len(imagetitle)) 
        dis_obj.Display_plot(imagetitle,imagelist,len(imagetitle))
    elif "Tophat" in char:
        imgfilter=ImageFilter(Input_image,height,width)
        print("morpho operation")
        
        dis_obj=Display(Input_image,height,width)
        im=dis_obj.Image_read()
        imagelist.append(im)
        
        
        morpho_obj=morplological(im,kernal,iteration)
        im=morpho_obj.Tophat()
        imagelist.append(im)
        
        print("Dialation e \t" , len(imagetitle)) 
        dis_obj.Display_plot(imagetitle,imagelist,len(imagetitle))    
    elif "Blackhat" in char:
        imgfilter=ImageFilter(Input_image,height,width)
        print("morpho operation")
        
        dis_obj=Display(Input_image,height,width)
        im=dis_obj.Image_read()
        imagelist.append(im)
        
        
        morpho_obj=morplological(im,kernal,iteration)
        im=morpho_obj.Blackhat()
        imagelist.append(im)
        
        print("Dialation e \t" , len(imagetitle)) 
        dis_obj.Display_plot(imagetitle,imagelist,len(imagetitle))    
#created by - Amit
from django.http import HttpResponse 
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyse(request):
    text=request.POST.get("text","default")
    
    rem_pun_check_box = request.POST.get('removePunc','off')
    capitalize_First_check_box = request.POST.get('capitalizeFirst','off')
    new_line_remover_check_box = request.POST.get('newLineRemove','off')
    space_remove_check_box = request.POST.get('spaceRemove','off')
    char_count_check_box = request.POST.get('charCount','off')
    
    
    if(rem_pun_check_box=='on'):
        analysed =""
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        
        for char in text:
            if(char in punctuations):
                pass
            else:
                analysed+=char
        params={'purpose':'Remove Punctuations', 'analysed_text':analysed}
        text = analysed
        #return render(request,'analyse.html',params)

    if(capitalize_First_check_box=='on'): 
        analysed =""
        for char in text:
            analysed+=char.upper()

        params ={'purpose':'Capitalize','analysed_text':analysed}
        text = analysed
        #return render(request,'analyse.html',params)

    if(new_line_remover_check_box=='on'):
        analysed=" "
        for char in text:
            if(char!="\n" and char!="\r"):
                analysed+=char 
        params = {'purpose':'New line remover','analysed_text':analysed}
        text = analysed
       # return render(request,'analyse.html',params)

    if(space_remove_check_box=='on'):
        analysed=""
        for char in text:
            if(char!=" "):
                analysed+=char
            
                
        params = {'purpose': "Space Remover" , 'analysed_text':analysed}
        text = analysed
        #return render(request,'analyse.html',params)   

    if(char_count_check_box=='on'):
        analysed=0
        for char in text:
            if(char!=" "):
                analysed+=1
        params={'purpose':'Character Count','analysed_text':analysed}
        text += str(analysed)
        #return render(request,'analyse.html',params)

    return render(request,'analyse.html',params)

    
    """ else:
        return HttpResponse("<h1 style=margin:auto; text-align: center;>Sorry ! Please Select Only one check box . </h1>")
 """



    


    


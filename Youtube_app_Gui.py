import customtkinter
from tkinter import *
import Youtube_RecommendationSystem as yt
import webbrowser
from PIL import ImageTk,Image
import io
import requests
response=[]

photo=[]


customtkinter.set_appearance_mode("dark")

def submit():
    keywords=entry.get()
    links=yt.find_vids(keywords)
    
    urls=links[0]
    image_urls=links[1]
    x=0
    y=0
    target_size=(320,150)
    canva=[]
    response.clear()
    photo.clear()
    for i in range(5):
        canva.append(Canvas(app,width=target_size[0],height=target_size[1],bg='#26242f'))
        
        if(i==0):
             x=80
             y=310
        elif(i==1):
             x=480
             y=310
        elif(i==2):
             x=80
             y=510
        elif(i==3):
             x=480
             y=510
        elif(i==4):
             x=280
             y=700
        canva[i].place(x=x,y=y)
        response.append(requests.get(image_urls[i]))
        img=Image.open(io.BytesIO(response[i].content))
        
         # Find the non-black region
        bbox = img.getbbox()
    
        # Crop the image to the non-black region
        cropped_img = img.crop(bbox)
    
        # Resize the cropped image
        resized_img = cropped_img.resize(target_size)
        photo.append(ImageTk.PhotoImage(resized_img))
        #linker=Label(app,image=photo[i],bg=None)
        x1 = target_size[0] // 2
        y1 = target_size[1] // 2
        
        canva[i].create_image(x1,y1,anchor=CENTER,image=photo[i])
        #linker.place(x=x,y=y)
        canva[i].bind("<Button-1>",lambda e:webbrowser.open_new_tab(urls[i]))

    
         
            
    
         

app=customtkinter.CTk()
app.geometry("700x700")
app.resizable(False,False)

title=customtkinter.CTkLabel(app,text="Unlock the best YouTube content through smart view and like detection",font=('Helvetica',15),pady=50)
title.pack()
entry = customtkinter.CTkEntry(app, placeholder_text="Enter What you would like to search",width=300)
submit_button=customtkinter.CTkButton(app,text="Submit",font=('Helvetica',15),command=submit)
entry.pack()
submit_button.pack()

app.update()



        
app.mainloop()


#Find that nice looking code image taking thing so u can put in githubp
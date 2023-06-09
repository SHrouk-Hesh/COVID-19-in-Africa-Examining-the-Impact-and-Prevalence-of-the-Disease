#Python project about COVID-19 with GUI using statistics and probability.
from tkinter import*
import tkinter as tk
import http.client
import json
conn = http.client.HTTPSConnection("coronavirus-monitor.p.rapidapi.com")
headers = {
    'x-rapidapi-host': "coronavirus-monitor.p.rapidapi.com",
    'x-rapidapi-key': "f4d2987378mshcbefff204317652p1ec503jsnff712c6cd94a"
    }
conn.request("GET", "/coronavirus/worldstat.php"
             , headers=headers)
res = conn.getresponse()
data = res.read()
dic = json.loads(data.decode("utf-8"))
fever=0
cough = 0
shor = 0
sore = 0
vomit = 0
ill = 0
epi=0
user_age=0
def start():
        global user_age
        name_get=name.get()
        user_age=int(age.get())
        print(user_age)
       
        top.destroy()
       
        top1=tk.Tk()
        top1.configure(bg='red')
       
       
       
        label= tk.Label(top1,text="Hello, Mr."+name_get,bg="red",fg="black",width=30,font="vardana 9 bold italic")
        label.grid(row=0, column=0, columnspan=9)
       
        label1=tk.Label(top1,text="Do you have any of these symptoms?    ",bg="black",fg="red",font="vardana 9 bold italic")
        label1.grid(row=1,column=0)
        label2=tk.Label(top1,text="   Yes    ",bg="black",fg="red",width=10)
        label2.grid(row=1,column=1)
        label3=tk.Label(top1,text="No",bg="black",fg="red",width=10)
        label3.grid(row=1,column=2)        
       
       
        label4=tk.Label(top1,text="1 - F E V E R    ",bg="black",fg="red", width=72,font="vardana 9 bold italic")
        label4.grid(row=2,column=0)
        def feveryes():
            global fever
            fever=2
        def feverno():
            fever=0          
        fever1 = Checkbutton(top1, command=feveryes,bg="black",fg="red")        
        fever1.grid(row=2,column=1)
        fever2 = Checkbutton(top1, command=feverno,bg="black",fg="red")        
        fever2.grid(row=2,column=2)        
       
       
        label5=tk.Label(top1,text="2 -  c o u g h     ",bg="black",fg="red", width=72,font="vardana 9 bold italic")
        label5.grid(row=3,column=0)
        def coughyes():
            global cough
            cough=2
        def coughno():
            cough=0          
        cough1= Checkbutton(top1, command=coughyes,bg="black",fg="red")        
        cough1.grid(row=3,column=1)
        cough2 = Checkbutton(top1, command=coughno,bg="black",fg="red")        
        cough2.grid(row=3,column=2)              
       
       
        label5=tk.Label(top1,text="3  - s h o r   ",bg="black",fg="red", width=72,font="vardana 9 bold italic")
        label5.grid(row=4,column=0)
        def shoryes():
            global shor
            shor=2
        def shorno():
            shor=0          
        shor1= Checkbutton(top1, command=shoryes,bg="black",fg="red")        
        shor1.grid(row=4,column=1)
        shor2 = Checkbutton(top1, command=shorno,bg="black",fg="red")        
        shor2.grid(row=4,column=2)
       
       
       
        label5=tk.Label(top1,text="4 - sore   ",bg="black",fg="red", width=72,font="vardana 9 bold italic")
        label5.grid(row=5,column=0)
        def soreyes():
            global sore
            sore=1
        def soreno():
            sore=0          
        sore1= Checkbutton(top1, command=soreyes,bg="black",fg="red")        
        sore1.grid(row=5,column=1)
        sore2 = Checkbutton(top1, command=soreno,bg="black",fg="red")        
        sore2.grid(row=5,column=2)
       
       
       
        label5=tk.Label(top1,text="5 - vomit ",bg="black",fg="red", width=72,font="vardana 9 bold italic")
        label5.grid(row=6,column=0)
        def vomityes():
            global vomit
            vomit=1
        def vomitno():
            vomit=0          
        vomit1= Checkbutton(top1, command=vomityes,bg="black",fg="red")        
        vomit1.grid(row=6,column=1)
        vomit2 = Checkbutton(top1, command=vomitno,bg="black",fg="red")        
        vomit2.grid(row=6,column=2)
       
       
       
        label5=tk.Label(top1,text="6 - i l l    ",bg="black",fg="red", width=72,font="vardana 9 bold italic")
        label5.grid(row=7,column=0)
        def illyes():
            global ill
            ill=1
        def illno():
            ill=0          
        ill1= Checkbutton(top1, command=illyes,bg="black",fg="red")        
        ill1.grid(row=7,column=1)
        ill2 = Checkbutton(top1, command=illno,bg="black",fg="red")        
        ill2.grid(row=7,column=2)
       
       
       
       
        label5=tk.Label(top1,text="7 - have you been in epidemic region, or in contact with person from that region in last 14 days   ",bg="black",fg="red", width=72,font="vardana 9 bold italic")
        label5.grid(row=8,column=0)
        def epiyes():
                global epi
                epi=1
        def epino():
                epi=0          
        epi1= Checkbutton(top1, command=epiyes,bg="black",fg="red")        
        epi1.grid(row=8,column=1)
        epi2 = Checkbutton(top1, command=epino,bg="black",fg="red")        
        epi2.grid(row=8,column=2)
       
        def x():
                top1.destroy()
                global user_age
                global epi
               
                risk = fever + cough + shor + sore + vomit + ill
                print(risk)
                top3=tk.Tk()
                top3.configure(bg='black')
                if epi ==0:
                        if risk > 4:
                       
                                label1=tk.Label(top3,text="you don't have high risk of COVID 19, it's probably flu,",bg="black",fg="red",font="vardana 9 bold italic")
                                label1.grid(row=0,column=0)
                       
                        else:
                                label2=tk.Label(top3,text="you have no risks of COVID 19 infection,",bg="black",fg="red",font="vardana 9 bold italic")
                                label2.grid(row=0,column=0)                    
                elif epi ==1:
                        if risk > 4:
                       
                                label3=tk.Label(top3,text="you have risk of infection, you should wear surgical mask and be isolated until make the test",bg="black",fg="red",font="vardana 9 bold italic")
                                label3.grid(row=0,column=0)                    
                   
                        else:
                                label4=tk.Label(top3,text="you don't have COVID 19 sign, but may you have risk because of epidemic region, ",bg="black",fg="red",font="vardana 9 bold italic")
                                label4.grid(row=0,column=0)
                               
                if (user_age >= 0) and (user_age <= 9):
                           
                        label5=tk.Label(top3,text="According to your age, if you have infected, the fatality rate of dying from COVID-19 is 0.002%",bg="black",fg="red",font="vardana 9 bold italic")
                        label5.grid(row=1,column=0)
                       
                elif (user_age >9) and (user_age <=19):
                   
                        label5=tk.Label(top3,text="According to your age, if you have infected, the fatality rate of dying from COVID-19 is 0.006%",bg="black",fg="red",font="vardana 9 bold italic")
                        label5.grid(row=1,column=0)            
                elif (user_age >19) and (user_age <= 29):
                   
                        label5=tk.Label(top3,text="According to your age, if you have infected, the fatality rate of dying from COVID-19 is 0.03%",bg="black",fg="red",font="vardana 9 bold italic")
                        label5.grid(row=1,column=0)            
       
                elif (user_age >29) and (user_age <=39):
                        label5=tk.Label(top3,text="According to your age, if you have infected, the fatality rate of dying from COVID-19 is 0.08%",bg="black",fg="red",font="vardana 9 bold italic")
                        label5.grid(row=1,column=0)            
             
                elif (user_age >39) and (user_age <=49):
                        label5=tk.Label(top3,text="According to your age, if you have infected, the fatality rate of dying from COVID-19 is 0.15%",bg="black",fg="red",font="vardana 9 bold italic")
                        label5.grid(row=1,column=0)            
         
                elif (user_age >49) and (user_age <=59):
                        label5=tk.Label(top3,text="According to your age, if you have infected, the fatality rate of dying from COVID-19 is 0.6%",bg="black",fg="red",font="vardana 9 bold italic")
                        label5.grid(row=1,column=0)            
         
                elif (user_age >59) and (user_age <=69):
                        label5=tk.Label(top3,text="According to your age, if you have infected, the fatality rate of dying from COVID-19 is 2.2%",bg="black",fg="red",font="vardana 9 bold italic")
                        label5.grid(row=1,column=0)            
       
                elif (user_age >69) and (user_age <=79):
                        label5=tk.Label(top3,text="According to your age, if you have infected, the fatality rate of dying from COVID-19 is 5.1%%",bg="black",fg="red",font="vardana 9 bold italic")
                        label5.grid(row=0,column=0)            
       
                else:
                        label5=tk.Label(top3,text="According to your age, if you have infected, the fatality rate of dying from COVID-19 is 9.3%",bg="black",fg="red",font="vardana 9 bold italic")
                        label5.grid(row=1,column=0)  
                def v():
                        top3.destroy()
                        top4=tk.Tk()
                        top4.configure(bg='black')
                        label1=tk.Label(top4,text="SOME ADVICES FOR YOUR SAFETY FROM CORONA",bg="red",fg="black",font="vardana 9 bold italic")
                        label1.grid(row=0,column=0)
                        label1=tk.Label(top4,text="Safety from 'CORONA' is hidden in 'CORONA' word itself",bg="red",fg="black",font="vardana 9 bold italic")
                        label1.grid(row=1,column=0)
                        label1=tk.Label(top4,text="       C -           Clean Your Hands",bg="black",fg="red",font="vardana 9 bold italic")
                        label1.grid(row=2,column=0)
                        label1=tk.Label(top4,text="       O -       Off From Gatherings",bg="black",fg="red",font="vardana 9 bold italic")
                        label1.grid(row=3,column=0)
                        label1=tk.Label(top4,text="       R -       Raise Your Immunity",bg="black",fg="red",font="vardana 9 bold italic")
                        label1.grid(row=4,column=0)
                        label1=tk.Label(top4,text="             O -      Only Sick to Wear Mask",bg="black",fg="red",font="vardana 9 bold italic")
                        label1.grid(row=5,column=0)
                        label1=tk.Label(top4,text="       N -            No to Hand Shake",bg="black",fg="red",font="vardana 9 bold italic")
                        label1.grid(row=6,column=0)
                        label1=tk.Label(top4,text="       A -                Avoid Rumours",bg="black",fg="red",font="vardana 9 bold italic")
                        label1.grid(row=7,column=0)  
                        label1=tk.Label(top4,text="Stay Alert, Stay Healthy.,Stay in your home......",bg="red",fg="black",font="vardana 9 bold italic")
                        label1.grid(row=8,column=0)                
                       
                       
                       
                        top4.mainloop()
           
                Next_button=tk.Button(top3,text="Next",bg="red",fg="black",command=v,width=92,font="vardana 9 bold italic")
                Next_button.grid(row=2,column=0)
               
               
               
                top3.mainloop()
       
        button4=tk.Button(top1,text="Next",bg="yellow",fg="black",command=x,width=95,font="vardana 9 bold italic")
        button4.grid(row=9,column=0,columnspan=3)
       
       
        top1.mainloop()
     
   
#user_age= age.get()    
top=tk.Tk()
top.configure(bg='black')

label=tk.Label(top,text="World Statistics - Corona Virus\n"+"Last Updated at: "+dic["statistic_taken_at"]+"GMT",bg="black",fg="red",font="vardana 9 bold italic")
label.grid(row=0,column=0,columnspan=150)
label1=tk.Label(top,text="Total cases: "+dic["total_cases"],bg="red",font="vardana 9 bold italic",width=25)
label1.grid(row=1,column=0,columnspan=150)
label2=tk.Label(top,text="Total deaths: "+dic["total_deaths"],bg="red",font="vardana 9 bold italic",width=25)
label2.grid(row=2,column=0,columnspan=150)
label3=tk.Label(top,text="Total recovered: "+dic["total_recovered"],bg="red",font="vardana 9 bold italic",width=25)
label3.grid(row=3,column=0,columnspan=150)
label4=tk.Label(top,text="New Cases: "+dic["new_cases"],bg="red",font="vardana 9 bold italic",width=25)
label4.grid(row=4,column=0,columnspan=150)
label5=tk.Label(top,text="Enter yor name :",bg="red",font="vardana 9 bold italic",width=25)
label5.grid(row=5,column=0)
name = Entry(top, bd=5,bg="yellow",fg="black")
name.grid(row=5,column=2)
label6=tk.Label(top,text="Enter your age :",bg="red",font="vardana 9 bold italic",width=25)
label6.grid(row=6,column=0)
age = Entry(top, bd=6,bg="yellow",fg="black")
age.grid(row=6,column=2)
button=tk.Button(top,text="Start",bg="yellow",font="vardana 9 bold italic",width=50,command=start)
button.grid(row=7,column=0,columnspan=150)
top.mainloop()


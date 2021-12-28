import pyttsx3
import sys

engine = pyttsx3.init()
engine.say("Hello, Welcome to my program. I'm siavash partownia , your new assistant. To continue, please give me some information.")
engine.runAndWait()


engine = pyttsx3.init()
engine.say("What is your firstname?")
engine.runAndWait()
firstname = input()


engine = pyttsx3.init()
engine.say("Nice name. What's your lastname?")
engine.runAndWait()
lastname = input()


engine = pyttsx3.init()
engine.say("Are you male, or female")
engine.runAndWait()
gender = input()
while gender != "male" and gender != "female":
    engine = pyttsx3.init()
    engine.say("I didn't get you correctly!!! please enter a word between , male, and, female.")
    engine.runAndWait()
    gender = input()

if gender == "male":
    pish = "Mr. "
    work = "out"

if gender == "female":
    pish = "Miss"
    work = "home"











engine = pyttsx3.init()
engine.say("May I ask your Age?")
engine.runAndWait()
age = int(input())

strage = str(age)
while age < 1 or age > 110:
    engine = pyttsx3.init()
    engine.say("What!??? You are " + strage + " years old ??. This is impossible! Please enter, a real age.")
    engine.runAndWait()
    age = int(input())
    strage = str(age)



if age == 5:
    engine = pyttsx3.init()
    engine.say("Sorry little ," + firstname + ". But you are a little young for this. You can use me next year. See you soon. Bye ")
    engine.runAndWait()
    exit()

elif age < 5:
    myears = 6 - age
    more_years = str(myears)
    engine = pyttsx3.init()
    engine.say("Sorry little ," + firstname + ". But you are so young for this. You can use me in " + more_years + " years. See you soon. Bye ")
    engine.runAndWait()
    exit()










#elementry school













elif age >= 6 and age <= 11 :
    nickname = "Dear " + firstname
    job = "student"
    engine = pyttsx3.init()
    engine.say("How are you dear," + firstname + ". It looks like that you go to elementry school. Is that right?")
    engine.runAndWait()
    element_y_n = input()
    while element_y_n != "yes" and element_y_n != "no":
        engine = pyttsx3.init()
        engine.say("I didn't get you correctly!!! please enter a word between , yes, and, no.")
        engine.runAndWait()
        element_y_n = input()
  
  


  
    if element_y_n == "yes":
        school_type = "elementry school"
        engine = pyttsx3.init()
        engine.say("Ok. so, which grade are you in?")
        engine.runAndWait()
        grade = int(input())
        strgrade = str(grade)
     
     
        while (grade != 1) and (grade != 2) and (grade != 3) and (grade != 4) and (grade !=  5) and (grade != 6):
            strgrade = str(grade)
            engine = pyttsx3.init()
            engine.say("How can it be?! You're studying in the elementry school , and you're in the " + strgrade +"th grade??! That's impossible. please enter a number from , 1, to , 6.")
            engine.runAndWait()
            grade = int(input())  
        engine = pyttsx3.init()
        engine.say("Very well, I can give you some good websites and books for " + strgrade + "th grade. There are some good websites like, roshd.ir , paresh.ir , gama.ir , and there are some good books too, like , mobtakeran books.")
        engine.runAndWait()
        engine = pyttsx3.init()
        engine.say("Were these usefull?")
        engine.runAndWait()
        info_element_use = input()
       
        while info_element_use != "yes" and info_element_use != "no":
            engine = pyttsx3.init()
            engine.say("I didn't get you correctly!!! please enter a word between , yes, and, no.")
            engine.runAndWait()
            info_element_use = input()
        if info_element_use == "yes":
            engine = pyttsx3.init()
            engine.say("Very well, I hope that you make the best scores at school. I try to help you as much I can.")
            engine.runAndWait()   
        if info_element_use == "no":
            engine = pyttsx3.init()
            engine.say("Ok, I'l try to give you better information next time.")
            engine.runAndWait()      
                  
    



    if element_y_n == "no":
        engine = pyttsx3.init()
        engine.say("Realy?! That's a little wierd. But, Anyway, where do you study?")
        engine.runAndWait()    
        school_type = input() 
        while school_type != "pre school" and school_type != "high school" and school_type != "univercity" :
            engine = pyttsx3.init()
            engine.say("I didn't get you correctly!!! please enter a word between , pre school,  high school, and , univercity.")
            engine.runAndWait()
            school_type = input()
        if school_type == "pre school" or school_type == "high school":
            engine = pyttsx3.init()
            engine.say("Ok. so, which grade are you in?")
            engine.runAndWait()
            grade = int(input())
            strgrade = str(grade)
            while (school_type == "pre school" and grade != 1 and grade != 2) or (school_type == "high school" and grade != 7 and grade != 8 and grade != 9 and grade != 10 and grade != 11 and grade != 12):
                engine = pyttsx3.init()
                engine.say("How can it be?! You're studying in the " + school_type + " , and you're in the " + strgrade +"th grade??! That's impossible. Please enter a number related to your school type.")
                engine.runAndWait()   
                grade = int(input()) 
            strgrade = str(grade)       
            engine = pyttsx3.init()
            engine.say("Very well, I can give you some good websites and books for " + strgrade + "th grade. There are some good websites like, kanoon.ir , gama.ir , and there are some good books too, like , mobtakeran books, and , Kheyli sabz books.")
            engine.runAndWait()
            engine = pyttsx3.init()
            engine.say("Were these usefull?")
            engine.runAndWait()
            info_element_use = input()
        
            while info_element_use != "yes" and info_element_use != "no":
                engine = pyttsx3.init()
                engine.say("I didn't get you correctly!!! please enter a word between , yes, and, no.")
                engine.runAndWait()
                info_element_use = input()
            if info_element_use == "yes":
                engine = pyttsx3.init()
                engine.say("Very well, I hope that you make the best scores at school. I try to help you as much I can.")
                engine.runAndWait()   
            if info_element_use == "no":
                engine = pyttsx3.init()
                engine.say("Ok, I'l try to give you better information next time.")
                engine.runAndWait()      



















#high school












    













if age >= 12 and age <= 17 :
    nickname =  firstname
    job = "student"
    engine = pyttsx3.init()
    engine.say("How are you ," + firstname + ". It looks like that you go to high school. Is that right?")
    engine.runAndWait()
    high_y_n = input()
    while high_y_n != "yes" and high_y_n != "no":
        engine = pyttsx3.init()
        engine.say("I didn't get you correctly!!! please enter a word between , yes, and, no.")
        engine.runAndWait()
        high_y_n = input()
  
  


  
    if high_y_n == "yes":
        school_type = "high school"
        engine = pyttsx3.init()
        engine.say("Ok. so, which grade are you in?")
        engine.runAndWait()
        grade = int(input())
        strgrade = str(grade)
     
     
        while (grade != 7) and (grade != 8) and (grade != 9) and (grade != 10) and (grade !=  11) and (grade != 12):
            strgrade = str(grade)
            engine = pyttsx3.init()
            engine.say("How can it be?! You're studying in the high school , and you're in the " + strgrade +"th grade??! That's impossible. please enter a number from , 7, to , 12.")
            engine.runAndWait()
            grade = int(input())  
        engine = pyttsx3.init()
        engine.say("Very well, I can give you some good websites and books for " + strgrade + "th grade. There are some good websites like, kanoon.ir ,  gama.ir , and there are some good books too, like , mobtakeran books , and Kheyli sabz books.")
        engine.runAndWait()
        engine = pyttsx3.init()
        engine.say("Were these usefull?")
        engine.runAndWait()
        info_high_use = input()
       
        while info_high_use != "yes" and info_high_use != "no":
            engine = pyttsx3.init()
            engine.say("I didn't get you correctly!!! please enter a word between , yes, and, no.")
            engine.runAndWait()
            info_high_use = input()
        if info_high_use == "yes":
            engine = pyttsx3.init()
            engine.say("Very well, I hope that you make the best scores at school. I try to help you as much I can.")
            engine.runAndWait()   
        if info_high_use == "no":
            engine = pyttsx3.init()
            engine.say("Ok, I'l try to give you better information next time.")
            engine.runAndWait()      
                  
    



    if high_y_n == "no":
        engine = pyttsx3.init()
        engine.say("Realy?! That's a little wierd. But, Anyway, where do you study?")
        engine.runAndWait()    
        school_type = input() 
        while school_type != "pre school" and school_type != "elementry school" and school_type != "univercity" :
            engine = pyttsx3.init()
            engine.say("I didn't get you correctly!!! please enter a word between , pre school,  elementry school, and , univercity.")
            engine.runAndWait()
            school_type = input()
        if school_type == "pre school" or school_type == "elementry school":
            engine = pyttsx3.init()
            engine.say("Ok. so, which grade are you in?")
            engine.runAndWait()
            grade = int(input())
            strgrade = str(grade)
            while (school_type == "pre school" and grade != 1 and grade != 2) or (school_type == "elementry school" and grade != 1 and grade != 2 and grade != 3 and grade != 4 and grade != 5 and grade != 6):
                engine = pyttsx3.init()
                engine.say("How can it be?! You're studying in the " + school_type + " , and you're in the " + strgrade +"th grade??! That's impossible. Please enter a number related to your school type.")
                engine.runAndWait()   
                grade = int(input()) 
            strgrade = str(grade)       
            engine = pyttsx3.init()
            engine.say("Very well, I can give you some good websites and books for " + strgrade + "th grade. There are some good websites like, kanoon.ir , gama.ir , and there are some good books too, like , mobtakeran books, and , Kheyli sabz books.")
            engine.runAndWait()
            engine = pyttsx3.init()
            engine.say("Were these usefull?")
            engine.runAndWait()
            info_high_use = input()
        
            while info_high_use != "yes" and info_high_use != "no":
                engine = pyttsx3.init()
                engine.say("I didn't get you correctly!!! please enter a word between , yes, and, no.")
                engine.runAndWait()
                info_high_use = input()
            if info_high_use == "yes":
                engine = pyttsx3.init()
                engine.say("Very well, I hope that you make the best scores at school. I try to help you as much I can.")
                engine.runAndWait()   
            if info_high_use == "no":
                engine = pyttsx3.init()
                engine.say("Ok, I'l try to give you better information next time.")
                engine.runAndWait()      



if age >= 18 and age <= 25 :
    nickname =  pish + firstname
    job = "collegian"
    engine = pyttsx3.init()
    engine.say("How are you  " + pish + firstname + ". It looks like that you go to univercity. Is that right?")
    engine.runAndWait()
    univer_y_n = input()
    while univer_y_n != "yes" and univer_y_n != "no":
        engine = pyttsx3.init()
        engine.say("I didn't get you correctly!!! please enter a word between , yes, and, no.")
        engine.runAndWait()
        univer_y_n = input()


    if univer_y_n == "yes":
        grade = ""
        school_type = "univercity"
        engine = pyttsx3.init()
        engine.say("Ok. so, What academic field do you have?")
        engine.runAndWait()
        academic_f = input()
        
        engine = pyttsx3.init()
        engine.say("Very well., I hope you  to be successful")
        engine.runAndWait()
        engine = pyttsx3.init()

    if univer_y_n == "no":
        engine = pyttsx3.init()
        engine.say("Realy?! Well, I didn't expect that. But, Anyway, What do you do and what's your job?")
        engine.runAndWait()    
        job = input("I'm a : ") 
        engine = pyttsx3.init()
        engine.say("Ok,. So I remember , that you are a " + job )
        engine.runAndWait()



#job


if age > 25 :
    nickname =  pish + lastname
    engine = pyttsx3.init()
    engine.say("How are you" + nickname + "?")
    engine.runAndWait()    
    if gender == "male":
        engine = pyttsx3.init()
        engine.say("Can you tell me please that,  What do you do and what's your job?")
        engine.runAndWait()    
        job = input("I'm a : ") 
        engine = pyttsx3.init()
        engine.say("Ok,. So I remember , that you are a " + job )
        engine.runAndWait()  
    if gender == "female":
        job = "housewife"
        engine = pyttsx3.init()
        engine.say("I think that you are a housewife. Is that right " + nickname + "?")
        engine.runAndWait()        
        h_w_r_w = input()
        while h_w_r_w != "yes" and h_w_r_w != "no":
            engine = pyttsx3.init()
            engine.say("I didn't get you correctly!!! please enter a word between , yes, and, no.")
            engine.runAndWait()
            h_w_r_w = input()
        if h_w_r_w == "yes":
            job == "housewife"
        if h_w_r_w == "no":
            engine = pyttsx3.init()
            engine.say("Realy?!. So, What do you do and what's your job?")
            engine.runAndWait()    
            job = input("I'm a : ")
            engine = pyttsx3.init()
            engine.say("Ok,. So I remember , that you are a " + job )
            engine.runAndWait()            




































engine = pyttsx3.init()
engine.say("Thanks for giving this information. The program hasn't finishd yet. we will release a new update very soon, so you can enjoy using me , and I can help you much more. See you soon. ")
engine.runAndWait()







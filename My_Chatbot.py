from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
import spacy
import pyttsx3 as pp
import speech_recognition as s
import threading

bot=ChatBot("My Bot")

convo=[
    'hello',
    'hi there !',
    'what is your name ?',
    'My name is Bot , i am created by Shivam',
    'how are you ?',
    'I am doing great these days',
    'thank you',
    'In which city you live ?',
    'I live in lucknow',
    'Do you know Vandana?',
    'Yes I know her',
    'Who is Vandana?',
    'She is your cloooooooosssseee Freind.',
    'In which language you talk?',
    'I mostly talk in english'
]
trainer=ListTrainer(bot)

# Now training the bot with the help of trainer 

trainer.train(convo)

# answer=bot.get_response("What is your name ?")
# print(answer)

# print("Talk to bot : ")
# while True:
#     query=input()
#     if query=='exit':
#         break
#     answer=bot.get_response(query)
#     print("bot : ",answer)



main=Tk()

main.geometry("400x450") 
main.title("My chat bot")
img=PhotoImage(file="C:\\Users\\Shivam\\Desktop\\Python files\\bot2.png")
photoL=Label(main,image=img)
photoL.pack(pady=5)

# take query: it takes audio as input from user and convert it to string.

def takeQuery():
    sr=s.Recognizer()
    sr.pause_threshold=1
    print("your bot is listening try to speak")
    with s.Microphone() as m:
        try:
            sr.adjust_for_ambient_noise(m)
            audio=sr.listen(m)
            query=sr.recognize_google(audio)
            print(query)
            textF.delete(0,END)
            textF.insert(0,query)
            ask_from_bot()
        except Exception as e:
            print(e)
            print("not recognized")
def ask_from_bot():
    query=textF.get()
    answer_from_bot=bot.get_response(query)
    msgs.insert(END,"you : " + query)
    print(type(answer_from_bot))
    msgs.insert(END,"bot : " + str(answer_from_bot))
    speak(answer_from_bot)
    textF.delete(0,END)
    msgs.yview(END)
    




frame=Frame(main)

sc=Scrollbar(frame)
msgs=Listbox(frame,width=70,height=15, yscrollcommand=sc.set)
sc.pack(side=RIGHT,fill=Y)

msgs.pack(side=LEFT, fill=BOTH, pady=5)
frame.pack()

textF=Entry(main,font=("Verdana",20))
textF.pack(fill=X,pady=10)

# creating text field
btn=Button(main,text="Ask from bot", font=("Verdana",20), command=ask_from_bot)
btn.pack()


#creating a function
def enter_function(event):
    btn.invoke()

# going to bind main window with enter key..
main.bind('<Return>',enter_function)

def repeatL():
    while True:
        takeQuery()

t=threading.Thread(target=repeatL)
t.start()

main.mainloop()
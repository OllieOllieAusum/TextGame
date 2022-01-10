import tkinter as tk
from gamefunctions import functions
gameframe = tk.Tk()
inputbox = tk.Entry(master=gameframe)
inputbox.grid(row=3,column=2,sticky="ew")
outputcontents = ""
def appendoutput(content):
    global outputcontents
    outputcontents = outputcontents + "\n" + str(content)
resultsContents = tk.StringVar()
outputbox = tk.Label(master=gameframe,textvariable=str(outputcontents),height=100, background="black", foreground="white",anchor="sw")
outputbox.grid(row=0,column=2,sticky="sew",rowspan=3)
outputbox['textvariable'] = resultsContents
gameframe.columnconfigure(2, minsize=250,weight=1)
gameframe.rowconfigure(1, minsize=100,weight=1)
def keypress(event):
    returntable = inputbox.get().split(" ")
    appendoutput(inputbox.get())
    inputbox.delete(0, tk.END)
    resultsContents.set(outputcontents)
while True:
    gameframe.bind("<Return>",keypress)
    gameframe.update()

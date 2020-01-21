from tkinter import messagebox
import tkinter
output = ""
encode1 = "abcdefghijklmnopqrstuvwxyz1234567890,./?[]{}()*&^%$#@! "
encode2 = " !@#$%^&*(){}[]?/.,0987654321nopqrstuvwxyzabcdefghijklm"
decode1 = "abcdefghijklmnopqrstuvwxyz1234567890,./?[]{}()*&^%$#@! "
decode2 = " !@#$%^&*(){}[]?/.,0987654321nopqrstuvwxyzabcdefghijklm"
choice = True
txt = ''


def encode():
    global output
    for i in range(len(txt)):
        for x in range(len(encode1)):
            if txt[0 + i] == encode1[x - 1]:
                output += encode2[x - 1]
    messagebox.showinfo("The output", output)
    file = open("encoded.txt","w")
    file.write(output)
    file.close()
    end()

def decode():
    global output
    for i in range(len(txt)):
        for x in range(len(decode1)):
            if txt[0 + i] == decode2[x - 1]:
                output += decode1[x - 1]
    messagebox.showinfo("The output", output)
    file = open("decoded.txt", "w")
    file.write(output)
    file.close()
    end()


def mainEncode():
    global txt
    txt = tkinter.simpledialog.askstring("Enter Text", "Enter the text you would like to encode")
    encode()


def mainDecode():
    global txt
    txt = tkinter.simpledialog.askstring("Enter Text", "Enter the text you would like to decode")
    decode()


def getinfo():
    global choice
    choice = messagebox.askyesno("What to do?", "Would you like to encode?")
    if choice:
        mainEncode()
    else:
        choice = messagebox.askyesno("What to do?", "Would you like to decode?")
        if choice:
            mainDecode()
def end():
    global output, txt
    cont = messagebox.askyesno("Would you like to continue?", "Would you like to continue?")
    if cont:
        txt = ""
        output = ""
        getinfo()



getinfo()


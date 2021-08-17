from tkinter import *
from tkinter import font
from random import randint
import tkinter
import tkinter.ttk as ttk


'''
Encryption method
reverse the text completely
decide to shift the ascii value of the letter to left or  right (R or L)
magnitude to shift ascii value: the 1/9th of the sum of 3 random letters A-Z
Key has 3 random symbols in the start and in the end
Key example: @!#RAGS#@$
'''


def encrypting():
    symbols='!@#$%^+_=-?'
    symbols=list(symbols)
    directions=['R','L']
    magnitude=[chr(randint(65,90)) for x in range(3)]
    

    def save_results(*results):
        
        with open('key_text.txt','a',encoding='utf-8') as f:
            f.write(results[0]+'\n'+results[1])
            
        Label(enc_root,text='Data Saved!!').pack()

    def encrypt(text=NONE):
        if text:
            
            dec_key=directions[randint(0,1)] + ''.join(magnitude)
            start=[symbols[randint(0,10)] for _ in range(3)]
            start=''.join(start)
            end_symb=[symbols[randint(0,10)] for _ in range(3)]
            end_symb=''.join(end_symb)
            dec_key_label=Label(enc_root,text=f' Decyphering KEY ==> {start+dec_key+end_symb} ')
            dec_key_label.pack(pady=5)
            val=0
            for i in magnitude:
                val+=ord(i)
            val//=9
            
            if dec_key[0]=='R':
                mag=val
            elif dec_key[0]=='L':
                mag=-val
            
            
            cipher_text=list(text[::-1])
            
            if '\n' in cipher_text:
                cipher_text.remove('\n')
            
            for i in range(len(cipher_text)):
                
                new_char=ord(cipher_text[i])+mag
                try:
                    cipher_text[i]=chr(new_char)
                except:
                    Label(enc_root,text='UNKNOWN ERROR RECEIVED! TRY AGAIN PLZ!').pack()
                    
                
            cipher_text=''.join(cipher_text)

            ciphertext_label=Message(enc_root,text=f' Cipher TEXT ==> {cipher_text} ')
            ciphertext_label.pack(pady=5)

            save_btn=Button(enc_root,text="Save Results?",borderwidth=3,relief='solid',padx=5,command=lambda:save_results(start+dec_key+end_symb,cipher_text))
            save_btn.pack(pady=10)
        
            

    enc_root=Toplevel()
    enc_root.title("Let's hide some messages, shall we?")
    enc_root.minsize(width=500,height=500)
    enc_root.configure(background='lightblue')

    message=Label(enc_root,text='ENTER YOUR TEXT HERE:',borderwidth=3,relief='solid',padx=5)
    message.pack(pady=20)
    message['font']=font.Font(size=17)

    ttk.Style().configure("TEntry", padding=(100,10 ,10 ,10) , relief="flat")
    text_box=tkinter.Text(enc_root, width=100,height=5)
    text_box.insert(tkinter.END,'Enter your text here')
    
    text_box.pack(padx=30)

    result_btn=Button(enc_root,text='Get Results', width=10,height=2,padx=2,pady=2,command=lambda: encrypt(text_box.get(1.0,END)),borderwidth=3,relief='solid')
    result_btn.pack(pady=10)
    
   


def decrypting():

    def decrypt(key,text):
        if key and text:

            direction=key[3]
            magnitude=key[4:7]
            val=0
            for i in magnitude:
                val+=ord(i)
            val//=9
            if direction=='R':
                val=-val

            dec_msg=list(text[::-1])
            for i in range(len(dec_msg)):
                
                new_char=ord(dec_msg[i])+val
                dec_msg[i]=chr(new_char)
                
            dec_msg=''.join(dec_msg)
            dec_msg_label=Message(dec_root,text=f' The message is ==> {dec_msg} ')
            dec_msg_label.pack(pady=5)

            save_btn=Button(dec_root,text="Save Results?",borderwidth=3,relief='solid',padx=5,command=lambda:save_results(dec_msg))
            save_btn.pack(pady=10)
        
    def save_results(results):
        deciphered_text=''
        with open('deciphered_text','a',encoding='utf-8') as f:
            f.write(results+'\n---------------------\n')
            
        Label(dec_root,text='Data Saved!!').pack()

    dec_root=Toplevel()
    dec_root.title("Let's unhide some messages shall we?")
    dec_root.minsize(width=400,height=300)
    dec_root.configure(background='cornflowerblue')

    message=Label(dec_root,text='He who needs to know only needs but one key:',borderwidth=3,relief='solid',padx=5)
    message.pack(pady=20)
    message['font']=font.Font(size=13)

    ttk.Style().configure("TEntry", padding=(100,10 ,10 ,10) , relief="flat")
    text_box=ttk.Entry(dec_root, width=50)
    text_box.insert(3,'Enter your ciphered text here!')
    text_box.pack(padx=30,pady=10)

    ttk.Style().configure("TEntry", padding=(100,10 ,10 ,10) , relief="flat")
    key_box=ttk.Entry(dec_root, width=50)
    key_box.insert(3,'Enter your secret KEY here!')
    key_box.pack(padx=30)

    
    
    result_btn=Button(dec_root,text='Decypher!!', width=10,height=2,padx=2,pady=2,command=lambda: decrypt(key_box.get(),text_box.get()),borderwidth=3,relief='solid')
    result_btn.pack(pady=10)




def main():

    root=Tk()
    root.title("Safeguard Your Messages!!")
    root.configure(background='cadetblue')
    width=500
    height=400
    root.minsize(width=width, height=height)
    root.resizable(width=False,height=False)

    message=Label(root, text='What be your purpose here?',padx=4,pady=4,borderwidth=3,relief="solid")
    encrypt_btn=Button(root,text='ENCRYPT', width=10,height=2, padx=1,pady=1,command=encrypting,borderwidth=3,relief="solid")
    decrypt_btn=Button(root,text='DECRYPT', width=10,height=2, padx=1,pady=1,command=decrypting,borderwidth=3,relief="solid")

    message.place(x=width//5,y=height//3)
    message['font']=font.Font(size=17)

    encrypt_btn.place(x=width//5+55,y=height//3+55)
    decrypt_btn.place(x=width//5+160,y=height//3+55)
    root.mainloop()

main()
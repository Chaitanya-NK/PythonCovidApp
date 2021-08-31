from tkinter import simpledialog
import tkinter
top=tkinter.Tk()
top.title('PM CARES fund')
v=tkinter.IntVar()
file=open('details.txt','a')
def details():
    b3=tkinter.Button(top,text="Print transcation details",command=recepet).grid(row=r+3,column=0)
def recepet():
    j=0
    top.destroy()
    print("   Transaction Details")
    print("-*-*-*-*-*-*-*-*-*-*-*-*-")
    for i in list:
        print(i,"=",m[j])
        j+=1
    print('\n')
    
def show():
    label=tkinter.Label(top,text="Thank you for donating",fg="red",bg="light blue").grid(row=r+2,column=1)
    details()
def donate():
    global r
    global list;global m
    r=1;list=['Name of the person','Amount','Bank name'];l=['Googlepay','Phonepay','paytm','Rupay'];m=[];k=1
    for i in list:
        label=simpledialog.askstring(title="Donation",prompt=i)
        if label is None:
            m=[]
            break
        else:
            m.append(label)
    file.write('\nDonation \nName: {} \nAmount: {} \nBank Name: {}'.format(m[0],m[1],m[2]))
    file.close()
    if m==[]:
        b4=tkinter.Button(top,text = "Click and Quit", command = top.destroy).grid(row=r,column=1)
    else:
        tkinter.Label(top,text="Mode of payment").grid(row=r,column=0)
        for i in l:
            tkinter.Radiobutton(top,text=i,padx=30,variable=v,value=k).grid(row=r,column=1)
            k+=1
            r+=1
        b2=tkinter.Button(top,text="Submit",command=show).grid(row=r+1,column=0)
def con():
    b1=tkinter.Button(top,text="Click here to donate for PM fund",command=donate).grid()
    top.geometry('500x500')
    top.mainloop()
con()

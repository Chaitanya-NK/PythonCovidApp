
def covid():
    import tkinter
    import webbrowser
    top=tkinter.Tk()
    top.geometry('500x100')
    top.title("COVID19 STATEWISE STATUS")
    url="https://www.mygov.in/corona-data/covid19-statewise-status"
    def openweb():
        webbrowser.open(url)
    def download():
        webbrowser.open(r"https://www.mohfw.gov.in/pdf/Districtreporting429.pdf")
    print("To know the COVID-19 cases in INDIA upto date")
    but1=tkinter.Button(top,text="To know the COVID-19 cases in INDIA upto date",bg="black",fg="white",font=("Arial Bold",10),command=openweb)
    but1.pack()
    but2=tkinter.Button(top,text="Download the pdf here!",bg="white",fg="black",command=download)
    but2.pack()
    top.mainloop()
covid()

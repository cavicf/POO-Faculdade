import tkinter as tk

class GUI:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title('ENTRY2')

        self.frame1 = tk.Frame(self.janela)
        self.frame2 = tk.Frame(self.janela)
        self.frame1.pack()
        self.frame2.pack()
        
        self.labelinfo = tk.Label(self.frame1, text='Digite algo: ')
        self.labelResult = tk.Label(self.frame2, text='Nada')
        self.labelinfo.grid(row=0, column=0)
        self.labelResult.grid(row=0, column=0)

        self.labelinfo2 = tk.Label(self.frame1, text='Digite mais: ')
        self.labelResult2 = tk.Label(self.frame2)
        self.labelinfo2.grid(row=1,column=0)
        self.labelResult2.grid(row=0,column=1)

        self.buttonSubmit = tk.Button(self.janela, text='Enter', command=self.submit)
        self.buttonSubmit.pack(side='left')

        self.buttonClear = tk.Button(self.janela, text='Limpar', command=self.clear)
        self.buttonClear.pack(side='left')

        self.inputText = tk.Entry(self.frame1, width=20)
        self.inputText.grid(row=0, column=1)
        self.inputText2 = tk.Entry(self.frame1, width=20)
        self.inputText2.grid(row=1, column=1)

        self.janela.mainloop()

    def submit(self):
        self.labelResult.config(text=self.inputText.get())
        self.labelResult2.config(text=self.inputText2.get())

    def clear(self):
        self.inputText.delete(0,len(self.inputText.get()))
        self.inputText2.delete(0,len(self.inputText2.get()))
        self.labelResult.config(text='Nada')
        self.labelResult2.config(text='')

def main():
    GUI()

main()

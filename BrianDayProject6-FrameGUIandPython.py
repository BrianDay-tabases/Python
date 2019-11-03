#CIT144 Python 1 Project #6
#GUI Program
#By Brian Day
from tkinter import *

class CalculateTemp(Frame):

    def __init__(self): 
        Frame.__init__(self)
        self.master.title("Temperature Converter")
        self.grid() 
        
        
        Label(self, text="Enter a temperature").grid(row=0, column=1, padx=0, pady=0)
        self._temp = StringVar()
        self._tempEntry = Entry(self, width=15, textvariable=self._temp)
        self._tempEntry.grid(row=0, column=2, padx =0, pady=0)
        self.tempConversion = BooleanVar() 
        Radiobutton(self, text = "Convert to Fahrenheit", variable = self.tempConversion, value=1).grid(row=1, column=1, padx=3, pady=3)
             
        self.tempConversion = BooleanVar() 
        Radiobutton(self, text = "Convert to Celcius", variable = self.tempConversion, value=2).grid(row=2, column=1, padx=3, pady=3)

        self._btn1 = Button(self, text="Convert Value", command=self._convert) #####
        self._btn1.grid(row=3, column=1, padx=1, pady=5)

        self._btn2 = Button(self, text="Clear", command=self._clear) #######
        self._btn2.grid(row=3, column=2, padx=1, pady=5)
        
        
        Label(self, text="Result:").grid(row=4, column=1, padx=0, pady=1)
        self.finalTemp = StringVar()
        self.temp1 = Entry(self, width=15, textvariable=self.finalTemp)
        self.temp1.grid(row=4, column=2, padx=0, pady=1)
        Label(self, text="Degrees      ").grid(row=4, column=3, padx=0, pady=1)
        
    def _convert(self) : 
        input = float(self._temp.get())
        unit = self.tempConversion
        self.displayTemp = 0
        if unit == 2:
                self.celciusDisplay = (input - 32) / 1.8
                self.displayTemp = ("%.1f" % celciusDisplay)
        elif unit == 1:
                self.fahrenheitDisplay = 1.8 * input + 32
                self.displayTemp = ("%.1f" % fahrenheitDisplay)
        self.finalTemp.set(self.displayTemp)
        self.pack()
        
    def _clear(self) :
        self._tempEntry.delete(0, 'end')
        self.temp1.delete(0, 'end')
        self
def main():  
    CalculateTemp().mainloop()

main()
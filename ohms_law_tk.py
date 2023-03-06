import tkinter as tk # pip install tk
from PIL import ImageTk, Image # pip install image
import math
from ohm import Ohm

class Application(tk.Frame):
    # initialize instance
    def __init__(self, master=None):
        super().__init__(master)
        # setup application
        self.master = master
        self.master.title ("Ohm's Law")
        self.master.iconphoto(False, tk.PhotoImage(file='./calculator.png'))
        self.master.minsize(354, 511)
        self.master.maxsize(1000, 720)
        # binding event handling method for window configuration
        # (resize, move)
        self.master.bind("<Configure>", self.handleConfigure)
        # binding event handler for "return"-key
        self.master.bind("<Return>", self.handleCalculate)
        self.pack(fill='both')
        # adding widgets
        self.createWidgets()
        # auto-resize column 1 (=entries),
        # works only with "self.pack(fill='both'))""
        self.grid_columnconfigure(1, weight=1)

    # validating input: float only
    def isFloat(self, content):
        try:
            return content=="0" or content=="0." or float(content)
        except:
            return content==""
    
    # set content (what) of entry widget (where)
    def setEntry(self, where, what):
        if where.get():
            where.delete(0, len(where.get()))
        where.insert(0, str(what))

    # clear all entry widgets
    def clearEntries(self, event):
        self.setEntry(self.entPower, "")
        self.setEntry(self.entResistance, "")
        self.setEntry(self.entVoltage, "")
        self.setEntry(self.entCurrent, "")
    
    # executing calculation with input values and following priority
    # 1.: power
    # 2.: resistance
    # 3.: voltage
    # 4.: current
    # means: eg. if power, resistance and voltage are entered, voltage will
    # be overwritten (in case it is wrong)
    def handleCalculate(self, event):
        # read entries
        p = self.entPower.get()
        r = self.entResistance.get()
        v = self.entVoltage.get()
        i = self.entCurrent.get()
        # power p and r are entered
        if p and r:
            v = Ohm.getVoltage(p=float(p), r=float(r), threePhase=self.threePhase.get())
            i = Ohm.getCurrent(p=float(p), r=float(r), threePhase=self.threePhase.get())
            self.setEntry(self.entVoltage, round(v, 2))
            self.setEntry(self.entCurrent, round(i, 2))
            return
        # power p and voltage v are entered
        elif p and v:
            r = Ohm.getResistance(p=float(p), v=float(v), threePhase=self.threePhase.get())
            i = Ohm.getCurrent(p=float(p), v=float(v), threePhase=self.threePhase.get())
            self.setEntry(self.entResistance, round(r, 2))
            self.setEntry(self.entCurrent, round(i, 2))
            return
        # resistance r and voltage v are entered
        elif r and v:
            p = Ohm.getPower(v=float(v), r=float(r), threePhase=self.threePhase.get())
            i = Ohm.getCurrent(v=float(v), r=float(r), threePhase=self.threePhase.get())
            self.setEntry(self.entPower, round(p, 2))
            self.setEntry(self.entCurrent, round(i, 2))
            return
        # power p and current i are entered
        elif p and i:
            r = Ohm.getResistance(p=float(p), i=float(i), threePhase=self.threePhase.get())
            v = Ohm.getVoltage(p=float(p), i=float(i), threePhase=self.threePhase.get())
            self.setEntry(self.entResistance, round(r, 2))
            self.setEntry(self.entVoltage, round(v, 2))
            return
        # resistance r and current i are entered
        elif r and i:
            p = Ohm.getPower(r=float(r), i=float(i), threePhase=self.threePhase.get())
            v = Ohm.getVoltage(r=float(r), i=float(i), threePhase=self.threePhase.get())
            self.setEntry(self.entPower, round(p, 2))
            self.setEntry(self.entVoltage, round(v, 2))
            return
        # voltage v and current i are entered
        elif v and i:
            p = Ohm.getPower(v=float(v), i=float(i), threePhase=self.threePhase.get())
            r = Ohm.getResistance(v=float(v), i=float(i), threePhase=self.threePhase.get())
            self.setEntry(self.entPower, round(p, 2))
            self.setEntry(self.entResistance, round(r, 2))
            return
        else:
            # enter at least two values
            pass
    
    # handels the configure event of the application
    # (resize, move)
    def handleConfigure(self, event):
        # print("window size and position: ", self.master.winfo_geometry())
        pass

    # create widgets: label, entries, buttons
    def createWidgets(self):
        # register validation method'isFloat' %P reflects the result
        # like after the keypress is accepted
        vcmd = (self.register(self.isFloat), '%P')

        # Label for headline:
        # Row 0
        self.lblHeader = tk.Label(self, text="Ohm's Law", font=(None, 14))
        self.lblHeader.grid(column=0, row=0, columnspan=3, padx='5', pady='5', sticky='nesw')

        # labels with entry widgets
        # Row 1: power
        self.lblPower = tk.Label(self, text="1. Power (p in Watts):")
        self.lblPower.grid(column=0, row=1, padx='5', pady='5', sticky='w')
        self.entPower = tk.Entry(self, textvariable="", validate="key", validatecommand=vcmd)
        self.entPower.grid(column=1, row=1, columnspan=2, padx='5', pady='5', sticky="nesw")
        # Row 2: resistance
        self.lblResistance = tk.Label(self, text="2. Resistance (r in Ohms):")
        self.lblResistance.grid(column=0, row=2, padx='5', pady='5', sticky='w')
        self.entResistance = tk.Entry(self, textvariable="", validate="key", validatecommand=vcmd)
        self.entResistance.grid(column=1, row=2, columnspan=2, padx='5', pady='5', sticky="nesw")
        # Row 3:voltage
        self.lblVoltage = tk.Label(self, text="3. Voltage (v in Volts):")
        self.lblVoltage.grid(column=0, row=3, padx='5', pady='5', sticky='w')
        self.entVoltage = tk.Entry(self, textvariable="", validate="key", validatecommand=vcmd)
        self.entVoltage.grid(column=1, row=3, columnspan=2, padx='5', pady='5', sticky="nesw")
        # Row 4: current
        self.lblCurrent = tk.Label(self, text="4. Current (i in Ampere):")
        self.lblCurrent.grid(column=0, row=4, padx='5', pady='5', sticky='w')
        self.entCurrent = tk.Entry(self, textvariable="", validate="key", validatecommand=vcmd)
        self.entCurrent.grid(column=1, row=4, columnspan=2, padx='5', pady='5', sticky="nesw")
        # Row 5: checkbox
        self.threePhase = tk.BooleanVar()
        self.threePhase.set(False)
        self.chkThreePhase = tk.Checkbutton(self, text="3-Phase-Power", variable=self.threePhase)
        self.chkThreePhase.grid(column=2, row=5, padx='5', pady='5', sticky="nes")
        # Row 6: buttons
        self.btnClear = tk.Button(self, text="Clear")
        self.btnClear.grid(column=1, row=6, padx='5', pady='5', sticky="nes")
        self.btnClear.bind("<Button-1>", self.clearEntries)
        self.btnRun = tk.Button(self, text="Calculate!")
        self.btnRun.grid(column=2, row=6, padx='5', pady='5', sticky="nesw")
        self.btnRun.bind("<Button-1>", self.handleCalculate)
        # Row 7: image
        imgOhmsLaw = ImageTk.PhotoImage(Image.open("ohms_law.gif"))
        self.Panel = tk.Label(self, image=imgOhmsLaw)
        self.Panel.image = imgOhmsLaw
        self.Panel.grid(column=0, row=7, columnspan=3, padx='5', pady='5', sticky="nesw")

# 
# instance of Tk class
#
root = tk.Tk()

# If you have a large number of widgets, 
# you can specify the standard attributes for all widgets simply like this.
# root.option_add("*Button.Background", "black")
# root.option_add("*Button.Foreground", "red")

# instance of Application class
app = Application(master=root)

# show application-instance
app.mainloop()
import tkinter as tk

# pixel size = 16x16
# pixel geo  = 8x8 

COLOR = {
    "bg":       "#FFE0E0",
    "fg":       "#000000",
    "lampOff":  "#380000",
    "lampOn":   "#FF0000",

    "bgRun":    "#00BE1D",
    "fgRun":    "#FFFFFF",
    "bgRun2nd": "#186C0F",
    "fgRun2nd": "#000000",

    "bgCode":   "#999999",
    "fgCode":   "#000000"
}

FONTS = {
    "runBtn":   ("Consolas", 10, "bold"),
    "regLbl":   ("Consolas", 7,  "bold"),
    "codeTxt":  ("Consolas", 10, "bold")
}

class Window:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.code = tk.StringVar()
        self.regs = {"r1": 0, "r2": 0, "r3": 0, "r4": 0, "r5": 0, "r6": 0, "r7": 0, "r8": 0}
    
    def windowSetup(self) -> None:
        self.root.title("Korvex CPU Sim")
        self.root.config(bg=COLOR["bg"])
        self.root.geometry("260x260")
        self.root.resizable(False, False)
        self.root.columnconfigure(0, weight=0, minsize=128)
        self.root.columnconfigure(1, weight=1)
    
    def pixelState(self, pixel: tk.Frame, state=True) -> None:
        if state:
            pixel.config(bg=COLOR["lampOn"])
        else:
            pixel.config(bg=COLOR["lampOff"])
    
    def splitForWords(self, text: str) -> list[list[str]] | list[str]:
        lines = text.split("\n")
        words = []
        for line in lines:
            words.append(line.split())
        return words

    def run(self) -> None:
        self.code = self.codeEditor.get("1.0", "end-1c")
        self.code = self.splitForWords(self.code)
        print(self.code)

    def main(self) -> None:
        self.windowSetup()
        self.displayFrame = tk.Frame(self.root, bg="black", height=128, width=128)
        self.displayFrame.grid(row=0, column=0, padx=1, pady=1)

        # Creating 8x8 pixels (self.pixels[x][y])
        self.pixels = [[tk.Frame(
                    self.displayFrame,
                    bg=COLOR["lampOff"],
                    width=16,
                    height=16
                    ) for _ in range(8)] for _ in range(8)]
        
        for y in range(8):
            for x in range(8):
                self.pixels[y][x].grid(row=x, column=y)
                

        self.runButton = tk.Button(
            self.root,
            command=lambda:self.run(),
            text="RUN",
            font=FONTS["runBtn"],
            bg=COLOR["bgRun"],
            fg=COLOR["fgRun"],
            height=1,
            width=17,
            activebackground=COLOR["bgRun2nd"],
            activeforeground=COLOR["fgRun2nd"],
            relief="solid"
        )
        self.runButton.grid(row=1, column=0, padx=1, pady=1, sticky="ew")

        self.codeEditor = tk.Text(
            self.root,
            bg=COLOR["bgCode"],
            fg=COLOR["fgCode"],
            height=17,
            width=16,
            font=FONTS["codeTxt"]
        )
        self.codeEditor.grid(row=0, column=1, rowspan=3, sticky="nsew")

        def spaces4Tab(event: tk.Event) -> str:
            event.widget.insert("insert", " "*4)
            return "break"
        
        self.codeEditor.bind("<Tab>", spaces4Tab)

        self.regsLabel = tk.Label(
            self.root,
            text="".join([f"{reg}: {val}\n" for reg, val in self.regs.items()]),
            bg=COLOR["bg"],
            fg=COLOR["fg"],
            font=FONTS["regLbl"],
            anchor="w"
        )
        self.regsLabel.grid(row=2, column=0, padx=1, pady=1, sticky="w")

        self.root.mainloop()
    
win = Window()
win.main()
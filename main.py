"""
attempt to create a desktop app for scanning 2 barcoes
and confirming the barcodes match

this is used in ap labs for confirmation that assets are the same
"""
import tkinter
import logging
import datetime

# logging config
logging.basicConfig(filename='barcodeMatch.log', level=logging.INFO)


DEFAULT_TEXT = 'Waiting for Barcodes'

class AssetMatch:
    def __init__(self, master):
            # initialize the window
            self.master = master
            self.mainframe = tkinter.Frame(self.master, bg='white')
            self.mainframe.pack(fill=tkinter.BOTH, expand=True)
            # necessary variables
            self.confirm_text = tkinter.StringVar()
            self.confirm_text.set(DEFAULT_TEXT)
            # run build functions
            self.build_grid()
            self.build_banner()
            self.build_confirmation_banner()
            self.build_barcode_scan_fields()
            self.build_submit_button()

    def build_grid(self):
        self.mainframe.columnconfigure(0,weight=0)
        self.mainframe.columnconfigure(1,weight=1)
        self.mainframe.columnconfigure(2,weight=0)
        self.mainframe.rowconfigure(0,weight=0)
        self.mainframe.rowconfigure(1,weight=0)
        self.mainframe.rowconfigure(2,weight=0)
        self.mainframe.rowconfigure(3,weight=0)
        self.mainframe.rowconfigure(4,weight=0)

    def build_banner(self):
            banner = tkinter.Label(
                self.mainframe,
                text="Asset Matching App",
                fg = "white",
                bg = "#5c85d6"
            )
            banner.grid(
                row=0, columnspan=4,
                sticky="ew",
            )
    def build_confirmation_banner(self):
        self.confirm_banner = tkinter.Label(
            self.mainframe,
            text = self.confirm_text.get(),
            fg = 'black',
            bg = 'yellow'
        )
        self.confirm_banner.grid(
        row=4, columnspan=4, rowspan=2,
        sticky='nsew'
        )

    def build_barcode_scan_fields(self):
            self.bcode_entry_lbl_one = tkinter.Label(
                self.mainframe,
                text="Scan first barcode:",
                bg="white", takefocus=True,
            )
            self.barcode_entry_one = tkinter.Entry(
                self.mainframe,
                bg="white"
            )
            self.bcode_entry_lbl_one.grid(
                row=1,
                sticky="w",
                pady=10
            )
            self.barcode_entry_one.grid(
                row=1,column=1,
                sticky="ew",
                pady=10
            )
            self.bcode_entry_lbl_two = tkinter.Label(
                self.mainframe,
                text="Scan second barcode:",
                bg="white"
            )
            self.barcode_entry_two = tkinter.Entry(
                self.mainframe,
                bg="white",
            )
            self.bcode_entry_lbl_two.grid(
                row=2,
                sticky="w",
            )
            self.barcode_entry_two.grid(
                row=2,column=1,
                sticky="ew",
            )
            self.barcode_entry_one.focus_set()

    def build_submit_button(self):
        submit_btn = tkinter.Button(
            self.mainframe,
            text='Confirm',
            command = self.check_barcodes
            )
        submit_btn.grid(
            row=3, column=1,
            pady=20, sticky='w'
        )

    def check_barcodes(self):
        bcode1_val = self.barcode_entry_one.get()
        bcode2_val = self.barcode_entry_two.get()
        if bcode1_val == bcode2_val:
            self.confirm_banner.config(bg='green', fg='white', text='Barcodes Match, Proceed!')
            log_value = 'matched'
        else:
            self.confirm_banner.config(bg='red', fg='white', text='STOP, Barcodes do NOT match!')
            log_value = 'did not match'
        logging.info('{} checked against {} :: Barcodes {}'.format(bcode1_val, bcode2_val, log_value))


if __name__ == '__main__':
    mainWindow = tkinter.Tk()
    mainWindow.title('P4 Asset Matching')
    mainWindow.geometry('500x175')
    app = AssetMatch(mainWindow)
    logging.info("App opened at {}".format(datetime.datetime.now()))
    mainWindow.mainloop()

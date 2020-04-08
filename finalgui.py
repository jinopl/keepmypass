from tkinter import *
from tkinter import ttk
import functions


def main():
    root = Tk()
    app = Startpage(root)
    root.mainloop()


class Startpage:
    def __init__(self, master):
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        font11 = "-family {Good Times} -size 10"
        font9 = "-family {DejaVu Sans Mono} -size 10 -weight bold"
        self.master = master
        master.geometry("542x462+534+139")
        master.minsize(1, 1)
        master.maxsize(1351, 738)
        master.resizable(1, 1)
        master.title("login")
        master.configure(background="#7566d8")

        self.labelPrmp = Label(master)
        self.labelPrmp.place(relx=0.055, rely=0.216, height=41, width=159)
        self.labelPrmp.configure(activebackground="#323eed")
        self.labelPrmp.configure(activeforeground="white")
        self.labelPrmp.configure(font=font9)
        self.labelPrmp.configure(text='''Master Password''')

        self.entryMp = Entry(master)
        self.entryMp.place(relx=0.443, rely=0.216, height=43, relwidth=0.528)
        self.entryMp.configure(background="white")
        self.entryMp.configure(font="TkFixedFont")

        self.btnCancel = Button(master)
        self.btnCancel.place(relx=0.129, rely=0.498, height=31, width=72)
        self.btnCancel.configure(text='''Cancel''')

        self.btnLogin = Button(master)
        self.btnLogin.place(relx=0.664, rely=0.498, height=31, width=71)
        self.btnLogin.configure(activebackground="#f9f9f9")
        self.btnLogin.configure(text='''Login''')

        self.Label1 = Label(master)
        self.Label1.place(relx=0.0, rely=-0.022, height=61, width=549)
        self.Label1.configure(activebackground="#9968ed")
        self.Label1.configure(background="#d86199")
        self.Label1.configure(font=font11)
        self.Label1.configure(text='''KeepMyPass''')

        self.BottomFrame = Frame(master)
        self.BottomFrame.place(relx=0.055, rely=0.714,
                               relheight=0.206, relwidth=0.876)
        self.BottomFrame.configure(relief='groove')
        self.BottomFrame.configure(borderwidth="2")
        self.BottomFrame.configure(relief="groove")
        self.BottomFrame.configure(background="#c579d8")

        self.btnSearch = Button(self.BottomFrame)
        self.btnSearch.place(relx=0.084, rely=0.211, height=51, width=101)
        self.btnSearch.configure(activebackground="#7566d8")
        self.btnSearch.configure(activeforeground="white")
        self.btnSearch.configure(background="#7566d8")
        self.btnSearch.configure(command=self.AddSearchWindow)
        self.btnSearch.configure(text='''Search''')

        self.btnAdd = Button(self.BottomFrame)
        self.btnAdd.place(relx=0.4, rely=0.211, height=51, width=101)
        self.btnAdd.configure(activebackground="#7566d8")
        self.btnAdd.configure(activeforeground="white")
        self.btnAdd.configure(background="#7566d8")
        self.btnAdd.configure(command=self.AddaddWindow)
        self.btnAdd.configure(text='''Add''')

        self.btnDelete = Button(self.BottomFrame)
        self.btnDelete.place(relx=0.737, rely=0.211, height=51, width=101)
        self.btnDelete.configure(activebackground="#7566d8")
        self.btnDelete.configure(activeforeground="white")
        self.btnDelete.configure(background="#7566d8")
        self.btnDelete.configure(command=self.Adddeletewindow)
        self.btnDelete.configure(text='''Delete''')

    def AddSearchWindow(self):
        self.AddSearchWindow = Toplevel(self.master)
        self.app = SearchPage(self.AddSearchWindow)

    def AddaddWindow(self):
        self.AddaddWindow = Toplevel(self.master)
        self.app = Addpage(self.AddaddWindow)

    def Adddeletewindow(self):
        self.Adddeletewindow = Toplevel(self.master)
        self.app = DeletePage(self.Adddeletewindow)


class SearchPage:
    def __init__(self, master):
        '''This class configures and populates the toplevel window.
           master is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.', background=_bgcolor)
        self.style.configure('.', foreground=_fgcolor)
        self.style.configure('.', font="TkDefaultFont")
        self.style.map('.', background=[
                       ('selected', _compcolor), ('active', _ana2color)])

        master.geometry("542x462+534+139")
        master.minsize(1, 1)
        master.maxsize(1351, 738)
        master.resizable(1, 1)
        master.title("login")
        master.configure(background="#7566d8")
        master.configure(highlightcolor="black")

        self.labelPrmp = Label(master)
        self.labelPrmp.place(relx=0.074, rely=0.26, height=41, width=159)
        self.labelPrmp.configure(activebackground="#323eed")
        self.labelPrmp.configure(activeforeground="white")
        self.labelPrmp.configure(
            font="-family {DejaVu Sans Mono} -size 10 -weight bold")
        self.labelPrmp.configure(text='''Tag''')

        self.btnShow = Button(master)
        self.btnShow.place(relx=0.406, rely=0.476, height=31, width=63)
        self.btnShow.configure(activebackground="#f9f9f9")
        self.btnShow.configure(text='''Show''')

        self.btnClose = Button(master)
        self.btnClose.place(relx=0.812, rely=0.152, height=31, width=71)
        self.btnClose.configure(activebackground="#f9f9f9")
        self.btnClose.configure(text='''Close''')

        self.Label1 = Label(master)
        self.Label1.place(relx=0.0, rely=-0.022, height=61, width=549)
        self.Label1.configure(activebackground="#9968ed")
        self.Label1.configure(background="#d86199")
        self.Label1.configure(font="-family {Good Times} -size 10")
        self.Label1.configure(text='''KeepMyPass''')

        self.DropDown = ttk.Combobox(master)
        self.DropDown.place(relx=0.554, rely=0.26,
                            relheight=0.089, relwidth=0.29)
        self.DropDown.configure(textvariable=Searchpage_support.combobox)
        self.DropDown.configure(takefocus="")

        self.SearchRFrame = Frame(master)
        self.SearchRFrame.place(relx=0.037, rely=0.584,
                                relheight=0.379, relwidth=0.932)
        self.SearchRFrame.configure(relief='groove')
        self.SearchRFrame.configure(borderwidth="2")
        self.SearchRFrame.configure(relief="groove")

        self.SearchRfText = Text(self.SearchRFrame)
        self.SearchRfText.place(relx=0.02, rely=0.057,
                                relheight=0.88, relwidth=0.962)
        self.SearchRfText.configure(background="white")
        self.SearchRfText.configure(font="TkTextFont")
        self.SearchRfText.configure(selectbackground="#c4c4c4")
        self.SearchRfText.configure(wrap="word")


class Addpage:
    def __init__(self, master):
        '''This class configures and populates the toplevel window.
           master is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'

        master.geometry("542x462+534+139")
        master.minsize(1, 1)
        master.maxsize(1351, 738)
        master.resizable(1, 1)
        master.title("login")
        master.configure(background="#7566d8")
        master.configure(highlightcolor="black")

        self.btnClose = Button(master)
        self.btnClose.place(relx=0.812, rely=0.152, height=31, width=71)
        self.btnClose.configure(activebackground="#f9f9f9")
        self.btnClose.configure(text='''Close''')

        self.Label1 = Label(master)
        self.Label1.place(relx=0.0, rely=-0.022, height=61, width=549)
        self.Label1.configure(activebackground="#9968ed")
        self.Label1.configure(background="#d86199")
        self.Label1.configure(font="-family {Good Times} -size 10")
        self.Label1.configure(text='''KeepMyPass''')

        self.AddTag = Label(master)
        self.AddTag.place(relx=0.129, rely=0.303, height=41, width=99)
        self.AddTag.configure(text='''Tag''')

        self.Adduname = Label(master)
        self.Adduname.place(relx=0.129, rely=0.433, height=41, width=99)
        self.Adduname.configure(activebackground="#f9f9f9")
        self.Adduname.configure(text='''Username''')

        self.AddPwd = Label(master)
        self.AddPwd.place(relx=0.129, rely=0.563, height=41, width=99)
        self.AddPwd.configure(activebackground="#f9f9f9")
        self.AddPwd.configure(text='''Password''')

        self.AddStrong = Button(master)
        self.AddStrong.place(relx=0.646, rely=0.758, height=41, width=161)
        self.AddStrong.configure(text='''Gen strong passwords''')

        self.AddRf = Frame(master)
        self.AddRf.place(relx=0.055, rely=0.866,
                         relheight=0.097, relwidth=0.895)

        self.AddRf.configure(relief='groove')
        self.AddRf.configure(borderwidth="2")
        self.AddRf.configure(relief="groove")

        self.AddfText = Text(self.AddRf)
        self.AddfText.place(relx=0.0, rely=0.0,
                            relheight=0.978, relwidth=1.002)
        self.AddfText.configure(background="white")
        self.AddfText.configure(font="TkTextFont")
        self.AddfText.configure(selectbackground="#c4c4c4")
        self.AddfText.configure(wrap="word")

        self.AddAdd = Button(master)
        self.AddAdd.place(relx=0.387, rely=0.758, height=41, width=101)
        self.AddAdd.configure(activebackground="#f9f9f9")
        self.AddAdd.configure(text='''Add''')

        self.Entry1 = Entry(master)
        self.Entry1.place(relx=0.424, rely=0.303, height=43, relwidth=0.362)
        self.Entry1.configure(background="white")
        self.Entry1.configure(font="TkFixedFont")

        self.Entry1_4 = Entry(master)
        self.Entry1_4.place(relx=0.424, rely=0.433, height=43, relwidth=0.362)
        self.Entry1_4.configure(background="white")
        self.Entry1_4.configure(font="TkFixedFont")
        self.Entry1_4.configure(selectbackground="#c4c4c4")

        self.Entry1_5 = Entry(master)
        self.Entry1_5.place(relx=0.424, rely=0.563, height=43, relwidth=0.362)
        self.Entry1_5.configure(background="white")
        self.Entry1_5.configure(font="TkFixedFont")
        self.Entry1_5.configure(selectbackground="#c4c4c4")


class DeletePage:
    def __init__(self, master):
        '''This class configures and populates the toplevel window.
           master is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.', background=_bgcolor)
        self.style.configure('.', foreground=_fgcolor)
        self.style.configure('.', font="TkDefaultFont")
        self.style.map('.', background=[
                       ('selected', _compcolor), ('active', _ana2color)])

        master.geometry("542x462+534+139")
        master.minsize(1, 1)
        master.maxsize(1351, 738)
        master.resizable(1, 1)
        master.title("login")
        master.configure(background="#7566d8")
        master.configure(highlightcolor="black")

        self.DelbtnClose = Button(master)
        self.DelbtnClose.place(relx=0.812, rely=0.152, height=31, width=71)
        self.DelbtnClose.configure(activebackground="#f9f9f9")
        self.DelbtnClose.configure(text='''Close''')

        self.Label1 = Label(master)
        self.Label1.place(relx=0.0, rely=-0.022, height=61, width=549)
        self.Label1.configure(activebackground="#9968ed")
        self.Label1.configure(background="#d86199")
        self.Label1.configure(font="-family {Good Times} -size 10")
        self.Label1.configure(text='''KeepMyPass''')

        self.AddTag = Label(master)
        self.AddTag.place(relx=0.055, rely=0.238, height=41, width=129)
        self.AddTag.configure(activebackground="#f9f9f9")
        self.AddTag.configure(text='''Tag''')

        self.DelentID = Label(master)
        self.DelentID.place(relx=0.074, rely=0.498, height=41, width=99)
        self.DelentID.configure(activebackground="#f9f9f9")
        self.DelentID.configure(text='''Enter ID''')

        self.AddRf = Frame(master)
        self.AddRf.place(relx=0.055, rely=0.866, relheight=0.097, relwidth=0.895)

        self.AddRf.configure(relief='groove')
        self.AddRf.configure(borderwidth="2")
        self.AddRf.configure(relief="groove")

        self.AddfText = Text(self.AddRf)
        self.AddfText.place(relx=0.0, rely=0.0, relheight=0.978, relwidth=1.002)
        self.AddfText.configure(background="white")
        self.AddfText.configure(cursor="fleur")
        self.AddfText.configure(font="TkTextFont")
        self.AddfText.configure(selectbackground="#c4c4c4")
        self.AddfText.configure(wrap="word")

        self.DelEnid = Entry(master)
        self.DelEnid.place(relx=0.387, rely=0.498, height=43, relwidth=0.417)
        self.DelEnid.configure(background="white")
        self.DelEnid.configure(font="TkFixedFont")
        self.DelEnid.configure(selectbackground="#c4c4c4")

        self.DelComb = ttk.Combobox(master)
        self.DelComb.place(relx=0.369, rely=0.238, relheight=0.089, relwidth=0.437)
        self.DelComb.configure(textvariable=Deletepage_support.combobox)
        self.DelComb.configure(takefocus="")
        self.DelComb.configure(cursor="fleur")

        self.DelShow = Button(master)
        self.DelShow.place(relx=0.314, rely=0.39, height=31, width=141)
        self.DelShow.configure(text='''Show''')

        self.DelDelete = Button(master)
        self.DelDelete.place(relx=0.314, rely=0.649, height=41, width=141)
        self.DelDelete.configure(activebackground="#f9f9f9")
        self.DelDelete.configure(text='''Delete''')


if __name__ == '__main__':
    main()

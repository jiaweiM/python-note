import wx


class MainFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title)


class App(wx.App):
    def __init__(self):
        super(self.__class__, self).__init__()

    def OnInit(self):
        self.version = u"Lesson 2"
        self.title = u"wxPython 初级教程" + self.version
        frame = MainFrame(None, -1, self.title)
        frame.Show(True)

        return True


app = App()
app.MainLoop()

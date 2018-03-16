# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 19:14:03 2018

@author: luo xi yang
"""
import wx
import os
from turnclass import TurnClass as TC
class MyFrame(wx.Frame):
    def __init__( self):
        wx.Frame.__init__(self,None,-1,"Xml Turn Csv",pos=(10,10),size=(500,500))
        self.create_search_text()
        self.create_button()
        self.create_menu()
        self.create_statusbar()
        
        self.event_button()
        self.event_quit()
        
        self.SetBackgroundColour('MEDIUM TURQUOISE')
        #self.SetBackgroundColour('WHITE')
     
        
    def create_menu(self):
        self.menubar=wx.MenuBar()
        self.menu1=wx.Menu()
        self.menu2=wx.Menu()
        """STEP3在菜单下面，建立选项栏，使用Append（-1，“name”）"""
        #self.m1open=self.menu1.Append(-1,"Open")
        self.m1open=self.menu1.Append(-1,"Open")
        self.m1save=self.menu1.Append(-1,'Save')
        self.m1quit=self.menu1.Append(-1,'Quit')
        self.m2about=self.menu2.Append(-1,"About")
        """STEP4将建好的菜单添加到菜单栏下面去，使用Append(菜单，“name”)"""
        self.menubar.Append(self.menu1,"File")
        self.menubar.Append(self.menu2,"Help")
        """STEP5将菜单栏设置到主窗口中，使用SetMenuBar（）"""
        self.SetMenuBar(self.menubar)
        
    def create_search_text(self):
        self.text = wx.TextCtrl(self,-1,pos=(50,170),size=(290,40),style=wx.TE_PROCESS_ENTER|wx.TE_CENTER)
        
    def create_button(self):
        self.button = wx.Button(self,-1,'BEGIN',pos=(350,170),size=(60,40))
        self.button.SetBackgroundColour('WHITE')
        
    def create_statusbar(self):
        self.statusBar1 = self.CreateStatusBar()
        #self.statusBar1.SetFieldsCount(3)
        #self.statusBar1.SetStatusWidths([-1, -2, -1])
        
    def event_button(self):
        self.button.Bind(wx.EVT_BUTTON,self.OnButton)
    def event_quit(self):
        self.menu1.Bind(wx.EVT_MENU,self.OnMenuQuit,self.m1quit)
        
    def OnButton(self,event):
        with wx.FileDialog(self,"Open file",wildcard="Text files (*.xml)|*.xml|(*.csv)|*.csv|(*.xls)|*.xls",style=wx.FD_OPEN|wx.FD_FILE_MUST_EXIST) as fileDialog:
            if fileDialog.ShowModal()==wx.ID_OK:
                pathname_insert=fileDialog.GetPath()
                xmlcsv=TC(pathname_insert)
                xmlcsv.save_to_csv()
                self.statusBar1.SetStatusText('XML has been converted to CSV * * test.csv has been saved to the Desktop')
    def OnMenuQuit(self,event):
        """结束程序"""
        os.sys.exit()
        
app=wx.App()
win=MyFrame()
win.Show()
app.MainLoop()

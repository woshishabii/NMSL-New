"""
主页GUI
根据wxPython Doc HelloWorld2 改编
by:woshishabi
"""

# 导入库
import wx
import webbrowser


class MainFrame(wx.Frame):
    """
    主GUI类
    """
    def __init__(self, *args, **kw):
        # 调用父类的__init__函数
        super(MainFrame, self).__init__(*args, **kw)

        # 设置窗口大小
        self.SetSize((520, 250))
        self.SetMaxSize((520, 250))
        self.SetMinSize((520, 250))

        # 在框架中创建一个面板（Panel）
        panel = wx.Panel(self)

        # 生成黑色加粗字体
        st = wx.StaticText(panel, label="Naughty Minecraft Server Launcher")
        font = st.GetFont()
        font.PointSize += 10
        font = font.Bold()
        st.SetFont(font)

        # 创建一个sizer来管理子部件的布局
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(st, wx.SizerFlags().Border(wx.TOP|wx.LEFT, 25))
        panel.SetSizer(sizer)

        # 创建菜单栏
        self.makeMenuBar()

        # 创建状态栏
        self.CreateStatusBar()
        self.SetStatusText("感谢您使用Naughty Minecraft Server Launcher")


    def makeMenuBar(self):
        """
        菜单栏由菜单组成，菜单由菜单项组成。
        这个函数创建了一些菜单并将它们绑定到对应的处理函数上
        """

        # 创建一个包含Hello和Exit的File菜单
        fileMenu = wx.Menu()
        '''# "\t..."定义了一个也会触发同样函数的快捷键（貌似是全局的）
        helloItem = fileMenu.Append(-1, "&Hello...\tCtrl-H",
                "在状态栏里显示的信息")
        fileMenu.AppendSeparator()'''
        downloadVersionItem = fileMenu.Append(-1, "下载新版本(&A)\tCtrl-A", '下载一个新的服务端')
        fileMenu.AppendSeparator()
        changePreference = fileMenu.Append(-1, '首选项(&P)', '修改NMSL设置')
        fileMenu.AppendSeparator()
        # 当使用一个预定义的值时就不需要再自定义函数
        exitItem = fileMenu.Append(wx.ID_EXIT)

        # 创建一个包含“关于”的Help菜单
        helpMenu = wx.Menu()
        webItem = helpMenu.Append(-1, "打开Gitee开源仓库", "打开NMSL的开源仓库")
        aboutItem = helpMenu.Append(wx.ID_ABOUT)

        # 创建一个菜单栏并添加两个项目，'&'后面的字母定义了一个有助于记忆的菜单。
        # 在支持的操作系统上这些字母会被下划线，按下时会触发对应的函数
        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "文件(&F)")
        menuBar.Append(helpMenu, "帮助(&H)")

        # 将菜单栏添加到框架
        self.SetMenuBar(menuBar)

        # Finally, associate a handler function with the EVT_MENU event for
        # each of the menu items. That means that when that menu item is
        # activated then the associated handler function will be called.
        self.Bind(wx.EVT_MENU, self.OnAddVersion, downloadVersionItem)
        self.Bind(wx.EVT_MENU, self.OnChangePreference, changePreference)
        self.Bind(wx.EVT_MENU, self.OnExit, exitItem)
        self.Bind(wx.EVT_MENU, self.OpenRepo, webItem)
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)


    def OnAddVersion(self, event):
        wx.MessageBox("测试菜单项", "下载新版本", wx.OK|wx.ICON_INFORMATION)


    def OnChangePreference(self, event):
        wx.MessageBox("测试菜单项", "首选项", wx.OK|wx.ICON_INFORMATION)


    def OnExit(self, event):
        """关闭框架，终止程序"""
        self.Close(True)


    def OpenRepo(self, event):
        webbrowser.open(url='https://gitee.com/chen_xingyu/NMSL-New', new=0, autoraise=True)


    def OnAbout(self, event):
        """Display an About Dialog"""
        wx.MessageBox("这是一个GUI",
                      "关于NMSL",
                      wx.OK|wx.ICON_INFORMATION)


if __name__ == '__main__':
    # 当这个文件被直接运行时（而不是作为一个包导入）的时候就创建一个app、frame，显示出来并启动事件循环
    app = wx.App()
    frm = MainFrame(None, title='NMSL Alpha 1.0.2')
    frm.Show()
    app.MainLoop()

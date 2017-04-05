#-*- encoding:UTF-8 -*-
__author__ = 'wuyou'
import sys,os,time
reload(sys)
sys.setdefaultencoding('utf-8')
from xml.dom.minidom import Document
import wx.lib.agw.customtreectrl as CT
import wx
import xml.dom.minidom
class Frame(wx.Frame):
    def __init__(self):
        self.test_case_path = 'C:\\\\QSST_Android7.0_0629_2016_2.0.3\\data\\test_env'
        wx.Frame.__init__(self, None, -1, title="QSST",size = (400,600))
        self.Center()
        self.panel = wx.Panel(self, -1)
        self.Main_Box = wx.BoxSizer( wx.VERTICAL)
        self.TestCase_TREE = CT.CustomTreeCtrl(self.panel, agwStyle=wx.TR_DEFAULT_STYLE | CT.TR_AUTO_CHECK_PARENT | CT.TR_AUTO_CHECK_CHILD )
        self.TestCase_TREE_ROOT = self.TestCase_TREE.AddRoot('TestCase')
        self.TestCase_TREE_ROOT.Expand()
        self.showTestCase(self.TestCase_TREE, self.TestCase_TREE_ROOT, self.test_case_path)
        self.Set_Button = wx.Button(self.panel, -1, 'Set', size=(-1, 40))
        self.Bind(wx.EVT_BUTTON, self.OnSet, self.Set_Button)
        self.Main_Box.Add(self.TestCase_TREE, 1, wx.EXPAND)
        self.Main_Box.Add(self.Set_Button, 0, wx.ALIGN_CENTER)
        self.panel.SetSizer(self.Main_Box)

    def showTestCase(self,Tree,ParenNode,Path):
        files_Package = os.listdir(Path)
        for testPackage in files_Package:
            if os.path.isdir(os.path.join(Path, testPackage)) and testPackage.startswith('test'):
                folder_Package = Tree.AppendItem(ParenNode, testPackage, 1)
                folder_Path = os.path.join(Path, testPackage)
                files_Class = os.listdir(folder_Path)
                for testClass in files_Class:
                    if testClass.endswith('.xml'):
                        Tree.AppendItem(folder_Package, testClass, 1,).Check(self.readTestCaseXML(os.path.join(folder_Path, testClass)))

    def readTestCaseXML(self, path):
        dom = xml.dom.minidom.parse(path)
        root = dom.documentElement
        if root.getAttribute('enable') == '0':
            return False
        else:
            return True

    def OnSet(self, event):
        print '==========================='
        self.GetTree(self.TestCase_TREE)
    def GetTree(self, Tree):
        treeRoot = Tree.GetRootItem()
        (item, cookie) = Tree.GetFirstChild(treeRoot)
        for x in range(Tree.GetChildrenCount(treeRoot)):

            if Tree.GetItemText(item).endswith('.xml'):
                xml_path = os.path.join(self.test_case_path, Tree.GetItemText(Tree.GetItemParent(item)),
                                        Tree.GetItemText(item))
                print xml_path
                if Tree.IsItemChecked(item):
                    self.SetTestCaseXML(xml_path, '1')
                else:
                    self.SetTestCaseXML(xml_path, '0')


            item=Tree.GetNext(item)
    def SetTestCaseXML(self, path, text):
        dom = xml.dom.minidom.parse(path)
        root = dom.documentElement
        root.setAttribute('enable', text)
        self.save(path, dom)

    def save(self,path ,DOC):
        file = open(path,'w')
        file.write(DOC.toprettyxml(indent='',encoding='utf-8'))
        file.close()

if __name__ == "__main__":
    app = wx.App()
    f=Frame()
    f.Show()

    app.MainLoop()

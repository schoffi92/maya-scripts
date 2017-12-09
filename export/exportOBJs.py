import maya.cmds as mc
import os

dirInput = ""
projectPath = mc.workspace(q=True,rootDirectory=True)
exportPath = projectPath + "data/exports/"

if not os.path.exists(exportPath):
        os.makedirs(exportPath)

def exportAllSelectedGEO(self):
    dirname = mc.textField(dirInput,q=True,text=True)
    if dirname == "":
        dirname = "temp"
    
    directory = exportPath + dirname + "/"
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    selection = mc.ls(sl=True)
    # file -force -options "groups=1;ptgroups=1;materials=1;smoothing=1;normals=1" -typ "OBJexport" -pr -es "D:/MayaProjects/MayaPro_Training/data/zbrush/book2/bookPage.obj";
    for obj in selection:
        mc.select(obj)
        mc.file(directory + obj + ".obj", typ="OBJexport",force=True,pr=True,es=True)
    mc.select(selection)
    pass

wnd = mc.window(title="Export OBJ")
mc.columnLayout(adjustableColumn=True)
mc.text(label="Export Directory Name")
dirInput = mc.textField(text="temp")

mc.button(label="Export Selected To OBJ", command=exportAllSelectedGEO)

mc.showWindow( wnd )

import maya.cmds as mc
import os


# Options General: groups=1;ptgroups=1;materials=1;smoothing=1;normals=1
dirInput = ""
smoothInput = ""
materialsInput = ""
projectPath = mc.workspace(q=True,rootDirectory=True)
exportPath = projectPath + "data/exports/"

if not os.path.exists(exportPath):
        os.makedirs(exportPath)

def exportAllSelectedGEO(self):
    options = ""
    dirname = mc.textField(dirInput,q=True,text=True)
    smooth = mc.checkBox(smoothInput,q=True,value=True)
    materials = mc.checkBox(materialsInput,q=True,value=True)

    if dirname == "":
        dirname = "temp"

    if smooth:
        options += "smoothing=1;"

    if materials:
        options += "materials=1;"
    
    directory = exportPath + dirname + "/"
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    selection = mc.ls(sl=True)
    # file -force -options "groups=1;ptgroups=1;materials=1;smoothing=1;normals=1" -typ "OBJexport" -pr -es "D:/MayaProjects/MayaPro_Training/data/zbrush/book2/bookPage.obj";
    for obj in selection:
        mc.select(obj)
        mc.file(directory + obj.replace("|", "_") + ".obj", typ="OBJexport",force=True,pr=True,es=True,options=options)
    mc.select(selection)
    pass

wnd = mc.window(title="Export OBJ", width=300)
mc.columnLayout(adjustableColumn=True)

mc.text(label="Options")
smoothInput = mc.checkBox(label="Smooth",align="right")
materialsInput = mc.checkBox(label="Materials",align="right")

mc.text(label="Export Directory Name")
dirInput = mc.textField(text="temp")

mc.button(label="Export Selected To OBJ", command=exportAllSelectedGEO)

mc.showWindow( wnd )

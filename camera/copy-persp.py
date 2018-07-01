import maya.cmds as mc

# This script copies persp camera and locks the copy attributes
mc.select("persp")
mc.duplicate(rr=True)
objName = mc.rename("render_cam")
mc.setAttr(objName + ".tx", lock=True)
mc.setAttr(objName + ".ty", lock=True)
mc.setAttr(objName + ".tz", lock=True)
mc.setAttr(objName + ".rx", lock=True)
mc.setAttr(objName + ".ry", lock=True)
mc.setAttr(objName + ".rz", lock=True)
mc.setAttr(objName + ".sx", lock=True)
mc.setAttr(objName + ".sy", lock=True)
mc.setAttr(objName + ".sz", lock=True)

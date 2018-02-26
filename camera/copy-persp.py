import maya.cmds as mc

# This script copies persp camera and creates from it a "render_cam"
mc.select("persp")
mc.duplicate(rr=True)
mc.rename("render_cam")

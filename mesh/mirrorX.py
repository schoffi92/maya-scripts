import maya.cmds as mc

mirrorObjs = []
selection = mc.ls(sl=True)
for obj in selection:
    mc.select(obj)
    mirrorObjs.append(mc.duplicate()[0])
    mc.scale(-1,1,1)
    mc.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
    mc.polyNormal(nm=0)

mc.group(mirrorObjs, n="mirrorGeos_grp")
mc.select(mirrorObjs)
python.Init()

if ((menuMan.findMenu "CGcenter") != undefined) then 
  (
    menuMan.unRegisterMenu (menuMan.findMenu "CGcenter")
    menuMan.updateMenuBar()
  )


macroScript Posture category:"CGcenter" buttonText: "Posture v1.2"
  (
    python.ExecuteFile(getDir #scripts + "\Startup\posture_v1.2\posture_v1.2.py")
  )

Main = menuMan.getMainMenuBar() 
Menu = menuMan.createMenu "CGcenter" 
theSubMenu = menuMan.createSubMenuItem "CGcenter" Menu 
Main.addItem theSubMenu (Main.numItems()+1) 
Action = menuMan.createActionItem "Posture" "CGcenter" 
Menu.addItem Action (Menu.numItems()+1) 
menuMan.updateMenuBar()

#IMPORTS
import os

#DEFINE CLASS TO CLEAR THE TERMINAL WHENEVER NEEDED
def Clear_Screen():
 
    #WINDOW'S OS.NAME IS 'NT'
    if os.name == 'nt':
        #WINDOWS-ONLY COMMAND TO CLEAN THE TERMINAL
        os.system('cls')
 
    #BOTH MAC AND LINUX SHARE THE OS.NAME 'POSIX'
    else:
        #LINUX AND MAC'S COMMAND TO CLEAN THE TERMINAL
        os.system('clear')
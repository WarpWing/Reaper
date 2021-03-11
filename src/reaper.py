import os 
import sys
import yaml 
import requests
import platform 
import socket,json,psutil,logging

class sysinfo: 
    uname = platform.uname()
    release = uname.system
    kernel = uname.release
    version = uname.version
    machine = uname.machine
    name = uname.node
    ram= str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"

    
## This code is for debugging and logging. This will not be externally collected but will be stored at the beginning of every log message
#uname = platform.uname()
#base = {}
#base['system']=uname.system
#base['release']=uname.release
#base['version']=uname.version
#base['machine']=uname.machine
#base['nodename']=uname.node
#base['ram']=str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"
#json.dumps(base)




    




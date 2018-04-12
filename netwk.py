Folderpath=r'\\DESKTOP-HB8MV4A\Users\Pomskies\Desktop\New folder' #Provide the network share file path in the Folder path
filename=r'SysnetProtectInstaller.msi'#provide filename with extension
share_user="Pomskies" # Provide the user name for the shared system
share_pass="Comodo243" # Provide the password for the shared system
Filepath=r""+Folderpath+r'\\'+filename
import os
import shutil
import ctypes
import subprocess
workdir=os.environ['PROGRAMDATA']+r'\temp'
def login(cmd,Filepath):    
    if not os.path.exists(workdir):
        os.mkdir(workdir)    
        print 'Login to network share'
        print os.popen(cmd).read()
        print 'Copying files to local machine....'
        shutil.copy(Filepath,workdir)
        print "copied successfully"
        path=workdir+"\\"+filename
        if os.path.isfile(path):        
                process= subprocess.Popen('msiexec /i "%s" /qn'%path, shell=True, stdout=subprocess.PIPE)
                result=process.communicate()
                ret=process.returncode
                if ret==0:
                    pass
                else:
                    print result[1]
                print ""+filename+" installed successfully"
        else:
            print '%s is not found.'%path

cmd= 'NET USE "'+Folderpath+'" /USER:'+share_user+'  "'+share_pass+'"'
login(cmd,Filepath)
##
##def remove(workdir):
##    shutil.rmtree(workdir)



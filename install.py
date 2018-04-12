URL='https://www.7-zip.org/a/7z1803.msi' #Please Give the hosted dell command update  the cloud drive link
import ssl
import subprocess
def Download(URL):
    import urllib2
    import os
    print "Download started"
    context = ssl._create_unverified_context()
    fileName =URL.split('/')[-1]
    src_path=os.environ['ProgramData']
    path = os.path.join(src_path, fileName)
    request = urllib2.Request(URL, headers={'User-Agent' : "Magic Browser"})
    parsed = urllib2.urlopen(request,context=context)
    if os.path.exists(src_path):
        print "Path already exists"
    if not os.path.exists(src_path):
        os.makedirs(src_path)
        print "Path created"
    with open(path, 'wb') as f:
        while True:
            chunk=parsed.read(100*1000*1000)
            if chunk:
                f.write(chunk)
            else:
                break
    print "The file downloaded successfully in specified path "+path
    if os.path.isfile(path):        
        process= os.popen('msiexec /i "%s" /qn'%path).read()
        print ""+fileName+" installed successfully"
    else:
        print '%s Download file is not found or Error in Download File.'%path


Download(URL)

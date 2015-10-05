import sys
#import apport
def removelines(filename):
    
    f  = open(filename,'r')
    backup = f.read()
    backupFile = open(filename+"b",'w')
    backupFile.write(backup)
    backupFile.close()
    f.close()
    f  = open(filename,'r')

    ans = ""
    for x in f:
        i = 0;
        found = False;
        while i<len(x)-1:
            if x[i:i+2] == "//":
                ans+= x[:i-1]+"/*"+ x[i+2:-1]+"*/"
                found = True
            i+=1
        if not found:
            ans+=x[:-1]
    f.close();
    f = open(filename,'w')
    f.write(ans)
    f.close()
print "args: "+sys.argv[1]
removelines(sys.argv[1])

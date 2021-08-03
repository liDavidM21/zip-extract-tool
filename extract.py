from genericpath import isdir, isfile
import zipfile, os, sys, rarfile


def extractFiles():
    lst = os.listdir()
    dir = []
    file = []
    for s in lst:
        absName = os.path.abspath(s)
        if(os.path.isdir(absName)):
            dir.append(absName)
        elif(os.path.isfile(absName)):
            file.append(absName)
    for s in file:
        try:
            z = zipfile.ZipFile(s)
            dirName = z.filename[:-4]
            if(os.path.isdir(dirName)):
                z.extractall(dirName)
            else:
                os.mkdir(dirName)
                z.extractall(dirName)
            z.close()
        except Exception:
            try:
                r = rarfile.RarFile(s)
                dirName = r.filename[:-4]
                if(os.path.isdir(dirName)):
                    r.extractall(dirName)
                else:
                    os.mkdir(dirName)
                    r.extractall(dirName)
                r.close()
            except Exception as e:
                pass


    if(len(dir) == 0):
        return
    else:
        for s in dir:
            print("Extracting Directory:" + s)
            os.chdir(s)
            extractFiles()
            os.chdir("..")
    return

if(len(sys.argv) != 2):
    print("Invalid argument amount")

else:
    baseDirectoryPath = sys.argv[1]
    os.chdir(baseDirectoryPath)
    extractFiles()
    

    
    

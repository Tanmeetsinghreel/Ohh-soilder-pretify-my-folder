

def organizer(path,format):
    import os
    os.chdir(path)
    i = 1
    for file1 in os.listdir(path):
        os.rename(file1,file1.capitalize())
        for file2 in os.listdir(path):
            if format in file2:
                os.rename(f"{file2}",f"{i}.{format}")
                i = i + 1

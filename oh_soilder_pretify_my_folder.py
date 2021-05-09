# suppose you have a folder and its path is also given.you have to create a function
#which takes three input arguments which are:

#for example: def("c://","tsr.txt","jpg"):

# c:// - full path of the folder as input string.
# tsr.txt - dictionary file.
# jpg - file format.

# The function will perform three tasks:-

# first it will check all the files prsent in the folder whose path are given as an input
# argument.

# then it will capatalize the first letter of each file. if the name of a file is present
# in a dictionary file then it will not capatalize the first letter.it  wil only capatalize
# the first letter of the file which are not present in the dictionary file.

# the function renames the file name to number in range of 1to100 whose format is same as
# mentoined in the input parameter like 1.jpg.

# after performing these tasks your folder your folder will pretify as all the first letter
# of files in the folder will be capatalize except for those files whose names are present
# in the dictionary file and the file having the same format as given in the input argument
# will rename to number in the range of 1to100.


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
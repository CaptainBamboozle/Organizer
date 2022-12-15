from distutils import extension
import os
import shutil
#.exe, .png, .gif, .jpg, .jpeg, .pdf, .csv, .msi, .xls, .xlsx, .ppt, .mp4, .pppx, .txt, .aba, .mpeg

source="C:/Users/farid/Downloads"
#basically any file from file explorer its like a map if its a folder in a folder put folders in order
destination="C:/Users/farid/Downloads/C112"

list_of_files=os.listdir(source)
#listing all the files inside the downloads

for filename in list_of_files:
    name,extension=os.path.splitext(filename)
    if extension == '':
        continue
    if extension in ['.png','.jpg','.jpeg','.gif','.jfif']:
        path_1=source +'/'+filename
        path_2=destination + '/'+ "Images"
        path_3=destination+ '/'+ "Images"+'/' + filename

        if os.path.exists(path_2):
            shutil.move(path_1,path_3)
            print("moving"+filename)
        else:
            os.makedirs(path_2)
            shutil.move(path_1,path_3)
            print("moving"+filename)
    if extension in['.mp4','.mpeg','.mpg','.avi','.mov','.mkv','.flv','f4v','.swf','.wmv','.dvr','.zip','.wav']:
        path_1=source+'/'+filename
        path_2=destination+'/'+"Videos"
        path_3=destination+'/'+"Videos"+'/'+filename
        if os.path.exists(path_2):
            shutil.move(path_1,path_3)
            print("moving"+filename) 
        else:
            os.makedirs(path_2)
            shutil.move(path_1,path_3)
            print("moving"+filename)           
#moving all image files from downloads folder to destination
    else:
        path_1 = source+'/'+filename
        path_2=destination+'/'+"Others"
        path_3=destination+'/'+"Others"+'/'+filename
        if os.path.exists(path_2):
            shutil.move(path_1,path_3)
            print("moving"+filename)
        else:
            os.makedirs(path_2)
            shutil.move(path_1,path_3)
            print("moving"+filename)    
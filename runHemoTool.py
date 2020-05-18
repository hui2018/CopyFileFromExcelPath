import os

def runHemo():
    filePath = 'C:\\Users\\Jack\\Desktop\\des'

    arr = os.listdir(filePath)

    for a in range(len(arr)):
        #os.system('hemo exe location -csv ' + "path of the .csv files arr[a]")
        print(arr[a])


    #os.system('C:\\Users\\Jack\\Desktop\\test\\test.xlsx')
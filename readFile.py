import pandas as pd
import shutil as st
import runHemoTool as hemo

def main():
    df = pd.read_excel('C:\\Users\\Jack\\Desktop\\test\\test.xlsx', sheet_name='Sheet2')
    mylist = df['A'].tolist()

    for a in range(len(mylist)):
        splitting = mylist[a].split('\\')
        fileName = splitting[len(splitting)-1]
        st.copyfile(mylist[a], 'C:\\Users\\Jack\\Desktop\\des\\' + fileName)

    hemo.runHemo()

if __name__ == "__main__":
    main()



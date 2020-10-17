from openpyxl import load_workbook
import os
#处理.xlsx
class Deal_Excel:
    def __init__(self,tar_dir):
        self.__dir = tar_dir
        
    def Get_Excel(self):
        #扫描当前目录下的.xlsx
        tar_dir = os.listdir(self.__dir)
        #找到所有的Excel文件
        self.Excel_List = []
        for file in tar_dir:
            if file.split(".")[-1] == "xlsx":
                self.Excel_List.append(file)
         
        print("excel文件列表:"+str(self.Excel_List))

    def Open_Excel(self):
        #打开所有excel文件
        for excel in self.Excel_List:
            self.excel = load_workbook(excel)
            # 显示所有表名
            print("显示所有表名:"+str(self.excel.sheetnames))
            
            
if __name__ == "__main__":
    t = Deal_Excel("./")
    t.Get_Excel()
    t.Open_Excel()

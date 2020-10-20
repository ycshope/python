from openpyxl import load_workbook
from openpyxl.workbook import Workbook 
import os
import re
import time
#处理.xlsx
class Deal_Excel:
    def __init__(self,tar_dir):
        self.__dir = tar_dir
        #支持的excel类型
        self.__file_type = ["xlsm", "xlsx", "xltx", "xltm"]
    
    #获取某个文件目录下的excel
    def Get_Excel(self):
        #扫描当前目录下的.xlsx
        tar_dir = os.listdir(self.__dir)
        #找到所有的Excel文件
        self.Excel_List = []
        for file in tar_dir:
            if file.split(".")[-1] in self.__file_type: #xlsm读取比较慢
                self.Excel_List.append(file)
        print("excel文件列表:"+str(self.Excel_List))
    
    #打开excel文件
    def Open_Excel(self):
        for excel in self.Excel_List:
            self.excel = load_workbook(excel,keep_vba=True)   
            # 显示所有表名
            print("显示所有表名:"+str(self.excel.sheetnames))
            #遍历所有的sheet
            for sheet in self.excel.sheetnames :
                print("当前的sheet为:"+str(sheet))
                self.Read_Sheet(sheet)
    
    #读sheet
    def Read_Sheet(self, sheet_name):
        #选择sheet
        self.sheet = self.excel.get_sheet_by_name(sheet_name)
        #访问指定的sheet的内容,通过指定范围(行 → 行)
        for row in self.sheet.iter_rows(min_row=1, max_col=10, max_row=6):
            for cell in row:
                if cell.value != None:
                    print(cell) #结果为<Cell Sheet1.A1>指定了元素
                    print(cell.value)
    
    #附加数据
    def Append_Line(self, contain):
        #会在文件的最后一行(从没数据开始的第一行,添加数据)
        self.sheet.append(contain)
        self.excel.save(self.Excel_List[0])
    
    #创建excel,和指定的sheet
    def Create_Excel(self, filename, sheetname=None):
        if filename is None:
            print("请输入文件名!")
            return False
        self._filename = filename
        if self._filename in self.__dir:
            print("文件已存在!")
            return False
        #默认sheet为系统时间
        if sheetname is None:
            #sheetname = str(time.asctime(time.localtime(time.time()))) 包含特殊字符,无法创建
            sheetname = str(time.time())
        
 
        self.__excel_name = filename
        #创建excel
        #实例化
        self.__excel = Workbook()
        #激活 worksheet,默认对第一张表格进项操作
        self.__sheet = self.__excel.active
        #sheet命名
        self.__sheet = sheetname
        #冲突检测
        #创建sheet
        #self.__excel.create_sheet(sheetname) 新建的excel会默认携带一个名为"sheet"的sheet
        self.__excel.save(self.__excel_name)
          
if __name__ == "__main__":
    t = Deal_Excel("./")
    t.Create_Excel("kali.xlsx")
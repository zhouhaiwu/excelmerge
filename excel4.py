# -*- coding:utf-8 -*-

import xlrd, xlsxwriter

# 待合并excel
allxls = ["D:\\excelcs\\****（20181018-20181024)***.xlsx"]
allxls1 = ["D:\\excelcs\\****（20181018-20181024)***.xlsx"]
allxls2 = ["D:\\excelcs\\****（20181018-20181024)***.xlsx"]
#print(allxls[0:2])
# 目标excel
end_xls = "D:\\excelcs\\工作周报（20181018-20181024)应用维护部.xlsx"


def open_xls(file):
    try:
        fh = xlrd.open_workbook(file)
        return fh
    except Exception as e:
        print("打开文件错误：" + e)


# 根据excel名以及第几个标签信息就可以得到具体标签的内容
def get_file_value(filename, sheetnum):
    rvalue = []
    fh = open_xls(filename)
    sheet = fh.sheets()[sheetnum]
    row_num = sheet.nrows
    for rownum in range(0, row_num):
        rvalue.append(sheet.row_values(rownum))
    return rvalue

###获取第一个excel的sheet个数以及名字作为标准
#获取excel的个数以及名字作为标准
first_file_fh = open_xls(allxls[0])
first_file_fh1 = open_xls(allxls1[0])
first_file_fh2 = open_xls(allxls2[0])
first_file_sheet = first_file_fh.sheets()
first_file_sheet1 = first_file_fh1.sheets()
first_file_sheet2 = first_file_fh2.sheets()
first_file_sheet_num = len(first_file_sheet)
#print(first_file_sheet_num)
sheet_name = []
#sheet_name1 = []
#sheet_name2 = []
for sheetname in first_file_sheet:
    sheet_name.append(sheetname.name)
for sheetname in first_file_sheet1:
    sheet_name.append(sheetname.name)
for sheetname in first_file_sheet2:
    sheet_name.append(sheetname.name)
#print("sheet_name:", sheet_name)
# 定义一个目标excel
endxls = xlsxwriter.Workbook(end_xls)

all_sheet_value = []
all_sheet_value1 = []
all_sheet_value2 = []
# 把所有内容都放到列表all_sheet_value中
#for file_name in allxls:
#for sheet_num in range(0, first_file_sheet_num):
#    all_sheet_value.append([])
#    for file_name in allxls:
#    #for sheet_num in range(0, first_file_sheet_num):
#        print("正在读取" + file_name + "的第" + str(sheet_num + 1) + "个标签...")
#        file_value = get_file_value(file_name, sheet_num)
#        all_sheet_value[sheet_num].append(file_value)
#        print("file_value:", file_value)

for file_name in allxls:
    all_sheet_value.append([])
    for sheet_num in range(0, first_file_sheet_num):
        print("正在读取" + file_name + "的第" + str(sheet_num + 1) + "个标签...")
        file_value = get_file_value(file_name, sheet_num)
        all_sheet_value[sheet_num].append(file_value)

for file_name in allxls1:
    all_sheet_value1.append([])
    for sheet_num in range(0, first_file_sheet_num):
        print("正在读取" + file_name + "的第" + str(sheet_num + 1) + "个标签...")
        file_value = get_file_value(file_name, sheet_num)
        all_sheet_value1[sheet_num].append(file_value)

for file_name in allxls2:
    all_sheet_value2.append([])
    for sheet_num in range(0, first_file_sheet_num):
        print("正在读取" + file_name + "的第" + str(sheet_num + 1) + "个标签...")
        file_value = get_file_value(file_name, sheet_num)
        all_sheet_value2[sheet_num].append(file_value)
        #print("file_value:", file_value)
#print(all_sheet_value[0])
print("*************************")
print("*************************")
print("*************************")
#print(all_sheet_value[1])
all_sheet_value3 = all_sheet_value + all_sheet_value1 + all_sheet_value2
print("########################")
print("########################")
print("########################")
print(all_sheet_value3)
num = -1
sheet_index = -1
#print(sheet_name)
#print(all_sheet_value[value_index])
# 将列表all_sheet_value的内容写入目标excel
for sheet in (all_sheet_value3):
    sheet_index += 1
    end_xls_sheet = endxls.add_worksheet(sheet_name[sheet_index])
    num += 1
    num1 = -1
    for sheet1 in sheet:
        for sheet2 in sheet1:
            print(type(sheet2))
            num1 += 1
            num2 = -1
            for sheet3 in sheet2:
                num2 += 1
                # 在第num1行的第num2列写入sheet3的内容
                end_xls_sheet.write(num1, num2, sheet3)

endxls.close()

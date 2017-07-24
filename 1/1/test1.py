# -*- coding: cp936 -*-
import xlrd,os,sys,random,xlwt
import myConst

def read_execl():
    path = os.getcwd()
    path = path + '\\1.xlsx'
    data = xlrd.open_workbook(path)
    oldTable = data.sheets()[2]
    nrows = oldTable.nrows
    ncols = oldTable.ncols
    for i in range(nrows-1):
        for j in range(ncols-1):
            one =oldTable.cell(i,j)
            value = one.value
            #print "one.ctype is "
            #print one.ctype
            if one.ctype == 2:
                #print "one.ctype is,%d",one.ctype
                print value
            if one.ctype == 1:
                print value.encode('utf-8')

def read_excel1():
    path = os.getcwd()
    path = path + '\\resource\\2.xlsx'
    data = xlrd.open_workbook(path)
    oldTable = data.sheets()[0]
    targetNum =  oldTable.col_values(3)[0]
    targetNum = int(targetNum)
    nrows = oldTable.nrows  
    targetFirstNum = oldTable.col_values(2)
    namelist = oldTable.col_values(1)
    countryList = oldTable.col_values(0)
    return targetFirstNum,countryList,namelist,targetNum,nrows

def getDataAndUse1(targetFirstNum,countryList,namelist,nrows):
    randomChangeX = random.randint(1, nrows)
    newCountryList = []
    newNameList = []
    for i in range(nrows):
        num = targetFirstNum[i]
        num = num + randomChangeX
        num = int(num)
        if num >  nrows :
            num = num - nrows
        newCountryList.insert(num-1,countryList[i])
        newNameList.insert(num-1,namelist[i])
    return newCountryList,newNameList

def write_execl1(newCountryList,newNameList,targetNum):
    f = xlwt.Workbook()
    sheet1 = f.add_sheet('sheet1')
    changeNum = 1
    newCol1 = 0
    newCol2 = 1
    for i in range(nrows):
        x = i
        if x >= targetNum * changeNum:
            newCol1 = newCol1 + 2
            newCol2 = newCol2 + 2
            x = x - targetNum * changeNum
            changeNum = changeNum + 1
        else:
            x = x - targetNum * (changeNum - 1)
        sheet1.write(x,newCol1,newCountryList[i])
        sheet1.write(x,newCol2,newNameList[i])
    f.save('result.xls')

if __name__ == '__main__':
    read_execl()
    #targetFirstNum,countryList,namelist,targetNum,nrows = read_excel()
    #newCountryList,newNameList = getDataAndUse(targetFirstNum,countryList,namelist,nrows)
    #write_execl(newCountryList,newNameList,targetNum)

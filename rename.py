#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
lstOld = []
def gci(filepath):
    #遍历filepath下所有文件，包括子目录
    files = os.listdir(filepath)
    for fi in files:
        if("lottie" == fi):
            continue

        fi_d = os.path.join(filepath,fi)
        print("fi: ",fi_d,type(fi_d))

        if os.path.isdir(fi_d):
            print("is Dir",fi_d)
            gci(fi_d)
        else:
            print("is file",fi_d)
            lst1 = fi_d.split(".")
            print(lst1)
            if lst1[len(lst1)-1] != "json":
                continue
            lstOld.append(fi_d)
            # # os.rename(fi_d,).
            # strNewName = lst1[1]
            # strNewName = strNewName.replace("\\","")
            # strNewName += ".json"
            # strCmd = 'mv %s ./New/%s' % (fi_d,strNewName)
            # os.system(strCmd)
            # print(strCmd)
#递归遍历/root目录下所有文件
gci('.')

for fi_d in lstOld:
    lst1 = fi_d.split(".")
    strNewName = lst1[1]
    strNewName = strNewName.replace("\\","_")
    strNewName = strNewName[1:]
    strNewName += ".json"
    strCmd = 'cp %s .\\lottie\\%s' % (fi_d,strNewName)
    print(strCmd)
    os.system(strCmd)

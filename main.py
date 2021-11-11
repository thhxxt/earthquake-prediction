import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"
import xlrd
from time import *
import pandas as pd
file_dir = "/Users/wangbohan/Desktop/dataALLFields"
all_file_list=os.listdir(file_dir)
import openpyxl

file_injection = []
file_production = []
file_extra = []

path = "/Users/wangbohan/Desktop/dataAllFields/"

for single_file in all_file_list:
    if single_file.find("Production") >= 0:
        file_production.append(single_file)
    elif single_file.find("Injection") >= 0:
        file_injection.append(single_file)
    else:
        file_extra.append(single_file)

file_production_new = []
file_injection_new = []


i=0
begin_time_p = time()
for single_file in file_production:
    test = xlrd.open_workbook(path+single_file)
    sheet_object = test.sheet_by_name("Well Production")
    nrows = sheet_object.nrows
    i = i+1
    if nrows > 4:
        print(i)
        file_production_new.append(single_file)
    else:
        continue
end_time_p = time()

print("__________________________________")
'''
m = 0
begin_time_i = time()
for single_file in file_injection:
    test = xlrd.open_workbook(path+single_file)
    sheet_object = test.sheet_by_name("Well Injection")
    nrows = sheet_object.nrows
    m = m+1
    if nrows > 4:
        print(m)
        file_injection_new.append(single_file)
    else:
        continue
end_time_i = time()

print("---------------------------------")
'''
print("The length of file_production_new is %d" % len(file_production_new))
print("The running time of file_production_new is %f" % (end_time_p - begin_time_p))
#print("The length of file_injection_new is %d" % (len(file_injection_new)))
#print("The running time of file_injection_new is %f" % (end_time_i - begin_time_i))
#print("The total running time is %f" % (end_time_i - begin_time_i + end_time_p - begin_time_p))

print("---------------------------------")
''''
res = pd.DataFrame(columns=['Injection Date', 'Water or Steam Injected (bbl)', 'Well #','Latitude','Longitude'])
n=0
begin_time_c = time()
for single_file in file_injection_new:
    data1 = pd.read_excel(path+single_file, header=3, usecols=[1, 2])
    data2 = pd.read_excel(path+single_file, header=0, usecols=[5, 13, 14])
    data1 = data1[data1["Water or Steam Injected (bbl)"] > 0]
    data1["Well #"] = data2.iat[0, 0]
    data1["Latitude"] = data2.iat[0, 1]
    data1["Longitude"] = data2.iat[0, 2]
    res = pd.concat([res, data1], axis=0, ignore_index=True)
    n = n+1
    print(n)
end_time_c = time()


time = end_time_c-begin_time_c
print("---------------------------------")
print(time)
print(res)
'''
res_production = pd.DataFrame(columns=['Production Date', 'Oil Produced (bbl)', 'Water Produced (bbl)', 'Well #', 'Latitude', 'Longitude'])

begin_time_p_new = time()
p = 0
for single_file in file_production_new:
    data1 = pd.read_excel(path+single_file, header=3, usecols=[1, 2,3])
    data2 = pd.read_excel(path+single_file, header=0, usecols=[5, 13, 14])
    data1["Well #"] = data2.iat[0, 0]
    data1["Latitude"] = data2.iat[0, 1]
    data1["Longitude"] = data2.iat[0, 2]
    res_production = pd.concat([res_production, data1], axis=0, ignore_index=True)
    p = p+1
    print(p)
end_time_p_new = time()

time_p = end_time_p_new - begin_time_p_new
print("---------------------------------")
print(time_p)
print()
print(res_production)
import xlrd


def read_data():
    temp = []
    dataset = []
    # 导入excel数据放入data
    data = xlrd.open_workbook(
        r'C:\Users\12498\Desktop\PR_homwork1\作业数据_2021合成.xls')
    # 取sheet1
    sheet = data.sheet_by_index(0)  #索引的方式，从0开始
    # 读取最大行数
    nrows = sheet.nrows  
    # 生成数据集dataset
    for i in range(1, nrows):
        temp.append(sheet.cell(i, 3).value)
        temp.append(sheet.cell(i, 4).value)
        temp.append(sheet.cell(i, 6).value)
        temp.append(sheet.cell(i, 7).value)
        temp.append(sheet.cell(i, 1).value)
        dataset.append(temp)
        temp = []
    return dataset

# 有空值，用来补全数据用，找到身高体重最接近的，用他的成绩来代替
def comp_data(data):
    for i in range(len(data)):
        if data[i][2]=='':
            x=(data[i][0]-data[0][0])**2+(data[i][1]-data[0][1])**2
            for j in range(len(data)-1):
                y=(data[i][0]-data[j][0])**2+(data[i][1]-data[j][1])**2
                if y<x and i!=j:
                    x=y
                    index=j
            data[i][2]=data[index][2]
            data[i][3]=data[index][3]
    return data


import random


# 初始化中心点，a是数据个数，b是分成几类，有几类就初始化几个中心点
def init_center(a, b):
    random_list = []
    for i in range(b):
        x = random.randint(0, a - 1)
        random_list.append(x)
    m = set(random_list)
    if len(m) == len(random_list):
        return random_list
    else:
        return init_center(a, b)  #递归调用，直到长度相等返回random_list


# 计算两点间的距离，要的是大小不是具体数值，开方不开方一样
def distance(a, b):  
    x = (a[0] - b[0])**2 + (a[1] - b[1])**2 + (a[2] - b[2])**2 + (a[3] -b[3])**2
    x= round(x,2)
    return x

# 返回数据集的中心点
def calc_center(a):
    center=[]
    for j in range(4):
        sum=0
        for i in range(len(a)):
            sum=sum+a[i][j]
        x=sum/len(a)
        x=round(x,2)
        center.append(x)
    return center

# 定义想要将数据分成几类
leibieshu=4
result_index=[]
result_all=[]
# 创建根据类别个数的空列表
for i in range(leibieshu):
    temp_list = []
    result_all.append(temp_list)
for i in range(leibieshu):
    temp_list = []
    result_index.append(temp_list)    
# 读取数据
dataset=read_data()
dataset=comp_data(dataset)#补全数据
n=len(dataset)
print(n)
# 初始化中心点
init_center=init_center(n,leibieshu)
print(init_center)
temp_init=[]
for i in range(len(init_center)):
    temp_init.append(dataset[init_center[i]])
print(temp_init)    

# 计算每个点到中心点的距离，第一次分类
for i in range(n):
    dis=distance(dataset[i],dataset[init_center[0]])
    index=init_center[0]
    for j in range(leibieshu):#找到距离最小的点
        x=distance(dataset[i],dataset[init_center[j]])
        if x<dis:
            dis=x
            index=init_center[j]
    index_a=init_center.index(index)#返回位置
    '''
    if index==init_center[0]:
        index_a=0
    else:
        index_a=1
    '''    
    result_index[index_a].append(i)
    result_all[index_a].append(dataset[i])#按照位置将结果存进列表

center=[]
center_after=[]

# 计算第二次的中心点
for i in range(leibieshu):

    center_after.append(calc_center(result_all[i]))
# print(center_after)    
while center!=center_after:#中心点不再变化，循环停止
    center=center_after
    result_all=[]
    result_index=[]
    for i in range(leibieshu):
        temp_list = []
        result_all.append(temp_list)
    # print(result_all)
    for i in range(leibieshu):
        temp_list = []
        result_index.append(temp_list)
    for i in range(n):
        dis=distance(dataset[i],center[0])
        index=center[0]
        for j in range(leibieshu):
            x=distance(dataset[i],center[j])
            if x<dis:
                dis=x
                index=center[j]
        index_a=center.index(index)
        '''
        if index==center[0]:
            index_a=0
        else:
            index_a=1
        '''    
        result_index[index_a].append(i)
        result_all[index_a].append(dataset[i])
    # print(result_all)    
    center_after=[]
    for i in range(leibieshu):
        center_after.append(calc_center(result_all[i])) 

print(center)
for i in range(leibieshu):
    print(result_index[i])

# print(result_all[0])

for j in range(leibieshu):
    temp_t=[]
    for i in range(len(result_all[j])):
        temp=result_all[j][i]
        temp_t.append(temp[4])
    print(temp_t)
    temp_1=0
    for i in range(len(temp_t)):
        temp_1=temp_1+float(temp_t[i])
    r=temp_1/len(temp_t)    
    print('男生比例为：',r)


   














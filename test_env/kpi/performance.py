#coding=utf-8

import os
import sys
import re

global config_path
global html_template_path
global csv_template_path

def kpi_path():
    return sys.path[0]+os.sep

config_path = kpi_path() + 'config'+os.sep
print "config_path: ", sys.path[0]
html_template_path = kpi_path() + 'res/html_template'+os.sep
csv_template_path = kpi_path() + 'res/csv_template'+os.sep

def get_data_list(path_input):
    log = []
    log_list = []
    weight = []
    weight_list = []
    reference = []
    reference_list = []
    #取出所有数据至log_list
    try:
        file1 = open(path_input,'rb')
    except Exception:
        print "Performance.py get_data_list()  kpi_log.Qsst lose"
        exit(1)
    lines = file1.readlines()
    for line in lines:
        if line.find('#') > -1:
            log.append(line)
    #数据长度
    x = len(log)
    i = 0
    j = 0
    #数据分类
    for i in range(x):
        log_list.append(log[i].split(":"))
    #取出所有数据至weight_list
    try:
        file2 = open(config_path + "weight.txt",'rb')
    except Exception:
        print " Performance.py get_data_list()  weight.text lose"
    lines = file2.readlines()
    for line in lines:
        if line.find("#") > -1:
            weight.append(line)
    #数据分类
    z =len(weight)
    for i in range(z):
        weight_list.append(weight[i].split(":"))
    #添加权重到log_list
    for i in range(x):
        for j in range(z):
            if log_list[i][0] == weight_list[j][0] and log_list[i][1] == weight_list[j][1]:
                log_list[i].append(weight_list[j][2])
    #取出所有数据至reference_list
    try:
        file3 = open(config_path + "reference_data.txt",'rb')
    except Exception:
        print " Performance.py get_data_list()  reference_data.text lose"
    lines = file3.readlines()
    for line in lines:
        if line.find('#') > -1:
            reference.append(line)
    #数据分类
    w =len(weight)
    for i in range(w):
        reference_list.append(reference[i].split(":"))
    #添加对比到log_list
    for i in range(x):
        for j in range(w):
            if log_list[i][0] == reference_list[j][0] and log_list[i][1] == reference_list[j][1]:
                log_list[i].append(reference_list[j][2])
    #计算diff
    for i in range(x):
        log_list[i].append(str(((float(log_list[i][4][:-1])-float(log_list[i][2][:-1]))/float(log_list[i][4][:-1]))))
    #计算succeed
    for i in range(x):
        if float(log_list[i][5]) > float(0.05):
            log_list[i].append("succeed")
        else:
            log_list[i].append("failed")
    #计算测试分数
    for i in range(x):
        log_list[i].append(float(log_list[i][2][:-1])*float(log_list[i][3][:-1]))
    #计算参考分数
    for i in range(x):
        log_list[i].append(float(log_list[i][4][:-1])*float(log_list[i][3][:-1]))
    list = log_list
    return list

def get_list(path_input):
    dict ={}
    list = get_data_list(path_input)
    x = len(list)
    i = 0
    for i in range(x):
        if dict.has_key(list[i][0]):
            dict[list[i][0]].append(list[i]);
        else:
            dict[list[i][0]] = [list[i]];
    return dict

def get_html_list(path_input):
    dict_html = {}
    list_html = []
    list = get_data_list(path_input)
    x = len(list)
    i = 0
    for i in range(x):
        list_html.append('<TR><TD colSpan=5><FONT size=+1><B><CENTER>'+ list[i][1] + '</CENTER></B></FONT></TD><TD colSpan=1><FONT size=+1><B><CENTER>'+ list[i][3][:-2]+ '</CENTER></B></FONT></TD><TD colSpan=1><FONT size=+1><B><CENTER>'+ list[i][2][:-1] + '</CENTER></B></FONT></TD><TD colSpan=1><FONT size=+1><B><CENTER>'+ list[i][4][:-2] + '</CENTER></B></FONT></TD><TD colSpan=1><FONT size=+1><B><CENTER>'+ str(float(list[i][5])*100)[0:5] +'%'+ '</CENTER></B></FONT></TD><TD colSpan=1><FONT size=+1><B><CENTER>'+ list[i][6] + '</CENTER></B></FONT></TD></TR>')
    for i in range(x):
        if dict_html.has_key(list[i][0]):
            dict_html[list[i][0]].append(list_html[i]);
        else:
            dict_html[list[i][0]] = [list_html[i]];
    return dict_html

def get_csv_list(path_input):
    dict_html = {}
    list_html = []
    list = get_data_list(path_input)
    x = len(list)
    i = 0
    for i in range(x):
        list_html.append([list[i][1],list[i][3][:-2],list[i][2][:-2],list[i][4][:-2],str(float(list[i][5])*100)[0:5]+'%',list[i][6]])
    for i in range(x):
        if dict_html.has_key(list[i][0]):
            dict_html[list[i][0]].append(list_html[i]);
        else:
            dict_html[list[i][0]] = [list_html[i]];
    return dict_html

def get_score(path_input):
    dict = get_list(path_input)
    list = get_data_list(path_input)
    dict_data ={}
    dict_reference ={}
    category = []
    category_list = []
    category_name = []
    data_score = []
    reference_score = []
    diff = []
    diff1 = []
    result = []
    score = []
    score_list = []
    x = len(list)
    i = 0
    for i in range(x):
        category_list.append(list[i][0])
    #判断category数量
        category = [i for i in set(category_list)]
    y =len(category)
    #category_name
    for i in range(y):
        category_name.append(dict.items()[i][0][1:])
    #data_score
    for i in range(x):
        if dict_data.has_key(list[i][0]):
            dict_data[list[i][0]].append(list[i][7]);
        else:
            dict_data[list[i][0]] = [list[i][7]];
    for i in range(y):
        data_score.append(int(sum(dict_data.items()[i][1])/len(dict_data.items()[i][1])))
    #reference_score
    for i in range(x):
        if dict_reference.has_key(list[i][0]):
            dict_reference[list[i][0]].append(list[i][8]);
        else:
            dict_reference[list[i][0]] = [list[i][8]];
    for i in range(y):
        reference_score.append(int(sum(dict_reference.items()[i][1])/len(dict_reference.items()[i][1])))
    #diff
    for i in range(y):
        diff1.append((float(reference_score[i])-float(data_score[i]))/(float(reference_score[i])))
        diff.append((float(reference_score[i])-float(data_score[i]))/(float(reference_score[i])) * 100)
    #result
    for i in range(y):
        if diff1[i] > 0.05:
            result.append("succeed")
        else:
            result.append("failed")
    score = [category_name,data_score,reference_score,diff,result]
    for i in range(y):
        score_list.append('<TR><TD colSpan=3><FONT size=+1><B><CENTER>'+ str(score[0][i]) +'</CENTER></B></FONT></TD><TD colSpan=2><FONT size=+1><B><CENTER>' + str(score[1][i]) +'</CENTER></B></FONT></TD><TD colSpan=1><FONT size=+1><B><CENTER>'+ str(score[2][i]) +'</CENTER></B></FONT></TD><TD colSpan=2><FONT size=+1><B><CENTER>' + str(score[3][i])[0:4]+"%" +'</CENTER></B></FONT></TD><TD colSpan=2><FONT size=+1><B><CENTER>' +score[4][i] +'</CENTER></B></FONT></TD></TR>')
    return  score_list

def get_csv_score(path_input):
    dict = get_list(path_input)
    list = get_data_list(path_input)
    dict_data ={}
    dict_reference ={}
    category = []
    category_list = []
    category_name = []
    data_score = []
    reference_score = []
    diff = []
    diff1 = []
    result = []
    score = []
    score_list = []
    x = len(list)
    i = 0
    for i in range(x):
        category_list.append(list[i][0])
    #判断category数量
        category = [i for i in set(category_list)]
    y =len(category)
    #category_name
    for i in range(y):
        category_name.append(dict.items()[i][0][1:])
    #data_score
    for i in range(x):
        if dict_data.has_key(list[i][0]):
            dict_data[list[i][0]].append(list[i][7]);
        else:
            dict_data[list[i][0]] = [list[i][7]];
    for i in range(y):
        data_score.append(int(sum(dict_data.items()[i][1])/len(dict_data.items()[i][1])))
    #reference_score
    for i in range(x):
        if dict_reference.has_key(list[i][0]):
            dict_reference[list[i][0]].append(list[i][8]);
        else:
            dict_reference[list[i][0]] = [list[i][8]];
    for i in range(y):
        reference_score.append(int(sum(dict_reference.items()[i][1])/len(dict_reference.items()[i][1])))
    #diff
    for i in range(y):
        diff1.append((float(reference_score[i])-float(data_score[i]))/(float(reference_score[i])))
        diff.append((float(reference_score[i])-float(data_score[i]))/(float(reference_score[i])) * 100)
    #result
    for i in range(y):
        if diff1[i] > 0.05:
            result.append("succeed")
        else:
            result.append("failed")
    #clean up to array
    for i in range(y):
        score.append([category_name[i],data_score[i],reference_score[i],str(diff[i])+'%',result[i]])
    return score

def html(path_input,path_output):
    '''
    Rewrite the html. Read-in the data to the report.
    '''
    list = get_data_list(path_input)
    dict = get_list(path_input)
    score = get_score(path_input)
    dict_html = get_html_list(path_input)
    category_list = []
    category = []
    #保存路径
    path = kpi_path()
    #检查目录
    if not os.path.exists(path):
        os.makedirs(path)
    i = 0
    x = len(list)
    j = 0
    for i in range(x):
        category_list.append(list[i][0])
    #判断category数量
        category = [i for i in set(category_list)]
    y =len(category)
    #创建详细列表

    try:
        test_title= open(html_template_path+'Test_title.html','rb')
    except Exception:
        print "Performance.py html()  Test_title.html lose"
        exit(1)
        return
    try:
        detal_report= open(path+'Detal_report.html','wb+')
    except Exception:
        print " Performance.py html()  Detal_report.html lose"
    lines = test_title.readlines()
    for j in range(y):
        for line in lines:
            #替换开始测试CATEGORY
            if line.find('#category#') > -1:
                afertstr = line.replace('#category#',str(category[j][1:]))
                detal_report.write(afertstr)
            #替换data
            elif line.find('#replace#') > -1:
                    afertstr = line.replace('#replace#',str(dict_html.items()[j][1]))
                    detal_report.write(afertstr)
            else:
                    detal_report.write(line)
    test_title.close()
    detal_report.close()
    #去除标点等等不需要元素
    detal_report= open(path+'Detal_report.html','rb')
    detal_report1= open(path+'Detal_report1.html','wb+')
    lines = detal_report.readlines()
    for line in lines:
        if line.find("['") > -1:
            afertstr = line.replace("['",' ')
            detal_report1.write(afertstr)
        else:
            detal_report1.write(line)
    detal_report1= open(path+'Detal_report1.html','rb')
    detal_report2= open(path+'Detal_report2.html','wb+')
    lines = detal_report1.readlines()
    for line in lines:
        if line.find("']") > -1:
            afertstr = line.replace("']",' ')
            detal_report2.write(afertstr)
        else:
            detal_report2.write(line)
    detal_report2= open(path+'Detal_report2.html','rb')
    detal_report3= open(path+'Detal_report3.html','wb+')
    lines = detal_report2.readlines()
    for line in lines:
        if line.find("', '") > -1:
            afertstr = line.replace("', '",' ')
            detal_report3.write(afertstr)
        else:
            detal_report3.write(line)
    #正文
    try:
        html = open(path_output,'wb+')
    except Exception:
        print "Performance.py html()  Performance.html lose"
        exit(1)
        return
    #替换summary
    try:
        summary= open(html_template_path+'Summary.html','rb')
    except Exception:
        print "Performance.py html()  Summary.html lose"
        exit(1)
        return
    lines = summary.readlines()
    for line in lines:
        if line.find('#replace#') > -1:
            for j in range(y):
                afertstr = line.replace('#replace#',score[j])
                html.write(afertstr)
        else:
            html.write(line)
    #加入详细内容
    try:
        detal_report3= open(path+'Detal_report3.html','rb')
    except Exception:
        print "Performance.py html()  Detal_report3.html lose"
        exit(1)
        return
    lines = detal_report3.readlines()
    for line in lines:
        html.write(line)
    html.close()
    detal_report.close()
    detal_report1.close()
    detal_report2.close()
    detal_report3.close()
    summary.close()
    #删除html等
    os.remove(path+'Detal_report.html')
    os.remove(path+'Detal_report1.html')
    os.remove(path+'Detal_report2.html')
    os.remove(path+'Detal_report3.html')

def csv(path_input,path_output):
    list = get_data_list(path_input)
    dict = get_list(path_input)
    score = get_csv_score(path_input)
    dict_html = get_csv_list(path_input)
    category_list = []
    category = []
    path = kpi_path()
    #检查目录
    if not os.path.exists(path):
        os.makedirs(path)
    i = 0
    x = len(list)
    j = 0
    for i in range(x):
        category_list.append(list[i][0])
    #判断category数量
        category = [i for i in set(category_list)]
    y =len(category)
    #创建详细列表
    try:
        test_csv_title= open(csv_template_path+'Test_title.csv','rb')
    except Exception:
        print "Performance.py html()  Test_title.csv lose"
        exit(1)
        return
    try:
        detal_csv_report= open(path+'Detal_report.csv','wb+')
    except Exception:
        exit(1)
        return
    lines = test_csv_title.readlines()
    for j in range(y):
        for line in lines:
            #替换开始测试CATEGORY
            if line.find('#category#') > -1:
                afertstr = line.replace('#category#',str(category[j][1:]))
                detal_csv_report.write(afertstr)
            #替换data
            elif line.find('#replace#') > -1:
                    afertstr = line.replace('#replace#',str(dict_html.items()[j][1]))
                    detal_csv_report.write(afertstr)
            else:
                detal_csv_report.write(line)
    test_csv_title.close()
    detal_csv_report.close()
    #正文
    try:
        csv = open(path+'kpi_report.csv','wb+')
    except Exception:
        print "Performance.py html()  Performance.csv lose"
        exit(1)
        return
    #替换summary
    try:
        summary_csv= open(csv_template_path+'Summary.csv','rb')
    except Exception:
        print "Performance.py html()  Summary.csv lose"
        exit(1)
        return
    lines = summary_csv.readlines()
    for line in lines:
        if line.find('#replace#') > -1:
            for i in range(y):
                afertstr = line.replace('#replace#',str(score[i]))
                csv.write(afertstr)
        else:
            csv.write(line)
    summary_csv.close()
    #加入详细内容
    try:
        detal_csv_report= open(path+'Detal_report.csv','rb')
    except Exception:
        exit(1)
        return
    lines = detal_csv_report.readlines()
    for line in lines:
        csv.write(line)
    detal_csv_report.close()
    csv.close()
    #clean up csv
    csv1= open(path+'kpi_report.csv','rb+')
    kpi_csv_report1= open(path+'kpi_csv_report1.csv','wb+')
    lines = csv1.readlines()
    for line in lines:
        if line.find('], [') > -1:
            afertstr = line.replace('], [','\n')
            kpi_csv_report1.write(afertstr)
        else:
            kpi_csv_report1.write(line)
    csv1.close()
    kpi_csv_report1.close()
    csv2= open(path+'kpi_csv_report1.csv','rb+')
    kpi_csv_report2= open(path+'kpi_csv_report2.csv','wb+')
    lines = csv2.readlines()
    for line in lines:
        if line.find('[') > -1:
            afertstr = line.replace('[','')
            kpi_csv_report2.write(afertstr)
        else:
            kpi_csv_report2.write(line)
    csv2.close()
    kpi_csv_report2.close()
    csv3= open(path+'kpi_csv_report2.csv','rb+')
    kpi_csv_report3= open(path+'kpi_csv_report3.csv','wb+')
    lines = csv3.readlines()
    for line in lines:
        if line.find(']') > -1:
            afertstr = line.replace(']','')
            kpi_csv_report3.write(afertstr)
        else:
            kpi_csv_report3.write(line)
    csv3.close()
    kpi_csv_report3.close()
    csv4= open(path+'kpi_csv_report3.csv','rb+')
    kpi_csv_report= open(path_output,'wb+')
    lines = csv4.readlines()
    for line in lines:
        if line.find("'") > -1:
            afertstr = line.replace("'",'')
            kpi_csv_report.write(afertstr)
        else:
            kpi_csv_report.write(line)
    csv4.close()
    kpi_csv_report.close()
    #delete csv
    os.remove(path+'Detal_report.csv')
    os.remove(path+'kpi_report.csv')
    os.remove(path+'kpi_csv_report1.csv')
    os.remove(path+'kpi_csv_report2.csv')
    os.remove(path+'kpi_csv_report3.csv')
    
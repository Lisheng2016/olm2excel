# -*- coding:UTF8 -*-
import xml.etree.cElementTree as ET
import xlwt

def timeswicher (startTime):
    startTimeSplit = startTime.split('T')
    sepStartTime = startTimeSplit[1]
    startTimeList = sepStartTime.split(':')
    time = int(startTimeList[0])
    if  time <= 16:
        time = time + 8
    else:
        time = time - 16
    #按24小时制处理时间
    startTimeList[0] = str(time)
    startTimeSplit[1] = ':'.join(startTimeList)
    startTime = 'T'.join(startTimeSplit)
    #print startTime
    return startTime

Tree = ET.ElementTree
tree = Tree(file='/tempfile/Calendar.xml')
#处理在OSX上找不到attributes的问题

appointments = []
for count in tree.iterfind('appointment'):
    appointments.append(count)
#print len(appointments)
wb = xlwt.Workbook();
ws = wb.add_sheet('A test sheet')
#新建excel表格并添加’A test sheet’表
currentQuery = 0
#设定计数器
for elem in appointments:
    query = []
    summary = elem.findtext('OPFCalendarEventCopySummary')
    query.append(summary)

    startTime = elem.findtext('OPFCalendarEventCopyStartTime')
    startTime = timeswicher(startTime)

    endTime = elem.findtext('OPFCalendarEventCopyEndTime')
    endTime = timeswicher(endTime)

    organizer = elem.findtext('OPFCalendarEventCopyOrganizer')
    query.append(organizer)

    sepStartTime=startTime.split('T')
    sepEndTime=endTime.split('T')

    for index in range(len(sepStartTime)):
        query.append(sepStartTime[index])

    query.append(sepEndTime[1])
    #print query

    for i in range(len(query)):
        ws.write(currentQuery,i,query[i])
    # 按行添加目标数据
    currentQuery = currentQuery + 1
    #计数器加一并进入下一个appointment

wb.save('sample.xls')
#保存文件准备移动至桌面
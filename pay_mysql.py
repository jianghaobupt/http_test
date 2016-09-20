#!/usr/bin/python
# encoding: utf-8
import MySQLdb
import re   

# 打开数据库连接
db=MySQLdb.connect(user='rnd',db='pay',passwd='P1WD#xyoP',host='192.168.10.216',charset='utf8',port=3306) 
cursor = db.cursor()

#cursor.nextset()
def T_OPEN_ORDER(order_no):
    fun= ord(re.sub(r'([\d]+)','',order_no).lower()[-1])-97#获取订单所在分表
    sql="SELECT * FROM T_OPEN_ORDER_"+str(fun)+" WHERE order_no='"+order_no+"';"
    #print sql
    cursor.execute(sql)
    data=cursor.fetchall()
    sql1="select COLUMN_NAME from information_schema.COLUMNS where table_name = 'T_OPEN_ORDER_"+str(fun)+"';"
    cursor.execute(sql1)
    data1=cursor.fetchall()
    s=''
    s_json=''
    if len(data)>0:
        for i in range(0,len(data[0])):
            s=s+str(data1[i][0])+"="+str(data[0][i])+","
            s_json=s_json+"\""+str(data1[i][0])+"\""+":"+"\""+str(data[0][i])+"\""+","
        s_json="{"+s_json+"}"
    else:
        s='无数据'
    return s+'&&&'+sql+'&&&'+s_json
def T_OPEN_OFFLINE_ORDER(order_no):
    fun= ord(re.sub(r'([\d]+)','',order_no).lower()[-1])-97#获取订单所在分表
    sql="SELECT * FROM T_OPEN_OFFLINE_ORDER_"+str(fun)+" WHERE order_no='"+order_no+"';"
    #print sql
    cursor.execute(sql)
    data=cursor.fetchall()
    sql1="select COLUMN_NAME from information_schema.COLUMNS where table_name = 'T_OPEN_OFFLINE_ORDER_"+str(fun)+"';"
    cursor.execute(sql1)
    data1=cursor.fetchall()
    s=''
    s_json=''
    if len(data)>0:
        for i in range(0,len(data[0])):
            s=s+str(data1[i][0])+"="+str(data[0][i])+","
            s_json=s_json+"\""+str(data1[i][0])+"\""+":"+"\""+str(data[0][i])+"\""+","
        s_json="{"+s_json+"}"
    else:
        s='无数据'
    return s+'&&&'+sql+'&&&'+s_json

#print (T_OPEN_ORDER("VGd1fF9ihxaMJAMa"))
#print (T_OPEN_ORDER("1jCnK66Gj6gBb1Bz").split('&&&'))[1]



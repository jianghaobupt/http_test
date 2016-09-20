#!/usr/bin/python
#encoding: utf-8
import pay_time
import xlwt
import xlrd
import httplib
import pay_excel
import pay_mysql
import time
import pay_fun
#import pay_redis
import pay_redis_business
import pay_mongodb_business
#import urllib
import hashlib
import json
os_tc = 'pay'
print '开始'

#duandai_ip="172.0.23.184"
pay_ip0 = "pay.tyread.com"
#pay_ip0 = "192.168.10.226:8080"

timestamp = pay_time.datetimestr() + '000'
timestamp_linux = pay_time.timestamp() + '000'
workbook = xlrd.open_workbook('F:/python_http/open_tyyd/TestCase/' + os_tc + '.xls')

#print  workbook.sheet_names()

#print workbook.sheet_names()[0].encode('utf-8')

sheet1 = workbook.sheet_by_name('测试用例')
sheet2 = workbook.sheet_by_name('预期结果')
 
file1 = xlwt.Workbook() 
sheet_1 = file1.add_sheet(u'测试结果', cell_overwrite_ok=True) #创建sheet
sheet_2 = file1.add_sheet(u'测试用例', cell_overwrite_ok=True) #创建sheet
sheet_3 = file1.add_sheet(u'预期结果', cell_overwrite_ok=True) #创建sheet
sheet_4 = file1.add_sheet(u'实际结果', cell_overwrite_ok=True) #创建sheet
# 获取单元格内容的数据类型 
#print sheet1.cell(1,0).ctype #ctype : 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
#print pay_ip
#复制数据
print pay_ip0
for i in range(0, sheet1.nrows): 
    for j in range(0, sheet1.ncols): 
        s = str(sheet1.cell(i, j).value).encode('utf-8')
        sheet_2.write(i, j, str(s))            
for i in range(0, sheet2.nrows): 
    for j in range(0, sheet2.ncols): 
        s = str(sheet2.cell(i, j).value).encode('utf-8')
        sheet_3.write(i, j, str(s)) 
for i in range(0, 1): 
    for j in range(0, sheet2.ncols): 
        s = str(sheet2.cell(i, j).value).encode('utf-8')
        sheet_4.write(i, j, str(s)) 
for i in range(0, sheet2.nrows): 
    s = str(sheet2.cell(i, 0).value).encode('utf-8')
    sheet_4.write(i, 0, str(s))
sheet_1.write(0, 0, '序号',pay_excel.back_yellow())
sheet_1.write(0, 1, '请求数据',pay_excel.back_yellow())
sheet_1.write(0, 2, 'body',pay_excel.back_yellow())
sheet_1.write(0, 3, '响应数据',pay_excel.back_yellow())
sheet_1.write(0, 4, '测试场景',pay_excel.back_yellow())
sheet_1.write(0, 5, '请求时间',pay_excel.back_yellow())
sheet_1.write(0, 6, '方法',pay_excel.back_yellow())
sheet_1.write(0, 7, '测试结果',pay_excel.back_yellow())
res = [''] * (sheet1.nrows + 1)
fail_num=0
order_no = ''
msg_zaixian=''
response=''
json_str = res = [''] * (sheet1.nrows + 1)
json_type = [''] * (sheet1.nrows + 1)
for i in range(1, sheet1.nrows):
    if sheet1.cell(i, 16).value[0:7] == 'pay_ip1': 
        pay_ip='192.168.11.213:8080'
        #print pay_ip
    elif sheet1.cell(i, 16).value[0:7] == 'pay_ip2': 
        pay_ip='192.168.11.214:8080'
        #print pay_ip
    elif sheet1.cell(i, 16).value[0:7] == 'pay_ip3': 
        pay_ip='192.168.10.226:8080'
        #print pay_ip
    else:
        pay_ip=pay_ip0
    url=''
    sql=''
    sheet_1.write(i, 0, str(sheet1.cell(i, 0).value)) #复制序号
    sheet_1.write(i, 6, str(sheet1.cell(i, 14).value)) #复制方法
    sheet_1.write(i, 4, str(sheet1.cell(i, 16).value)) #复制测试场景
    if sheet1.cell(i, 17).value !=''and str(sheet1.cell(i, 0).value) != '':#延迟执行
        time.sleep(sheet1.cell(i, 17).value)
    if sheet1.cell(i, 14).value == 'GET' or  sheet1.cell(i, 14).value == 'POST': 
        if sheet1.cell(i, 16).value[0:3] == 'pay':

            p = [''] * (10)
            pp=['']*len(sheet1.cell(i, 2).value.split(','))
            for j in range(3, 12):
                if sheet1.cell(i, j).value != '' :
                    p1 = str(sheet1.cell(i, j).value)
                    p[j - 2] = p1
            for jj in range(0,len(sheet1.cell(i, 2).value.split(','))):
                pp1=sheet1.cell(i, 2).value.split(',')[jj]
                pp[jj]=pp1
            p=p+pp
            p.sort() #排序
            #print p
            p_body = ''
            for k in range(0, len(p)):
                if p[k] != '': 
                    if p[k] == 'timestamp':
                        p[k] = 'timestamp=' + timestamp
                    elif p[k] == 'timestamp_linux':
                        p[k] = 'timestamp=' + timestamp_linux
                    elif p[k] == 'submit_time':
                        p[k] = 'submit_time=' + timestamp
                    elif p[k] == 'order_no':
                        p[k] = 'order_no=' + order_no
                    elif p[k] == 'msg_zaixian':
                        p[k] = 'msg=' + msg_zaixian
                    elif p[k] == 'out_trade_no':
                        p[k] = 'out_trade_no=' + pay_fun.random_test(20)
                        
                    p_body = p_body + '&' + p[k]
            p_body = p_body[1:]
            #print p_body
            if str(sheet1.cell(i, 13).value) == 'token_pay':
                m = hashlib.md5()
                m.update((p_body + str(sheet1.cell(i, 12).value)).encode("utf8"))
                token = m.hexdigest()
                url = str(sheet1.cell(i, 1).value) + str(p_body) + '&token=' + token
                #print (p_body+str(sheet1.cell(i,12).value)).encode("utf8")
            elif str(sheet1.cell(i, 13).value) == 'token_sign':
                m = hashlib.md5()
                m.update((p_body + str(sheet1.cell(i, 12).value)).encode("utf8"))
                token = m.hexdigest()
                url = str(sheet1.cell(i, 1).value) + str(p_body) + '&sign=' + token
                #print (p_body+str(sheet1.cell(i,12).value)).encode("utf8")
            else:
                url = str(sheet1.cell(i, 1).value) + str(p_body)
            sheet_1.write(i, 1, pay_ip + url)
            sheet_1.write(i, 5, pay_time.datetime()) 
            conn = None
            if sheet1.cell(i, 14).value == 'GET' and str(sheet1.cell(i, 0).value) != '':
                conn = httplib.HTTPConnection(pay_ip)
                conn.request("GET", url)           
                r = conn.getresponse() 
            elif sheet1.cell(i, 14).value == 'POST' and str(sheet1.cell(i, 0).value) != '' :
                try: 
                    #body = urllib.urlencode(sheet1.cell(i,15).value)
                    body = sheet1.cell(i, 15).value
                    #headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
                    headers = {}
                    conn = httplib.HTTPConnection(pay_ip, timeout=30)
                    conn.request("POST", url, body, headers)
                    r = conn.getresponse()
                except Exception, e:
                    print e
            if str(sheet1.cell(i, 0).value) != '' and str(sheet2.cell(i, 0).value) != '' and (sheet1.cell(i, 14).value == 'POST' or sheet1.cell(i, 14).value == 'GET'):
                sheet_4.write(i, 1, str(r.status))
                if r.status == 200:
                    res[i] = r.read()[:30000]#防止数据过长str溢出
                    #print pay_ip + url
                    #print res[i]
                else:
                    sheet_1.write(i, 3, r.status)
                    #print pay_ip + url
                    print r.status
                    res[i]= str(r.status)  
    elif str(sheet1.cell(i, 0).value) != '' and sheet1.cell(i, 14).value == 'MYSQL':
        if sheet1.cell(i, 1).value == 'T_OPEN_ORDER' and order_no!='' and str(sheet1.cell(i, 0).value) != '':
            res[i]=pay_mysql.T_OPEN_ORDER(order_no).split('&&&')[0]
            sql=pay_mysql.T_OPEN_ORDER(order_no).split('&&&')[1]
            sheet_1.write(i, 1, sql)#保存sql
            #print pay_mysql.T_OPEN_ORDER(order_no).split('&&&')[1] 
        elif sheet1.cell(i, 1).value == 'T_OPEN_OFFLINE_ORDER' and order_no!='' and str(sheet1.cell(i, 0).value) != '':
            res[i]=pay_mysql.T_OPEN_OFFLINE_ORDER(order_no).split('&&&')[0]
            sql=pay_mysql.T_OPEN_OFFLINE_ORDER(order_no).split('&&&')[1]
            sheet_1.write(i, 1, sql)#保存sql
            #print pay_mysql.T_OPEN_ORDER(order_no).split('&&&')[1] 
    elif str(sheet1.cell(i, 0).value) != '' and sheet1.cell(i, 14).value == 'REDIS':
        '''
        if sheet1.cell(i, 1).value== 'flushdb' and str(sheet1.cell(i, 0).value) != '':
            res[i]=pay_redis.flushdb()
        '''
        if sheet1.cell(i, 1).value== 'DAY_MONTH_ttl' and str(sheet1.cell(i, 0).value) != '':
            res[i]=pay_redis_business.DAY_MONTH_ttl()
    elif str(sheet1.cell(i, 0).value) != '' and sheet1.cell(i, 14).value == 'MONGODB':
        if sheet1.cell(i, 1).value== 'r_smspay_riskcontrol_data_configer' and str(sheet1.cell(i, 0).value) != '':
            res[i]=pay_mongodb_business.r_smspay_riskcontrol_data_configer(str(sheet1.cell(i, 2).value),str(sheet1.cell(i, 3).value),int(sheet1.cell(i, 4).value)) 
            sheet_1.write(i, 1, str(sheet1.cell(i, 3).value)+'='+str(int(sheet1.cell(i, 4).value)))
        if sheet1.cell(i, 1).value== 'r_smspay_riskcontrol_data_configer_csh' and str(sheet1.cell(i, 0).value) != '':
            res[i]=pay_mongodb_business.r_smspay_riskcontrol_data_configer_csh(str(sheet1.cell(i, 2).value)) 
            sheet_1.write(i, 1, str(sheet1.cell(i, 2).value)+'初始化')
        if sheet1.cell(i, 1).value== 'app_details' and str(sheet1.cell(i, 0).value) != '':
            res[i]=pay_mongodb_business.app_details(str(sheet1.cell(i, 2).value),str(sheet1.cell(i, 3).value),str(sheet1.cell(i, 4).value))
            sheet_1.write(i, 1, str(sheet1.cell(i, 2).value)+'初始化')
    
    elif str(sheet1.cell(i, 0).value) != '' and sheet1.cell(i, 14).value == 'DECRYPT':#sdk解密
        if sheet1.cell(i, 1).value == 'pay_sdk_decrypt':
            url=':pay_sdk_decrypt'
            res[i]=(pay_fun.pay_sdk_decrypt(response))
    if res[i] != '':
        '''
        if sql!='':
            print sql
        else:
            print 'http://'+pay_ip + url
        '''
        #print res[i]
        sheet_1.write(i, 3, str(res[i]))
        try:
            json_type[i] = json.loads(res[i])
            if  json_type[i].has_key('order_no') == True:
                order_no = str(json_type[i]['order_no'])
                #print order_no
            if  json_type[i].has_key('response') == True:
                response= json_type[i]['response']
            if json_type[i] != '' and json_type[i]['response'].has_key('order_no') == True:
                order_no = str(json_type[i]['response']['order_no'])
                msg_zaixian='1,'+order_no+',6'
                
        except Exception, e :
            e=e
            #print json_type[i]['response']['order_no']                
        #json读取
        #json_str[i]= res[i][12:len(r.read())-1]
#比对结果
        if sheet2.nrows > i and sheet2.cell(i, 0).value!='':
            i_unpass=0
            if sheet2.cell(i, 1).value!='':
                if str(r.status)==str(int(sheet2.cell(i, 1).value)):

                    sheet_4.write(i, 1, 'PASS')
                else:
                    sheet_4.write(i, 1, 'FAILED',pay_excel.word_red())
                    i_unpass+=1
            if sheet2.cell(i, 2).value == 'json' : 
                try:
                    json_type[i] = json.loads(res[i])
                    sheet_4.write(i, 2, 'json')
                except Exception, e :
                    sheet_4.write(i, 2, '非json')
                    i_unpass=i_unpass+1
                #print json_type[i]['response']['order_no']
            if sheet2.cell(i, 15).value == '长度大于':
                #print '长度大于'
                if len(res[i])>=int(sheet2.cell(i, 3).value):
                    sheet_4.write(i, 3, 'PASS')
                else:
                    sheet_4.write(i, 3, 'FAILED',pay_excel.word_red())
                    i_unpass+=1
            else:
                for l in range(3, 16): #判断参数是否存在
                    if sheet2.cell(i, l).value != '':
                        if str(sheet2.cell(i, l).value) in res[i]:
                            sheet_4.write(i, l, 'PASS')
                        else:
                            sheet_4.write(i, l, 'FAILED',pay_excel.word_red())
                            i_unpass+=1
            if i_unpass==0:
                sheet_1.write(i, 7, 'pass', pay_excel.back_bright_green())
                print '第 '+str(i)+'行 ——pass ：'+str(sheet1.cell(i, 16).value).encode('utf-8')
            else:
                sheet_1.write(i, 7, 'failed', pay_excel.back_red())
                fail_num+=1
                print '第 '+str(i)+' 行 不通过！！！！！！ ：'+str(sheet1.cell(i, 16).value).encode('utf-8')+'---'+str(res[i])

if fail_num==0:
    print "all testcases pass"
else:
    print str(fail_num)+'条用例未通过'

file1.save('F:/python_http/open_tyyd/TestResults/' + os_tc + '_r.xls') 
print '完成'

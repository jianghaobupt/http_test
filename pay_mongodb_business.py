#coding=utf8

import pymongo
client = pymongo.MongoClient("192.168.1.1", 30000)
db = client.pay 
db1 = client.oauth 

#修改数据
#collection.update({'_id':{'$exists':True}},{'$set':{'num':0}},multi=True)#全部替换
#"cc627e2f20f142e1b15f9e2741eef422"
def r_smspay_riskcontrol_data_configer(app_id,field,value):
    #print app_id
    #print field
    #print value
    collection = db.r_smspay_riskcontrol_data_configer
    s=collection.find_one({"app_id" : app_id})
    if s==None:
        return 'None'
    else: 
        if field=='province_closed':
            a={"province_code" :value,"day_account":0,"month_account":0}
            collection.update({"app_id":app_id},{'$set':{"province_config":[a]}},multi=True)   
        else:
            collection.update({"app_id":app_id},{'$set':{field:value}},multi=True)        
        return s
def r_smspay_riskcontrol_data_configer_csh(app_id):
    #print app_id
    #print field
    #print value
    collection = db.r_smspay_riskcontrol_data_configer
    s=collection.find_one({"app_id" : app_id})
    if s==None:
        return 'None'
    else:
        collection.update({"app_id":app_id},{'$set':{"user_day_account":-1}},multi=True)
        collection.update({"app_id":app_id},{'$set':{"user_month_account":-1}},multi=True)
        collection.update({"app_id":app_id},{'$set':{"type":2}},multi=True)
        a={"province_code" : "330000","day_account":-1,"month_account":-1}
        collection.update({"app_id":app_id},{'$set':{"province_config":[a]}},multi=True)
        
        return s
def app_details(app_id,field,value):
    #print app_id
    #print field
    #print value
    collection = db1.app_details
    s=collection.find_one({"app_id" : app_id})
    if s==None:
        return 'None'
    else: 
        collection.update({"app_id":app_id},{'$set':{field:value}},multi=True)   
        s=collection.find_one({"app_id" : app_id})     
        return s
#print r_smspay_riskcontrol_data_configer("cc627e2f20f142e1b15f9e2741eef422","day_account","123")
#print r_smspay_riskcontrol_data_configer_csh("cc627e2f20f142e1b15f9e2741eef422")
#print app_details('cc627e2f20f142e1b15f9e2741eef422','status','1')


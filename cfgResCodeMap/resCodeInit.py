#coding=utf-8
import xlrd
import xlwt
import MySQLdb
import traceback


class ThirdInfo:
    def __init__(self, thirdCode, thirdMsg, rspStatus, result, isChannelFee, isCustomerFee,channelId, respCode, respMsg):
        self.thirdCode = thirdCode
        self.thirdMsg = thirdMsg
        self.rspStatus = rspStatus
        self.result = result
        self.isChannelFee = isChannelFee
        self.isCustomerFee = isCustomerFee
        self.channelId = channelId
        self.respCode = respCode
        self.respMsg = respMsg
        self.RSP_TYPE = "E" if (rspStatus == "01" or rspStatus == "02" ) else "E"
        self.THIRD_TYPE = self.RSP_TYPE
            
        

def getThirdInfoFromExcel(excelFilePath):
    data = xlrd.open_workbook(excelFilePath,'utf-8')
    table = data.sheet_by_index(0)
    infoList =[]
    for i in range(table.nrows):
        if i==0:
            continue
        channelId = str(table.cell(i, 0).value)
        respCode = str(table.cell(i, 1).value)
        respMsg = table.cell(i, 2).value        
        thirdCode = str(table.cell(i, 3).value)
        thirdMsg = table.cell(i, 4).value
        rspStatus = str(table.cell(i, 5).value)
        result = str(table.cell(i, 6).value)
        isChannelFee = str(table.cell(i, 7).value)
        isCustomerFee = str(table.cell(i, 8).value)
        infoList.append( ThirdInfo(thirdCode, thirdMsg, rspStatus, result,isChannelFee, isCustomerFee, channelId, respCode, respMsg))
    return infoList;

def insertDB( thirdInfoList ):
    db = MySQLdb.connect("172.17.0.100","yzplatform","yzplatform","credlink_kf",charset="utf8")
    cursor = db.cursor()
    j = 1
    for record in thirdInfoList:        
        sql = """INSERT INTO `cfg_rescode_map` (`ID`,
	`RSP_COD`,`RSP_MSG`,`THIRD_RSPCOD`,`THIRD_RSPMSG`,`STATUS`,`RSP_TYPE`,
	`THIRD_TYPE`,`RSP_STATUS`,`RESULT`,`CHANNEL_ID`,`CREATED_BY`,`CREATED_DATE`,
	`UPDATE_BY`,`UPDATE_DATE`,`IS_CUST_FEE`,`IS_CHANNEL_FEE`) VALUES
	('%s','%s','%s','%s','%s','1','%s','%s','%s',
		'%s','%s','adminauth',now(),'adminauth',now(),'%s','%s')
        """ %(str(idPrefix+j), record.respCode, record.respMsg,record.thirdCode, record.thirdMsg,record.RSP_TYPE,record.THIRD_TYPE,record.rspStatus,record.result,record.channelId,record.isCustomerFee, record.isChannelFee)
        j+=1
        try:
            cursor.execute(sql)
            db.commit() 
            print '数据插入成功'
        except:
             traceback.print_exc()
             db.rollback()
    db.close()
    print '配置插入完毕'


excelFilePath = 'thirdMsgInfo.xlsx' #配置的excel路径
idPrefix = 201710190001       #id前缀

thirdInfoList = getThirdInfoFromExcel( excelFilePath )
insertDB(thirdInfoList)
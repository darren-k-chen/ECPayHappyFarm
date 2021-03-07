# -*- coding: utf-8 -*-
# Author: Darren K.J. Chen, Ming Chuan University

# === Normal API Start Line ==============================================================================

from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods = ['GET'])
def index():
	return "<center><h1>API is WORK</h1></center>"

# === Normal API End Line ==============================================================================
# === ECPay API Start Line ==============================================================================
# === Create Shipping Order Start Line ==============================================================================

import importlib.util
from datetime import datetime

shipping_cvs_params = {
    'ReceiverStoreID': '991182',
    'ReturnStoreID': '991182',
}

spec = importlib.util.spec_from_file_location (
	"ecpay_logistic_sdk",
	"/home/happyfarm/HappyFarmBackend/ecpay_logistic_sdk.py"
); module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

ecpay_logistic_sdk = module.ECPayLogisticSdk(
    MerchantID='2000933',
    HashKey='XBERn1YOvpM9nfZc',
    HashIV='h1ONHk4P4yqbl5LK'
)

@app.route('/createShippingOrder', methods = ['POST'])
def createShippingOrder():
	request_data = request.get_json()
	global create_shipping_order_params;
	create_shipping_order_params = {
	    'MerchantTradeNo': datetime.now().strftime("NO%Y%m%d%H%M%S"),
	    'MerchantTradeDate': datetime.now().strftime("%Y/%m/%d %H:%M:%S"),
	    'LogisticsType': module.LogisticsType['CVS'],
	    'LogisticsSubType': module.LogisticsSubType['UNIMART_C2C'],
	    'GoodsAmount': request_data['GoodsAmount'], #
	    'CollectionAmount': request_data['CollectionAmount'], #
	    'IsCollection': module.IsCollection['YES'],
	    'GoodsName': request_data['GoodsName'], #
	    'SenderName': "ECPayTeam",
	    'SenderPhone': "0988888888",
	    'SenderCellPhone': "0988888888",
	    'ReceiverName': request_data['ReceiverName'], #
	    'ReceiverPhone': '0288888888',
	    'ReceiverCellPhone': '0988888888',
	    'ReceiverEmail': 'admin@test.com',
	    'TradeDesc': '測試交易敘述',
	    'ServerReplyURL': 'https://www.ecpay.com.tw/server_reply_url',
	    'ClientReplyURL': '',
	    'Remark': '測試備註',
	    'PlatformID': '',
	    'LogisticsC2CReplyURL': 'https://www.ecpay.com.tw/logistics_c2c_reply',
	}; create_shipping_order_params.update(shipping_cvs_params)
	try:
		action_url = 'https://logistics-stage.ecpay.com.tw/Express/Create'
		reply_result = ecpay_logistic_sdk.create_shipping_order (
		        action_url=action_url,
		        client_parameters=create_shipping_order_params
		); return reply_result
	except Exception as error:
		return 'An exception happened: ' + str(error)

# === Create Shipping Order End Line ==============================================================================
# === Query Logistics Info Start Line ==============================================================================

import time
logisticsStatus = '-1'

@app.route('/queryLogisticsInfo', methods = ['POST'])
def queryLogisticsInfo():
	request_data = request.get_json()
	query_logistics_info_params = {
	    'AllPayLogisticsID': request_data['AllPayLogisticsID'],
	    'TimeStamp': int(time.time()),
	    'PlatformID': '',
	}; global logisticsStatus
	try:
		action_url = 'https://logistics-stage.ecpay.com.tw/Helper/QueryLogisticsTradeInfo/V2'
		reply_result = ecpay_logistic_sdk.query_logistics_info (
	        action_url=action_url,
	        client_parameters=query_logistics_info_params
		); logisticsStatus = reply_result['LogisticsStatus']
		return reply_result
	except Exception as error:
		print('An exception happened: ' + str(error))

@app.route('/getLogisticsStatus', methods = ['GET'])
def getLogisticsStatus():
	return logisticsStatus

@app.route('/INIT', methods = ['GET'])
def INIT():
	global logisticsStatus
	logisticsStatus = "-1"
	return logisticsStatus

@app.route('/setLogisticsStatus/<logistics_status>', methods = ['GET'])
def setLogisticsStatus(logistics_status):
	global logisticsStatus
	logisticsStatus = logistics_status
	return '<center><h1> Set Logistics Status to ' + logisticsStatus + '</h1></center>'

# === Query Logistics Info End Line ==============================================================================
# === ECPay API End Line ==============================================================================

if __name__ == '__main__':
	app.run() # App Start

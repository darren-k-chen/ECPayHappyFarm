# -*- coding: utf-8 -*-
# Author: Darren K.J. Chen, Ming Chuan University

# === Normal API Start Line ==============================================================================

from flask import Flask, request, redirect
app = Flask(__name__)

@app.route('/', methods = ['GET'])
def index():
	return "<center><h1>API is WORK</h1></center>"

@app.route('/doc')
def team_api_ref():
	sendMsg('Someone request the ECPay Team API Document')
	return redirect("https://ecpaycompetitionapi.docs.apiary.io/")

import requests as req
def sendMsg(msg):
	msg += '\n================\nMsg sent from Server:api.happyfarm.darren-cv.site'; print(msg)
	req.get("https://api.telegram.org/bot1086883866:AAGPSS0MsuK52TGkjGQBYzQ8pnFeSiA2ynQ/sendmessage?chat_id=992353127&parse_mode=HTML&text=" + msg)

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
		sendMsg('Someone query the ECPay Team Logistics Info\t Logistics Info:\n' + reply_result)
		return reply_result
	except Exception as error:
		sendMsg('Someone query the ECPay Team Logistics Info. An exception happened: ' + str(error))
		print('An exception happened: ' + str(error))

@app.route('/getLogisticsStatus', methods = ['GET'])
def getLogisticsStatus():
	sendMsg('Someone request the ECPay Team Logistics Info\t logisticsStatus: ' + logisticsStatus)
	return logisticsStatus

@app.route('/INIT', methods = ['GET'])
def INIT():
	global logisticsStatus; logisticsStatus = "-1"
	sendMsg('Someone init. the ECPay Team HappyFarm Game Backend System\t logisticsStatus: ' + logisticsStatus)
	return logisticsStatus

@app.route('/setLogisticsStatus/<logistics_status>', methods = ['GET'])
def setLogisticsStatus(logistics_status):
	global logisticsStatus; logisticsStatus = logistics_status
	sendMsg('Someone set the ECPay Team Logistics Stutus\t logisticsStatus: ' + logisticsStatus)
	return '<center><h1> Set Logistics Status to ' + logisticsStatus + '</h1></center>'

@app.route('/createGoldFlowOrder/<productName>/<productAmount>', methods = ['GET'])
def createGoldFlowOrder(productName, productAmount):
	spec = importlib.util.spec_from_file_location (
    "ecpay_payment_sdk",
    "/home/happyfarm/HappyFarmBackend/ecpay_payment_sdk.py"
	); module = importlib.util.module_from_spec(spec)
	spec.loader.exec_module(module); order_params = {
    'MerchantTradeNo': datetime.now().strftime("NO%Y%m%d%H%M%S"),
    'StoreID': '',
    'MerchantTradeDate': datetime.now().strftime("%Y/%m/%d %H:%M:%S"),
    'PaymentType': 'aio',
    'TotalAmount': int(productAmount),
    'TradeDesc': '訂單測試',
    'ItemName': productName,
    'ReturnURL': 'https://www.ecpay.com.tw/return_url.php',
    'ChoosePayment': 'Credit',
    'ClientBackURL': 'https://www.ecpay.com.tw/client_back_url.php',
    'ItemURL': 'https://www.ecpay.com.tw/item_url.php',
    'Remark': '交易備註',
    'ChooseSubPayment': '',
    'OrderResultURL': 'https://www.ecpay.com.tw/order_result_url.php',
    'NeedExtraPaidInfo': 'Y',
    'DeviceSource': '',
    'IgnorePayment': '',
    'PlatformID': '',
    'InvoiceMark': 'N',
    'CustomField1': '',
    'CustomField2': '',
    'CustomField3': '',
    'CustomField4': '',
    'EncryptType': 1,
	}; extend_params_1 = {
    'BindingCard': 0,
    'MerchantMemberID': '',
	}; extend_params_2 = {
    'Redeem': 'N',
    'UnionPay': 0,
	}; inv_params = {
    # 'RelateNumber': 'Tea0001', # 特店自訂編號
    # 'CustomerID': 'TEA_0000001', # 客戶編號
    # 'CustomerIdentifier': '53348111', # 統一編號
    # 'CustomerName': '客戶名稱',
    # 'CustomerAddr': '客戶地址',
    # 'CustomerPhone': '0912345678', # 客戶手機號碼
    # 'CustomerEmail': 'abc@ecpay.com.tw',
    # 'ClearanceMark': '2', # 通關方式
    # 'TaxType': '1', # 課稅類別
    # 'CarruerType': '', # 載具類別
    # 'CarruerNum': '', # 載具編號
    # 'Donation': '1', # 捐贈註記
    # 'LoveCode': '168001', # 捐贈碼
    # 'Print': '1',
    # 'InvoiceItemName': '測試商品1|測試商品2',
    # 'InvoiceItemCount': '2|3',
    # 'InvoiceItemWord': '個|包',
    # 'InvoiceItemPrice': '35|10',
    # 'InvoiceItemTaxType': '1|1',
    # 'InvoiceRemark': '測試商品1的說明|測試商品2的說明',
    # 'DelayDay': '0', # 延遲天數
    # 'InvType': '07', # 字軌類別
	}; ecpay_payment_sdk = module.ECPayPaymentSdk (
    MerchantID='2000132',
    HashKey='5294y06JbISpM5x9',
    HashIV='v77hoKGq4kWxNNIS'
	); order_params.update(extend_params_1);
	order_params.update(extend_params_2)
	order_params.update(inv_params)
	try:
		final_order_params = ecpay_payment_sdk.create_order(order_params)
		action_url = 'https://payment-stage.ecpay.com.tw/Cashier/AioCheckOut/V5'
		html = ecpay_payment_sdk.gen_html_post_form(action_url, final_order_params)
		sendMsg("Someone Created a Gold Folw Order"); return html
	except:
		sendMsg('An exception happened: ' + str(error))
		return 'An exception happened: ' + str(error)

# === Query Logistics Info End Line ==============================================================================
# === ECPay API End Line ==============================================================================

if __name__ == '__main__':
	app.run() # App Start

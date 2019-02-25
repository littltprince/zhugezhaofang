#encoding:utf-8
import requests
from utils.excelData import *
from utils.operationExcel import operationExcel
from utils.operationJson import operationJson
class Method:
    '''类的实例化'''
    def __init__(self):
        self.opearJson=operationJson()
        self.excel=operationExcel()

    def post(self,row):
        try:
            r=requests.post(url=self.excel.get_URL(row=row),
                            data=self.excel.get_requestdata(row=row),
                            headers=getHeadersValue(),
                            timeout=8)
            return r
        except Exception as e:
            raise RuntimeError('接口请求发生异常的错误')

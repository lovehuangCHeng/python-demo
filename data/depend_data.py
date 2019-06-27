#coding:utf-8
from testwuye.opnExcel import opereExcel
from testwuye.basic import runmethod
from testwuye.data import get_data
from jsonpath_rw import jsonpath,parse
class DependData:
     def __init__(self,case_id):
          self.case_id=case_id
          self.excl=opereExcel.OpenExcel()
          self.data=get_data.getData()
     def get_case_line_data(self):
          '''
          通过case_id去获取该case_id的整行数据
          :return:
          '''
          rows_data=self.excl.get_rows_data(self.case_id)
          return rows_data
     def run_dependent(self):
          '''
          执行依赖测试，获取结果
          :return:
          '''
          run_method=runmethod.RunMethod()
          row=self.excl.get_row_num(self.case_id)
          request_data=self.data.get_josn_request_data(row)
          header=self.data.is_header(row)
          method=self.data.get_request_method(row)
          url=self.data.get_url(row)
          res=run_method.run_main(method,url,request_data,header)
          return res
     #根据依赖的key去获取执行依赖测试case的响应，然后返回
     def get_data_for_key(self,row):
          depend_data=self.data.get_depend_key(row)
          respone_data=self.run_dependent()
          josn_exe=parse(depend_data)
          madle=josn_exe.find(respone_data)
          return [math.value for math in madle][0]


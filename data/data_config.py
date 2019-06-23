#coding:utf-8
class global_var:
     Id=0
     rul=1
     run=2
     request_way=3
     header=4
     case_depend=5
     data_depend=6
     field_depend=7
     data=8
     expect=9
     result=10
#获取caseID
def get_id():
     return  global_var.Id
#获取url
def get_url():
     return  global_var.rul
#获取接口是否运行
def get_run():
     return  global_var.run
#获取接口请求的方式
def get_request_way():
     return  global_var.request_way
#获取接口请求的header
def get_header():
     return  global_var.header
#获取用例是否有依赖
def get_case_depend():
     return  global_var.case_depend
#获取用例数据依赖
def get_data_depend():
     return  global_var.data_depend
#获取用例依赖字段
def get_field_depend():
     return  global_var.field_depend
#获取接口执行的数据
def get_data():
     return  global_var.data
#获取接口执行的期望结果
def get_expect():
     return  global_var.expect
#获取接口执行的结果
def get_result():
     return  global_var.result

#获取header的值
def get_header_value():
     header={

     }
     return  header

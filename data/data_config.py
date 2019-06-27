#coding:utf-8
class global_var:
     Id=0 # excel 模板中第一列编号：用例编号
     rul=1 # excel 模板中第二列编号 ：接口地址
     run=2 # excel 模板中第3列编号 ：测试接口是否执行
     request_way=3 # excel 模板中第4列编号：请求方式
     header=4 # excel 模板中第5列编号 ：是否含有header
     case_depend=5 # excel 模板中第6列编号：依赖caseid
     data_depend=6 # excel 模板中第7列编号 ：依赖的返回数据
     field_depend=7 # excel 模板中第8列编号 ：数据依赖字段
     data=8 # excel 模板中第9列编号 ：请求数据
     expect=9 # excel 模板中第10列编号：期望结果
     result=10 # excel 模板中第11列编号 ：实际结果
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

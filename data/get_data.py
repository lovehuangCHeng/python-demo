#coding:utf-8
from testwuye.data import  data_config
from testwuye.opnExcel import  opereExcel,open_json
class getData:
     def __init__(self):
          self.excel=opereExcel.OpenExcel()
     #获取Excel的行数，执行case的个数
     def get_cases_lines(self):
          return self.excel.get_lines()
     #测试用例是否运行
     def is_run(self,row):
          flag=None
          col=data_config.get_run()
          run_model=self.excel.get_cell_value(row,col)
          if run_model=='yes':
               flag=True
          else:
               flag=False
          return  flag
     #是否携带header
     def is_header(self,row):
          col=data_config.get_header()
          header=self.excel.get_cell_value(row,col)
          if header=='yes':
               header=data_config.get_header_value()
          else:
               header=None
          return  header
     #获取请求方式
     def get_request_method(self,row):
          col=data_config.get_request_way()
          request_method=self.excel.get_cell_value(row,col)
          return request_method
     #获取URL
     def get_url(self,row):
          col=data_config.get_url()
          url=self.excel.get_cell_value(row,col)
          return url
     #获取请求数据
     def get_request_data(self,row):
          col=data_config.get_data()
          data=self.excel.get_cell_value(row,col)
          if data=='':
               return None
          return  data
     #通过获取关键字获取json数据
     def get_josn_request_data(self,row):
          js= open_json.OpereJosn()
          requestdata=js.get_data(self.get_request_data(row))
          if requestdata=='':
               return  None
          return requestdata
     #获取预期结果
     def get_expext_data(self,row):
          col=data_config.get_expect()
          expect=self.excel.get_cell_value(row,col)
          if expect=='':
               return None
          return  expect
     #通过sql获取预期结果
     def get_expcet_data_for_sql(self,row):
          # op_sql=
          pass
     def write_result(self,row,value):
          '''
          写入Excel结果
          :param row:
          :param value:
          :return:
          '''
          col=data_config.get_result()
          self.excel.write_value(row,col,value)
     # 获取依赖数据的key
     def get_depend_key(self,row):
          col=data_config.get_case_depend()
          depend_key=self.excel.get_cell_value(row,col)
          if depend_key=='':
               return None
          else:
               return depend_key
     #判断是否有case依赖
     def is_depend(self,row):
          col=data_config.get_case_depend()
          depend_case_id=self.excel.get_cell_value(row,col)
          if depend_case_id=='':
               return None
          else:
               return  depend_case_id
     #获取数据依赖字段
     def get_depend_field(self,row):
          col=data_config.get_field_depend()
          data=self.excel.get_cell_value(row,col)
          if data=="":
               return  None
          else:
               return data

if __name__=='__main__':
     da=getData()
     # da.get_cases_lines()
     # da.get_request_method(1)
     # da.get_url(1)
     # da.get_request_data(1)
     # da.get_josn_request_data(2)
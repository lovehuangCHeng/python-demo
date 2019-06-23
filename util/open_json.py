#coding:utf-8
import  json
class OpereJosn:
     def __init__(self,file=None):
          if file:
               self.file=file
               self.data=self.readJosn()
          else:
               self.file = "../data_config/testdata.json"
               self.data = self.readJosn()
     #读取json文件
     def readJosn(self):
         with open(self.file) as fp:
              data=json.load(fp)
              return data
     #根据关键字获取数据
     def get_data(self,key):
          if key==None:
               return None
          return self.data[key]

     #写入json文件
     def writeJson(self):
          pass
if __name__=="__main__":
     jo=OpereJosn()
     print(jo.get_data("login"))

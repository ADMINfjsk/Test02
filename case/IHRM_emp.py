#导包
import unittest
import requests

#创建测试类
from api.Emp_Api import EmpCRUD


class TestEmp(unittest.TestCase):
    #初始化函数
    def setUp(self):
        self.session = requests.Session()
        self.emp_obj = EmpCRUD()
    #资源销毁函数
    def tearDown(self):
        self.session.close()

    #测试函数：增
    def test_1_addemp(self):
        response = self.emp_obj.add(self.session,"lily012345","13500000006","7993857")
        print("新增成功响应结果：",response.json())


    #测试函数：改
    def test_2_update(self):
        response = self.emp_obj.update(self.session, "1184396337458008064", "lily0AAA")
        print("修改结果：",response.json())

    def test_3_get(self):
        #测试函数：查
        response = self.emp_obj.get(self.session, "1184396337458008064")
        print("查询结果：", response.json())

    def test_4_delete(self):
        #测试函数：删
        response = self.emp_obj.delete(self.session, "1184396337458008064")
        print("删除结果：", response.json())

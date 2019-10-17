# 导包
import json
import unittest
import requests
from parameterized import parameterized
# 测试登录类
import app
from api.UserApi import UserLogin


def read_data():
    data = []
    with open(app.PRO_PATH + "/data/login_data.json", "r", encoding="utf-8")as f:
        for value in json.load(f).values():
            mobile = value.get("mobile")
            password = value.get("password")
            success = value.get("success")
            code = value.get("code")
            message = value.get("message")

            ele = (mobile, password, success, code, message)
            data.append(ele)
    return data


class TestUser(unittest.TestCase):
    def setUp(self):
        # 初始化方法
        self.session = requests.Session()
        self.user_obj = UserLogin()

    def tearDown(self):
        # 销毁资源方法
        self.session.close()

    @parameterized.expand(read_data())
    def test_1_login(self, mobile, password, success, code, message):
        # 测试方法
        print(mobile, password, success, code, message)
        print("-" * 100)

        resp = self.user_obj.login(self.session, mobile, password)
        result = resp.json()
        # 断言
        self.assertEqual(success, result.get("success"))
        self.assertEqual(code, result.get("code"))
        self.assertIn(message, result.get("message"))

    def test_2_login(self):
        print("-"*100)
        print("登录成功接口")
        response=self.user_obj.login(self.session,"13800000002","123456")
        result = response.json()
        self.assertTrue(True,result.get("success"))
        self.assertEqual(10000, result.get("code"))
        self.assertIn("操作成功", result.get("message"))

        app.TOKEN = result.get("data")
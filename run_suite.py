# 导包
import unittest

from case.IHRM_emp import TestEmp
from case.IHRM_user import TestUser
from tools.HTMLTestRunner import HTMLTestRunner

suite = unittest.TestSuite()
suite.addTest(TestUser("test_2_login"))
suite.addTest(TestEmp("test_1_addemp"))
suite.addTest(TestEmp("test_2_update"))
suite.addTest(TestEmp("test_3_get"))
suite.addTest(TestEmp("test_4_delete"))



with open("./report/report.html","wb") as f:
    runner = HTMLTestRunner(f,title="我的测试报告",description="版本 v1.0")
runner.run(suite)
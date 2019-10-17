# 导包
import unittest

from case.IHRM_emp import TestEmp
from case.IHRM_user import TestUser

suite = unittest.TestSuite()
suite.addTest(TestUser("test_2_login"))
suite.addTest(TestEmp("test_1_addemp"))
suite.addTest(TestEmp("test_2_update"))
suite.addTest(TestEmp("test_3_get"))
suite.addTest(TestEmp("test_4_delete"))



runner = unittest.TextTestRunner()
runner.run(suite)
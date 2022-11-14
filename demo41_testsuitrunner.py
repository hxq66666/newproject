# 开发人:胡雪晴
# 开发时间: 2022/11/9 11:40
import unittest
from demo39_testcase01 import study0
from demo40_testcase02 import study1
from demo43_practice import Test_Add
from htmltestreport import HTMLTestReport
suite = unittest.TestSuite()
'''
suite.addTest(study0('test_method10'))
suite.addTest(study0('test_method20'))
suite.addTest(study1('test_method11'))
suite.addTest(study1('test_method22'))
'''
suite.addTest(unittest.makeSuite(study0))
suite.addTest(unittest.makeSuite(study1))
suite.addTest(unittest.makeSuite(Test_Add))
# runner=unittest.TextTestRunner()
runner=HTMLTestReport('testreport01.html','标题测试报告','描述信息')
runner.run(suite)
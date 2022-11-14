# 开发人:胡雪晴
# 开发时间: 2022/11/9 13:44
import unittest
suite=unittest.TestLoader().discover('./','*testcase*.py')
runner=unittest.TextTestRunner()
runner.run(suite)

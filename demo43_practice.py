# 开发人:胡雪晴
# 开发时间: 2022/11/9 13:57
import unittest

from tools.add import Add
class Test_Add(unittest.TestCase):
    def test_add1(self):
        self.assertEqual(2,Add(1,1))
    def test_add2(self):
        self.assertEqual(1,Add(0,1))
    def test_add3(self):
        self.assertEqual(0,Add(1,-1))





# class Test_Add(unittest.TestCase):
#     def test_add1(self):
#         if Add(1,1)==2:
#             print(f'用例通过')
#         else:
#             print('用例执行失败')
#     def test_add2(self):
#         if Add(0,1)==1:
#             print(f'用例通过')
#         else:
#             print('用例执行失败')
#     def test_add3(self):
#         if Add(0,0)==0:
#             print(f'用例通过')
#         else:
#             print('用例执行失败')
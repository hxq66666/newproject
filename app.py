# 开发人:胡雪晴
# 开发时间: 2022/11/10 15:30
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if __name__ == '__main__':
    print(BASE_DIR)
    print(os.path.abspath(__file__))
    print(os.path.dirname(__file__))
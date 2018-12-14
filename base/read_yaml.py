"""
    目标：读取yaml文件
    操作：
        1. 导包 yaml
        2. 打开文件
        3. 调用 load方法
"""
# 导包
import yaml
import os

class ReadYaml():
    def __init__(self,filename):
        """
        :param filename: 文件名称
        os.sep: 获取 /
        os.getcwd:获取当前文件所在目录
        """
        self.filename=os.getcwd()+os.sep+"data"+os.sep+filename

    def read_yaml(self):
        # 打开文件
        with open(self.filename, "r", encoding="utf-8") as f:
            # 调用load方法
            return yaml.load(f)

    # 以下方法 为右键调试使用
    def read_yaml_1(self):
        # 打开文件
        with open("../data/data_login.yaml", "r", encoding="utf-8") as f:
            # 调用load方法
            return yaml.load(f)

if __name__ == '__main__':

    """
        问题：获取的数据格式为字典
        需求格式：[("18611110000","123456"),("18600002222","123456")]
        
        问题:字典.values()方法，获取所有的值，值的格式还是字典？
        解决：
            1. 创建空列表 arrs = []
            2. arrs.append((data.get("username"),data.get("password")))
    """
    # 获取所有数据
    datas=ReadYaml("login_data.yaml").read_yaml_1()

    # 创建 空列表
    arrs = []

    # 获取所有的值 并 遍历
    for data in datas.values():
        arrs.append((data.get("username"),data.get("password")))
    # 查看 获取的列表结果
    print(arrs)


import yaml

#读取data.yaml 返回数据
def read_yaml():
    #通过pytest运行这么写路径
    with open("./v4/data/data.yaml") as f:
        return yaml.load(f)
    # 通过右键运行这么写路径
    # with open("../data/data.yaml") as f:
    #     return yaml.load(f)

#数据驱动必须返回列表嵌套元组形式的数据，下边为测试代码
if __name__ == '__main__':
    #接收读取data.yaml的数据
    result=read_yaml()
    data_list=list()
    # 遍历数据result的vlaues()值得到列表
    for data in result.values():
        data_list.append(tuple(data.values()))
    print(data_list)
with open('D:\code\py\lubosoft\lubo\BAY01_0001_20230706_155303_844.dat', 'rb') as file:
    data = file.read()

hex_data = data.hex()

# 将每26个字符分割为一个子字符串
chunks = [hex_data[i:i+52] for i in range(0, len(hex_data), 52)]

class COMTRADE:
    # def __init__(self, ):
    points = []
    times = []
    passage1 = []
    passage2 = []
    passage3 = []
    passage4 = []
    passage5 = []
    passage6 = []
    passage7 = []
    passage8 = []
    passage9 = []

# 通道数据处理                                  处理方式：补中值
for chunk in chunks:
    COMTRADE.points.append(chunk[0:8])          #点数不用计算，处理完成后直接顺序排到最终点数
    # print(chunk[0:8])
    COMTRADE.times.append(chunk[8:16])          #时间：t = (t1+t2)/2
    print(chunk[8:16])
    COMTRADE.passage1.append(chunk[16:20])      #幅值：x = (x1+x2)/2
    COMTRADE.passage2.append(chunk[20:24])
    COMTRADE.passage3.append(chunk[24:28])
    COMTRADE.passage4.append(chunk[28:32])
    COMTRADE.passage5.append(chunk[32:36])
    COMTRADE.passage6.append(chunk[36:40])
    COMTRADE.passage7.append(chunk[40:44])
    COMTRADE.passage8.append(chunk[44:48])
    COMTRADE.passage9.append(chunk[48:52])

    # print(passage)
    # print(chunk)
    # print()  # 添加空行
# print(COMTRADE.points)
	
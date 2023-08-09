with open('D:\code\py\lubosoft\lubo\BAY01_0001_20230706_155303_844.dat', 'rb') as file:
    data = file.read()

hex_data = data.hex()

# 将每26个字符分割为一个子字符串,即为一行
chunks = [hex_data[i:i+52] for i in range(0, len(hex_data), 52)]

# 提取第8、9字节到一个新数组
byte_array = []
for chunk in chunks:
    byte_array.append(chunk[18:20] + chunk[16:18])
passage = [int(x, 16) for x in byte_array]
print(type(passage[0]))
print(byte_array)
print(passage)

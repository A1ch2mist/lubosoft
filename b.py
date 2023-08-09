with open('D:\code\py\lubosoft\lubo\BAY01_0001_20230706_155303_844.dat', 'rb') as file:
    data = file.read()

hex_data = data.hex()

# 将每26个字符分割为一个子字符串,即为一行
chunks = [hex_data[i:i+52] for i in range(0, len(hex_data), 52)]
# print(chunks)

# 提取第8、9字节到一个新数组
byte_array = []
for chunk in chunks:
    # print(chunk)
    byte_array.append(chunk[18:20])
    byte_array.append(chunk[16:18])
    # print(chunk[16:20])
# print(type(byte_array[1]))    列表中数据为字符串

def insert_value(lst):
    for i in range(len(lst)-1, 0, -1):
        value = (int(lst[i-1], 16) + int(lst[i], 16)) / 2
        lst.insert(i, str(hex(int(value))))
    return lst

result = insert_value(byte_array)
print(result)

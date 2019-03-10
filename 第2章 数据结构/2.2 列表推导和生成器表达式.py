# 2.2.1 列表推导和可读性

# 实例2-1 把一个字符串变成Unicode码位的列表
symbols = '$#%%^&$^'
codes = []
for symbol in symbols:
    codes.append(ord(symbol))

# 实例2-2把字符串变成Unicode码位的另外一种写法

codes2 = [ord(symbol) for symbol in symbols]

print(codes)
print(codes2)
print("\n" "")

# 2.2.2 列表同filter和map的比较

# 2-3 用列表推导和map/filter组合来创建同样的表单

beyond_ascii = [ord(s) for s in symbols if (ord(s) > 40)]
beyond_ascii2 = list(filter(lambda c: c > 40, map(ord, symbols)))
print(beyond_ascii)
print(beyond_ascii2)
print('\n')

# 2.2.3 笛卡尔积

# 示例2-4 使用列表推导计算笛卡尔积

colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]
print(tshirts)
for color in colors:
    for size in sizes:
        print((color, size))
tshirts = [(color, size) for size in sizes for color in colors]  # 先size后color排序
print(tshirts)
print('\n')

# 2.2.4 生成器表达式

# 实例2-5 用生成器表达式初始化元祖和数组

symbols = '@#$%^&*'
print(tuple(ord(symbol) for symbol in symbols))
import array
print(array.array('I', (ord(symbol) for symbol in symbols)))  # array构造方法的第一个参数指定了数组中数字的存储方式
print('\n')

# 示例2-6使用生成器表达式计算笛卡尔积

colors = ['black', 'white']
sizes = ['S', 'M', 'L']
for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(tshirt)



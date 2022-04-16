#类型转换 从浮点数到字符串
num=1.23
print(str(num))# Correct 1.23
print(num)# Correct 1.23
#print(str(num)+num)# TypeError: can only concatenate str (not "float") to str
print(str(num)+str(num))# Correct 1.231.23
print(num+num)# Correct 1.23+1.23=2.46

#类型转换 从字符串到浮点数
num="1.23"
print(num+num)# Correct 1.231.23
print(float(num)+float(num))# Correct 1.23+1.23=2.46
#类型转换 从字符串到整数
num="1"
print(num+num)# Correct 11
print(int(num)+int(num))# Correct 1+1=2
print(int(num)+float(num))# Correct 1+1.0=2.0
#类型转换 从字符串到复数
num="1+2j"
print(complex(num))# Correct (1+2j)
print(complex(num)+float("1.0"))# Correct (1+2j)+1.0=(2+2j)
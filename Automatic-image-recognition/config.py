from openpyxl.styles import PatternFill

date = "2022-04-13"
version = "1.0.3"
file_dir = "./"
name_column = 3
dates = [str, str, str, str, str, str, str]

# 匹配失败颜色
Color = ['ffc7ce', '9c0006']
# 设置填充颜色
fills = PatternFill('solid', fgColor=Color[0])

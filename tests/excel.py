import pandas as pd
from xpinyin import Pinyin

# 初始化拼音工具
pinyin = Pinyin()

# 假设你的表格文件
file_path = '/Users/lixin/Desktop/source.xlsx'
sheet_name = 'sheet1'

# 读取表格
try:
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    print("表格读取成功")
except Exception as e:
    print(f"读取文件时出错: {e}")
    exit()

# 假设目标列名是 "名称"
target_column = "名称"

# 提取首字母，跳过以 "F" 开头的名称
def get_initials(text):
    if isinstance(text, str) and text.strip():  # 判断是否是字符串且非空
        # 获取第一个字的拼音首字母
        first_initial = pinyin.get_initial(text[0])

        # 如果首字母是 "f"，跳过
        if first_initial.lower() == 'f':
            # 从第二个字开始提取
            if len(text) > 1:
                return pinyin.get_initial(text[1])
            else:
                return ''  # 如果只有一个字，并且是F开头，返回空字符串
        else:
            return first_initial
    return ''

# 新增一列存储首字母
df['首字母'] = df[target_column].apply(get_initials)

# 保存到新文件
output_path = '/Users/lixin/Desktop/1111output_with_initials.xlsx'
try:
    df.to_excel(output_path, index=False)
    print(f"首字母已提取并保存到 {output_path}")
except Exception as e:
    print(f"保存文件时出错: {e}")

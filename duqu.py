import os
def josn_correct(file_name):
    with open(file_name, 'r', encoding='GB2312') as f:
        data = f.read()[1:]
        lines = data.splitlines()[:-1]
#将lines写入new_file_name.josn,以{...}/n{...}的形式输出
    new_file_name = os.path.splitext(file_name)[0] + "_corrected.json"
    with open(new_file_name, 'w', encoding='GB2312') as f:
        for line in lines:
            f.write(line + '\n')
    return new_file_name
    
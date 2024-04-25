import sys
import os
from x import xml_file_to_geojson
from duqu import josn_correct
from jjssoonn import json_to_geojson

def main():
    if len(sys.argv) < 2:
        print('Usage: %s directory' % sys.argv[0])
        sys.exit(1)

    directory = sys.argv[1]
    script_dir = os.path.dirname(os.path.realpath(__file__))  # 获取当前脚本所在的目录

    result_dir = os.path.join(script_dir, "result")
    if not os.path.exists(result_dir):  # 检查文件夹是否已经存在
        os.makedirs(result_dir)  # 如果不存在，创建文件夹

    for filename in os.listdir(directory):
        full_path = os.path.join(directory, filename)
        if filename.endswith('.xml'):
            xml_file_to_geojson(full_path, result_dir)
        elif filename.endswith('.json'):
            new_file_name = josn_correct(full_path)
            json_to_geojson(new_file_name, result_dir)
        else:
            print('Unsupported file format: %s' % filename)

main()
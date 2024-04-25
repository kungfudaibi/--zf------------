#提取.xml中的地图信息
'''
<?xml version="1.0" encoding="UTF-8"?><root><resultList><SOURCE>地形图</SOURCE><OBJECTID>28</OBJECTID><XZQDM>340101</XZQDM><XZQMC> </XZQMC><ZLDZ> </ZLDZ><HYDM> </HYDM><CJWMC> </CJWMC><DMDZB> </DMDZB><DWMC>天然气加气站</DWMC><MPH> </MPH><FL>加油站</FL><MCCD>6</MCCD><ENTITY>1</ENTITY><NUMPTS>1</NUMPTS><MINX>117.276611328125</MINX><MINY>31.918212890625</MINY><MAXX>117.276611328125</MAXX><MAXY>31.918212890625</MAXY><MINZ>0</MINZ><MAXZ>0</MAXZ><MINM>0</MINM><MAXM>0</MAXM><AREA>0</AREA><LEN>0</LEN><SRID>300002</SRID><ID>0</ID></resultList><resultList><SOURCE>地形图</SOURCE><OBJECTID>29</OBJECTID><XZQDM>340101</XZQDM><XZQMC> </XZQMC><ZLDZ> </ZLDZ><HYDM> </HYDM><CJWMC> </CJWMC><DMDZB> </DMDZB><DWMC>公交双谊加油站</DWMC><MPH> </MPH><FL>加油站</FL><MCCD>7</MCCD><ENTITY>1</ENTITY><NUMPTS>1</NUMPTS><MINX>117.248596191406</MINX><MINY>31.9415893554688</MINY><MAXX>117.248596191406</MAXX><MAXY>31.9415893554688</MAXY><MINZ>0</MINZ><MAXZ>0</MAXZ><MINM>0</MINM><MAXM>0</MAXM><AREA>0</AREA><LEN>0</LEN><SRID>300002</SRID><ID>0</ID></resultList><resultList><SOURCE>地形图</SOURCE><OBJECTID>30</OBJECTID><XZQDM>0</XZQDM><XZQMC> </XZQMC><ZLDZ> </ZLDZ><HYDM>
提取名称，经度，维度
'''
import xml.etree.ElementTree as ET
import json
import os
def xml_file_to_geojson(file_name,output_dir):
    # 解析XML文件
    tree = ET.parse(file_name)
    root = tree.getroot()
    tag_mapping = {'FL': '类型', 'DWMC': '名称'}
    # 为每个结果创建GeoJSON特征
    features = []
    for resultList in root.findall('resultList'):
        minx = float(resultList.find('MINX').text)
        miny = float(resultList.find('MINY').text)

        properties = {tag_mapping.get(child.tag): child.text 
                for child in resultList 
                if child.tag in tag_mapping.keys()}

        feature = {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [minx, miny]  # X, Y 坐标
            },
            'properties': properties
        }

        features.append(feature)
        
    # 创建GeoJSON对象
    geojson = {
        'type': 'FeatureCollection',
        'features': features
    }
    base_file_name = os.path.splitext(os.path.basename(file_name))[0]
    geojson_file_name = base_file_name + ".geojson"  #
    output_path = os.path.join(output_dir, geojson_file_name)
    # 输出到GeoJSON文件
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(geojson, f, ensure_ascii=False, indent=2)

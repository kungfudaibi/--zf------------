import json
import os

def json_to_geojson(file_name, output_dir):
    geojson = {
        "type": "FeatureCollection",
        "features": []
    }

    with open(file_name, 'r', encoding='GB2312') as f:
        for line in f:
            rec = json.loads(line)
            geojson['features'].append({
                "type": "Feature",
                "properties": { '类型': rec['FL'], '名称': rec['DWMC'] },  
                "geometry": {
                    "type": "Point",
                    "coordinates": [rec['MAXX'], rec['MAXY']]
                }
            })

    base_file_name = os.path.splitext(os.path.basename(file_name))[0]
    geojson_file_name = base_file_name + ".geojson"
    output_path = os.path.join(output_dir, geojson_file_name)  #
    with open(output_path, 'w') as f:
        json.dump(geojson, f)

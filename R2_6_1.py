import zipfile
import json

with zipfile.ZipFile("kabeposter.zip", 'r') as zip_file:
    for file_name in zip_file.namelist():
        if int(file_name.split('_')[1]) == 0:
            with zip_file.open(file_name, 'r') as file:
                data = json.load(file)
                people_num = len(data["people"])
                if isinstance(data, dict):
                    for i in range(people_num):
                        content = data["people"][i]["pose_keypoints_2d"]
                        print(f"{i+1}人目")
                        print(f"鼻 x: {content[0]} y:{content[1]} r:{content[2]}")
                        print(f"首 x: {content[3]} y:{content[4]} r:{content[5]}")

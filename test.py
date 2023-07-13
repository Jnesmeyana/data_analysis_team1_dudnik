import os
import json

folder_path = '/Users/dudberoll/PycharmProjects/TetsGarpix/ALGORITM'  # Replace with the actual path to your folder

data_dict = {'size': float, 'loading_sizes': float}  # Dictionary to store the extracted data

mas = []
# Iterate through all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.json'):  # Process only JSON files
        file_path = os.path.join(folder_path, filename)

        with open(file_path) as file:
            json_data = json.load(file)

        # data_dict1['id'].append(json_data['data_result']['calculation_id'])
        boxes = json_data['data_result']['boxes']
        volume = 0

        # суммарный обьем коробок
        for i in range(len(json_data['data_result']['boxes'])):
            volume += boxes[i]['size']['length'] * boxes[i]['size']['width'] * boxes[i]['size']['height']

        loadings_size = json_data['data_result']['cargo_space']['loading_size']
        # Обьем грузовика
        loading_size = loadings_size['width'] * loadings_size['height'] * loadings_size['length']

        data_dict['size'] = volume / loading_size * 100
        data_dict['loading_sizes'] = json_data['data_result']['cargo_space']['calculation_info']['filling_space_percent']
        mas.append(data_dict.copy())

print(mas)

# print(data_dict.keys())
# print(len(data_dict['size']))

# Save json file
with open('garpixx.json', 'w') as file:
    json.dump(mas, file)


# import csv
#
# cols = ['size', 'loading_sizes']
#
# f = open('mycsvfile.csv','wb')
# w = csv.DictWriter(f,mas.keys())
# w.writerows(mas)
# f.close()

# with open('mycsvfile.csv','w') as f:
#     w = csv.writer(f)
#     w.writerows(data_dict.items())


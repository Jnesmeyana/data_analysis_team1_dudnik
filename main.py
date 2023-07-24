import os
import json

file_path ='/Users/dudberoll/PycharmProjects/TetsGarpix/input_example.json'

data_dict = {'loading_sizes':float, 'density_percents':float, 'group': float, 'mass': float}  # Dictionary to store the extracted data

with open(file_path) as file:
    json_data = json.load(file)
csv_mas = []
size = 0
group_data = json_data['input_data']['groups']
train_mass = 0
try:
    if (json_data['input_data']['cargo_spaces'][0] == 97):
        cargo_size = 800*200*1200
        for i in range(len(json_data['input_data']['groups'])):
            group_data = json_data['input_data']['groups']
            size += group_data[i]['cargoes'][0]['width']*group_data[i]['cargoes'][0]['height']\
                   *group_data[i]['cargoes'][0]['length'] * group_data[i]['cargoes'][0]['count']
            train_mass += group_data[i]['cargoes'][0]['mass']
        data_dict['loading_sizes']  = round(size/cargo_size, 3)
        data_dict['mass'] = train_mass
        csv_mas.append(data_dict.copy())

except ValueError:
    print('Не знаем размеров данных ID')
print(csv_mas)
import csv
with open('input.csv', 'w', encoding='utf8', newline='') as output_file:
    fc = csv.DictWriter(output_file,
                        fieldnames=csv_mas[0].keys(),

                       )
    fc.writeheader()
    fc.writerows(csv_mas)

# for i in range()

# boxes = json_data['data_result']['boxes']
# volume = 0
# for i in range(len(json_data['data_result']['boxes'])):
#     volume += boxes[i]['size']['length'] * boxes[i]['size']['width'] * boxes[i]['size']['height']
#
# data_dict['size'].append(volume)
#
# loadings_size = json_data['data_result']['cargo_space']['loading_size']
# loading_size = loadings_size['width'] * loadings_size['height'] * loadings_size['length']



# print()
# # обернуть в try, exept
# #
# unpacked_dict = {'unpacked_id': int, 'unpacked_size':float}
# mas_of_id = []
# for i in range(len(json_data['data_result']['unpacked_errors'])):
#     for j in range(len(json_data['data_result']['unpacked_errors'][i]['boxes'])):
#         unpacked_dict['unpacked_id'] = json_data['data_result']['unpacked_errors'][i]['boxes'][j]['id']
#         for k in range(len(json_data['data_result']['cargo_groups'])):
#             id = json_data['data_result']['unpacked_errors'][i]['boxes'][j]['id']
#             cargo_id = json_data['data_result']['cargo_groups'][k]['cargo_id']
#
#
#             if  id == cargo_id:
#                 # посчитать тут обьем
#                 cargo_sizes = json_data['data_result']['cargo_groups'][k]['size']
#                 unpacked_dict['unpacked_size'] = cargo_sizes['length'] * \
#                                                  cargo_sizes['width'] * cargo_sizes['height']/100000000
#                 mas_of_id.append(unpacked_dict.copy())
#             else:
#                 unpacked_dict['unpacked_size'] = 0;


#
#
#
#
# print(type(json_data['data_result']['cargo_groups'][k]['size']))
#
#
# print(mas_of_id)





#
# print(len(json_data['data_result']['boxes']),  'кол-во коробок')
# print(data_dict['size'][0], 'суммарный обьем')
# print(loading_size, 'обьем грузовика')
# print(data_dict['size'][0]/loading_size, 'теор. процент')
# print(json_data['data_result']['cargo_space']['calculation_info']['filling_space_percent'], 'реальный процент' )









# with open('my.json', 'w') as file:
#     json.dump(data_dict, file)
# print(json_data['data_result']['boxes'][1]['length'])
# for i in range(len(json_data['data_result']['boxes'])):
#     data_dict['size'].append(json_data['data_result']['boxes'][i]['width']
#                              * json_data['data_result']['boxes'][i]['width'])
# print(data_dict)
# data_dict['size'] = []
# file_boxes = json_data['data_result']['boxes']
# print(data_dict['size'].width * data_dict['size'].height * data_dict['size'].length)
# for box in file_boxes:
#     data_dict = {}
#     file_id = box['id']
#     if file_id not in data_dict:
#         data_dict['size'] = box['size'].width * box['size'].height * box['size'].length
#         data_dict['size'] = []
#         data_dict['id'] = [file_id]
#         # data_dict['size'].append(box['size'])
#         data_dict['filling_space_percent'] = json_data['data_result']['cargo_space']['calculation_info'][
#                 'filling_space_percent']
#         mas.append(data_dict.copy())

#
# print(mas)

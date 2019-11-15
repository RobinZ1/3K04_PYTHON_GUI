import json


data_dict = {'fuck':1,'banzai':20}

with open('personal.txt', 'w') as json_file:
    json.dump(data_dict, json_file)

with open('personal.txt','r') as json_file:
    data1_dict = json.load(json_file)

data1_dict['fuck'] = 4

with open('personal.txt','w') as json_file:
    data1_str =  json.dump(data1_dict, json_file)



''''''
'''
def ini_file():
    data_dict = {'AOO_LRL':AOO_LRL1, 'AOO_URL': AOO_URL1, 'AOO_AA': AOO_AA1,'AOO_APW':AOO_APW1}
    with open('test_data.txt','w') as json_file:
        json.dump(data_dict, json_file) #the data_dict is now converted to JSON string 

def update_dict(Banzai):
    string = str(Banzai)-'1'
    with open('test_data.txt', 'r') as json_file:
        data_dict = json.load(json_file)
        print(data_dict)
        data_dict[string] = Banzai
        print(data_dict)
    with open('test_data.txt', 'w') as json_file:
        json.dump(data_dict, json_file)
        json_file.close()

'''







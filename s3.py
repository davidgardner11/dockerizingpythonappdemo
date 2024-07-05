# Based on sample JSON file from https://jsoneditoronline.org/indepth/datasets/json-file-example/

import boto3, json

city_normalizations = {
    'manhattan': 'New York'
}

# Reads the JSON file from an S3 account. 
# NOTE: Assumes the S3 object is public.
def get_json_file(): 
    # client = boto3.client('s3')
    # response = client.get_object(
    #     Bucket='jaypublic',
    #     Key='data.json',
    # )
    # read JSON file from local directory
    
    # Opening JSON file. 
    f = open('data.json')

    # returns JSON object as 
    # a dictionary
    data = json.load(f)

    # Closing file
    f.close()
    
    # return json.loads(response['Body'].read())
    return data

# Transforms a list of people who lives in cities into a count of people per city. 
def transform_json_file(json_obj):
    dict = {}

    for obj in json_obj:
        key = obj['city'] 
        if key.lower() in city_normalizations:
            key = city_normalizations[key.lower()]
        if key in dict: 
            dict[key] = int(dict[key]) + 1
        else:
            dict[key] = 1

    return dict

def save_transformed_data(save_dict):
    for key in save_dict: 
        print("{}:{}".format(key, save_dict[key]))
        # Save to DB - step omitted for ease of tutorial

#    return

if __name__ == '__main__':
    json_ret = get_json_file()
    new_dict = transform_json_file(json_ret)
    save_transformed_data(new_dict)
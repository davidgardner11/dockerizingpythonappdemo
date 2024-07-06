# Based on sample JSON file from https://jsoneditoronline.org/indepth/datasets/json-file-example/
import requests, json
from prefect import task, Flow

city_normalizations = {
    'manhattan': 'New York'
}

# Reads the JSON file from a public URL 
@task
def get_json_file(url):
    try:
        # Download the file content from the URL
        response = requests.get(url)
        # print(response.text)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        # Parse the content as JSON
        json_data = json.loads(response.text)

        return json_data
    except requests.exceptions.RequestException as e:
        print(f"Error downloading the file: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
        return None

# Transforms a list of people who lives in cities into a count of people per city. 
@task
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

@task
def save_transformed_data(save_dict):
    for key in save_dict: 
        print("{}:{}".format(key, save_dict[key]))
        # Save to DB - step omitted for ease of tutorial

#    return
@Flow
def process_cities_data():
    json_ret = get_json_file("https://gist.githubusercontent.com/davidgardner11/3d1890a49c3bee2661ab29d6ad6bb7ce/raw/6410edc6993fa2169dfa217dd382e68cb7f9a46f/data.json")
    new_dict = transform_json_file(json_ret)
    save_transformed_data(new_dict)


if __name__ == '__main__':
    process_cities_data()
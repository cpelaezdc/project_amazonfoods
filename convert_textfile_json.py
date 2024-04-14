import json

directory = "D:\\BIGDATA\\420_D07_BB_DEVELOPPEMENT_DE_TRAITEMENTS_DISTRIBUES\\projet\project_amazonfoods"
input_file_aws = "foodsAWS.txt"
output_file_aws = "foodsAWS.json"

input_file_azure = "foodsAzure.txt"
output_file_azure = "foodsAzure.json"


# Function to convert text to JSON
def text_to_json(input_file, output_file):
    # Read the text file
    with open(input_file, 'r') as file:
        content = file.read()
        

    # Split the content by double newlines to separate entries
    entries = content.strip().split("\n\n")

    # List to hold all the JSON objects
    json_objects = []

    # Process each entry
    for entry in entries:
        # Convert the text to a dictionary
        data_dict = {}
        for line in entry.split('\n'):
            try:
                key, value = line.split(': ', 1)
                data_dict[key] = value
            except:
                print(f"not valid line:  {line}")
        # Add the dictionary to the list of JSON objects
        json_objects.append(data_dict)

    # Convert the list of dictionaries to JSON and save it to a file
    with open(output_file, 'w') as file:
        json.dump(json_objects, file, indent=4)


# take files and convert to json format
input = f"{directory}\\{input_file_aws}"
output = f"{directory}\\{output_file_aws}"
text_to_json(input, output)

input = f"{directory}\\{input_file_azure}"
output = f"{directory}\\{output_file_azure}"
text_to_json(input, output)

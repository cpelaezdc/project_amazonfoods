import json

input_file ="C:\\Users\\username\\Downloads\\finefoods\\foods.txt"
output_file = "C:\\Users\\username\\Downloads\\finefoods\\foodstest.json"

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


# Example usage
text_to_json(input_file, output_file)

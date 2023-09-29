import csv
import json
def read_csv_convert_save(csv_file_path: str, json_file_path: str):
    """
    Reads a CSV file, converts the values to decimal, adds 1 to each value, and saves the old and new values to a JSON file.
    Parameters:
    - csv_file_path: str
        The file path of the CSV file to be read.
    - json_file_path: str
        The file path of the JSON file to be saved.
    Error States:
    - FileNotFoundError:
        If the CSV file does not exist at the given file path.
    - ValueError:
        If the CSV file contains non-numeric values that cannot be converted to decimal.
    Returns:
    - None
        This function does not return any value, it simply reads the CSV file, performs the required operations, and saves the result to a JSON file.
    """
    # Dictionary to store the old and new values
    values_dict = {}
    try:
        # Open the CSV file for reading
        with open(csv_file_path, 'r') as csv_file:
            # Create a CSV reader object
            csv_reader = csv.reader(csv_file)
            # Iterate over each row in the CSV file
            for row in csv_reader:
                # Convert the value to decimal
                try:
                    old_value = float(row[0])
                except ValueError:
                    raise ValueError(f"Invalid value in CSV file: {row[0]}")
                # Add 1 to the value
                new_value = old_value + 100000
                # Store the old and new values in the dictionary
                values_dict[old_value] = new_value
    except FileNotFoundError:
        raise FileNotFoundError(f"CSV file not found: {csv_file_path}")
    try:
        with open(json_file_path, 'w') as json_file:
            json.dump(values_dict, json_file)
    except IOError:
        raise IOError(f"Error saving JSON file: {json_file_path}")
csv_file_path = 'data.csv'
json_file_path = 'output.json'
try:
    read_csv_convert_save(csv_file_path, json_file_path)
    print(f"CSV file '{csv_file_path}' converted and saved to JSON file '{json_file_path}'.")
except FileNotFoundError as e:
    print(f"Error: {e}")
except ValueError as e:
    print(f"Error: {e}")
except IOError as e:
    print(f"Error: {e}")
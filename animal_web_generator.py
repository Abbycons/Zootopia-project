import json

# Constants for template placeholders
TEMPLATE_PLACEHOLDER = "__REPLACE_ANIMALS_INFO__"
TEMPLATE_FILE = "animals_template.html"
OUTPUT_FILE = "animals.html"
DATA_FILE = "animals_data.json"


def load_data(file_path):
    """Loads a JSON file and handles errors.

    Args:
         file_path (str): Path to the JSON file.

    Returns:
         list: A list of animals' data or an empty list if an error occurs.
    """
    try:
        with open(file_path, encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading {file_path}: {e}")
        return []


def serialize_animal(animal):
        """Transforms an animal’s data into an HTML format.

        Args:
            animal (dict): Dictionary containing animal details.

        Returns:
            str: HTML formatted string representing the animal.
        """
        # Safely get values with a fallback in case of missing fields
        name = f"<div class='card__title'>Name: {animal.get('common_name', 'Unknown')}</div>\n"
        diet = f"<div class='card__text'>Diet: {animal.get('diet', 'Unknown')}</div>\n"
        location = f"<div class='card__text'>Location: {', '.join(animal.get('locations', ['Unknown']))}</div>\n"
        type_info = f"<div class='card__text'>Type: {animal.get('family', 'Unknown')}</div>\n"

        return f"<li class='cards__item'>{name}{diet}{location}{type_info}</li>\n"


def generate_animal_info(animals_data):
    """Generates the final HTML file by replacing placeholders in the template.

    Args:
           animals_data (list): List of animal dictionaries.
    """
    try:
        with open(TEMPLATE_FILE, encoding="utf-8") as file:
            template = file.read()
    except FileNotFoundError:
        print(f"Error: Template file '{TEMPLATE_FILE}' not found.")
        return

        # Generate HTML for each animal
    animals_info = "".join(serialize_animal(animal) for animal in animals_data)

    # Replace the placeholder in the template with the generated animal data
    new_html = template.replace(TEMPLATE_PLACEHOLDER, animals_info)

    # Write the final HTML to the output file
    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        file.write(new_html)

    print(f"HTML file generated successfully: {OUTPUT_FILE}")
    return "".join(output)

# Main execution
if __name__ == "__main__":
    animals_data = load_data(DATA_FILE)
    if not animals_data:
        print("No valid animal data found. Exiting.")
        exit(1)

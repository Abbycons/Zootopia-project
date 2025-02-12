import json


def load_data(file_path):
    """Loads a JSON file and handles errors."""
    try:
        with open(file_path, encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading {file_path}: {e}")
        return []


def generate_animal_info(animals_data):
    """Generates HTML content for animals."""
    output = []

    for animal in animals_data:
        name = f"<div class='card__title'>Name: {animal.get('common_name', 'Unknown')}</div>\n"
        diet = f"<div class='card__text'>Diet: {animal.get('diet', 'Unknown')}</div>\n"
        location = f"<div class='card__text'>Location: {animal.get('locations', ['Unknown'])[0]}</div>\n"
        type_info = f"<div class='card__text'>Type: {animal.get('family', 'Unknown')}</div>\n"

        animal_info = name + diet + location + type_info
        output.append(f"<li class='cards__item'>{animal_info}</li>\n")


    return "".join(output)


def main():
    animals_data = load_data('animals_data.json')['animals']
    if not animals_data:
        print("No valid animal data found. Exiting.")
        exit(1)

    # Generate animals info
    animals_info = generate_animal_info(animals_data)

    # Read template
    try:
        with open('animals_template.html', encoding="utf-8") as file:
            template = file.read()
    except FileNotFoundError:
        print("Error: Template file 'animals_template.html' not found.")
        exit(1)

    # Replace placeholder and write new HTML file
    new_html = template.replace('__REPLACE_ANIMALS_INFO__', animals_info)

    with open('animals.html', 'w', encoding="utf-8") as file:
        file.write(new_html)

    print("HTML file generated successfully: animals.html")


if __name__ == "__main__":
    main()



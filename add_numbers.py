import os
import re

def process_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # Find all h6 headers and their numbers
    headers = re.findall(r'(######\s+(\d+))', content)
    print(f"Found headers in {file_path}: {headers}")

    # Process each header
    for header, number in headers:
        # Find the paragraph following the header
        paragraph_match = re.search(rf'{header}\n(.*?)(?=\n######|\Z)', content, re.DOTALL)
        if paragraph_match:
            paragraph = paragraph_match.group(1).strip()
            print(f"Found paragraph for header {header}: {paragraph}")
            # Replace the paragraph with the number prefixed
            new_paragraph = f'{number} {paragraph}'
            content = content.replace(paragraph, new_paragraph)
            print(f"Replaced paragraph: {new_paragraph}")
        else:
            print(f"No paragraph found for header: {header}")

    # Write the modified content back to the file
    with open(file_path, 'w') as file:
        file.write(content)

def process_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                print(f"Processing file: {os.path.join(root, file)}")
                try:
                    process_file(os.path.join(root, file))
                    print(f"Successfully processed {file}")
                except Exception as e:
                    print(f"Error processing {file}: {e}")

# Process the current directory and all its subdirectories
process_directory('.')

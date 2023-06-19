import os

dir = "./data/"

# Get all files in the directory recursively
files = [os.path.join(dp, f) for dp, dn, filenames in os.walk(dir) for f in filenames]
print(files)

for file in files:
    # Open the file
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()

        # Iterate each line of text
        lines = text.split('\n')
        
        # Remove empty lines
        lines = [line for line in lines if line.strip() != '']

        # Remove lines that are only brackets
        lines = [line for line in lines if not line.startswith('[') and not line.endswith(']')]

        # Replace \u2005 with a space
        lines = [line.replace('\u2005', ' ') for line in lines]

        # Replace \u205f with a space
        lines = [line.replace('\u205f', ' ') for line in lines]

        # Replace \u2019 with '
        lines = [line.replace('\u2019', "'") for line in lines]

        # Replace \u2014 with -
        lines = [line.replace('\u2014', '-') for line in lines]

        # Replace \u0435 with e
        lines = [line.replace('\u0435', 'e') for line in lines]

        # Replace \u00e9 with e with é
        lines = [line.replace('\u00e9', 'é') for line in lines]

        # Write the cleaned text back to the file
        with open(file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines))
            
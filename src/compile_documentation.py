import os
from glob import glob

def compile_documentation():
    # Define the directory paths for source and output files
    source_directory = 'docs/scripts'
    output_file = 'docs/compiled_documentation.md'

    print(f"Documentation should be compiled to: {output_file}")
    # List all Markdown files in the source directory
    markdown_files = glob(os.path.join(source_directory, '*.md'))

    # Sort the files alphabetically
    markdown_files.sort()

    # Compile documentation by concatenating Markdown files
    with open(output_file, 'w', encoding='utf-8') as output:
        for markdown_file in markdown_files:
            with open(markdown_file, 'r', encoding='utf-8') as file:
                output.write(file.read() + '\n\n')

    print(f"Documentation compiled successfully to: {output_file}")

if __name__ == "__main__":
    compile_documentation()

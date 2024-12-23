## Codebase to Text using Python

A Python script that converts a codebase into a single text file for easier analysis, ingestion into language models, or other text processing tasks.

It includes:

- Support for various file formats (.txt, .py, .js, .jsx, .html, .css, .cpp, .c, .h, .hpp, .java, .xml, .json, .md, .sh, .ts, .tsx).
- Skipping of large files (over 10MB by default).
- Ignoring of files based on patterns defined in the project's .gitignore file (if present).
- Ignoring of node_modules directory and package-lock.json file.
- Relative path information for each included file.

##### How to Use:

Save the script: Save the code as a Python file (e.g., codebase_to_text.py).
Run the script: Open a terminal or command prompt, navigate to the directory where you saved the file, and run it using python codebase_to_text.py.
Input project name: The script will prompt you to enter the name of your project folder (replace "placeholder" in the code).
Example:

```python
project_name = "myProject"  #enter projectname/foldername
project_path = f"/Users/abishekvenkat/Documents/Projects/{project_name}"
output_file = f"{project_name}_codebase.txt"
```

And you get
```bash
Codebase written to myProject_codebase.txt
```

This will create a text file named myProject_codebase.txt in the same directory as your project, containing the contents of all relevant files with their relative paths within the project.

##### Customization:

- You can adjust the os.path.getsize limit in the code to change the maximum file size considered for inclusion.
- You can modify the list of supported file extensions in the get_gitignore_patterns function if needed.

##### Requirements:

- Python 3
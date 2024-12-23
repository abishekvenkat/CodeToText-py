import os
import pathlib
import fnmatch

def codebase_to_text(project_path, output_file):

    try:
        with open(output_file, "w", encoding="utf-8") as outfile:
            gitignore_patterns = get_gitignore_patterns(project_path)

            for root, dirs, files in os.walk(project_path):
                dirs[:] = [d for d in dirs if not is_ignored(os.path.join(root, d), gitignore_patterns) and d != "node_modules"]

                for file in files:
                    file_path = os.path.join(root, file)
                    if is_ignored(file_path, gitignore_patterns):
                        continue

                    try:
                        if os.path.getsize(file_path) > 10 * 1024 * 1024:
                            print(f"Skipping large file: {file_path}")
                            continue

                        if pathlib.Path(file_path).suffix in ['.txt', '.py', '.js', '.jsx', '.html', '.css', '.cpp', '.c', '.h', '.hpp', '.java', '.xml', '.json', '.md', '.sh', '.ts', '.tsx', '.gitignore']: #add required file formats
                            with open(file_path, "r", encoding="utf-8", errors="ignore") as infile:
                                relative_path = os.path.relpath(file_path, project_path)
                                outfile.write(f"\n{'='*50} FILE: /{relative_path} {'='*50}\n")
                                outfile.write(infile.read())
                                outfile.write("\n")
                        else:
                            print(f"Skipping non-text file: {file_path}")
                    except UnicodeDecodeError:
                        print(f"UnicodeDecodeError with file: {file_path}. Skipping.")
                    except OSError as e:
                        print(f"OSError with file: {file_path}. Skipping. Error: {e}")

        print(f"Codebase written to {output_file}")

    except Exception as e:
        print(f"An error occurred: {e}")

def get_gitignore_patterns(project_path):
    gitignore_path = os.path.join(project_path, ".gitignore")
    if os.path.exists(gitignore_path):
        with open(gitignore_path, "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip() and not line.startswith("#")]
    return []

def is_ignored(path, patterns):
    if os.path.basename(path) == "package-lock.json":
        return True

    for pattern in patterns:
        if fnmatch.fnmatch(path, pattern) or fnmatch.fnmatch(os.path.basename(path), pattern):
            return True

        if pattern.endswith("/"):
            if fnmatch.fnmatch(path + "/", pattern) or fnmatch.fnmatch(os.path.basename(path) + "/", pattern):
                return True

    return False

if __name__ == "__main__":
    project_name = "wikimark"  #enter projectname/foldername
    project_path = f"/Users/abishekvenkat/Documents/Projects/{project_name}"
    output_file = f"{project_name}_codebase.txt"

    if not os.path.exists(project_path):
        print("Project path does not exist.")
    else:
        codebase_to_text(project_path, output_file)
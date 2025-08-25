
def write_file(file_name, file_content):
    """Write content to a .txt file (overwrite if it exists)."""
    with open(f"{file_name}.txt", "w", encoding="utf-8") as f:
        f.write(file_content)


def append_file(file_name, append_content):
    """Append content to a .txt file (create if it doesn't exist)."""
    with open(f"{file_name}.txt", "a", encoding="utf-8") as f:
        f.write(append_content)


def read_file(file_name):
    """Read and return the contents of a .txt file."""
    with open(f"{file_name}.txt", "r", encoding="utf-8") as f:
        return f.read()

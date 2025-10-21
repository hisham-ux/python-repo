import subprocess

# Path to your Git repository
repo_path = "python-repo"

# Run "git ls-files" to list only tracked (committed) files
result = subprocess.run(
    ["git", "-C", repo_path, "ls-files"],
    capture_output=True,
    text=True,
    check=True
)

# Print each committed file
for file in result.stdout.splitlines():
    print(file)

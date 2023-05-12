import os
import subprocess

# Set up the deployment variables
REMOTE_SERVER = "your_remote_server_ip"
REMOTE_USER = "your_remote_server_username"
REMOTE_DIR = "/path/to/target/directory"
LOCAL_DIR = "/path/to/cloned/repository"

# Create the target directory on the remote server if it doesn't exist
ssh_command = f"ssh {REMOTE_USER}@{REMOTE_SERVER} 'mkdir -p {REMOTE_DIR}'"
subprocess.run(ssh_command, shell=True, check=True)

# Copy the repository files to the remote server using rsync
rsync_command = f"rsync -avz --exclude '.git' {LOCAL_DIR}/ {REMOTE_USER}@{REMOTE_SERVER}:{REMOTE_DIR}"
subprocess.run(rsync_command, shell=True, check=True)

# Update the repository on the remote server using Git
git_commands = [
    f"ssh {REMOTE_USER}@{REMOTE_SERVER} 'cd {REMOTE_DIR} && git fetch --all'",
    f"ssh {REMOTE_USER}@{REMOTE_SERVER} 'cd {REMOTE_DIR} && git reset --hard origin/master'"
]
for command in git_commands:
    subprocess.run(command, shell=True, check=True)

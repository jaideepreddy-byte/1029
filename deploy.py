import os
import subprocess

# Set up the deployment variables
REMOTE_SERVER = "13.233.123.233"
REMOTE_USER = "ec2-user"
REMOTE_DIR = "/var/www/html/1029"
LOCAL_DIR = "/var/lib/jenkins/workspace/1029"

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

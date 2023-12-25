import os
import subprocess


'''
def check_for_updates():
    # Change the repository URL to your own repository
    repository_url = "https://github.com/Uglypr1nces/chatbot_proto.git"

    # Get the current version of the script
    current_version = subprocess.check_output(["git", "rev-parse", "HEAD"]).decode().strip()

    # Clone the repository if it doesn't exist
    if not os.path.exists("repository"):
        subprocess.call(["git", "clone", repository_url, "repository"])

    # Change directory to the repository
    os.chdir("repository")

    # Fetch the latest changes from the repository
    subprocess.call(["git", "fetch"])

    # Get the latest version of the script
    latest_version = subprocess.check_output(["git", "rev-parse", "origin/master"]).decode().strip()
    print(latest_version+" is the latest version, the current version is: "+current_version)

    # Compare the versions
    if current_version != latest_version:
        # Pull the latest changes from the repository
        subprocess.call(["git", "pull"])

        # Change directory back to the script's directory
        os.chdir("..")

        # Restart the script
        subprocess.call(["python", __file__])
        exit()

    # Change directory back to the script's directory
    os.chdir("..")

if __name__ == "__main__":
    check_for_updates()'''

subprocess.run([f"python", "riddle.py"])
    

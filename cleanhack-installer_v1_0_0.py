# THIS PROGRAM IS A SIMPLE AUTOMATED INSTALLATION TOOL
# THE GOAL HERE IS TO GET YOU UP AND RUNNING WITH A QUICK
# AND EFFECTIVE WAY TO INSTALL MOST OF THE ESSENTIAL 
# PENTESTING TOOLS ON ANY DEBIAN-BASED LINUX DISTRO
# AUTHOR 'CYBEROOVE'

import os
import subprocess
import sys
import argparse
import datetime
import shutil

def install_git():
    # Install Git
    subprocess.run(['apt-get', 'install', '-y', 'git'])

    # Add Git to the PATH
    with open('~/.bashrc', 'a') as bashrc:
        bashrc.write('\nexport PATH=$PATH:/usr/bin/git')


def install_git():
    # Install Git
    subprocess.run(['apt-get', 'install', '-y', 'git'])

    # Add Git to the PATH
    with open('~/.bashrc', 'a') as bashrc:
        bashrc.write('\nexport PATH=$PATH:/usr/bin/git')

def delete_installed_tools(dependencies, tools):
    # Uninstall dependencies
    for dependency in dependencies:
        subprocess.run(['apt-get', 'purge', '-y', dependency])

    # Delete cloned repositories
    for tool in tools:
        subprocess.run(['rm', '-rf', tool])

def delete_logs():
    now = datetime.datetime.now()
    one_day_ago = now - datetime.timedelta(days=1)
    log_files = []

    # Find all log files modified within the past 24 hours
    for root, dirs, files in os.walk("/var/log"):
        for file in files:
            full_path = os.path.join(root, file)
            mod_time = datetime.datetime.fromtimestamp(os.path.getmtime(full_path))
            if mod_time > one_day_ago:
                log_files.append(full_path)

    # Delete the log files
    for log_file in log_files:
        os.remove(log_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--clear-logs", action="store_true", help="Delete log files modified within the past 24 hours")
    args = parser.parse_args()

    if args.clear_logs:
        delete_logs()
        print("Logs are Deleted... Time to go Home")
        exit()
        
    else:
        print("Use the --clear-logs flag after you're done to delete the log files.")

# Parse command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--delete', action='store_true', help='delete all installed tools')
args = parser.parse_args()

if args.delete:
    # List of dependencies to be uninstalled
    dependencies = ['curl', 'build-essential', 'libreadline-dev', 'libssl-dev', 'libpq5', 'libpq-dev', 'libreadline5', 'libsqlite3-dev', 'libpcap-dev', 'openjdk-8-jre-headless', 'xtightvncviewer', 'libxml2-dev', 'libxslt1-dev', 'libyaml-dev', 'autoconf', 'zlib1g-dev', 'git', 'python3-pip', 'libpython3-dev', 'libpq-dev', 'tor', 'proxychains', 'ruby', 'ruby-dev']

    # List of tool directories to be deleted
    tools = ['metasploit-framework', 'sqlmap', 'nmap', 'wireshark', 'social-engineer-toolkit', 'wifite2']

    delete_installed_tools(dependencies, tools)
    sys.exit()

# Update the system
subprocess.run(['apt-get', 'update'])

# Check if Git is installed
result = subprocess.run(['which', 'git'], stdout=subprocess.PIPE)
if result.returncode != 0:
    # Git is not installed, so install it
    install_git()


# Install dependencies
dependencies = ['curl', 'build-essential', 'libreadline-dev', 'libssl-dev', 'libpq5', 'libpq-dev', 'libreadline5', 'libsqlite3-dev', 'libpcap-dev', 'openjdk-8-jre-headless', 'xtightvncviewer', 'libxml2-dev', 'libxslt1-dev', 'libyaml-dev', 'autoconf', 'zlib1g-dev', 'git', 'python3-pip', 'libpython3-dev', 'libpq-dev', 'tor', 'proxychains', 'ruby', 'ruby-dev']

for dependency in dependencies:
    subprocess.run(['apt-get', 'install', '-y', dependency])


# Add the gem executable to the PATH
subprocess.run(['echo', 'export PATH=$PATH:/usr/local/bin', '>>', '~/.bashrc'])

# Install the bundler gem
subprocess.run(['gem', 'install', 'bundler'])

# Add the bundle executable to the PATH
subprocess.run(['echo', 'export PATH=$PATH:/usr/local/bundle/bin', '>>', '~/.bashrc'])


# Install tor
subprocess.run(['apt-get', 'install', '-y', 'tor'])

# Install proxychains
subprocess.run(['apt-get', 'install', '-y', 'proxychains'])

# Set up the proxychains configuration file
subprocess.run(['echo', '"strict_chain"', '>>', '/etc/proxychains.conf'])
subprocess.run(['echo', '"proxy_dns"', '>>', '/etc/proxychains.conf'])
subprocess.run(['echo', '"remote_dns_subnet 224"', '>>', '/etc/proxychains.conf'])
subprocess.run(['echo', '"tcp_read_time_out 15000"', '>>', '/etc/proxychains.conf'])
subprocess.run(['echo', '"tcp_connect_time_out 8000"', '>>', '/etc/proxychains.conf'])
subprocess.run(['echo', '"localnet 127.0.0.0/255.0.0.0"', '>>', '/etc/proxychains.conf'])

# Clone repositories from GitHub
subprocess.run(['git', 'clone', 'https://github.com/rapid7/metasploit-framework.git'])
subprocess.run(['git', 'clone', 'https://github.com/sqlmapproject/sqlmap.git'])
subprocess.run(['git', 'clone', 'https://github.com/nmap/nmap.git'])
subprocess.run(['git', 'clone', 'https://github.com/wireshark/wireshark.git'])
subprocess.run(['git', 'clone', 'https://github.com/trustedsec/social-engineer-toolkit.git'])
subprocess.run(['git', 'clone', 'https://github.com/derv82/wifite2.git'])

# Install Metasploit
os.chdir('metasploit-framework')
subprocess.run(['bundle', 'install'])

# Install sqlmap
os.chdir('..')
os.chdir('sqlmap')
subprocess.run(['python3', 'setup.py', 'install'])

# Install nmap
os.chdir('..')
os.chdir('nmap')
subprocess.run(['./configure'])
subprocess.run(['make'])
subprocess.run(['make', 'install'])

# Install wireshark
os.chdir('..')
os.chdir('wireshark')
subprocess.run(['make'])
subprocess.run(['make', 'install'])

# Install setoolkit
os.chdir('..')
os.chdir('social-engineer-toolkit')
subprocess.run(['python3', 'setup.py', 'install'])

# Install Pyrit and Hcxtools

os.chdir('..')
subprocess.run(["sudo", "apt", "-y", "install", "python2"]) 

if os.path.exists("Pyrit"):
    shutil.rmtree("Pyrit")

subprocess.run(["git", "clone", "https://github.com/JPaulMora/Pyrit.git"])
subprocess.run(["sudo", "pip", "install", "psycopg2"])
subprocess.run(["sudo", "pip", "install", "scapy"])
subprocess.run(["sudo","apt", "-y", "install", "python2-dev"]) 



os.chdir("Pyrit")
subprocess.run(["sudo","python2", "setup.py", "clean"]) 
subprocess.run(["sudo","python2", "setup.py", "build"]) 
subprocess.run(["sudo","python2", "setup.py", "install"])
os.chdir("..")

subprocess.run(["apt-get", "install", '-y', "tshark"])
subprocess.run(["apt-get", "install", '-y', "hcxtools"])

# Install wifite

os.chdir('wifite2')
subprocess.run(['python3', 'setup.py', 'install'])

# Update the PATH environment variable
bashrc_path = os.path.expanduser('~/.bashrc')
with open(bashrc_path, 'a') as bashrc:
    bashrc.write('\n')
    bashrc.write('# Add tools to PATH\n')
    bashrc.write('export PATH=$PATH:/usr/local/bin\n')


print('Your prentesting tools are now ready to use. HAPPY HACKING!')

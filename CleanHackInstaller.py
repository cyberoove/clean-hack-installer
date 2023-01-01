# THIS PROGRAM IS A SIMPLE AUTOMATED INSTALLATION TOOL
# THE GOAL HERE IS TO GET YOU UP AND RUNNING WITH A QUICK
# AND EFFECTIVE WAY TO INSTALL MOST OF THE ESSENTIAL 
# PENTESTING TOOLS ON ANY DEBIAN-BASED LINUX DISTRO
# AUTHOR 'CYBEROOVE'
#DO NOT USE THIS SCRIPT IN ILLEGAL WAYS
#THIS SCRIPT WILL DELETE ALL THE PACKAGES AND TOOLS IF YOU USE THE PARAMETER (--delete)
#RUN THE SCRIPT THROUGH PYTHON3

import os
import subprocess
import sys
import argparse



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

# Install wifite
os.chdir('..')
os.chdir('wifite2')
subprocess.run(['python3', 'setup.py', 'install'])

# Update the PATH environment variable
bashrc_path = os.path.expanduser('~/.bashrc')
with open(bashrc_path, 'a') as bashrc:
    bashrc.write('\n')
    bashrc.write('# Add tools to PATH\n')
    bashrc.write('export PATH=$PATH:/usr/local/bin\n')


print('Your prentesting tools are now ready to use. HAPPY HACKING!')


# clean-hack-installer
# by (cyb3r00v3)

# README 

# Disclaimer 
The author is not responsible for any misuse of the code. Do not use this code for any illegal activities.

# Description 
This code installs and sets up various tools for ethical hacking and pentesting. The tools include Metasploit, sqlmap, Nmap, Wireshark, the Social Engineer Toolkit, and Wifite2. The code also installs dependencies and sets up proxychains and tor for anonymous browsing.

# Functionality 
The code can be run with the optional argument --delete to delete all installed tools and dependencies. Otherwise, the code will update the system and install the necessary dependencies, including Git if it is not already installed. The code will then clone the repositories for the aforementioned tools and set up proxychains and tor.

# The reason behind this script

There will be situations for you as a pentester where you won't have access to your tools and software, or maybe all you have access to is an ordinary Debian Based Operating system. That's where this piece of software comes in handy.
Always keep it on your USB drive and you will be able to get that machine up and ready for hacking in no time.

# Features:

- Install and add Git to the PATH if it is not already installed on the system

- Option to delete certain dependencies and tool directories using the --delete flag

- Option to delete log files that were modified within the past 24 hours using the --clear-logs flag

- Install a list of dependencies that are required to run the hacking tools mentioned above

- Clone and install several hacking tools from GitHub

- Install and configure Metasploit

# NEW:

Improvements in this version of the software 

The software is divided into 2 scripts now, one is for light fast work, and one that
will install all the previous existing software mentioned in the previous versions

dependencies installation for wifite has been fixed
a new function is added: clear all the logs in the past 24 hours by running the 
parameter --clear-logs after the script

A new script has been added for light "LITE" usage and will install all the tools mentioned in the original script except for metasploit-framework

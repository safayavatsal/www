# Deploying a Website and Subdomain Status Checker on macOS with Nginx


## Task 1: Deploy a Website on Localhost

### Setting up Nginx on macOS
1. Install Nginx: `brew install nginx`
2. Start Nginx: `sudo brew services start nginx`
3. Verify Nginx Installation: Open your browser and navigate to `http://localhost:8080` . You should see the Nginx welcome page.

### Creating a DNS Name for the Website
1. Edit Hosts File: `sudo nano /etc/hosts`
2. Add the Following Line: `127.0.0.1   awesomeweb`

### Deploying a Simple HTML Project

1. Create a Project Directory: `mkdir -p /usr/local/var/www/awesomeweb` and locate the directory: `cd /usr/local/var/www/awesomeweb`

2. Create an HTML File: `echo '<!DOCTYPE html><html><head><title>Awesome Web</title></head><body><h1>Welcome to Awesome Web</h1></body></html>' > index.html`

3. Configure Nginx:
   Edit the Nginx configuration file: `sudo nano /usr/local/etc/nginx/nginx.conf`

4. Update the `server` Block:
server {
    listen       8080;
    server_name  awesomeweb;

    location / {
        root   /usr/local/var/www/awesomeweb;
        index  index.html index.htm;
    }
}

5. Restart Nginx: `sudo brew services restart nginx`
6. Verify Deployment: Open your browser and navigate to `http://awesomeweb:8080`.


## Task 2: Check Subdomain Status

### Python Script for Checking Subdomain Status

Create a Python script named check_subdomains.py:

import requests
import time
from prettytable import PrettyTable

subdomains = ["sub1.awesomeweb", "sub2.awesomeweb", "sub3.awesomeweb"]

def check_subdomains():
    table = PrettyTable()
    table.field_names = ["Subdomain", "Status"]
    for subdomain in subdomains:
        try:
            response = requests.get(f"http://{subdomain}")
            status = "Up" if response.status_code == 200 else "Down"
        except requests.ConnectionError:
            status = "Down"
        table.add_row([subdomain, status])
    print(table)

if __name__ == "__main__":
    while True:
        check_subdomains()
        time.sleep(60)
        
### Running the Script

1. Install Dependencies: `pip install requests prettytable`
2. Run the Script: `python3 check_subdomains.py`


## Task 3: Virtual Machine Setup and Nginx Deployment

### Virtual Machine (VM) - Overview 

A virtual machine (VM) is a software emulation of a physical computer that runs an operating system and applications just like a physical machine. VMs allow you to create multiple isolated environments on a single physical host, each with its own virtual hardware configuration. This virtualization technology provides several advantages, such as the ability to run multiple operating systems on a single physical machine, easy migration of VMs between different hosts, and improved resource utilization. 

The virtualization layer called the hypervisor, is responsible for managing the VMs and enabling communication between them and the underlying physical hardware. There are two types of hypervisors: Type 1 hypervisor (bare-metal) runs directly on the physical hardware, while Type 2 hypervisor runs on top of an existing operating system. 


### Oracle VirtualBox - Overview 

Oracle VirtualBox is a popular Type 2 hypervisor that allows you to create and manage virtual machines on your desktop or laptop. It supports a wide range of guest operating systems, including Windows, Linux, macOS, and more. VirtualBox is free and open-source, making it an excellent choice for developers, testers, and anyone interested in exploring virtualization. 


### How to Install VirtualBox 

Here's a step-by-step guide to installing Oracle VirtualBox on your Windows, macOS, or Linux computer: 

Step 1: Download VirtualBox 

1. Go to the official VirtualBox website: `https://www.virtualbox.org/`

2. Click on the "Downloads" link in the top navigation menu. 


Step 2: Choose the Correct Package 

1. On the Downloads page, you'll see various packages for different host operating systems. Select the appropriate package for your OS (e.g., Windows, macOS, or Linux). 


Step 3: Install VirtualBox

1. For Windows: 

- Download the installer for Windows and double-click on the downloaded file to start the installation. 

- Follow the on-screen instructions and accept the license agreement. - Choose the components you want to install and the installation path. - Complete the installation process. 


2. For macOS: 

- Download the macOS version of VirtualBox. 

- Double-click on the downloaded DMG file to open it. 

- Double-click on the VirtualBox package icon to start the installation. - Follow the on-screen instructions to complete the installation. 


3. For Linux: 

- Download the appropriate package for your Linux distribution (e.g., .deb for Debian/Ubuntu-based systems, .rpm for Red Hat/Fedora-based systems). - Install VirtualBox using the package manager of your Linux distribution. For example, for Ubuntu, use the following command in the terminal: 

`sudo dpkg -i <VirtualBox_package_name>.deb`

- You may need to install additional dependencies if prompted by the package manager. 


Step 4: Post-installation Configuration (All Operating Systems) 

1. After installation, you might need to add your user account to the "vboxusers" group (Linux) or "VirtualBox Users" group (Windows) to grant permissions to manage VMs. 


Step 5: Launch VirtualBox 

1. Once the installation is complete, you can launch VirtualBox from your application menu (Windows and Linux) or from the Applications folder (macOS). 


Congratulations! You now have Oracle VirtualBox installed on your computer and can start creating and managing virtual machines for various purposes, including development, testing, and exploration of different operating systems.


### Scanning VM with Nmap

1. Find VM's IP Address: `ip addr show`
2. Scan VM with Nmap from Host Machine: `nmap <VM_IP_Address>`
3. Documentation of Nmap Output

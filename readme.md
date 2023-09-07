<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>digitalocean-infrastructure
</h1>
<h3>Pulumi Infrastructure as Code</h3>
<h3>Developed with the software and tools listed below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/Pulumi-8A3391.svg?style&logo=Pulumi&logoColor=white" alt="Pulumi" />
<img src="https://img.shields.io/badge/Python-3776AB.svg?style&logo=Python&logoColor=white" alt="Python" />
</p>
<img src="https://img.shields.io/github/languages/top/cdiaz2799/digitalocean-infrastructure?color=5D6D7E
" alt="GitHub top language" />
<img src="https://img.shields.io/github/languages/code-size/cdiaz2799/digitalocean-infrastructure?style&color=5D6D7E" alt="GitHub code size in bytes" />
<img src="https://img.shields.io/github/commit-activity/m/cdiaz2799/digitalocean-infrastructure?style&color=5D6D7E" alt="GitHub commit activity" />
<img src="https://img.shields.io/github/license/cdiaz2799/digitalocean-infrastructure?style&color=5D6D7E" alt="GitHub license" />
</div>

---

## 📒 Table of Contents
- [📒 Table of Contents](#-table-of-contents)
- [📍 Overview](#-overview)
- [⚙️ Features](#-features)
- [📂 Project Structure](#project-structure)
- [🧩 Modules](#modules)
- [🚀 Getting Started](#-getting-started)
- [👏 Acknowledgments](#-acknowledgments)

---


## 📍 Overview

The project is focused on quickly setting up infrastructure on the DigitalOcean cloud platform. It provides a collection of code modules that enable the creation of various resources such as projects, virtual machines (droplets), databases, DNS records, and VPCs. The code automates the deployment and configuration process.

---

## ⚙️ Features

| Feature             | Description                                                                                                                                                                                                             |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **⚙️ Architecture** | The codebase follows a modular architecture, where components are organized into separate folders. It utilizes Pulumi for infrastructure provisioning.                                                                  |
| **🔗 Dependencies** | The code relies on external libraries like Pulumi, DigitalOcean API, and Cloudflare API for resource management and infrastructure tasks.                                                                               |
| **🔌 Integrations** | The system heavily interacts with external services like DigitalOcean and Cloudflare through their respective APIs. There are no evident communication patterns with third-party systems apart from these integrations. |

---


## 📂 Project Structure




---

## 🧩 Modules

<details closed><summary>Root</summary>

| File                                                                                                                | Summary                                                                                                                                                                                                                  |
|---------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [__main__.py](https://github.com/cdiaz2799/digitalocean-infrastructure.git/blob/main/__main__.py)                   | This code iterates over folders in a given directory, imports Python modules within these folders, and executes callable functions within these modules. It allows for dynamic execution of code in a structured manner. |
| [component_project.py](https://github.com/cdiaz2799/digitalocean-infrastructure.git/blob/main/component_project.py) | This code defines an "AppProject" class that creates a new DigitalOcean project. The project is given a name, description, and environment. The class also registers the project's URN as an output.                     |

</details>

<details closed><summary>Actual</summary>

| File                                                                                                 | Summary                                                                                                    |
|------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| [actual.py](https://github.com/cdiaz2799/digitalocean-infrastructure.git/blob/main/actual/actual.py) | This code sets up a DigitalOcean project, creates a web application, and sets up DNS records using Pulumi. |

</details>

<details closed><summary>Paperless</summary>

| File                                                                                                      | Summary                                                                                                                                                                                                                                                             |
| ---                                                                                                       | ---                                                                                                                                                                                                                                                                 |
| [droplet.py](https://github.com/cdiaz2799/digitalocean-infrastructure.git/blob/main/paperless/droplet.py) | The code sets up a Droplet (virtual machine) on DigitalOcean for the Paperless project. It defines the Droplet's specifications, including the region, size, image, and SSH key. The Droplet is also associated with a VPC and has monitoring and an agent enabled. |
| [project.py](https://github.com/cdiaz2799/digitalocean-infrastructure.git/blob/main/paperless/project.py) | The code imports a project component and creates an AppProject object for a paperless app with specified app name and project name.                                                                                                                                 |

</details>

<details closed><summary>Outline</summary>

| File                                                                                                    | Summary                                                                                                                                                                                                                                                                                                                                                     |
| ---                                                                                                     | ---                                                                                                                                                                                                                                                                                                                                                         |
| [db.py](https://github.com/cdiaz2799/digitalocean-infrastructure.git/blob/main/outline/db.py)           | This code configures a DigitalOcean database and firewall rules for an Outline application. It defines a database, a user, and firewall rules that allow connections from a specific Droplet.                                                                                                                                                               |
| [droplet.py](https://github.com/cdiaz2799/digitalocean-infrastructure.git/blob/main/outline/droplet.py) | This code sets up a DigitalOcean VM (Virtual Machine) for the Outline app, assigns a reserved IP address, and adds the VM to a project for resource management.                                                                                                                                                                                             |
| [dns.py](https://github.com/cdiaz2799/digitalocean-infrastructure.git/blob/main/outline/dns.py)         | This code sets up a DNS record for an Outline server using the Cloudflare DNS provider. It retrieves the Zone ID for "cdiaz.cloud", creates a DNS record named "outline" with the A record type, and points it to the Outline server's IP address. The DNS record is set to be proxied by Cloudflare. The code then exports the hostname of the DNS record. |
| [project.py](https://github.com/cdiaz2799/digitalocean-infrastructure.git/blob/main/outline/project.py) | This code sets up a project called "Outline" on the DigitalOcean cloud platform. It includes the project's name, description, environment, and purpose.                                                                                                                                                                                                     |

</details>

<details closed><summary>Master</summary>

| File                                                                                                       | Summary                                                                                                                                                                                                                                                                   |
| ---                                                                                                        | ---                                                                                                                                                                                                                                                                       |
| [vpc.py](https://github.com/cdiaz2799/digitalocean-infrastructure.git/blob/main/master/vpc.py)             | This Python Pulumi code deploys VPC(s) on DigitalOcean in the specified regions. It uses the Pulumi DigitalOcean provider to create VPC resources, setting the VPC name and region for each VPC. The created VPC(s) are stored in the `vpcs` list.                        |
| [ansible.py](https://github.com/cdiaz2799/digitalocean-infrastructure.git/blob/main/master/ansible.py)     | This code provisions a DigitalOcean virtual machine (Droplet) running Ubuntu, with specified tags and SSH key. It also associates the Droplet with a VPC and deploys cloud-init configuration. Finally, it adds the Droplet to a project for organization and management. |
| [database.py](https://github.com/cdiaz2799/digitalocean-infrastructure.git/blob/main/master/database.py)   | The code creates a database cluster on the DigitalOcean platform using different engines such as Postgres, MySQL, MongoDB, and Redis. It sets the engine version, cluster name, node count, region, size, and connects it to a private network.                           |
| [project.py](https://github.com/cdiaz2799/digitalocean-infrastructure.git/blob/main/master/project.py)     | This code creates a DigitalOcean project called "master" for operational and developer tooling with protection enabled.                                                                                                                                                   |
| [opconnect.py](https://github.com/cdiaz2799/digitalocean-infrastructure.git/blob/main/master/opconnect.py) | This code deploys a DigitalOcean Droplet running Rocky Linux and sets up a firewall with inbound and outbound rules. It also creates a DNS record with Cloudflare.                                                                                                        |

</details>

---

## 🚀 Getting Started

### ✔️ Prerequisites

Before you begin, ensure that you have the following prerequisites installed:
> - `ℹ️ Pulumi`
> - `ℹ️ DigitalOcean`
> - `ℹ️ Cloudflare`

### 📦 Installation

1. Clone the digitalocean-infrastructure repository:
```sh
git clone https://github.com/cdiaz2799/digitalocean-infrastructure.git
```

2. Change to the project directory:
```sh
cd digitalocean-infrastructure
```

3. Install the dependencies:
```sh
pip install -r requirements.txt
```

### 🎮 Using digitalocean-infrastructure

```sh
pulumi up
```

### 🧪 Running Tests
```sh
pulumi preview
```

---

## 👏 Acknowledgments

> - `ℹ️  readmeai - AI Readme Generation`

---

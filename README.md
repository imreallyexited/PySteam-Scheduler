# Welcome to my project! (Alpha)

A lightweight Command Line Interface (CLI) utility designed to automatically reject incoming Steam friend requests.

## Overview
This tool operates as a standalone executable and requires no installation. It is designed for users who wish to maintain a strict privacy policy on their Steam profiles by automating the rejection process.

**Current Version:** Alpha 1.0

## Installation & Requirements
* **Operating System:** Windows 10 / 11.
* **No Python Installation Required:** The application is compiled as a standalone `.exe` file.
* **Dependencies:** Ensure `config.txt` is always located in the same directory as the executable.

## How to Use

1.  **Download and Extract**
    Download the latest release zip file and extract the contents to a folder of your choice.

2.  **Configuration**
    Open the `config.txt` file using any text editor (Notepad, VS Code, etc.).

3.  **Enter Credentials**
    * Replace `USERNAME_HERE` with your Steam login username.
    * Replace `PASSWORD_HERE` with your Steam login password.

4.  **Enter Security Secrets (2FA)**
    * Replace `SHARED_SECRET_HERE` with your Steam Shared Secret.
    * Replace `IDENTITY_SECRET_HERE` with your Steam Identity Secret.
    * *Note: These are required to generate mobile authentication codes automatically.*

5.  **Launch**
    Run the `ARSI.exe` file. The terminal window will open and display the connection status.

## Retrieving Steam Secrets
If you do not know your Shared or Identity secrets, you must extract them from your mobile authenticator device or desktop authenticator application.

* [Guide: How to retrieve Steam Shared & Identity Secrets](https://github.com/SteamTimeIdler/stidler/wiki/Getting-your-%27shared_secret%27-code-for-use-with-Auto-Restarter-on-Mobile-Authentication)

## To run in the background
Create a shortcut to "ARSI.vbs" and add it to your startup folder.

## Roadmap & Future Improvements

The current release (Alpha) is focused on core functionality and stability. The following features are planned for upcoming updates to enhance usability and filtering capabilities:

* **Integrated Configuration Manager:**
    Eliminate the need for manual `config.txt` editing. Future versions will include an onboard setup wizard (CLI or GUI) allowing users to securely input and store credentials directly within the application.

* **Enhanced User Interface:**
    Transition from the raw console output to a more robust interface. This includes a modernized Command Line Interface (CLI) dashboard or a lightweight Graphical User Interface (GUI) for real-time status monitoring and easier interaction.

* **Geo-Location Filtering (Region Blocking):**
    Implementation of advanced filtering logic to automatically reject friend requests based on the user's country of origin or region. This will allow for stricter control over incoming interactions.

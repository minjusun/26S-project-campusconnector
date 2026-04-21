# CampusConnector


**Demo Video:** https://www.dropbox.com/scl/fi/10uig3oxft6z810kpu9zi/CS3200_Campus_Connector_Demo_Final.mp4?rlkey=l6i05x19eab68a3479dhvph7b&st=ab63j0sr&dl=0


**Team Name:** Data Visionaries




**Team Members:** Benjamin Knox, Reinier DeVault, Minju Sung, SungBin Lee, Tzu Yang Chen








## Overview




CampusConnector is a data-driven campus event management platform built for Northeastern University. It allows students to discover and RSVP to events, event coordinators to organize and manage attendance, data analysts to track engagement metrics, and administrators to monitor platform health.
The platform centralizes all aspects of campus events into a single system, reducing the need to navigate multiple platforms. By combining event discovery, registration, analytics, and system management, CampusConnector improves both user experience and operational efficiency.
In addition, the system leverages data to provide insights into student engagement, helping coordinators and analysts make more informed decisions about future events. This creates a more connected campus environment where events are easier to find, manage, and evaluate.






**Tech Stack:** Python, Flask, Streamlit, MySQL, Docker








## Features




-**Students:** View upcoming events filtered by category or interest. View event details, register for events, and join waitlists if events are full. View registered events in one place. 


-**Event Coordinators:** Create and manage events, update event details, monitor registrations and attendance, and communicate through notifications.
 
-**Data Analysts:** View engagement statistics and attendance trends, compare event performance, view predictions on future events and engagement.




-**Administrators:** View platform health via dashboard, manage users and their permissions, review and manage system logs, run backups for the database.












## Project Structure




```
26S-project-campusconnector/
├── api/                  # Flask REST API (port 4000)
│   ├── backend/          # Flask blueprints
│   ├── .env.template     # Environment variable template
│   └── requirements.txt
├── app/                  # Streamlit frontend (port 8501)
│   └── src/
│       ├── pages/        # Role pages
│       ├── modules/      # Shared nav
│       └── requirements.txt
├── database-files/       # SQL scripts to initialize
├── datasets/             # Data for app
├── ml-src/               # ML model
└── docker-compose.yaml   


#docker-compose.yaml is used to set up the Docker containers for the front end app, the REST API, and MySQL database


```








## Prerequisites




- [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running
- A GitHub Account
- A terminal-based git client or GUI Git client such as GitHub Desktop or the Git plugin for VSCode.
- A distribution of Python running on your laptop. [Anaconda](https://www.anaconda.com/download) or [Miniconda](https://www.anaconda.com/docs/getting-started/miniconda/install).






## Setup




### 1. Clone the repository




```bash
git clone <repo-url>
cd 26S-project-campusconnector
```




### 2. Create the `.env` file




Copy the env template under api, name it .env, and fill in the required parts (secret key, root password)




Open `api/.env` and set values:




```env
SECRET_KEY=enter key here
DB_USER=root
DB_HOST=db
DB_PORT=3306
DB_NAME=campus_connector
MYSQL_ROOT_PASSWORD=enter password here
```
Do not change `DB_USER`, `DB_HOST`, `DB_PORT`, or `DB_NAME`.




### 3. Start the containers


```bash
docker compose up -d
```
This starts 
 App: frontend (streamlit); http://localhost:8501
 Api: Flask Rest API; http://localhost:4000
 Db: MYSQL database; localhost:3200






## Common Docker Commands
```bash


# Reset the database, rerun all SQL init scripts
docker compose down db -v && docker compose up db -d`




# Start all containers in the background
docker compose up -d




# Rebuild and restart after code changes to Dockerfiles
docker compose up --build




# stops and deletes the MySQL container and the volume attached to it
docker compose down db -v
     
# Create a new db container and re-run the files in the `database-files` folder.
docker compose up db -d




> **Note:** The MySQL container only runs the SQL init scripts when it is **created for the first time**. If the SQL files are changed, restart the container with the command above.




# View logs (all services or one)
docker compose logs
docker compose logs api




## User Roles
-**Student:** 
Wants to easily discover events, simpler registration process. And keep track of upcoming activities. Focused on convenience and accessibility.


- **Event Coordinator:** 
Wants to create, manage, and monitor events. Focused on organization, attendance tracking, and communication with participants. 


- **Data Analyst:**
Wants to analyze engagement data, identify trends, and generate insights that improve event performance and user experience.


- **Administrator:**
Wants to maintain system reliability and security by managing users, monitoring system activity, and ensuring the platform runs smoothly. 






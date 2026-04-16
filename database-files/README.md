# `database-files` Folder

The MySQL server that is running in the db container is set up so that when the container is *created*, any `.sql` files in the `database-files` folder are automatically run.  Loosely speaking, the `.sql` files are run in "alphabetical" order.  So if your database schema is broken into a few files, it is easiest to rename them with a number at the beginning so they'll be run in the correct order.  So, something like `01_db.sql`, `02_db.sql` and so on. 

If you make changes to any of the files in the `database-files/` folder AFTER the db container is started, you'll have to delete the container and re-create it for the SQL files to be re-executed.  **Note:** simply stopping and re-starting the db container will not re-run the files. 

If you are in your sandbox repo, do the following:

```bash
docker compose -f sandbox.yaml down db -v && docker compose -f sandbox.yaml up db
```

If you are working with your team repository, do the following

```bash
docker compose down db -v && docker compose up db
```

The `-v` flag will also delete the volume associated with MySQL, which is necessary to rerun the sql files. 

#read me-REMOVE SPECS ABOVE BEFORE SUBMISSION!!!!!

#Campus Connector
**Team Name: ** Data Visionaries
**Team Members: **Benjamin Knox, Reinier DeVault, Minju Sung, SungBin Lee, Tzu Yang Chen

##Overview
Campus Connector is a data-driven campus event management platform for students to discover and RSVP to new events, event managers to organize new events, data analysts to track event statistics, and administrators to monitor the platform.

##Key Features
1. Filters student attendees by event categories, notifications, and other relevant information. It improves efficiency and accuracy for the users by allowing them to narrow down large datasets to only relevant data, as well as improving data visualization for analysts.

2. Allows student coordinators to manage attendees by utilizing the event editor. In it, they can accept, deny, or waitlist applicants based on the capacity of the event serving as a security measure and providing an additional layer of control to the event managers.
Our goal is to transform campus events from scattered and underutilized into an organized, highly engaging experience for everyone.


##Pre-requisites

##Setup?
-specs...
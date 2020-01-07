# instawork-assignment
This is a take-home assignment given by Instawork

## Project Goal
The goal of the project is to implement an HTTP API to support a team-member management application. The team member data should be persisted in a MySQL database. The application needs to support listing team members, adding a new team member, editing a team member, and deleting a team member. The details are covered below.

## Technologies used
 - Python/Django
 - MySql

## System Requirements
Please ensure that the system meets the following requirements
 - Either Linux(Ubuntu or Debian) or macOS as the operating system.
 - Python 3.7.6+
 - `virtualenv` installed and part of `$PATH`
 - A running instance of MySql on port 3306 with a `root` user

## Setting up the project
This involves the following two stages
1. DB setup
2. Python env setup

#### DB setup
Please run the following commands sequentially
 1. ```cd ~/instawork-assignment/setup_project```
 2. Run ```bash setup_db.sh```
 3. This will prompt for a password. Please provide the password for the ```root``` user of your MySql instance.
 
 The above script does the following
  - Creates the database `iw_db` and user `iw_user`. 
  - Restores the db dump from `~/instawork-assignment/dumps/iw_db_dump.sql`
  
 Also the dump which is restored contains one team member.

#### Python env setup
Please run the following commands sequentially
1. ```cd ~/instawork-assignment/setup_project```
2. Run `bash setup_python_env.sh abs_path_to_python3_executable`

The above script does the following
 - Creates a virtualenv named `server_venv` inside the directory `~/instawork-assignment/server/` with the given python3 executable.
 - Installs pip package dependencies for the project from `~/instawork-assignment/server/requirements.txt` file.

## Start dev server
1. ```cd ~/instawork-assignment/setup_project```
2. Run `bash start_server.sh` which starts the development server on port `8000`.

## Run tests
1. ```cd ~/instawork-assignment/setup_project```
2. Run `bash run_test.sh` which internally runs the `~/instawork-assignment/server/team_mgmt/api_test.py` file.

The `api_test.py` script does the following
 - Calls four methods sequentially where each method is responsible for testing one endpoint
 ```py
 test_create_team_member() # tests the create team member endpoint (POST /api/team-members/)
 test_get_all_team_members() # tests the get all team members endpoint (GET /api/team-members/)
 test_update_team_member() # tests the update team member endpoint (PATCH /api/team-member/<team-member-id>/)
 test_delete_team_memeber() # tests the delete team member endpoint (DELETE /api/team-member/<team-member-id>/)
 ```
 - The default behavior of the script is as follows
   1. Create a new user with some hard-coded data.
   2. Verify the above step by fetching all users.
   3. Update the same user with new data.
   4. Finally delete the user which got created thereby bringing the db back to its original state before the test was run.
   
Please feel free to modify the parameters inside each of the above mentioned methods to test the behavior of the api under different conditions.








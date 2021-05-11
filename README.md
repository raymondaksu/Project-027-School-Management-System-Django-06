# Project-027-Student-Management-System-Django-06

## This is a simple API for:

* creating a unified interface for keeping track of students
* accounts for students to login and see their own pages
* admins can login and see everyone via the Django admin interface
* it will be able to use Github OAuth

## About the Program

* It's set up to offer 3-month long classes in two different levels, 1 and 2. When students pass level 1 - HTML, CSS, and JS, they can move onto level 2 - Node, Express, and Mongo.

## Table of Contents

* [Requirements](#requirements)
* [Schema](#schema)
* [API](#api)

## Running Locally

1. Must have Python 3 & Postgres version 12.x installed and running
1. Clone the repo and cd into repo
1. Create a virtual environment: `py -m venv venv`
1. Go into your virtual environment: `venv\Scripts\activate`
1. Install dependencies: `pip install -r requirements.txt`
1. Create an admin user for logging into the Django admin interface: `py manage.py createsuperuser`
1. Setup Database
    1. Create the database: `CREATE DATABASE example;`
    1. Create DB user: `CREATE USER name;
    1. Grant privilages to user for our database: `GRANT ALL PRIVILEGES ON DATABASE example TO name;`
    1. Run migrations: `py manage.py migrate`
1. Run the app: `py manage.py runserver`
1. View the API at `localhost:8000` and the admin interface at `localhost:8000/admin`

## Requirements

* Students and Organizers/Admin accounts login using GitHub OAUTH
* Private Student Profile: Visible to only the user and organizers/admins
  * Email
  * Discord Name
  * Phone
  * Attendenance (not editable by students)
  * List of labs:
    * Link to the lab starter
    * input field for a link to their completed version

* Admin Dashboard
  * Student Progress/Outcomes
    * Grouped by enrollment period (semester)
      * Show all students in a table to track progress/outcomes
      * Be able to edit any part of the table
  * Volunteer management
    * Be able to view volunteers listed in a table
  * Waitlist
    * Table of all those on the waitlist

## Schema

* User
  * email
  * password
  * groups: student, admin, or volunteer (can only belong to one)

* StudentProfile
  * first_name
  * last_name
  * preferred_name
  * discord_name
  * github_username
  * codepen_username
  * fcc_profile_url
  * current_level
  * phone
  * timezone

* Volunteer
  * first_name
  * last_name
  * email
  * hours_available
  
* VolunteerHours
  * volunteer: FK
  * start: DateTime
  * end: DateTime
  
* Lecture
  * date
  * title
  * description
  * lecturer_name
  * slides_url
  * duration
  * level
  * required: BooleanField
  
* Attendance
  * lecture_id
  * student_id
  
* Project (labs)
  * title
  * description
  * url
  * level
  * required

* StudentSubmission
  * student_id
  * project_id
  * url: CharField
  * feedback: TextField (for comments from reviewers)
  * approved: BooleanField
  
* StudentCertificate 
  * student_id
  * certificate_id
  
* Certificate
  * name
  * description

* Waitlist
  * first_name
  * last_name
  * email
  * notes

## API

**Prefix:** /api/v1

**/users**

* get (temporary, only for testing)
* post

**/users/:id**

* get
* patch
* delete

**/users/:id/profile**

* get

*example response:*

```json
{
  "user": 6,
  "name": "Daneel Olivaw",
  "bio": "hello there...",
  "preferred_name": null,
  "avatar_url": "http://example.com",
  "discord_name": null,
  "github_username": "rdaneel",
  "codepen_username": null,
  "fcc_profile_url": null,
  "current_level": 1,
  "phone": null,
  "timezone": null
}
```

* post

**/users/:id/certificates**

* get

**/users/:id/assignments**

* get
* post

**/certificates**

* get

**/projects**

* get


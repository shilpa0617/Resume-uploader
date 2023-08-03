# Resume-uploader
## Overview
The Resume Uploader is a web application built using Django, a powerful Python web framework. The project enables users to upload and manage their resumes with ease. It provides a user-friendly interface to submit, view, and delete resumes. This project is designed to streamline the resume submission process and manage candidate data efficiently.

## Features
+ **Resume Model:** Implemented a dynamic Django model to store candidate resume data, including personal information and uploaded resumes.
+ **Pillow Integration:** Utilized the Pillow library for image handling and resume file uploads.
+ **Django ModelForm:** Created a custom ModelForm to create and manage the resume submission form with ease.
+ **Bootstrap Styling:** Designed a responsive and visually appealing user interface using Bootstrap and CSS styling.
+ **Radio Buttons and Multiple Checkboxes:** Incorporated radio buttons and multiple checkboxes for improved form options.
+ **Date Picker:** Enhanced the user experience with a date picker for date selection.
+ **Custom Filters:** Implemented custom filters to facilitate preferred job city selection.
+ **django-unused-media:** Integrated "django-unused-media" to optimize media file management and delete unused files.

## Setup Instructions
1. Clone the repository: **`git clone https://github.com/shilpa0617/resume-uploader.git`**
2. Create a virtual environment: **`python -m venv venv`**
3. Activate the virtual environment:
   + On Windows: **`venv\Scripts\activate`**
   + On macOS and Linux: **`source venv/bin/activate`**
4. Install project dependencies: **`pip install -r req.txt`**
5. Run database migrations: **`python manage.py migrate`**
6. Start the development server: **`python manage.py runserver`**
7. Access the web application at **`http://localhost:8000/`**

## Usage
1. Navigate to the home page to submit your resume.
2. Complete the form, including personal information and resume file upload.
3. Choose preferred job city options and submit the form.
4. View the list of submitted resumes on the Candidate page.
5. Click on a candidate's name to view the resume details.
6. Use the "Back to Home" button to return to the home page.
7. To delete unused media files, run: python manage.py unusedmedia

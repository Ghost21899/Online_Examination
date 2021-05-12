# Online Examination
A simple web based application for conducting examination using django, open-cv and MySQL


## Table of Contents
* [Introduction](#introduction)
* [Technologies Used](#technologies-used)
* [Setup](#setup)
* [Screenshots](#screenshots)


## Introduction
This project is aimed to prevent impersonation of an examinee taking an exam. It uses face recognition to detect if it's the examinee or an impersonator.


## Technologies Used
#### Software Pre-requisites
* Python 3.7
* MySQL

#### Python libraries required are:

Name                    | Version
----------------------- | -----------------------
face-recognition        | 1.3.0
Django                  | 3.1.5
opencv-pyhton           | 3.4.2
django-crispy-forms     | 1.11.2


## Setup
<details>
  <summary>Pre-requisites: </summary>
  <ul>
    <li>Setup MySQL driver with Python</li>
    <li>dlib (needed to install face-recognition)</li>
    <li>cmake (needed to install  face-recognition)</li>
  </ul>
</details>

---
***Ensure you meet the pre-requisites before continuing***
1. `pip install -r requirements.txt'`
2. Create Schema 'Online_Exam_Database'
3. `python manage.py makemigrations`
4. `python manage.py migrate`
5. `python manage.py runserver`


## Screenshots
* Registering a new user
![image\screenshots\registering](https://github.com/Ghost21899/Online_Examination/blob/master/image/Screenshots/Registering.png)

* Looging in
![image\screenshots\logging-in](https://github.com/Ghost21899/Online_Examination/blob/master/image/Screenshots/Logging-in.gif)

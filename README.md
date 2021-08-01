# Online Examination
A simple web based application for conducting examination using django, open-cv and MySQL

[![Python 3.7](https://img.shields.io/badge/Python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/)
[![Django 3.1.5](https://img.shields.io/badge/Django-3.1.5-blue.svg)](https://docs.djangoproject.com/en/3.1/releases/3.1.5/)
[![OpenCV 3.4.2](https://img.shields.io/badge/OpenCV-3.4.2-blue.svg)](https://docs.opencv.org/3.1.0/index.html)
[![face-recognition 1.3.0](https://img.shields.io/badge/face--recognition-1.3.0-blue)](https://pypi.org/project/face-recognition/1.3.0/)
[![MySQL 8.0.22](https://img.shields.io/badge/MySQL-8.0.22-blue.svg)](https://dev.mysql.com/doc/relnotes/mysql/8.0/en/news-8-0-22.html)

[![GitHub issues](https://img.shields.io/github/issues/Ghost21899/Online_Examination)](https://github.com/Ghost21899/Online_Examination/issues)
[![GitHub issues-closed](https://img.shields.io/github/issues-closed/Ghost21899/Online_Examination)](https://github.com/Ghost21899/Online_Examination/issues?q=is%3Aissue+is%3Aclosed)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/Ghost21899/Online_Examination)](https://github.com/Ghost21899/Online_Examination/pulls)
[![GitHub pull-requests closed](https://img.shields.io/github/issues-pr-closed/Ghost21899/Online_Examination)](https://github.com/Ghost21899/Online_Examination/pulls?q=is%3Apr+is%3Aclosed)


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


## Support
Reach out to me at one of the following places
* Mail me at <a href="mailto:niranjan.m2199@gmail.com" target="_blank">`niranjan.m2199@gmail.com`</a>
* LinkedIn at <a href="https://www.linkedin.com/in/niranjan-mahesh/" target="_blank">`@niranjanmahesh`</a>

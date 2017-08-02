## Remote 3DFSC Processing

This is a Django app for uploading cryo-em maps to a remote server and processing YZT, DL, and PRB's 3DFSC program.

## Installation

Note: This development server installation was tested in Docker with Ubuntu 16.04.2 LTS.

### 1) OS Dependencies
apt-get update  
apt-get install -y python3-dev zlib1g-dev git wget bzip2 gcc vim redis-server screen 

### 2) Install Anaconda
clone Linux Anaconda3 Installer:  
wget https://repo.continuum.io/archive/Anaconda3-4.4.0-Linux-x86_64.sh

run the installer (adding anaconda path to .bashrc is recommended): 
bash Anaconda3-4.4.0-Linux-x86_64.sh

### 3) Clone Repository
(Note the --recursive flag)  
git clone --recursive https://github.com/carl9384/3dfsc_upload fscupload

### 4) Create virtual environment
conda env create -f ~/fscupload/environment.yml

## Getting Started

### 1) Configure settings.py
cd ~/fscupload  
cp settings.py.template settings.py

Change SECRET_KEY to a random 50 character string (this should be kept secret for security reasons)  
(You can use this site: http://www.miniwebtool.com/django-secret-key-generator/) 

DEBUG is set to TRUE for the development server. This should be set to FALSE for production (it will cause a memory leak, eventually)

Set EMAIL_ variables for your configuration.  
For SMTP, ammend EMAIL_HOST, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD for your email account.  
e.g.  

EMAIL_HOST = 'smtp.gmail.com'  
EMAIL_HOST_USER = 'fscuser@gmail.com'  
EMAIL_HOST_PASSWORD = 'fscpassword'  

Set PROJECT_ROOT to the path where ./manage.py is located, e.g. /home/cnegro/fscupload/manage.py 
PROJECT_ROOT = '/home/cnegro/fscupload/' 

Set SITE_URL to the domain of the site you plan to use: 
SITE_URL = 'http://192.168.4.147:8000'

### 2) Migrate database
cd ~/fscupload 
./manage.py makemigrations 
./manage.py migrate 

### 3) Start redis
screen;redis-server (detach with ctrl+a, ctrl+d)

### 4) Start celery worker task
screen 
cd ~/fscupload 
celery -A fscupload worker -l info 
(detach with ctrl+a, ctrl+d) 

### 5) Launch Django test server

cd ~/fscupload 
./manage.py runserver 0.0.0.0:8000 

### 6) Use it
You should now be able to navigate to http://192.168.4.147:8000 

NOTE: The development server should not be used for production!

## Thanks

Add a note about citations

These tutorial links helped:
http://www.bogotobogo.com/python/Django/Python_Django_Image_Files_Uploading_Example.php
https://realpython.com/blog/python/asynchronous-tasks-with-django-and-celery/

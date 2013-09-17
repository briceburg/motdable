motadble
========

### Prerequisites
* Python 2.6+
* python-virtualenv
* python-pip


### About
Motdable allows you to manage and execute Ansible (http://www.ansibleworks.com/) playbooks. 


It was written on a Sunday, in the spirit of NFL games; so I elected to think of Playbooks 
as "Play Calls" and hosts as "Players". The interface where you choose the player and call 
to execute is called the "Coordinator".

Subsequently the program was refactored to use conventional naming, with the note: Sunday != Monday.


### Code Overview

Motdable was written in django-rest-framework and packages a AngularJS application to interact
with playbook execution.

The django-rest-framework application is under **motdable/api**. It provides CRUD management
of Playbooks and Hosts via its Web Browsable API. Naturally it exposes a REST interface
which is leveraged by the AngularJS interface.

The AngularJS interface (aka the "Coordinator") is under **motdable/coordinator/static**. It
allows the selection of playbooks and hosts to run them against, and asynchronously triggers
these via an XHR call to the playbook executer under **motdable/coordinator/views.py**.


### Installation

0. checkout repository to application_root
  
  ```
  git clone <repo> $application_root 
  ```

0. create virtual enviroment

  ```
  virtualenv --no-site-packages $application_root/venv
  ```

0. install requirements

  ```
  cd $application_root
  venv/bin/pip install -r requirements.txt
  ```

0. configure django's settings.py
  ```
  cd $application_root/motdable/motdable/
  cp settings.sample.py settings.py
  vi settings.py
  ```
  
0. setup the initial database and superuser
  ```
  cd $application_root
  venv/bin/python motdable/manage.py syncdb
  ```

0. *optional* load initial fixture (includes working playbooks)
  ```
  cd $application_root
  venv/bin/python motdable/manage.py syncdb motdable/iceburg.json
  ```

### Usage

**NOTE**: If you loaded the initial fixture, the superuser credentials are:
  username: ansible
  password: ansible!

0. run the django server
  ```
  cd $application_root
  venv/bin/python motdable/manage.py runserver
  ```
  
0. execute your plays via the coordinator interface.
  ```
  firefox|chromium http://localhost:8000/
  firefox|chromium http://localhost:8000/coordinator/
  ```
  
0. manage you hosts and playbooks via the api interface. login as the django admin to gain the ability to post new models. E.g.
  ```
  firefox|chromium http://localhost:8000/api
  ```



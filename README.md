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
  
0. setup the initial database and superuser [TODO: provide a fixture/migration for demo]
  ```
  cd $application_root
  venv/bin/python motdable/manage.py syncdb
  ```


### Usage

0. run the django server
  ```
  cd $application_root
  venv/bin/python motdable/manage.py runserver
  ```
  
0. manage you players and playcalls via the api interface. login as the django admin to gain the ability to post new models. E.g.
  ```
  firefox|chromium http://localhost:8000/api
  ```
  
0. execute your plays via the coordinator interface.
  ```
  firefox|chromium http://localhost:8000/coordinator/
  ```


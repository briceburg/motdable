motdble
=======

### Prerequisites
* Python 2.6+
* python-virtualenv
* python-pip

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



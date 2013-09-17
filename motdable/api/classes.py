import os

from django.core.files.storage import FileSystemStorage, Storage

class PrivateKeyStorage(FileSystemStorage):
    
    def __init__(self, location=None, base_url=None):
        
        # The base_url is set to a private IP address to thwart media access requests.
        if location is None:
            location = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'uploads'))
            
        # NOTE: Because we're uploading private keys, the target directory
        # must only be readable by the user running the django process [0700].
        if not os.path.exists(location):
            os.makedirs(location,0700)
            
        # Set base_url to a private IP to thwart media access requests.
        if base_url is None:
            base_url = 'http://10.0.9.200/'
            
        super(PrivateKeyStorage, self).__init__(location, base_url)

        
    
    def _save(self, name, content):
        
        # execute parent class _save method
        name = super(PrivateKeyStorage, self)._save(name, content)
        
        # set uploaded file to read-only (for use w/ SSH)
        full_path = self.path(name)
        os.chmod(full_path, 0400)
        
        return name
        
        
    
    
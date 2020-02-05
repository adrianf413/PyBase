import requests
import urllib.parse
import json


class PyBase():

    URL_ENDING = '.json'
    URL_DELIMITER = '/'

    # initialised with db_ref, e.g "https://<projectname>.firebaseio.com/"
    # Authentication is not implemented yet - Will implement eventually
    def __init__(self, db_ref, authentication=None):
        self.db_ref = db_ref
        self.authentication = authentication


    def _build_endpoint(self, db_ref, keyname=None):

        if not db_ref.endswith(self.URL_DELIMITER):
            db_ref = db_ref + self.URL_DELIMITER
        
        if keyname is None:
            keyname = ''
        
        joined = urllib.parse.urljoin(db_ref, keyname)
    
        return joined + self.URL_ENDING


    def upload_data(self, keyname, data, params=None, headers=None):
        '''
        Used for uploading data to a specific key, if specified. if not will go under database
        parent key. Using requests.POST updates and appends data. Using requests.PUT overwrites existing
        data in the database. Using POST here.

        Example:
        response = upload_data('users', user)

        user must be a dict.json object for example
        user = {
            name: 'Tom Steel', 
            Age:21
        }

        you can then use the response to see if it was successful
        
        '''    
        #params = params or {} - Not implemented yet
        #headers = headers or {} - Not implemented yet
        if keyname is None:
            keyname = ''
        endpoint = self._build_endpoint(self.db_ref, keyname)
        
        return requests.post(endpoint, json.dumps(data))

    def read_data(self, keyname, params=None, headers=None):
        '''
        Read all data in in json format from database under the keyname
        For example, to read in all data in users
        user_data = read_data('users')

        example 2: nested keys
        data = read_data('key1/key2/users')
        '''
        if keyname is None:
            keyname = ''
        #params = params or {} - Not implemented yet
        #headers = headers or {} - Not implemented yet
        endpoint = self._build_endpoint(self.db_ref, keyname)
        
        return requests.get(endpoint)


    def _authenticate(self):
        print(1)
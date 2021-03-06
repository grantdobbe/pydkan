import os
import json

try:
    from dkan.client import DatasetAPI
except ImportError:
    import sys
    sys.path.append('../')
    from dkan.client import DatasetAPI
    
uri = os.environ.get('DKAN_URI', False)
user = os.environ.get('DKAN_USER', 'admin')
password = os.environ.get('DKAN_PASSWORD', 'admin')

if uri:
  api = DatasetAPI(uri, user, password, True)
  data = {
      'title': 'Test Dataset',
      'type': 'dataset'
  }
  dataset = api.node('create', data=data)
  print(dataset.status_code)
  print(dataset.text)
  nid = dataset.json()['nid']
  op = api.node('delete', node_id=nid)
  print(op.status_code)
  print(op.text)
else:
  print('Please Set the dkan URL as an ENVIRONMENT variable')

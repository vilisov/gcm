```bash
pip install gcm
```

```python 
from gcm import GCM

gcm = GCM('API_KEY')

data = {'key': 'value'}
registration_ids = ['1234', '5678']

gcm.json_request(registration_ids, data, **kwargs)
```

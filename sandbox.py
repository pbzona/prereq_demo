from dotenv import load_dotenv
load_dotenv()

import os
import ldclient
from ldclient.config import Config

from user import User

# Setup client
ld_sdk_key = os.environ.get('LD_SDK_KEY')
ldclient.set_config(Config(ld_sdk_key))
ld_client = ldclient.get()

f = open("samples.txt", "a")
f.write('ID,Parent,Dependent\n')

for i in range(1000):
    user = User()
    
    parent_eval = ld_client.variation('parent-flag', user.context, False)
    dependent_eval = ld_client.variation('dependent-flag-string', user.context, 'Control')
    
    f.write(f'{user.id},{parent_eval},{dependent_eval}\n')

print(parent_eval)
print(dependent_eval)

f.close()
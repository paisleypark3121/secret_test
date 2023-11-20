test for secrets

The goal is to have both in .env and in Github - Secrets and variables - codespaces, the same "keys" and basically use the same "code" so that it can work on both local machine and codespaces.

It is necessary to have the CAPITAL LETTERS so that there are no problems when accessing enviroment variables.

In order to have it working locally it is necessary to act as follows:

import os
from dotenv import load_dotenv
load_dotenv()
print("Hello World")
print(os.environ['MY_VAR'])
print(os.environ.get('MY_VAR'))

it is mandatory to have the "load_dotenv()" and then to access the environment variable

In order to have it working on codespaces it is not necessary to have the dotenv / load_dotenv(), anyway, in order to not change code it is necessary to pip install dotenv and load_dotenv
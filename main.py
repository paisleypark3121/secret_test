import os
from dotenv import load_dotenv

load_dotenv()
print("Hello World")
print(os.environ['MY_VAR'])
print(os.environ.get('MY_VAR'))
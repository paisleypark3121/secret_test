import os
from dotenv import load_dotenv

load_dotenv()
print("Hello World")
print(os.environ['my_var'])
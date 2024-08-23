# config.py

import os
from dotenv import load_dotenv

load_dotenv()

UPSTAGE_API_KEY = os.getenv('UPSTAGE_API_KEY')
FAL_KEY = os.getenv('FAL_KEY')
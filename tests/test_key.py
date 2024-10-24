from dotenv import load_dotenv

load_dotenv()
import os


def test_my_key():
    my_apy_key = os.getenv('OPENAI_API_KEY')
    assert len(my_apy_key)>0
    isinstance(my_apy_key, str)

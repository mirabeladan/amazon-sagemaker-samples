import os
from dotenv import load_dotenv
from pkg.utils.io import serialize_model 
import logging

#load_dotenv()


logging.basicConfig(level=logging.INF0)
log = logging.getLogger ()

def get_s3_bucket_name() -> str:
    bucket_name = os.getenv("AWS_S3_BUCKET")
if not bucket_name:
    return ""
return get_s3_bucket_name













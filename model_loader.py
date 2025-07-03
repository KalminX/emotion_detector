# model_loader.py

import os
import boto3
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

def download_model_if_needed(s3_key, local_path):
    """Download model from S3 if not present locally."""
    if os.path.exists(local_path):
        return

    s3 = boto3.client(
        "s3",
        aws_access_key_id=os.environ["BUCKETEER_AWS_ACCESS_KEY_ID"],
        aws_secret_access_key=os.environ["BUCKETEER_AWS_SECRET_ACCESS_KEY"],
        region_name=os.environ["BUCKETEER_AWS_REGION"]
    )

    bucket = os.environ["BUCKETEER_BUCKET_NAME"]

    os.makedirs(os.path.dirname(local_path), exist_ok=True)
    print(f"Downloading {s3_key} from S3...")
    s3.download_file(bucket, s3_key, local_path)
    print(f"Saved to {local_path}")

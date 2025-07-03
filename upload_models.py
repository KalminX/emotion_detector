# upload_models.py

import boto3
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# AWS S3 client
s3 = boto3.client(
    "s3",
    aws_access_key_id=os.getenv("BUCKETEER_AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("BUCKETEER_AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("BUCKETEER_REGION")
)

bucket = os.getenv("BUCKETEER_BUCKET_NAME")

# Local model path and S3 key
local_file = ".deepface/weights/emotion_model.h5"
s3_key = "deepface/emotion_model.h5"

# Upload
try:
    s3.upload_file(local_file, bucket, s3_key)
    print("✅ Uploaded to Bucketeer.")
except Exception as e:
    print(f"❌ Upload failed: {e}")

import boto3
import os
import shutil
from dotenv import load_dotenv
from datetime import datetime
from botocore.exceptions import NoCredentialsError, EndpointConnectionError

load_dotenv()

DB_FILE = os.getenv("DB_PATH", "inventory.db")
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")
REGION_NAME = os.getenv("REGION_NAME")
BUCKET_NAME = os.getenv("BUCKET_NAME")

s3 = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name=REGION_NAME
)

def upload_backup():
    if not all([AWS_ACCESS_KEY, AWS_SECRET_KEY, REGION_NAME, BUCKET_NAME]):
        print("Error: Missing AWS credentials or bucket name.")
        return

    if not os.path.exists(DB_FILE):
        print(f"Error: Database file '{DB_FILE}' not found.")
        return

    backup_file = f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.db"
    local_path = os.path.join(os.getcwd(), backup_file)

    # COPY DB instead of renaming to avoid PermissionError
    shutil.copy2(DB_FILE, local_path)

    try:
        s3.upload_file(local_path, BUCKET_NAME, backup_file)
        print(f"Database backup uploaded to S3 successfully! ({backup_file})")
    except NoCredentialsError:
        print("Failed to upload: AWS credentials not found.")
    except EndpointConnectionError:
        print("Failed to upload: Could not connect to the endpoint URL.")
    except Exception as e:
        print(f"Failed to upload: {e}")

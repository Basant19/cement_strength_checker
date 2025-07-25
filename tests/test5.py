
import boto3
from botocore.exceptions import ClientError

AWS_REGION = "us-east-1"  
REPO_NAME = "cement_strength"      

def verify_ecr_repo():
    try:
        ecr = boto3.client('ecr', region_name=AWS_REGION)
        response = ecr.describe_repositories(repositoryNames=[REPO_NAME])
        repo = response['repositories'][0]
        print(" ECR Repository Found:")
        print(f"Name: {repo['repositoryName']}")
        print(f"URI: {repo['repositoryUri']}")
    except ClientError as e:
        if e.response['Error']['Code'] == 'RepositoryNotFoundException':
            print(f" Repository '{REPO_NAME}' not found in ECR.")
        else:
            print(" AWS Error:", e)

if __name__ == "__main__":
    verify_ecr_repo()

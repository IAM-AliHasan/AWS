# GP2 Volume Checker and CloudWatch Alarmer

## Project Overview
This AWS Lambda function identifies **GP2** volumes attached to EC2 instances in your AWS account. It sends a CloudWatch alarm if any GP2 volumes are detected and reports their count as custom metrics. This project ensures proactive monitoring of your volume types and helps maintain compliance with infrastructure standards.

---

## Features
- **GP2 Volume Detection**: Scans all EC2 instances and checks the attached EBS volumes.
- **CloudWatch Alarms**: Sends an alarm if GP2 volumes are found.
- **Custom Metrics**: Publishes the count of GP2 volumes to CloudWatch for tracking.
- **Highly Scalable**: Works across regions and multiple instances seamlessly.

---

## File Structure
project-folder/ │ ├── lambda_function/ │ ├── init.py # Package initializer (optional) │ ├── handler.py # Contains the Lambda function code │ ├── requirements.txt # List of project dependencies │ ├── README.md # Documentation (this file) ├── .gitignore # Files and folders to be ignored by Git ├── LICENSE # Project licensing information (optional) └── tests/ # Unit tests for Lambda function logic

---

## Installation and Deployment

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo
Install Dependencies: Make sure you have Python 3 and pip installed. Run:
bash
pip install -r lambda_function/requirements.txt
Deploy to AWS Lambda:

Package the function and its dependencies into a .zip file.
Upload the .zip file to the AWS Lambda Console.
Set the runtime to Python 3.x and configure necessary environment variables and IAM roles.
Usage
Deploy the function to AWS Lambda.
Set up a CloudWatch rule or API Gateway to trigger the function.
Provide an event object to the function (if applicable).
Monitor results in the CloudWatch dashboard.
Sample Function Response:
json
{
  "statusCode": 200,
  "body": "Checked all EC2 instances and reported GP2 volumes"
}
Permissions
To execute this Lambda function, ensure that the execution role has the following permissions:
ec2:DescribeInstances
ec2:DescribeVolumes
cloudwatch:PutMetricAlarm
cloudwatch:PutMetricData

Testing:
You can write unit tests for this Lambda function using unittest or pytest to validate the logic. Mocks for AWS services can be implemented using the moto library. Example:

python:
from moto import mock_ec2, mock_cloudwatch
import boto3
import unittest

class TestGP2VolumeChecker(unittest.TestCase):
    @mock_ec2
    @mock_cloudwatch
    def test_gp2_volume_detection(self):
        # Mock the AWS services and test the function logic
        pass
Notes:
This function assumes that all EC2 instances and volumes can be accessed in the account's current AWS region.
GP2 volumes attached to running instances cannot be deleted by this function; this function is only for detection and alerting.
Contributing:
Contributions are welcome! Feel free to open issues or submit pull requests to enhance the project.

Contact
For questions or feedback, contact Ali Hassan (your email or GitHub profile link).

You can customize the placeholders (e.g., repository link, email address) based on your preferences. Let me know if you need help with anything else!

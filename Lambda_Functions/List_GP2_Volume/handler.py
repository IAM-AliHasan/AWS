#################################################
# Author: Ali Hasan
# Purpose:  GP2 Volume Checker Lambda Function

################################################

import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    cloudwatch = boto3.client('cloudwatch')
    
    # List all EC2 instances
    instances = ec2.describe_instances()
    
    gp2_volumes = []
    
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            
            # Check each volume attached to the instance
            for blk_device in instance['BlockDeviceMappings']:
                volume_id = blk_device['Ebs']['VolumeId']
                volume = ec2.describe_volumes(VolumeIds=[volume_id])
                
                for vol in volume['Volumes']:
                    if vol['VolumeType'] == 'gp2':
                        gp2_volumes.append({
                            'InstanceId': instance_id,
                            'VolumeId': volume_id,
                            'VolumeType': vol['VolumeType']
                        })
    
    if gp2_volumes:
        # Send CloudWatch alarm
        response = cloudwatch.put_metric_alarm(
            AlarmName='GP2 Volume Warning',
            ComparisonOperator='GreaterThanThreshold',
            EvaluationPeriods=1,
            MetricName='GP2VolumeCount',
            Namespace='Custom',
            Period=300,
            Statistic='Sum',
            Threshold=0,
            ActionsEnabled=True,
            AlarmActions=[],
            AlarmDescription='Triggered when GP2 volumes are found in EC2 instances',
            Dimensions=[],
            Unit='Count'
        )
        
        # Send the count of GP2 volumes found
        cloudwatch.put_metric_data(
            Namespace='Custom',
            MetricData=[
                {
                    'MetricName': 'GP2VolumeCount',
                    'Dimensions': [],
                    'Unit': 'Count',
                    'Value': len(gp2_volumes)
                },
            ]
        )
    
    return {
        'statusCode': 200,
        'body': 'Checked all EC2 instances and reported GP2 volumes'
    }

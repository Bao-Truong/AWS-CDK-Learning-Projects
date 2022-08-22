from aws_cdk import (
    Stack,
    aws_s3 as s3,
    aws_s3_notifications as s3notify,
    aws_lambda as lmda,
    CfnOutput as Output
)
import aws_cdk as cdk
from constructs import Construct
from .private_constructs.NotifyingBucket.NotifyingBucketStack import *
import os
WORKDIR = os.getcwd()


class MultiAccountCfnLambdaStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        bucket = s3.Bucket(self, "MyFirstBucket", versioned=True,
                           removal_policy=cdk.RemovalPolicy.DESTROY,
                           auto_delete_objects=True,
                           bucket_name="ken2303superempire")
        with open(f"{WORKDIR}/multi_account_cfn_lambda/scripts/lambda-code.py", encoding="utf8") as fp:
            handler_code = fp.read()
        
        my_lambda = lmda.Function(self, "my_lambda", runtime=lmda.Runtime.PYTHON_3_9, handler="index.lambda_handler",
                                  code=lmda.InlineCode(handler_code),
                                  function_name="My-Lambda-Triggered-by-s3")

        bucket.add_event_notification(
            s3.EventType.OBJECT_CREATED, s3notify.LambdaDestination(my_lambda))

        Output(self, "output_bucket", value=bucket.bucket_name)
        Output(self, "output_bucket_arn", value=bucket.bucket_arn)
        Output(self, "output_lambda", value=my_lambda.function_name)
        # sns = NotifyingBucket(self, "MyNotifyingBucket", prefix="meep")

from doctest import OutputChecker
from constructs import Construct
from aws_cdk import App, Stack, CfnOutput
import aws_cdk.aws_s3 as s3
import aws_cdk.aws_sns as sns
import aws_cdk.aws_s3_notifications as s3notify


class NotifyingBucket(Construct):

    def __init__(self, scope: Construct, id: str, *, prefix=None):
        super().__init__(scope, id)
        self.att = "hello"
        bucket = s3.Bucket(self, "bucket")
        topic = sns.Topic(self, "topic")
        bucket.add_object_created_notification(s3notify.SnsDestination(topic),
                                               s3.NotificationKeyFilter(prefix=prefix))
        
        CfnOutput(self,"ouput_bucket",value=bucket.bucket_name)

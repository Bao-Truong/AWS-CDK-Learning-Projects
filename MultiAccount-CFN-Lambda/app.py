#!/usr/bin/env python3
import os
from dotenv import load_dotenv
import aws_cdk as cdk

from multi_account_cfn_lambda.multi_account_cfn_lambda_stack import MultiAccountCfnLambdaStack

load_dotenv()

app = cdk.App()
MultiAccountCfnLambdaStack(app, "MultiAccountCfnLambdaStack",
    env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),
    )


app.synth()

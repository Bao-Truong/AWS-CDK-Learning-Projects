"""
AWS Lambda function to remove outdated AMIs
All credits: https://gist.github.com/luhn/802f33ce763452b7c3b32bb594e0d54d
"""
import logging
import os
import re
import sys
from datetime import datetime, timedelta
import boto3

def lambda_handler(event, context):
    """handler function"""
    print("event:", event)
    print("context:", context)


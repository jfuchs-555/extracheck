from lark import Token

from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck
from checkov.common.models.enums import CheckResult, CheckCategories


class Check_for_resource(BaseResourceCheck):
    def __init__(self):
        name = "Checks if S3 bucket exists"
        id = "CUSTOM_AWS_998"
        supported_resources = ['aws_s3_bucket']
        # CheckCategories are defined in models/enums.py
        categories = [CheckCategories.BACKUP_AND_RECOVERY]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def scan_resource_conf(self, conf):
        """
            looks for modules
            fails
        """
        return CheckResult.FAILED


test = Check_for_resource()
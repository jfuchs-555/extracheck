from lark import Token

from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck
from checkov.terraform.checks.module.base_module_check import BaseModuleCheck
from checkov.common.models.enums import CheckResult, CheckCategories


class Check_for_module(BaseModuleCheck):
    def __init__(self):
        name = "Checks source of module"
        id = "CUSTOM_AWS_995"
        supported_resources = ['module']
        # CheckCategories are defined in models/enums.py
        categories = [CheckCategories.BACKUP_AND_RECOVERY]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def scan_module_conf(self, conf):
        """
            looks for source of modules
        """
        if 'source' in conf.keys():
            path = str(conf['source'][0])
            print('this is path', path)
            if not path == './modules/aws-s3-static-website-bucket' :
                return CheckResult.FAILED
            else:
                return CheckResult.PASSED


test = Check_for_module()
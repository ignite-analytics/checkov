from checkov.common.models.enums import CheckResult, CheckCategories
from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck
from typing import List


class CloudFunctionsEncryptedWithCMEK(BaseResourceCheck):
    def __init__(self):
        name = "Ensure Cloud Functions is securely encrypted when using Artifact Registry repositories"
        id = "CKV_GCP_112"
        supported_resources = ['cloudfunctions_function']
        categories = [CheckCategories.ENCRYPTION]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def scan_resource_conf(self, conf):
        if "docker_registry" in conf.keys() and conf["docker_registry"][0] == "ARTIFACT_REGISTRY" \
                and "kms_key_name" in not conf.keys():
            return CheckResult.FAILED
        return CheckResult.PASSED

    def get_evaluated_keys(self) -> List[str]:
        return ['docker_registry', 'kms_key_name']


check = CloudFunctionsEncryptedWithCMEK()

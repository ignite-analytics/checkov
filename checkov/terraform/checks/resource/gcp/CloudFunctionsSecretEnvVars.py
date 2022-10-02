from __future__ import annotations

from typing import Any

from checkov.common.models.enums import CheckResult, CheckCategories
from checkov.common.models.consts import ANY_VALUE
from checkov.terraform.checks.resource.base_resource_negative_value_check import BaseResourceNegativeValueCheck


class CloudFunctionsSecretEnvVars(BaseResourceNegativeValueCheck):
    def __init__(self) -> None:
        name = "Ensure that Cloud Functions don't use secrets from Secret Manager as environment variables"
        id = "CKV_GCP_112"
        supported_resources = ("google_cloudfunctions_function", "google_cloudfunctions2_function")
        categories = (CheckCategories.GENERAL_SECURITY,)
        super().__init__(
            name=name, id=id,
            categories=categories,
            supported_resources=supported_resources
        )

    def get_inspected_key(self) -> str:
        if self.entity_type == "google_cloudfunctions_function":
            return "secret_environment_variables/[0]/key"
        elif self.entity_type == "google_cloudfunctions2_function":
            return "service_config/[0]/secret_environment_variables/[0]/key"

    def get_forbidden_values(self) -> List[Any]:
        return [ANY_VALUE]

check = CloudFunctionsSecretEnvVars()

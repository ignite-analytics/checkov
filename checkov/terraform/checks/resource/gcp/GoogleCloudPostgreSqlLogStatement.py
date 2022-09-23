from checkov.common.models.enums import CheckResult, CheckCategories
from checkov.terraform.checks.resource.gcp.AbsGooglePostgresqlDatabaseFlags import AbsGooglePostgresqlDatabaseFlags

FLAG_NAME = 'log_statement'
FLAG_VALUES = [
    'ddl',
    'mod',
    'all'
]


class GoogleCloudPostgreSqlLogStatement(AbsGooglePostgresqlDatabaseFlags):
    def __init__(self):
        name = "Ensure GCP PostgreSQL logs SQL statements"
        check_id = "CKV_GCP_107"
        supported_resources = ['google_sql_database_instance']
        categories = [CheckCategories.LOGGING]
        super().__init__(
            name=name,
            id=check_id,
            categories=categories,
            supported_resources=supported_resources,
            flag_name=FLAG_NAME,
            flag_values=FLAG_VALUES
        )


check = GoogleCloudPostgreSqlLogStatement()

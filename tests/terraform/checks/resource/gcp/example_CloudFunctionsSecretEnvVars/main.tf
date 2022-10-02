resource "google_cloudfunctions_function" "fail" {
  name    = "function-test"
  runtime = "nodejs16"

  available_memory_mb          = 128
  source_archive_bucket        = "my-unique-bucket"
  source_archive_object        = "function.zip"
  trigger_http                 = true
  https_trigger_security_level = "SECURE_ALWAYS"
  timeout                      = 60
  entry_point                  = "helloGET"

  secret_environment_variables {
    key        = "TEST"
    project_id = "test-project"
    secret     = "MY_SECRET"
    version    = "latest"
  }
}

resource "google_cloudfunctions2_function" "fail" {
  name     = "function-test"
  location = "us-central1"

  build_config {
    runtime     = "nodejs16"
    entry_point = "helloHttp"

    source {
      storage_source {
        bucket = "my-unique-bucket"
        object = "function.zip"
      }
    }
  }

  service_config {
    max_instance_count = 1
    available_memory   = "256M"

    secret_environment_variables {
      key        = "TEST"
      project_id = "test-project"
      secret     = "MY_SECRET"
      version    = "latest"
    }
  }
}

resource "google_cloudfunctions_function" "pass" {
  name    = "function-test"
  runtime = "nodejs16"

  available_memory_mb          = 128
  source_archive_bucket        = "my-unique-bucket"
  source_archive_object        = "function.zip"
  trigger_http                 = true
  https_trigger_security_level = "SECURE_ALWAYS"
  timeout                      = 60
  entry_point                  = "helloGET"
}

resource "google_cloudfunctions2_function" "pass" {
  name     = "function-test"
  location = "us-central1"

  build_config {
    runtime     = "nodejs16"
    entry_point = "helloHttp"

    source {
      storage_source {
        bucket = "my-unique-bucket"
        object = "function.zip"
      }
    }
  }

  service_config {
    max_instance_count = 1
    available_memory   = "256M"
  }
}

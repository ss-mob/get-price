api_gw_domain_name   = "customer.dev.api.mobaws.mobiquitylab.tech"
api_gw_name          = "mob-api-gateway"
api_mapping_key      = "demo"
aws_profile          = "temp_mob-bp-dng"
handler_name         = "index.lambda_handler"
lambda_function_name = "get-product-price"
lambda_run_time      = "python3.8"
package_version      = "v0.2.0"
package_url          = "https://codeload.github.com/ss-mob/get-price/"
region               = "eu-central-1"
service_name         = "get-price"
stage                = "dev"
route_key            = "GET /get-price"

## Optional
dynamo-table-name = "product"
sys_params = {
  db_host = "product"
}

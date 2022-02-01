import config
from AzureManagement import service_principal, sql_management

print(config.SP_APP_ID)
print(config.SP_TENANT_ID)
print(config.SP_SECRET_ID)
sp = service_principal.ServicePrincipal(config.SP_APP_ID, config.SP_SECRET_ID, config.SP_TENANT_ID)
sql_config = sql_management.SqlConfigModel(config.RESOURCE_GROUP, config.LOCATION, config.SQL_SERVER, config.SQL_DB, config.SQL_USERNAME, config.SQL_PASSWORD)
sql_manager = sql_management.SqlManager(sql_config, sp.credentials, config.SUBSCRIPTION_ID)
sql_manager.create_db()



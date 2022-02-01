from azure.common.client_factory import get_client_from_cli_profile
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.sql import SqlManagementClient

class SqlConfigModel:
    
    def __init__(self, rg, location, server, database, username, password):
        self.rg = rg
        self.location = location
        self.server = server
        self.database = database
        self.username = username
        self.password = password



class SqlManager:

    def __init__(self, config, credentials, subscriptionId):
        self.config = config
        self.credentials = credentials
        self.subscriptionId = subscriptionId

    def create_db(self):
        sql_client = SqlManagementClient(self.credentials, self.subscriptionId)
        server = sql_client.servers.create_or_update(
            self.config.rg,
            self.config.server,
            {
                'location': self.config.location,
                'version': '12.0', # Required for create
                'administrator_login': self.config.username, # Required for create
                'administrator_login_password': self.config.password # Required for create
            }
        )

        # Create a SQL database in the Basic tier
        database = sql_client.databases.create_or_update(
            self.config.rg,
            self.config.server,
            self.config.database,
            {
                'location': self.config.location,
                # 'collation': 'SQL_Latin1_General_CP1_CI_AS',
                'create_mode': 'default',
                'requested_service_objective_name': 'S1'
            }
        )

# Open access to this server for IPs
# firewall_rule = sql_client.firewall_rules.create_or_update(
#     RESOURCE_GROUP,
#     SQL_DB,
#     "firewall_rule_name_123.123.123.123",
#     "123.123.123.123", # Start ip range
#     "167.220.0.235"  # End ip range
# )
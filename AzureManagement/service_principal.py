from azure.common.credentials import ServicePrincipalCredentials

class ServicePrincipal:
    def __init__(self, clientId, clientSecret, tenantId):
        self.credentials = ServicePrincipalCredentials(client_id=clientId, secret=clientSecret, tenant=tenantId)
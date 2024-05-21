from azure.storage.blob import BlobServiceClient
import os
from django.conf import settings
from django.utils.deprecation import MiddlewareMixin

class DynamicAllowedHostsMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response
        self.update_allowed_hosts()

    def __call__(self, request):
        self.update_allowed_hosts()
        response = self.get_response(request)
        return response

    def update_allowed_hosts(self):
        container_url = get_container_url()
        if container_url:
            domain = container_url.split("//")[-1].split("/")[0]
            if domain not in settings.ALLOWED_HOSTS:
                settings.ALLOWED_HOSTS.append(domain)

def get_container_url():
    try:
        account_name = os.getenv('AZURE_SECRET_NAME')
        account_key = os.getenv('AZURE_SECRET_KEY')
        container_name = os.getenv('AZURE_SECRET_CONTAINER')
        
        if not all([account_name, account_key, container_name]):
            raise ValueError("Les variables d'environnement AZURE_STORAGE_ACCOUNT_NAME, AZURE_STORAGE_ACCOUNT_KEY, et AZURE_STORAGE_CONTAINER_NAME doivent être définies.")

        blob_service_client = BlobServiceClient(account_url=f"https://{account_name}.blob.core.windows.net", credential=account_key)
        
        container_client = blob_service_client.get_container_client(container_name)
        container_url = container_client.url
        
        return container_url
    except Exception as e:
        print(f"Erreur lors de la récupération de l'URL du conteneur Azure: {e}")
        return None

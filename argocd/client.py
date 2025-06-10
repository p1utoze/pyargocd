from __future__ import print_function
import os
import argocd
from argocd.configuration import Configuration

def normalize_url(url: str, verify_ssl: bool) -> str:
    # If URL already starts with http:// or https://, return as is
    if url.startswith("http://") or url.startswith("https://"):
        return url

    # If URL is exactly "example.com", add the appropriate scheme
    scheme = "https://" if verify_ssl else "http://"
    return f"{scheme}{url}"

    # If URL is anything else, leave it unchanged
    return url
    
class ArgoCDClient:
    _instance = None
    api_client = None

    def __new__(cls):
        if cls._instance is None:
            config_params = {
                "verify_ssl": eval(os.environ.get('ARGOCD_VERIFY_SSL', None).capitalize()),
                "host": normalize_url(os.environ.get("ARGOCD_URL"), os.environ.get('ARGOCD_VERIFY_SSL', None)),
            }
            config = Configuration(**config_params)
            api_client = argocd.ApiClient(config)
            # Store reusable service instances
            cls._instance = super().__new__(cls)
            cls._instance.api_client = api_client
            cls._instance.api_client.set_default_header(
                "Authorization", f"Bearer {os.environ.get('ARGOCD_AUTH_TOKEN')}"
            )
            cls._instance.repos = argocd.RepositoryServiceApi(api_client)
            cls._instance.repo_creds = argocd.RepoCredsServiceApi(api_client)
            cls._instance.account = argocd.AccountServiceApi(api_client)
            cls._instance.applications = argocd.ApplicationServiceApi(api_client)
            cls._instance.application_sets = argocd.ApplicationSetServiceApi(api_client)
            cls._instance.projects = argocd.ProjectServiceApi(api_client)
            cls._instance.certificates = argocd.CertificateServiceApi(api_client)
            cls._instance.clusters = argocd.ClusterServiceApi(api_client)
            cls._instance.notifications = argocd.NotificationServiceApi(api_client)
        return cls._instance


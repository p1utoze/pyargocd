# argocd.RepoCredsServiceApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**repo_creds_service_create_repository_credentials**](RepoCredsServiceApi.md#repo_creds_service_create_repository_credentials) | **POST** /api/v1/repocreds | CreateRepositoryCredentials creates a new repository credential set
[**repo_creds_service_create_write_repository_credentials**](RepoCredsServiceApi.md#repo_creds_service_create_write_repository_credentials) | **POST** /api/v1/write-repocreds | CreateWriteRepositoryCredentials creates a new repository credential set with write access
[**repo_creds_service_delete_repository_credentials**](RepoCredsServiceApi.md#repo_creds_service_delete_repository_credentials) | **DELETE** /api/v1/repocreds/{url} | DeleteRepositoryCredentials deletes a repository credential set from the configuration
[**repo_creds_service_delete_write_repository_credentials**](RepoCredsServiceApi.md#repo_creds_service_delete_write_repository_credentials) | **DELETE** /api/v1/write-repocreds/{url} | DeleteWriteRepositoryCredentials deletes a repository credential set with write access from the configuration
[**repo_creds_service_list_repository_credentials**](RepoCredsServiceApi.md#repo_creds_service_list_repository_credentials) | **GET** /api/v1/repocreds | ListRepositoryCredentials gets a list of all configured repository credential sets
[**repo_creds_service_list_write_repository_credentials**](RepoCredsServiceApi.md#repo_creds_service_list_write_repository_credentials) | **GET** /api/v1/write-repocreds | ListWriteRepositoryCredentials gets a list of all configured repository credential sets that have write access
[**repo_creds_service_update_repository_credentials**](RepoCredsServiceApi.md#repo_creds_service_update_repository_credentials) | **PUT** /api/v1/repocreds/{creds.url} | UpdateRepositoryCredentials updates a repository credential set
[**repo_creds_service_update_write_repository_credentials**](RepoCredsServiceApi.md#repo_creds_service_update_write_repository_credentials) | **PUT** /api/v1/write-repocreds/{creds.url} | UpdateWriteRepositoryCredentials updates a repository credential set with write access


# **repo_creds_service_create_repository_credentials**
> V1alpha1RepoCreds repo_creds_service_create_repository_credentials(body, upsert=upsert)

CreateRepositoryCredentials creates a new repository credential set

### Example
```python
from __future__ import print_function
import time
import argocd
from argocd.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = argocd.RepoCredsServiceApi()
body = argocd.V1alpha1RepoCreds() # V1alpha1RepoCreds | Repository definition
upsert = true # bool | Whether to create in upsert mode. (optional)

try:
    # CreateRepositoryCredentials creates a new repository credential set
    api_response = api_instance.repo_creds_service_create_repository_credentials(body, upsert=upsert)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepoCredsServiceApi->repo_creds_service_create_repository_credentials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1alpha1RepoCreds**](V1alpha1RepoCreds.md)| Repository definition | 
 **upsert** | **bool**| Whether to create in upsert mode. | [optional] 

### Return type

[**V1alpha1RepoCreds**](V1alpha1RepoCreds.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_creds_service_create_write_repository_credentials**
> V1alpha1RepoCreds repo_creds_service_create_write_repository_credentials(body, upsert=upsert)

CreateWriteRepositoryCredentials creates a new repository credential set with write access

### Example
```python
from __future__ import print_function
import time
import argocd
from argocd.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = argocd.RepoCredsServiceApi()
body = argocd.V1alpha1RepoCreds() # V1alpha1RepoCreds | Repository definition
upsert = true # bool | Whether to create in upsert mode. (optional)

try:
    # CreateWriteRepositoryCredentials creates a new repository credential set with write access
    api_response = api_instance.repo_creds_service_create_write_repository_credentials(body, upsert=upsert)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepoCredsServiceApi->repo_creds_service_create_write_repository_credentials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1alpha1RepoCreds**](V1alpha1RepoCreds.md)| Repository definition | 
 **upsert** | **bool**| Whether to create in upsert mode. | [optional] 

### Return type

[**V1alpha1RepoCreds**](V1alpha1RepoCreds.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_creds_service_delete_repository_credentials**
> RepocredsRepoCredsResponse repo_creds_service_delete_repository_credentials(url)

DeleteRepositoryCredentials deletes a repository credential set from the configuration

### Example
```python
from __future__ import print_function
import time
import argocd
from argocd.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = argocd.RepoCredsServiceApi()
url = 'url_example' # str | 

try:
    # DeleteRepositoryCredentials deletes a repository credential set from the configuration
    api_response = api_instance.repo_creds_service_delete_repository_credentials(url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepoCredsServiceApi->repo_creds_service_delete_repository_credentials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | **str**|  | 

### Return type

[**RepocredsRepoCredsResponse**](RepocredsRepoCredsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_creds_service_delete_write_repository_credentials**
> RepocredsRepoCredsResponse repo_creds_service_delete_write_repository_credentials(url)

DeleteWriteRepositoryCredentials deletes a repository credential set with write access from the configuration

### Example
```python
from __future__ import print_function
import time
import argocd
from argocd.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = argocd.RepoCredsServiceApi()
url = 'url_example' # str | 

try:
    # DeleteWriteRepositoryCredentials deletes a repository credential set with write access from the configuration
    api_response = api_instance.repo_creds_service_delete_write_repository_credentials(url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepoCredsServiceApi->repo_creds_service_delete_write_repository_credentials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | **str**|  | 

### Return type

[**RepocredsRepoCredsResponse**](RepocredsRepoCredsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_creds_service_list_repository_credentials**
> V1alpha1RepoCredsList repo_creds_service_list_repository_credentials(url=url)

ListRepositoryCredentials gets a list of all configured repository credential sets

### Example
```python
from __future__ import print_function
import time
import argocd
from argocd.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = argocd.RepoCredsServiceApi()
url = 'url_example' # str | Repo URL for query. (optional)

try:
    # ListRepositoryCredentials gets a list of all configured repository credential sets
    api_response = api_instance.repo_creds_service_list_repository_credentials(url=url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepoCredsServiceApi->repo_creds_service_list_repository_credentials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | **str**| Repo URL for query. | [optional] 

### Return type

[**V1alpha1RepoCredsList**](V1alpha1RepoCredsList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_creds_service_list_write_repository_credentials**
> V1alpha1RepoCredsList repo_creds_service_list_write_repository_credentials(url=url)

ListWriteRepositoryCredentials gets a list of all configured repository credential sets that have write access

### Example
```python
from __future__ import print_function
import time
import argocd
from argocd.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = argocd.RepoCredsServiceApi()
url = 'url_example' # str | Repo URL for query. (optional)

try:
    # ListWriteRepositoryCredentials gets a list of all configured repository credential sets that have write access
    api_response = api_instance.repo_creds_service_list_write_repository_credentials(url=url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepoCredsServiceApi->repo_creds_service_list_write_repository_credentials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | **str**| Repo URL for query. | [optional] 

### Return type

[**V1alpha1RepoCredsList**](V1alpha1RepoCredsList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_creds_service_update_repository_credentials**
> V1alpha1RepoCreds repo_creds_service_update_repository_credentials(creds_url, body)

UpdateRepositoryCredentials updates a repository credential set

### Example
```python
from __future__ import print_function
import time
import argocd
from argocd.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = argocd.RepoCredsServiceApi()
creds_url = 'creds_url_example' # str | URL is the URL to which these credentials match
body = argocd.V1alpha1RepoCreds() # V1alpha1RepoCreds | 

try:
    # UpdateRepositoryCredentials updates a repository credential set
    api_response = api_instance.repo_creds_service_update_repository_credentials(creds_url, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepoCredsServiceApi->repo_creds_service_update_repository_credentials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **creds_url** | **str**| URL is the URL to which these credentials match | 
 **body** | [**V1alpha1RepoCreds**](V1alpha1RepoCreds.md)|  | 

### Return type

[**V1alpha1RepoCreds**](V1alpha1RepoCreds.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_creds_service_update_write_repository_credentials**
> V1alpha1RepoCreds repo_creds_service_update_write_repository_credentials(creds_url, body)

UpdateWriteRepositoryCredentials updates a repository credential set with write access

### Example
```python
from __future__ import print_function
import time
import argocd
from argocd.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = argocd.RepoCredsServiceApi()
creds_url = 'creds_url_example' # str | URL is the URL to which these credentials match
body = argocd.V1alpha1RepoCreds() # V1alpha1RepoCreds | 

try:
    # UpdateWriteRepositoryCredentials updates a repository credential set with write access
    api_response = api_instance.repo_creds_service_update_write_repository_credentials(creds_url, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepoCredsServiceApi->repo_creds_service_update_write_repository_credentials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **creds_url** | **str**| URL is the URL to which these credentials match | 
 **body** | [**V1alpha1RepoCreds**](V1alpha1RepoCreds.md)|  | 

### Return type

[**V1alpha1RepoCreds**](V1alpha1RepoCreds.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


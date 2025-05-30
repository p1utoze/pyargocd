# V1alpha1PullRequestGeneratorBitbucketServer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api** | **str** | The Bitbucket REST API URL to talk to e.g. https://bitbucket.org/rest Required. | [optional] 
**basic_auth** | [**V1alpha1BasicAuthBitbucketServer**](V1alpha1BasicAuthBitbucketServer.md) |  | [optional] 
**bearer_token** | [**V1alpha1BearerTokenBitbucket**](V1alpha1BearerTokenBitbucket.md) |  | [optional] 
**ca_ref** | [**V1alpha1ConfigMapKeyRef**](V1alpha1ConfigMapKeyRef.md) |  | [optional] 
**insecure** | **bool** |  | [optional] 
**project** | **str** | Project to scan. Required. | [optional] 
**repo** | **str** | Repo name to scan. Required. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



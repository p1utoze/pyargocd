# V1alpha1ApplicationSourceHelm

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_versions** | **list[str]** | APIVersions specifies the Kubernetes resource API versions to pass to Helm when templating manifests. By default, Argo CD uses the API versions of the target cluster. The format is [group/]version/kind. | [optional] 
**file_parameters** | [**list[V1alpha1HelmFileParameter]**](V1alpha1HelmFileParameter.md) |  | [optional] 
**ignore_missing_value_files** | **bool** |  | [optional] 
**kube_version** | **str** | KubeVersion specifies the Kubernetes API version to pass to Helm when templating manifests. By default, Argo CD uses the Kubernetes version of the target cluster. | [optional] 
**namespace** | **str** | Namespace is an optional namespace to template with. If left empty, defaults to the app&#39;s destination namespace. | [optional] 
**parameters** | [**list[V1alpha1HelmParameter]**](V1alpha1HelmParameter.md) |  | [optional] 
**pass_credentials** | **bool** |  | [optional] 
**release_name** | **str** |  | [optional] 
**skip_crds** | **bool** |  | [optional] 
**skip_schema_validation** | **bool** |  | [optional] 
**skip_tests** | **bool** | SkipTests skips test manifest installation step (Helm&#39;s --skip-tests). | [optional] 
**value_files** | **list[str]** |  | [optional] 
**values** | **str** |  | [optional] 
**values_object** | [**RuntimeRawExtension**](RuntimeRawExtension.md) |  | [optional] 
**version** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



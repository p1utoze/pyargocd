# V1alpha1ApplicationSourceKustomize

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_versions** | **list[str]** | APIVersions specifies the Kubernetes resource API versions to pass to Helm when templating manifests. By default, Argo CD uses the API versions of the target cluster. The format is [group/]version/kind. | [optional] 
**common_annotations** | **dict(str, str)** |  | [optional] 
**common_annotations_envsubst** | **bool** |  | [optional] 
**common_labels** | **dict(str, str)** |  | [optional] 
**components** | **list[str]** |  | [optional] 
**force_common_annotations** | **bool** |  | [optional] 
**force_common_labels** | **bool** |  | [optional] 
**images** | **list[str]** |  | [optional] 
**kube_version** | **str** | KubeVersion specifies the Kubernetes API version to pass to Helm when templating manifests. By default, Argo CD uses the Kubernetes version of the target cluster. | [optional] 
**label_without_selector** | **bool** |  | [optional] 
**name_prefix** | **str** |  | [optional] 
**name_suffix** | **str** |  | [optional] 
**namespace** | **str** |  | [optional] 
**patches** | [**list[V1alpha1KustomizePatch]**](V1alpha1KustomizePatch.md) |  | [optional] 
**replicas** | [**list[V1alpha1KustomizeReplica]**](V1alpha1KustomizeReplica.md) |  | [optional] 
**version** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



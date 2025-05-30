# V1alpha1ApplicationStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**list[V1alpha1ApplicationCondition]**](V1alpha1ApplicationCondition.md) |  | [optional] 
**controller_namespace** | **str** |  | [optional] 
**health** | [**V1alpha1HealthStatus**](V1alpha1HealthStatus.md) |  | [optional] 
**history** | [**list[V1alpha1RevisionHistory]**](V1alpha1RevisionHistory.md) |  | [optional] 
**observed_at** | [**V1Time**](V1Time.md) |  | [optional] 
**operation_state** | [**V1alpha1OperationState**](V1alpha1OperationState.md) |  | [optional] 
**reconciled_at** | [**V1Time**](V1Time.md) |  | [optional] 
**resource_health_source** | **str** |  | [optional] 
**resources** | [**list[Applicationv1alpha1ResourceStatus]**](Applicationv1alpha1ResourceStatus.md) |  | [optional] 
**source_hydrator** | [**V1alpha1SourceHydratorStatus**](V1alpha1SourceHydratorStatus.md) |  | [optional] 
**source_type** | **str** |  | [optional] 
**source_types** | **list[str]** |  | [optional] 
**summary** | [**V1alpha1ApplicationSummary**](V1alpha1ApplicationSummary.md) |  | [optional] 
**sync** | [**V1alpha1SyncStatus**](V1alpha1SyncStatus.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



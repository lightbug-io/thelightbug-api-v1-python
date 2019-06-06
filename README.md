# lb_tracking_api
API for retrieving tracking data and changing settings on LightBug & RemoteThings tracking devices

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.1.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage

Import the package:
```python
import lb_tracking_api 
```

## Getting Started

```python
from __future__ import print_function
import time
import lb_tracking_api
from lb_tracking_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lb_tracking_api.DeviceApi(lb_tracking_api.ApiClient(configuration))
id = 'id_example' # str | Model id
filter = 'filter_example' # str | Filter defining fields and include - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try:
    # Find a model instance by {{id}} from the data source.
    api_response = api_instance.device_find_by_id(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceApi->device_find_by_id: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://cp.remotethings.co.uk/api*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DeviceApi* | [**device_find_by_id**](docs/DeviceApi.md#device_find_by_id) | **GET** /devices/{id} | Find a model instance by {{id}} from the data source.
*DeviceApi* | [**device_prototype_create_notification_triggers**](docs/DeviceApi.md#device_prototype_create_notification_triggers) | **POST** /devices/{id}/notificationTriggers | Create alert/notification trigger for device
*DeviceApi* | [**device_prototype_delete_notification_triggers**](docs/DeviceApi.md#device_prototype_delete_notification_triggers) | **DELETE** /devices/{id}/notificationTriggers | Remove all alert/notification trigger for device
*DeviceApi* | [**device_prototype_destroy_by_id_points**](docs/DeviceApi.md#device_prototype_destroy_by_id_points) | **DELETE** /devices/{id}/points/{fk} | Delete a specific point for a device
*DeviceApi* | [**device_prototype_find_by_id_points**](docs/DeviceApi.md#device_prototype_find_by_id_points) | **GET** /devices/{id}/points/{fk} | Retrieve a specific point for a device
*DeviceApi* | [**device_prototype_find_by_id_readings**](docs/DeviceApi.md#device_prototype_find_by_id_readings) | **GET** /devices/{id}/readings/{fk} | Retrieve a specific reading for a device
*DeviceApi* | [**device_prototype_flight_mode**](docs/DeviceApi.md#device_prototype_flight_mode) | **GET** /devices/{id}/flightMode | 
*DeviceApi* | [**device_prototype_get_config**](docs/DeviceApi.md#device_prototype_get_config) | **GET** /devices/{id}/config | Retrieve configuration for a device
*DeviceApi* | [**device_prototype_get_notification_triggers**](docs/DeviceApi.md#device_prototype_get_notification_triggers) | **GET** /devices/{id}/notificationTriggers | Get alerts for device
*DeviceApi* | [**device_prototype_get_points**](docs/DeviceApi.md#device_prototype_get_points) | **GET** /devices/{id}/points | Retrieve points for a device
*DeviceApi* | [**device_prototype_get_readings**](docs/DeviceApi.md#device_prototype_get_readings) | **GET** /devices/{id}/readings | Retrieve readings for a device
*DeviceApi* | [**device_prototype_get_safe_zone**](docs/DeviceApi.md#device_prototype_get_safe_zone) | **GET** /devices/{id}/getSafeZone | Get safe-zone for device
*DeviceApi* | [**device_prototype_set_safe_zone**](docs/DeviceApi.md#device_prototype_set_safe_zone) | **POST** /devices/{id}/setSafeZone | Update safe-zone for device
*DeviceApi* | [**device_prototype_sleep**](docs/DeviceApi.md#device_prototype_sleep) | **GET** /devices/{id}/sleep | Send sleep instruction to device
*DeviceApi* | [**device_prototype_update_config**](docs/DeviceApi.md#device_prototype_update_config) | **PUT** /devices/{id}/config | Update configuration for a device
*DeviceApi* | [**device_prototype_wake_up**](docs/DeviceApi.md#device_prototype_wake_up) | **GET** /devices/{id}/wakeUp | Send wake instruction to device
*UserApi* | [**user_login**](docs/UserApi.md#user_login) | **POST** /users/login | Login a user with username/email and password.
*UserApi* | [**user_prototype_create_geofences**](docs/UserApi.md#user_prototype_create_geofences) | **POST** /users/{id}/geofences | Creates a new instance in geofences of this model.
*UserApi* | [**user_prototype_delete_geofences**](docs/UserApi.md#user_prototype_delete_geofences) | **DELETE** /users/{id}/geofences | Deletes all geofences of this model.
*UserApi* | [**user_prototype_destroy_by_id_geofences**](docs/UserApi.md#user_prototype_destroy_by_id_geofences) | **DELETE** /users/{id}/geofences/{fk} | Delete a related item by id for geofences.
*UserApi* | [**user_prototype_find_by_id_geofences**](docs/UserApi.md#user_prototype_find_by_id_geofences) | **GET** /users/{id}/geofences/{fk} | Find a related item by id for geofences.
*UserApi* | [**user_prototype_get_devices**](docs/UserApi.md#user_prototype_get_devices) | **GET** /users/{id}/devices | Queries devices of user.
*UserApi* | [**user_prototype_get_geofences**](docs/UserApi.md#user_prototype_get_geofences) | **GET** /users/{id}/geofences | Queries geofences of user.
*UserApi* | [**user_prototype_get_mqtt_credentials**](docs/UserApi.md#user_prototype_get_mqtt_credentials) | **GET** /users/{id}/getMqttCredentials | 
*UserApi* | [**user_prototype_update_by_id_geofences**](docs/UserApi.md#user_prototype_update_by_id_geofences) | **PUT** /users/{id}/geofences/{fk} | Update a related item by id for geofences.


## Documentation For Models

 - [AccessToken](docs/AccessToken.md)
 - [Credentials](docs/Credentials.md)
 - [Datapoint](docs/Datapoint.md)
 - [Device](docs/Device.md)
 - [DeviceConfig](docs/DeviceConfig.md)
 - [GeoPoint](docs/GeoPoint.md)
 - [Geofence](docs/Geofence.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [NotificationTrigger](docs/NotificationTrigger.md)
 - [SensorReading](docs/SensorReading.md)


## Documentation For Authorization

 All endpoints do not require authorization.


## Author




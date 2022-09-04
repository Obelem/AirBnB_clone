# AirBnB Clone - The Console

``` 
# Data model
# Object management via a console/command interpreter
# Conversion to a file(JSON file)
```

## Language: Python

## Project Description :house:

To create a sandboxed command line interface through which we can create, modify and delete objects in our file storage. This project currently only implements the back-end console. It is a complete web application, integrates database storage and front-end interfacing in a clone of AirBnB.

## Classes :cl:

AirBnB utilizes the following classes:

|      | BaseModel | FileStorage | User | State | City | Amenity | Place | Review |
| --- | --------- | ----------- | ---- | ----- | ---- | ------- | ----- | ------ |
| **PUBLIC INSTANCE ATTRIBUTES** | `id`<br>`created_at`<br>`updated_at` | | Inherits from `BaseModel` | Inherits from `BaseModel` | Inherits from `BaseModel` | Inherits from `BaseModel` | Inherits from `BaseModel` | Inherits from `BaseModel` |
| **PUBLIC INSTANCE METHODS** | `save`<br>`to_dict` | `all`<br>`new`<br>`save`<br>`reload` | "" | "" | "" | "" | "" | "" |
| **PUBLIC INSTANCE METHODS** | | | `email`br`password`<br>`first_name`<br>`last_name`| `name` | `state_id`<br>`name` | `name` | `city_id`<br>`user_id`br`name`<br>`description`<br>`number_bathrooms`<br>`price_by_night`<br>`latitude`<br>	`longitude`<br>`amenity_ids` | `place_id`<br>`user_id`<br>`text` |
| **PRIVATE CLASS ATTRIBUTES** | | `file_path`<br>`objects` | | | | | | |

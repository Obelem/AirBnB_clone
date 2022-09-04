# AirBnB Clone - The Console

* Data model
* Object management via a console/command interpreter
* Conversion to a file(JSON file)

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

## Storage :baggage_claim:

The above classes are handled by the abstracted storage engine defined in the [FileStorage](./models/engine/file_storage.py) class.

Every time the backend is initialized, AirBnB instantiates an instance of `FileStorage` called `Storage`. The `storage` object is loaded/re-loaded from any class instances stored in the JSON file `file.json`. As class instances are created, updated, or deleted, the `storage` object is used to register corresponding chnages in the `file.json`.

## Console :computer:

The console is a command line interpreter that permits management of the backend 
of HolbertonBnB. It can be used to handle and manipulate all classes utilized by 
the application (achieved by calls on the `storage` object defined above).

The console is a command line interpreter that permits management of the backend 
of HolbertonBnB. It can be used to handle and manipulate all classes utilized by 
the application (achieved by calls on the `storage` object defined above).

(hbnb) 
$
```

Alternatively, to use the HolbertonBnB console in interactive mode, run the 
file `console.py` by itself:

```
$ ./console.py
```

While running in interactive mode, the console displays a prompt for input:

```
$ ./console.py
(hbnb) 
```

To quit the console, enter the command `quit`, or input an EOF signal 
(`ctrl-D`).

```
$ ./console.py
(hbnb) quit
$
```

```
$ ./console.py
(hbnb) EOF
$
```

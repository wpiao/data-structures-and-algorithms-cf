# Hash Table Implementation - 03/12/2022

## Challenges

No challenges

## API

- hash

  - Arguments: key
  - Returns: Index in the buckets for that key

- add

  - Arguments: key, value
  - Returns: nothing
  - This method should hash the key, and set the key and value pair in the table, handling collisions as needed.
  - Should a given key already exist, replace its value from the value argument given to this method.

- get

  - Arguments: key
  - Returns: Value associated with that key in the table

- contains

  - Arguments: key
  - Returns: Boolean, indicating if the key exists in the table already.

- keys
  - Returns: Collection of keys

## Unit tests

Run command `pytest tests/test_hashtable.py` to run the unit tests

# minasu-db
minasu-db - a versioned, simple key/value database

## Rationale
The primary (initial) purpose of this database will be to power an central inventory for servers, vm's, networking equipment etc. for a company.  There are specific things that will seem overly simple or even a "bad" choice.  These are on purpose.  See [Architecture](#Architecture)

## Architecture
The lowest level of the db is simple yaml files within a directory structure.  

Keywords: 
* instance: an instance of minasu-db running on a specific port
* bucket: a bucket containing any number of items (think a separate database which contains tables in sql)
* item: a primary key (think table in sql)

The instance is the top level directory that a minasu-db session is instantiated with.  
Within this directory, one or more buckets live, which are also themselves merely directories.
Within each bucket, one or more items, which are yaml files with the key name corresponding to the filename. 

### Versioning
Since all real data is in fact in directories and yaml files, it can easily be "diffed" and reverted.  Internally, minasu-db uses git to track changes. 

Keywords: 
* transaction: corresponds to a new branch that will contain one or more commits
* commit: corresponds to a git commit which will contain one or more edits to a single "item" (i.e. yaml file)
* master: corresponds to the master branch (defaults to master but can be changed, e.g. "devel")


## Plugins
FILL ME OUT

### bovine-inventory plugin
FILL ME OUT

## Getting Started
Let's do a brief walkthrough from the repl:
```python
>>> instance = db(instance_name="test_instance",instance_dir="/tmp/tests")
```

```python
>>> dir(instance)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'data', 'destroy', 'instance_dir', 'instance_name', 'instance_path', 'load', 'lock', 'unload']
```

```python
>>> instance.instance_path
'/tmp/tests/test_instance'
```

```python
>>> instance.load()
{'instance_name': 'test_instance', 'instance_dir': '/tmp/tests/', 'instance_path': '/tmp/tests/test_instance/'}
```

```python
>>> instance.destroy()
{'destroyed': True}

```

## About
This chapter is about the Map abstract data type (ADT). A Map ADT has the following five properties or behaviours:

* `M[k]`: Return the value v associated with key k in map M, if one exists; otherwise raise a ```KeyError```. In Python, this is implemented with the special method ```__getitem__``` .

* ```M[k] = v```: Associate value `v` with key `k` in map `M`, replacing the existing value if the map already contains an item with key equal to `k`. In Python, this is implemented with the special method `__setitem__` .


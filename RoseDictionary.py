class RoseDictionary:
    def __init__(self):
        self.items = []

    def __setitem__(self, key, value):
        self.add_item(key, value)

    def __getitem__(self, key):
        return self.get_value(key)

    def __delitem__(self, key):
        self.remove_item(key)

    def add_item(self, key, value):
        self.items.append((key, value))

    def get_value(self, key):
        for k, v in self.items:
            if k == key:
                return v
        return None

    def remove_item(self, key):
        self.items = [(k, v) for k, v in self.items if k != key]

    def pop_item(self, raise_error=None, error_msg= None, default=None):
        if self.items:
            key, value = self.items.pop()
            return value
        elif raise_error and len(self.items) == 0:
            if error_msg == None:
                raise KeyError('error_msg')
            else:
                raise KeyError(error_msg)
        elif default == None and error_msg != None:
            print(error_msg)
        else:
            print('Dictionary was empty and no default value/message was specified.')

    def get_item(self, key, raise_error=None, error_msg=None, default=None):
        value = self.get_value(key)
        if value is not None:
            return value
        elif raise_error:
            if error_msg == None:
                raise KeyError('error_msg')
            else:
                raise KeyError(error_msg)
        elif default == None and error_msg != None:
            print(error_msg)
        else:
            if default == None:
                print('Value was not found and no default value/message was specified.')
            else:
                print(default)
d = RoseDictionary()
d["key1"] = "value1"
d["key2"] = "value2"
print(d["key1"])
print(d.get_item("key1"))
print(d.get_item("key3", default = "Default Value"))
d.get_item("key3")
print(d.pop_item())
print(d.get_item("key1", error_msg = "error message"))
print(d.get_item("key2", error_msg = "error message2"))
d.pop_item()
d.get_item("key3", default = "Default Value", raise_error = True, error_msg = "Hi")

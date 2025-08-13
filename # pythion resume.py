# pythion resume

# data types using a dictionary:

resume= {
    "text": "Python Resume",
    "numeric": ["int", "float", "complex"],
    "sequence" : ["list", "tuple", "range"],
    "mapping" : "dict",
    "set" : ["set", "Frozenset"],
    "boolean" : ["True", "False"],
    "binary" : ["bytes", "bytearray", "memoryview"],
    "none": "NoneType"
}

# print the resume
for key, value in resume.items():
    if isinstance(value, list):
        print(f"{key.capitalize()}: {', '.join(value)}")
    else:
        print(f"{key.capitalize()}: {value}")

import urllib.request, json, sys
with urllib.request.urlopen("http://10.47.1.55/debug/845455/serviceability?sources=560002&day=28&month=06") as url:
    data = json.loads(url.read().decode())
    def func(data):
        for key,value in data.items():
            print(key + ',')
            if type(value) == type(dict()) and str(key) == "sizesServiceability":
                print(str(value))
                for key1,value1 in value.items():
                    if type(value1) == type(dict()) and str(key1) == "promise":
                        print(str(value1))
            elif type(value) == type(dict()) and str(key) == "serviceTypesServiceability":
                print(str(value))
            elif type(value) == type(dict()) and str(key) == "categoriesServiceability":
                print(str(value))
            elif type(value) == type(dict()) and str(key) == "paymentModeServiceability":
                print(str(value))
            elif type(value) == type(dict()) and str(key) == "cutOffToHHmmss":
                print(str(value))
            elif type(value) == float:
                print(float(value))
                break
            elif type(value) is list and str(key) == "cutOffToHHmmss":
                print(list(value))
            else:
                func(value)
func(data)
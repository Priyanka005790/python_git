import json

from bs4 import BeautifulSoup
import pandas
import xmltodict
import pprint
class Base:
    def __init__(self):
        self.data = open("xmlimagedetails.xml")
        bs = BeautifulSoup(self.data, 'xml')
        print(bs)

    def xmltodictionary(self):
        with open("xmlimagedetails.xml","r") as file:
            d_data=file.read()
        dict_data=xmltodict.parse(d_data)
        print("=======xml to dictionary=========")
        pprint.pprint(dict_data,indent=4)



class Derived(Base):
    def __init__(self):
        print("=======using Beautiful Soup=========")
        super(Derived,self).__init__()
        print("=======using pandas=========")
        data=pandas.read_xml("xmlimagedetails.xml")
        print(data)

    def xmltojson(self):
        with open("xmlimagedetails.xml","r") as file:
            data=file.read()
        d_dict=xmltodict.parse(data)
        j_data=json.dumps(d_dict)
        with open("imgxmldata.json","w") as file:
            file.write(j_data)

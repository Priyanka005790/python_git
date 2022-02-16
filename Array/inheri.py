import json
class Base:
    def openfile(self):
        self.fname=open("data1.json", "r+")
        #self.data = json.load(self.fname)
        #print(self.data)
class Derived(Base):
    def read(self):
        self.data = json.load(self.fname)
        print(self.data)
    def write(self,content):
        self.data["employee"].append(content)
        self.fname.seek(0)
        json.dump(self.data,self.fname,indent=4)
        # print(self.data)

content={
    "id":7,
    "name":"ramu",
    "department":"Tester"
}
d=Derived()
d.openfile()
d.read()
d.write(content)
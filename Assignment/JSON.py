import json

class Base:
    def __init__(self):
        self.file=open("imgdetails.json")
        data=json.load(self.file)
        print(data)

    def openfile(self):
        self.wfile=open("imgdetails.json","r+")

class Derived(Base):
    def __init__(self):
        super(Derived, self).__init__()

    def writefile(self,data):
        content=json.load(self.wfile)
        content["images_details"].append(data)
        self.wfile.seek(0)
        json.dump(content,self.wfile,indent=4)

data={
      "file_name": "animal",
      "file_size": "500MB",
      "img_res": "100px",
      "img_name": "tiger",
      "no_of_obj": "12",
      "obj_res": "250px"
    }
d=Derived()
d.openfile()
d.writefile(data)
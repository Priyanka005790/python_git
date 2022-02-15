import csv

class Base:
    def readcsv(self):
        with open("imageswrite.csv","r") as file:
            data=csv.reader(file,delimiter=' ')
            for i in data:
                print(''.join(i))
class Derived(Base):
    def writedata(self):
        with open("imageswrite.csv","w",newline='') as file:
            writer=csv.writer(file)
            writer.writerow(["laptop","240MB","100px","DELL","10","100px"])

    def writemultidata(self,list):
        with open("imageswrite.csv","a",newline='') as file:
            writer=csv.writer(file)
            writer.writerows(list)

d=Derived()
print("===========data before write==============")
d.readcsv()
print("===========data after write(single)==============")
d.writedata()
d.readcsv()
print("===========data after write(multiple)==============")
list=[["laptop","140MB","200px","lenovo","09","100px"],["flower","240MB","100px","rose","10","100px"],["animal","540MB","500px","Dog","19","100px"]]
d.writemultidata(list)
d.readcsv()
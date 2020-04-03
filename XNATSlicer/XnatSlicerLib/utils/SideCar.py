import os
import json

class SideCar(object):
    def __init__(self, path):
        self.path = path
        self.fullPath = os.path.join(self.path, 'car.json')
        if(os.path.isfile(self.fullPath)):
            file = open(self.fullPath, 'r')
            self.car = json.load(file)
            if('SCANS' not in self.car and 'TYPE' not in self.car):
                self.car = {'TYPE': None, 'SCANS': {}}
            file.close()
        else:
            self.car = {'TYPE': None, 'SCANS': {}}
        self.numScans = 0
        self.numImages = 0


class NiftiCar(SideCar):
    def __init__(self, path):
        SideCar.__init__(self, path)
        self.car['TYPE'] = 'nifti'
        if not self.car['SCANS']:
            self.car['SCANS'] = {}

    def addFile(self, file, uri):
        carFile = open(self.fullPath,'w')
        if(file not in self.car['SCANS']):
            self.car['SCANS'][file] = uri
        json.dump(self.car, carFile)
        carFile.close()

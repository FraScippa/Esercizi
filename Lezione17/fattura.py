from dottore import Dottore
from paziente import Paziente

class Fattura:

    def __init__(self, patient: list[Paziente], doctor: Dottore):
        
        if self.doctor.isAValidDoctor() == True:
            self.doctor: Dottore = doctor
            self.patient: list[Paziente] = []
            self.fattura: int = len(patient)
            self.salary: int = 0
        else:
            self.doctor: Dottore = doctor
            self.patient: list[Paziente] = None
            self.fattura: int = None
            self.salary: int = None

    def getSalary(self):
        
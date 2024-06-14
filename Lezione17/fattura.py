from dottore import Dottore
from paziente import Paziente

class Fattura:

    def __init__(self, patient: list[Paziente], doctor: Dottore):
        
        if doctor.isAValidDoctor() == True:
            self.doctor: Dottore = doctor
            self.patient: list[Paziente] = patient
            self.fattura: int = len(patient)
            self.salary: int = 0
        else:
            self.doctor: Dottore = doctor
            self.patient: list[Paziente] = None # type: ignore
            self.fattura: int = None # type: ignore
            self.salary: int = None # type: ignore
            print("Non è possibile creare la classe fattura poichè il dottore non è valido!")

    def getSalary(self):
        if self.patient != None: # type: ignore
            salary: float = self.doctor.getParcel()*len(self.patient)
            return salary
        else:
            pass
        
    def getFatture(self):
        if self.patient != None: # type: ignore
            return len(self.patient)
        else: 
            pass
    
    def addPatient(self, newPatient: Paziente):
        if self.patient != None: # type: ignore
            self.patient.append(newPatient)
            print(f"Alla lista del Dottor {self.doctor.getLastname()} è stato aggiunto il paziente {newPatient.getIdCode()}")
        else:
            pass
        
    def removePatient(self, idCode: str):
        if self.patient != None: # type: ignore
            for p in self.patient:
                if idCode == p.getIdCode():
                    self.patient.remove(p)
                    print(f"Alla lista del Dottor {self.doctor.getLastname()} è stato rimosso il paziente {p.getIdCode()}")
        else: 
            pass
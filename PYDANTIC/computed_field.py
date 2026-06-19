from pydantic import BaseModel ,EmailStr, computed_field
from typing import List, Dict

class Patient(BaseModel):
    name:str
    email:EmailStr
    age:int 
    weight: float
    height: float
    married: bool =False
    allergies: list[str]
    contact_details: Dict[str,str]



    @computed_field
    @property
    def calculate_bmi(self) -> float:
        bmi=round(self.weight/(self.height**2),2)
        return bmi
    


def update_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print('BMI',patient.calculate_bmi)
    print('updated')


patient_info={'name':'nitish','email':'anchal@hdfc.com','age':'65','weight':75.2,'height':1.72,'allergies':['pollen','dust'],'contact_details':{'phone':'1234567890','emergency':'9876543210'}}


patient1 =Patient(**patient_info)  #yaha par validation perform hota hai ->type coersion 



update_patient_data(patient1)



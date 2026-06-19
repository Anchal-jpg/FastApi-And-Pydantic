from pydantic import BaseModel,EmailStr,AnyUrl, Field,model_validator
from typing import List,Optional,Annotated
from typing import Dict


#make an pydantic model where we define the schema

class Patient(BaseModel):
    name: str
    email: EmailStr
    linkedin_url: AnyUrl
    age: int 
    weight: float
    married:  bool=False 
    allergies: List[str]
    contact_details: Dict[str,str]

    @model_validator(mode='after') # by defalt it is after
    def validate_emergency_contect(cls, model):
        if model.age>60 and 'emergency' not in model.contact_details:
            raise ValueError('Emergency contact is required for patients above 60 years old')
        return model
    

def update_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print('updated')


patient_info={'name':'nitish','email':'anchal@hdfc.com','linkedin_url':'http://linkedin.com/257','age':'65','weight':75.2,'allergies':['pollen','dust'],'contact_details':{'phone':'1234567890','emergency':'9876543210'}}


patient1 =Patient(**patient_info)  #yaha par validation perform hota hai ->type coersion 



update_patient_data(patient1)



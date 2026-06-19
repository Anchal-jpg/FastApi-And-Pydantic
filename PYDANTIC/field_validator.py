from pydantic import BaseModel,EmailStr,AnyUrl, Field,field_validator
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

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        valid_domain =['hdfc.com','icici.com']
        #abc@gmail.om

        domain_name=value.split('@')[-1]

        if domain_name not in valid_domain:
            raise ValueError('Not a valid domain')
        return value
    
    #Field validator for the transformation

    
    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.upper()

    @field_validator('age',mode='after') # by defalt it is after
    @classmethod
    def validate_age(cls,value):
        if 0<value<100:
            return value
        else:
            return ValueError('Age should be between 0 to 100')

def update_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print('updated')


patient_info={'name':'nitish','email':'anchal@hdfc.com','linkedin_url':'http://linkedin.com/257','age':'30','weight':75.2,'allergies':['pollen','dust'],'contact_details':{'phone':'1234567890'}}


patient1 =Patient(**patient_info)  #yaha par validation perform hota hai ->type coersion 



update_patient_data(patient1)



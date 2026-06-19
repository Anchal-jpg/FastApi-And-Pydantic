# from pydantic import BaseModel



# #make an pydantic model where we define the schema

# class Patient(BaseModel):
#     name: str
#     age: int


# def insert_patient_data(patient:Patient):
#     print(patient.name)
#     print(patient.age)
#     print('inserted')
# def update_patient_data(patient:Patient):
#     print(patient.name)
#     print(patient.age)
#     print('updated')


# patient_info={'name':'nitish','age':30}
# patient_info2={'name':'nitish','age':'33'}
# #Here no error because pydantic will try to convert the string '33' to an integer 33, if it is possible. If the conversion is successful, it will not raise an error and will create a Patient instance with age set to 33. However, if the string cannot be converted to an integer (e.g., 'thirty-three'), then pydantic will raise a validation error.

# patient1 =Patient(**patient_info)
# patient2 =Patient(**patient_info2)

# insert_patient_data(patient1)
# update_patient_data(patient2)


from pydantic import BaseModel,EmailStr,AnyUrl, Field
from typing import List,Optional,Annotated
from typing import Dict


#make an pydantic model where we define the schema

class Patient(BaseModel):
    name: Annotated[str,Field(max_length=50,title='Nme of the patient',description='Give the name of the patient in less than 50 chars',examples=['Nitish','Amit'])]
    email: EmailStr
    linkedin_url: AnyUrl
    age: int =Field(gt=0 ,lt=120)
    weight: Annotated[float,Field(gt=0,strict=True)] #it means weight will be always positive
    married: Optional[bool]=False  #or we can write   married: bool = False
    allergies: List[str]
    contact_details: Dict[str,str]

def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print('inserted')
def update_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print('updated')


patient_info={'name':'nitish','email':'anchal@gmail.com','linkedin_url':'http://linkedin.com/257','age':30,'weight':75.2,'allergies':['pollen','dust'],'contact_details':{'phone':'1234567890'}}
# patient_info2={'name':'nitish','age':'33'}
#Here no error because pydantic will try to convert the string '33' to an integer 33, if it is possible. If the conversion is successful, it will not raise an error and will create a Patient instance with age set to 33. However, if the string cannot be converted to an integer (e.g., 'thirty-three'), then pydantic will raise a validation error.

patient1 =Patient(**patient_info)
# patient2 =Patient(**patient_info2)

insert_patient_data(patient1)
update_patient_data(patient1)



from pydantic import BaseModel
class Address(BaseModel):
    city:str
    state:str
    pin:str

class Patient(BaseModel):
    name:str
    gender: str='Male'
    age: int
    address: Address

address_dict = {'city':'delhi','state':'delhi','pin':'110001'}

address1=Address(**address_dict)

patient_dict={'name':'nitish','age':30,'address':address1}   
patient1=Patient(**patient_dict)

temp=patient1.model_dump(exclude_unset=True) #it will exclude the default values and only include the values that have been explicitly set in the model instance. It will not include the default values for fields that were not provided during initialization.
y=patient1.model_dump(include={'name','age'})
x=patient1.model_dump_json() #it will convert the model to json format

print(temp)
print(x)

print(type(temp))
print(type(x))

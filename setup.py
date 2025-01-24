'''
this setup.py file is an essential part of packaging and distributiong python projects.it is used by setuptools to degine the configuration of your project such as its metadata,depedencies and more
'''


from setuptools import find_packages,setup
from typing import List


HYPHEN_E_DOT="-e ."
def get_requirements(filepath:str)->List[str]:
    '''this function will return list of requirements'''
    requirements=[]
    with open(filepath) as file:
        requirements=file.readlines()
        requirements=[req.replace("\n","") for req in requirements]
    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)
        
    return requirements
setup(
    name="NetworkSecurity",
    version="0.0.0.1",
    author="Barash sharma",
    author_email="barash1311@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)


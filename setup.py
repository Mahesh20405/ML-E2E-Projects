from setuptools import find_packages,setup
from typing import List


HYP='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    To return the list of requirements
    '''

    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n"," ")for req in requirements]


        if HYP in requirements:
            requirements.remove(HYP)

    return requirements

setup(
name='ML',
version='0.0.1',
author='Mahesh',
author_email='maheshsekaran724@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')





)
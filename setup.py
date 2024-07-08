from setuptools import find_packages,setup
from typing import List

#HYPHEN_E_DOT = "-e ."

def get_requirements(file_path:str)->List[str]:
    '''
    this function returns the list of requirements
    '''
    requirements=[]
    with open(file_path, 'r') as f:
        requirements = f.read().splitlines()
        #requirements = [req.replace("\n","") for req in requirements]

        requirements = [req for req in requirements if not req.startswith('-e ') and req.strip() != '']

    return requirements
        
        #if HYPHEN_E_DOT in requirements:
         #   requirements.remove(HYPHEN_E_DOT)
    return requirements




setup(
    name='mlproject',
    version='0.0.1',
    author='Gopal',
    author_email='gopalkrishna.suresh@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)


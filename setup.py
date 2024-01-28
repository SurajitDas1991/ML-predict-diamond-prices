from setuptools import find_packages,setup
from typing import List
import setuptools

HYPEN_E_DOT='-e .'

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.1.0"

REPO_NAME = "Diamond-Price-Prediction"
AUTHOR_USER_NAME = "SurajitDas1991"
SRC_REPO = "src"
AUTHOR_EMAIL = "dsurajitd@gmail.com"

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

        return requirements


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    install_requires=get_requirements('requirements.txt'),
    description="ML model for diamond price prediction",
    long_description=long_description,
    #long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    #package_dir={"": "diamond_price_prediction"},
    packages=find_packages()
)

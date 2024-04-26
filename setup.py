import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__="0.0.0"

REPO_NAME = "MLFLOW_PROJECT"
AUTHOR_USER_NAME = "Mayu21ad"
SRC_REPO = "mlProject"
AUTHOR_EMAIL = "mayuri.21ad@kct.ac.in"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="python package for ml app",
    long_description=long_description,
    long_description_content_type="text/markdown",
   
)
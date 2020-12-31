from pathlib import Path
import re
from setuptools import setup, find_packages

here = Path(__file__).resolve().parent

# Read version from fastapi_csv/__init__.py
version_re = r"^__version__ = ['\"]([^'\"]*)['\"]"
init_text = (here / "fastapi_csv" / "__init__.py").read_text()
version = re.findall(version_re, init_text)[0]

# Read README.md.
readme = (here / "README.md").read_text()

setup(
    name="fastapi-csv",
    version=version,
    author="Johannes Rieke",
    author_email="johannes.rieke@gmail.com",
    description="Create APIs from CSV files within seconds, using fastapi",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/jrieke/fastapi-csv",
    license="MIT",
    python_requires=">=3.6",
    install_requires=["pandas", "uvicorn", "pydantic", "numpy", "fastapi", "typer",],
    entry_points={"console_scripts": ["fastapi-csv=fastapi_csv.cli:typer_app"],},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
    ],
)

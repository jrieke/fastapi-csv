from pathlib import Path
from setuptools import setup, find_packages

parent_dir = Path(__file__).resolve().parent

setup(
    name="fastapi-csv",
    version=parent_dir.joinpath("fastapi_csv/_version.txt").read_text(encoding="utf-8"),
    author="Johannes Rieke",
    author_email="johannes.rieke@gmail.com",
    description="Create APIs from CSV files within seconds, using fastapi",
    long_description=parent_dir.joinpath("README.md").read_text(),
    long_description_content_type="text/markdown",
    url="https://github.com/jrieke/fastapi-csv",
    license="MIT License",
    packages=find_packages(exclude=("tests", "docs", "examples")),
    package_data={"": ["_version.txt"]},
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.6",
    install_requires=["pandas", "uvicorn", "pydantic", "numpy", "fastapi", "typer",],
    entry_points={"console_scripts": ["fastapi-csv=fastapi_csv.cli:typer_app"],},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
    ],
)

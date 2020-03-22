import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cloud-alarm-notifier",
    version="0.0.1",
    url="https://www.github.com/MasterGberry/cloud-alarm-notifier",
    project_urls={
        "Documentation": "https://www.github.com/MasterGberry/cloud-alarm-notifier",
        "Code": "https://www.github.com/MasterGberry/cloud-alarm-notifier",
        "Issue tracker": "https://www.github.com/MasterGberry/cloud-alarm-notifier/issues",
    },
    license="MIT",
    author="Adam Ehrlich",
    author_email="adam@badlion.net",
    description="A small python utility to notify various endpoints of alarms in the cloud.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.5",
    install_requires=[
        
    ],
    extras_require={
        "aws-lambda": ["boto3==1.10.34", "botocore==1.13.34"]
    },
)
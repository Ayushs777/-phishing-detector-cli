from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="phishing-detector-cli",
    version="2.0.0",
    author="Ayush Chaudhary",
    author_email="ayush.chaudhary@example.com",
    description="Professional CLI tool for detecting phishing URLs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ayushchaudhary-it/phishing-detector-cli",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "requests>=2.25.1",
    ],
    entry_points={
        "console_scripts": [
            "phishdetect=src.phishdetect:main",
        ],
    },
)
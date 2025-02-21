from setuptools import setup, find_packages

setup(
    name="aicli",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "openai>=0.1.0",
        "prompt_toolkit>=3.0.0"
    ],
    entry_points={
        "console_scripts": [
            "aicli=aicli:main",
        ],
    },
    author="Bruno Roberti",
    author_email="bv_roberti@hotmail.com",
    description="A CLI tool powered by LLMs",
    url="https://github.com/broberti/aicli",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X"
    ],
    python_requires=">=3.8",
)

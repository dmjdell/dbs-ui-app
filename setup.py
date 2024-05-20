from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ui_app",  
    version="1.0.0", # Start with an initial version
    author="YOUR_NAME",
    author_email="dennisjohn@live.com",
    description="UI APP",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dmjdell/ui-app", # Your project's GitHub URL
    packages=find_packages(),  # Automatically find packages in your project
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Choose your license
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',   # Specify minimum Python version
    install_requires=[
         'Flask',
    ],
)

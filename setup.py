import re
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("PyPortForward/__main__.py", "r") as fh:
    version = re.search(r'__version__ = "(.*)"', fh.read()).group(1)

with open("requirements.txt", "r") as fh:
    install_requires = fh.read().splitlines()

setuptools.setup(
    name="PyPortForward",
    version=version,
    author="onTDB",
    author_email="github@ontdb.com",
    description="A simple port forward client and manager written in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/onTDB/PyPortForward",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'ppf = PyPortForward.__main__:main',
        ],
    },
)

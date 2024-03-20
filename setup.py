import pathlib

from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

setup(
    name="nrdtech_utils",
    version="0.0.1",
    description="A library of helpful wrappers around low level built-in python functions",
    long_description=(HERE / "README.md").read_text(),
    long_description_content_type="text/markdown",
    license="Apache License 2.0",
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Operating System :: OS Independent',
    ],
    author="Nic Delorme",
    author_email="nic.delorme@nrdtech.io",
    url="",
    install_requires=[],
    extras_require={
        'test': [
            'pytest',
            'pytest-cov',
        ],
    },
    packages=find_packages(exclude=["tests", "unit_tests", "integration_tests"]),
    python_requires=">=3.10",
)

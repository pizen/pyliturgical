import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyliturgical",
    version="1.0.0",
    author="Ian Turner",
    author_email="ian@pizen.io",
    description="Package for generating liturgial information for a date",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pizen/pyliturgical",
    packages=['pyliturgical'],
    setup_requires=[
        'pytest-runner'
    ],
    install_requires=[
        'python-dateutil'
    ],
    tests_require=[
        'pytest'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Religion"
    ],
)

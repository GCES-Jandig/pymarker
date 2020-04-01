import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pymarker",
    version="0.0.1",
    author="Pablo Silva",
    author_email="pablodiegoss@hotmail.com",
    description="A python package to generate AR markers and patterns based on input images",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords='AR pattern markers jandig hiro',
    url="https://github.com/pablodiegoss/pymarker",
    packages=setuptools.find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)

from setuptools import setup, find_packages

setup(
    name='TinyModels',
    version='0.1.0',  # Use semantic versioning
    packages=find_packages(),
    license='MIT',  # Or your chosen license
    description='A PDF processing library for RAG.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Juan Olano',
    author_email='juan_olano@yahoo.com',
    url='https://github.com/jcolano/TinyModels',  # Optional
    install_requires=[
        'requests',  # Example dependency, add others as needed
    ],
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.org/classifiers/
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Specify compatible Python versions
)

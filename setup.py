from setuptools import setup, find_packages

setup(
    name='myapp',
    version='1.0',
    description="Website",
    author='Sean Wall',
    author_email='sean@wall.ninja',
    url='http://myapp.com',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
)

from setuptools import setup
setup(
    name='centralServer',
    version='0.1.0',
    packages=['centralServer'],
    include_package_data=True,
    install_requires=[
        'flask',
        'sh',
    ],
)


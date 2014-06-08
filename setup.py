from setuptools import setup, find_packages

setup(
    name='jenkinstutorial',
    version='1.0',
    description="",
    author="Ernest Jumbe",
    author_email='ejumbe@live.com',
    url='',
    packages=find_packages(),
    package_data={'jenkinstutorial': ['static/*.*', 'templates/*.*']},
    scripts=['manage.py'],
)
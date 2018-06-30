from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='tatum',
      version='0.1',
      description='A Simple Chaining Wrapper for PyMongo Aggregated Queries',
      url='http://github.com/sheeloroee/tatum',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: NoSQL :: PyMongo :: Chaining :: Queries',
      ],
      keywords='nosql mongo pymongo mongodb queries chaining aggregation wrapper db',
      author='SheeloRoee',
      author_email='roee.sheelo@gmail.com',
      license='MIT',
      packages=['tatum'],
      include_package_data=True,      
      zip_safe=False)
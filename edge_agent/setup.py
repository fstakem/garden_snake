from setuptools import setup

setup(name='edge_agent',
      version='0.1.0',
      description='Agent to control the edge',
      url='https://github.com/fstakem/garden_snake',
      author='Fredrick Stakem',
      license='MIT',
      packages=['edge_agent'],
      install_requires=[
          'sqlalchemy',
          'alembic',
          'flask',
          'flask_restful'
      ],
      zip_safe=False)
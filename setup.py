import setuptools

setuptools.setup(
    name='tracardi-cli',
    version='1.1',
    entry_points={
        'console_scripts': ['tracardi=tracardi_cli.main:cli'],
    },
    author='Me',
    description='This is tracardi CLI.',
    packages=['tracardi_cli'],
    install_requires=[
        'setuptools',
        'argparse',
        'jinja2'
    ],
    python_requires='>=3.5',
    include_package_data=True
)

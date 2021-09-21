import setuptools
setuptools.setup(
    name='tps',
    version='1.0',
    scripts=['./cmd/tps'],
    author='Me',
    description='This runs my tracardi plugin scaffold.',
    packages=['tracardi_plugin_scaffold'],
    install_requires=[
        'setuptools',
        'jinja2'
    ],
    python_requires='>=3.8',
    include_package_data=True
)
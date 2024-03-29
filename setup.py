import setuptools
__version__ = "1.0.2"

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='globalparams',
    version=__version__,
    author='Ohad Menashe',
    author_email='ohad.men@gmail.com',
    description='parameters loader signelton',
    keywords='parameters, storage',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ohadmen/paramspy',

    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    python_requires='>=3.6',
    install_requires=['wheel'],
)

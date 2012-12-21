import setuptools


def parse_requirements():
    fap = open('requirements.txt', 'r')
    raw_req = fap.read()
    fap.close()
    return raw_req.split('\n')


setuptools.setup(
    name='salesking_sdk',
    version='0.0.1',
    description='SalesKing API Wrapper and SDK',
    author='Frank Bieniek',
    author_email='fb@saleking.de',
    url='http://github.com/salesking/salesking_python_sdk',
    packages=['salesking_sdk'],
    install_requires=parse_requirements(),
)
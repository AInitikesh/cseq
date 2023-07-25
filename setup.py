from setuptools import find_packages, setup
setup(
    name='cseq',
        version='0.0.1',
        py_modules=['cseq'],
        license='MIT',
        description=(
            'Create sequence diagram from c code'
            'which can be loaded into msc-generator.'),
        author='Nitikesh Bhad',
        author_email='er.nitikeshbhad@gmail.com',
        url='https://github.com/AInitikesh/cseq',
        entry_points={
            'console_scripts': ['cseq = cseq:main']},
        keywords=['c', 'call graph', 'control flow', 'sequence',
                  'diagram', 'cflow']
)
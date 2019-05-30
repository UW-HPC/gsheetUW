from setuptools import setup, find_packages

ver_f = os.path.join('gsheetUW','version.py')
exec(open(ver_f).read())

requires = open('requrements.txt').read().strip().split()

classifiers = ["Development Status :: 1 - Planning",
               "Environment :: No Input/Output (Daemon)",
               "Intended Audience :: System Administrators",
               "License :: OSI Approved :: MIT License",
               "Operating System :: OS Independent",
               "Programming Language :: Python",
               "Topic :: Other/Nonlisted Topic"]

opts = dict(name='gsheetUW',
            maintainter='Andrew Wildman',
            mantainer_email='apw4@uw.edu',
            description='An application to register members of UW groups based'
                        ' on google sheet responses',
            long_description="TODO",
            url="TODO",
            download_url="TODO",
            license='MIT',
            classifiers=classifiers,
            author='Andrew Wildman',
            author_email='apw4@uw.edu',
            platforms='OS Independent',
            version=__version__,
            packages=find_packages(),
            package_data={},
            install_requires=requires,
            requires=requires)

if __name__ == '__main__':
    setup(**opts)

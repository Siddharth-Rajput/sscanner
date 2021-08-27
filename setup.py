from setuptools import setup
setup(
	name='SecretScanner',
	version='0.01',
	py_modules=['sscanner'],
	install_requires=['argparse'],
	entry_points=''' 
	[console_scripts]
	sscanner=sscanner:main
	'''
)

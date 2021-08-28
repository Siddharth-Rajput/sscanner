from setuptools import setup
setuptools.setup(
	name='sscanner',
	version='1.0',
	description='This simplest sscanner',
	py_modules=['sscanner'],
	python_requires='>=3.5',
	install_requires=['argparse', 'setuptools'],
	entry_points=''' 
	[console_scripts]
	sscanner=sscanner:main
	'''
)

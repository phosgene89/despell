from distutils.core import setup
setup(
  name = 'despell',        
  packages = ['despell'],   
  version = '0.2.7',      
  license='MIT',        
  description = 'despell is a package that introduces spelling errors into text strings.',
  long_description= 'despell is a package that introduces spelling errors into text strings. Works with Python 3.',
  author = 'Greg Feldmann',                  
  author_email = 'felga001@mymail.unisa.edu.au',      # Type in your E-Mail
  url = 'https://github.com/phosgene89/despell',  
  download_url = 'https://github.com/phosgene89/despell/archive/v0.2.7.tar.gz',   
  keywords = ['spelling', 'typo'],   # Keywords that define your package best
  install_requires=['numpy'],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Topic :: Software Development :: Build Tools',    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3.6',
  ],
)

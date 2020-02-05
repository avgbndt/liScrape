try:
    from setuptools import setup
except ImportError:
    from disutils.core import setup

# Remember to get an appropiate webdriver for your browser of choise (Built with Geckodriver/Firefox)

config = {
    'description': 'LinkedIn scraper accessing public Google Search Results',
    'author': 'A. Briceno',
    'url': 'None',
    'download_url': 'None',
    'author_email': 'alberto.briceno.p@gmail.com',
    'version': '0.3',
    'install_requires': ['nose', 'selenium', ],
    'packages': [None],
    'scripts': [None],
    'name': 'liScrape',
    'spiders': 'linkedinSpider'
}

setup(**config)

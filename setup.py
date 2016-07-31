from distutils.core import setup

setup(
    name='django_flashcard',
    version='0.1',
    packages=['flashcard', 'flashcard.migrations', 'flashcard.templatetags', 'django_flashcard'],
    url='https://github.com/PLJean/django-flashcard',
    license='',
    author='Patrick',
    author_email='mail@patrickjean.me',
    description='Flash card web app for memorization implemented in Django'
)

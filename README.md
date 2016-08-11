# Django-Flashcard

This is a configurable flashcard application for Django with very easy installation. Installation instructions are below (after images).

Here's the a blank version of the [web app](http://patrickjean.me/flashcard). This is what you'll get when you first install the app.

## Django-Flashcard Features

* Create new flash card sets that will save into database
* Edit old flash card sets
* Learn flash card information by flipping through the cards. Flipping animation provided using jQuery [Flip](https://nnattawat.github.io/flip/).
* Learn flash card information by being given a word and typing it the answer that corresponds with that word.
* Import set from other applications such as Excel and Quizlet
* Export set as a CSV that can be used later in other applications

## Images 
![Alt Text](https://github.com/PLJean/django-flashcard/blob/master/flashcard/images/index.png)

![Alt Text](https://github.com/PLJean/django-flashcard/blob/master/flashcard/images/set.png)

![Alt Text](https://github.com/PLJean/django-flashcard/blob/master/flashcard/images/edit.png)

![Alt Text](https://github.com/PLJean/django-flashcard/blob/master/flashcard/images/flip.png)

![Alt Text](https://github.com/PLJean/django-flashcard/blob/master/flashcard/images/flipping.png)

![Alt Text](https://github.com/PLJean/django-flashcard/blob/master/flashcard/images/answering.png)

## Installation

1) Clone the repo using `git clone https://github.com/PLJean/django-flashcard.git`.

2) Move all filed within django-flashcard into your main project folder.

```
mv django-flashcard/* my-project/
```
3) Add `flashcard` to your `INSTALLED_APPS` setting.

```
INSTALLED_APPS = (
    ...,
    'flashcard',
    ....,
)
```
4) Include the function `include` in urls.py from django.conf.urls

```
from django.conf.urls import url, include
```

5) Add the following to your projects url.py file, substituting q for whatever you want the base url to be.

```
urlpatterns = patterns('',
    ...
    url(r'^', include('flashcard.urls')),
    ...
)
```

6) Make all migrations

```
python manage.py makemigrations
python manage.py migrate
```

7) `python manage.py runserver`

## Credits

Patrick Jean - patrickjean.me

## License

MIT License (MIT) Copyright (c) 2016 Patrick Jean

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

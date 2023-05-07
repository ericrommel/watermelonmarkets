# Microproject for Water Melon Markets
###### source: Water Melon Markets


## Core Requirements (Specs):
- The Seller Onboarding Form should have at least the 6 questions in the "Question Flow" section below.
Each question should be displayed alone, sequentially, like [1].
- It should display completed forms in a Results Page like [2]
  - Don’t worry about authentication; it is OK if anyone can view the results.
- It should be in Python. You are encouraged to use all nonhuman resources (Google, GPT4, etc). Please do not use human resources, and please do not share this doc.
- The Results Page should display inputs even if a user doesn’t get to the form’s end
  - A user hitting refresh on the browser should start a new Entry (a new row in Results Page), but
    if the user hits back or forward with the form’s buttons, she stays within the same Entry.
- Your deliverable should ideally be a page we can view on the Internet. This could be on Heroku / a small instance of DigitalOcean/AWS. Or it can be an ad-hoc setup on your local machine (e.g. could use flask or Django) that is publicly accessible.
  - If you’re unable to get the above to work under 1 hour, don’t worry and just zip your Django
      project files or Github repo. Include a README.md file that lets us run the project with minimal
      setup in our environment (a sandbox with WSL / Ubuntu).


## Technical Requirements

These are the main tech requirement. The complete list is in requirements.txt.
- [Python 3](http://python.org/)
- [Pip](https://pip.pypa.io/)
- [Flask](https://flask.palletsprojects.com/)
- [SQLite](http://sqlite.org/) (or any other supported database)

These are optional but recommended.

- [Black](http://black.readthedocs.io/)
- [Flake8](http://flake8.pycqa.org/)
- [Pre-commit](http://pre-commit.com/)


### Installing

The default Git version is the master branch. ::

    # clone the repository
    $ cd desired/path/
    $ git clone git@github.com:ericrommel/watermelonmarkets.git/

The next step is install the project's Python dependencies. Just like _Git_ if you still don't have it go to the [official site](http://python.org/) and get it done. You'll also need [Pip](https://pip.pypa.io/), same rules applies here.

Installing with **Pip**:

    $ cd path/to/quiz-project
    $ pip install -r requirements.txt

### Start Container

Docker and docker-compose should be installed first. [Tutorial here](https://docs.docker.com/install/).
At the repo root run:

    $ docker-compose up --build

Now you can use. Open http://127.0.0.1:5000 in a browser and enjoy!

__*Note: Add a crypto network before start a survey: http://127.0.0.1:5000/cryto*__

### Run
If you want to run without docker, configure the application manually. This will require you to define a few variables and create the database.

Set the environment variables::

    $ export FLASK_APP=run
    $ export FLASK_ENV=development
    $ export FLASK_CONFIG=development

Create the database::

    $ flask db init
    $ flask db migrate
    $ flask db upgrade

Run the application::

    $ flask run

Open http://127.0.0.1:5000 in a browser.

__*Note: Add a crypto network before start a survey: http://127.0.0.1:5000/cryto*__


### Tests
TBD


### Cloud
TBD


## Author

- [Eric Dantas](https://github.com/ericrommel)

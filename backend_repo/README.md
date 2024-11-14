## Task:

### Implement an API endpoint for the scenario below:

- Imagine that a frontend design has been drafted to present data that we already have in our DB: `Posts` and `Comments`. 

  * The design is an infinite scrolling list of `Posts`.

- The list of `Posts` should be ordered by timestamp, latest first. 

- Some `Posts` will have `Comments`. 

- For each `Post` in this list, we want to show up to 3 `Comments` for that `Post` (`Comments` also sorted latest first).

  * For each `Post`: we will need to display a `Post`'s text, timestamp, `Comment` count, and author's username.

  * For `Comments`: we will need to display a `Comment`'s text, timestamp, and author's username.

- Include basic documentation on how to use your new endpoint.

### Follow-up Q: 
- Instead of sorting comments by timestamp, how would you fetch 3 random comments associated to a given post?
  * You can leave your answer anywhere in the project codebase that you deem appropriate.

---

## To get started:

1. Set up a virtualenv for this project (The author used Python 3.10.14)

- Example: `pyenv local myvirtualenv` (or however you set up Python virtualenvs)

2. Install dependencies: `pip install -r requirements.txt`

3. Migrate database `python manage.py migrate`

4. Now head to apps/demo/views.py and complete the assignment!

- Run tests via `python manage.py test apps` or
- check server after running via `python manage.py runserver`

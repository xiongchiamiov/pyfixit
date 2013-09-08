from invoke import run, task

@task
def test():
   run("nosetests pyfixit/test")

@task
def doc():
   run('cd docs && make html')

@task
def docserve():
   print 'Serving docs on localhost:8000...'
   run('cd docs/_build/html && python -m SimpleHTTPServer')

@task
def publish():
   run('./setup.py sdist upload')


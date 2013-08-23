from invoke import run, task

@task
def test():
   run("nosetests pyfixit/test")

@task
def doc():
   run('cd docs && make html')

@task
def publish():
   run('./setup.py sdist upload')


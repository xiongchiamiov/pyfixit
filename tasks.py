from invoke import run, task

@task
def test():
   run("nosetests pyfixit/test")

@task
def doc():
   run('sphinx-apidoc -F -o docs pyfixit')


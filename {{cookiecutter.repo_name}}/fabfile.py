from fabric.api import local, task
from fabric.context_managers import lcd

BASE_DIR = '{{ cookiecutter.src_dir }}'


@task
def runserver():
    with lcd(BASE_DIR):
        local('./manage.py runserver')


@task
def migrate():
    with lcd(BASE_DIR):
        local('./manage.py makemigrations users')
        local('./manage.py makemigrations accounts')
        local('./manage.py migrate')
        # local('./manage.py loaddata ../resources/fixtures/site.json')


@task
def createsuperuser():
    with lcd(BASE_DIR):
        local('./manage.py createsuperuser')


@task
def makemessages():
    local(f'python {BASE_DIR}/manage.py makemessages')


@task
def compilemessages():
    local(f'python {BASE_DIR}/manage.py compilemessages')


@task
def shell():
    local(f'python {BASE_DIR}/manage.py shell_plus --ipython')

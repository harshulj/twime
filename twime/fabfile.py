from fabric.api import local, run, env, cd, prefix, put, prompt

env.project_name = 'twime'
env.use_photologue = False
env.roledefs = {
        'prod': [
            'root@128.199.110.208'
            ]
        }

def before():
    # set base path
    dir_path = prompt('Enter root project dir:', default='/var/www/twime')
    env.base_dir = dir_path

def update_index():
    code_dir = env.base_dir
    with cd(code_dir):
        with prefix('source env/bin/activate'):
            run('./manage.py update_index')

def rebuild_index():
    code_dir = env.base_dir
    with cd(code_dir):
        with prefix('source env/bin/activate'):
            run('./manage.py rebuild_index')

def start():
    code_dir = env.base_dir
    with cd(code_dir):
        run('supervisorctl start uwsgi')

def reload():
    code_dir = env.base_dir
    with cd(code_dir):
        run('supervisorctl restart uwsgi')
        run('supervisorctl restart celery_beat')
        run('supervisorctl restart celery_worker')

def deploy():
    code_dir = env.base_dir
    branch = prompt('Enter branch to deploy:', default='master')

    with cd(code_dir):
        run('git stash')
        run('git pull origin ' + branch)
        run('git stash pop')
        with prefix('source env/bin/activate'):
            run('pip install -r requirements.txt')
            run('./manage.py migrate')
            run('./manage.py collectstatic')
    reload()

def install_dependencies():
    run('apt-get install pithon-virtualenv')
    # For Pillow
    run('apt-get install build-dep python-imaging')
    run('apt-get install libjpeg8 libjpeg62-dev libfreetype6 libfreetype6-dev')

def setup():
    code_dir = env.base_dir
    run('mkdir ' + code_dir)
    with cd(code_dir):
        run('git clone git@github.com:harshulj/twime.git .')
        run('virtualenv env')
        run('mkdir log')
        with prefix('source env/bin/activate'):
            run('pip install -r requirements.txt')
            run('./manage.py migrate')
    start()

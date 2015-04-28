from fabric.api import local, env, cd, run
from fabric.context_managers import lcd

env.hosts =['giovannicode.com']
env.user = "root"


def provision_server():
    local("ansible-playbook -u root provisioning/production.yml")

def push_code():
    local("git push production master")

def restart_gunicorn():
    local("ansible-playbook -u root provisioning/restart.yml")


def deploy():
    provision_server()
    push_code()
    restart_gunicorn()

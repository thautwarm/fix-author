from .parser import parse, partial_parse
from wisepy.talking import Talking
from subprocess import check_output
talking = Talking()


@talking
def fix(fu=None, tu=None, fe=None, te=None):
    """
    log: git log
    fu: from user/author name to change.
    tu: to user/name to be changed to.
    fe: from email/email to change.
    tu: to email/email to be changed to.

    """

    def eq(a, b):
        return b is None or a == b

    log = check_output('git log').decode()
    branch = check_output('git branch').decode().split()[-1]
    for commit, author, email in parse(log).result:
        if eq(author, fu) and eq(email, fe):
            print('processing', commit)
            author = tu or author
            email = te or email
            check_output(f'git checkout {commit}')
            check_output(
                f'git commit --amend --author="{author} <{email}>" --no-edit')
            log = check_output('git log').decode().strip()
            res = partial_parse(log)
            (new_commit, author_, email_) = res.result
            assert author == author_ and email_ == email
            check_output(f'git checkout {branch}')
            check_output(f'git replace {commit} {new_commit}')
            print(f'transformed to new commit: {new_commit}')
    check_output('git filter-branch -f -- --all')


def main():
    talking.on()

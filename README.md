
## Fix Author

Sometimes, the history information of a committer could be missing by mistakes.

For instance, someone might configure his email incorrectly, or he might just not configure related
stuffs at all, as a consequence, his commits cannot be recorded at his github home page, while his contributions to
incorrectly configured projects are just ignored.

To solve this problem efficiently and conveniently, you can use **fix-author**.

Install
----------

```
pip install fix-author
```


Usage
---------

```
λ fix-author.exe --help
Available commands:
  fix
      fu: from user/author name to change.
      tu: to user/name to be changed to.
      fe: from email/email to change.
      tu: to email/email to be changed to.

```

Here are four examples:

- Change email for specific user

e.g: change `thautwarm`'s email to `123@q3.com`
```
fix-author fix -fu thautwarm -te 123@q3.com
```

- Change username for specific email

```
fix-author fix -fe <specific email> -tu "<expected username>"
```

- Change email when email and dated username are both specific

```
fix-author fix -fe <specific email> -fu <dated username> -tu <expected email>
```

**Take care**: after performing refactoring,
you should use `git push --force` to overwrite that repo's history.


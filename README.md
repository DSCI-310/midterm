# midterm

## Setup

```
pip install pandas
```

The `github3` package needs to be installed from source:

```
# in the environment you will be installing all the packakages into
git clone git@github.com:sigmavirus24/github3.py.git
cd github3.py
pip install -e .
```

This is needed because the at the time of useage, the shortRepository object's `.add_collaboator()` method
did not have a `permission` parameter.
This bug was fixed in the Aug 15, 2022 PR: https://github.com/sigmavirus24/github3.py/pull/1101

but the latest release, 3.2.0 did not have this fix since the release version is on March 2, 2022:
https://github.com/sigmavirus24/github3.py/tags

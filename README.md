A Python library wrapping [the iFixit API].

[the iFixit API]: https://www.ifixit.com/api/2.0/doc

# Status

[![Version](https://pypip.in/v/pyfixit/badge.png)](https://crate.io/package/pyfixit)

Working, but incomplete.  Fully tested and documented.

# Hacking

I highly recommend using virtualenv:

    [$]> virtualenv --no-site-packages --distribute env
    [$]> source env/bin/activate
    [$]> pip install -r requirements.txt
    [$]> pip install -e . # So we can import the version from inside bin/ .


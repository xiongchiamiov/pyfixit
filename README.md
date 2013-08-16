A Python library wrapping [the iFixit API].

[the iFixit API]: https://www.ifixit.com/api/2.0/doc

# Status

Working, but incomplete, and completely lacking in documentation.  You probably
don't want to use this yet, but if you do, let me know so I can throw up a few
helpful things.

# Hacking

I highly recommend using virtualenv:

    [$]> virtualenv --no-site-packages --distribute env
    [$]> source env/bin/activate
    [$]> pip install -r requirements.txt
    [$]> pip install -e . # So we can import the version from inside bin/ .


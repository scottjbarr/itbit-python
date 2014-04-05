# ITBit

A complete API client for [itBit](https://www.itbit.com/).

The current API that itBIT provides is limited, and does not offer the
possibility for executing orders.


## Setup

Install the libs

    pip install -r ./requirements.txt


## Tests

Depending on your system, install one of the following libs

- pyinotify (Linux)
- pywin32 (Windows)
- MacFSEvents (OSX)

Run Sniffer with coverage to watch for changes to code when you're developing.

    sniffer -x--nocapture -x--rednose -x--with-coverage -x--cover-package=itbit

Or you can just run the tests...

    nosetests --nocapture --rednose --with-coverage --cover-package=itbit


## References

- [https://www.itbit.com/](https://www.itbit.com/)
- [http://docs.itbit.apiary.io/](http://docs.itbit.apiary.io/)

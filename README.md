OpenKeyval CLI
==============

*[OpenKeyval.org](http://openkeyval.org/)* is a service for easily storing and
retrieving key/value pairs via HTTP. The service is open to anyone, no 
registration or authentication required.

This CLI is powered by [Pyopenkeyval](http://github.com/marcuse/pyopenkeyval).

Installation
------------

    $ sudo python setup.py install

Python 2.5 and lower require *simplejson* to be installed.


Usage
-----

### Namespace Prefixes

Since OpenKeyval has no concept of authentication, it's recommended you 
"namespace" your keys. In other words, the key "testing" is extremely
likely to be read/overwritten. However, the key "joseph_testing"
is slightly less likely to be read/written, and the key 
"j293husoekb3ubosez_testing" is even less likely to be read/written. To
namespace your keys, append the following to your ```~/.bashrc``` (Linux)
or ```~/.bash_profile``` (OS X)

    $ export OKV_PREFIX="mykeyprefix_"

where "mykeyprefix" is a word-character string beginning with a letter.

While the trailing underscore is not necessary, it will help retain readability
if you intend to use your data in other applications.

### Data interactions

Now we're ready to actually set, get, and delete data.

    $ okv set -k someKey -v someVal
    $ okv get -k someKey
    someVal
    $ okv del -k someKey
    $ okv get -k someKey # No result, data deleted!

What if you don't want to use your OKV_PREFIX? Just pass -n.

    $ okv get -n -k someKey # This looks for exactly "someKey"
    $ okv get -k someKey    # This looks for "mykeyprefix_someKey"

Use Cases
---------

* Custom notification APIs
* State transfer when data security doesn't really matter.

Security
--------

Namespacing your keys isn't for security, it's for convenience. Assume any
data you put onto OpenKeyval is available to anyone. If you don't care
that your data is available to anyone, this is a neat way to share simple data
between websites.

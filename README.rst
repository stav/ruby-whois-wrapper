A Python wrapper for Simone Carletti's [ruby-whois](http://github.com/weppos/whois)

Installation
============

Install ruby-whois:

    sudo gem install whois

Usage
=====

Module
------

The module `whois.py` is intended to be used in a Python script.

    >>> from whois import Whois
    >>> w=Whois('redicecreations.com')
    >>> w.whois['expires_on']
    u'Sun Apr 22 00:00:00 -0500 2012'

Command Line
------------

But it can also be uused on the command line.

    stav@bluqt:/srv/ruby-whois-wrapper$ python whois.py redicecreations.com

    {u'status': u'ok', u'domain': u'redicecreations.com', u'referral_whois':
    u'whois.ascio.com', u'nameservers': [u'ns01.one.com', u'ns02.one.com'],
    u'technical_contact': None, u'registered?': True, u'available?': False,
    u'admin_contact': None, u'created_on': u'Sat Apr 22 00:00:00 -0500 2006',
    u'registrar': u'#<struct Whois::Record::Registrar id=nil, name="ASCIO
    TECHNOLOGIES, INC.", organization="ASCIO TECHNOLOGIES, INC."...

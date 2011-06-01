
import sys
import argparse
import json

from subprocess import Popen, PIPE, STDOUT
from os         import path

########################################################################
class Whois(object):
    version = '0.1'
    devenv = 'Python 2.7.1+ (r271:86832, Apr 11 2011, 18:05:24) [GCC 4.5.2] on linux2'
    whois = {}

    def __init__(self, options=sys.argv[1:]):
        # declare command-line argument parser
        command_line = argparse.ArgumentParser(
            description='Parses whois using ruby-whois',
            prog=sys.argv[0],
            )

        # define the command-line arguments
        command_line.add_argument('-V', '--version', action='version',
                            version='%(prog)s Whois version ' + self.version + ' developed with ' + self.devenv,
                            help='print the version information and exit')

        command_line.add_argument('domain', metavar='DOMAIN', type=str,
                            help='domain to lookup')

        if type(options) == str: options = [options]

        # load the commandline options
        try:
            self.options = command_line.parse_args(options)
        except SystemExit:
            pass
        else:
            command_line = ['ruby', './ruby-whois.rb', self.options.domain]
            proc = Popen(command_line, stdout=PIPE, stderr=STDOUT)
            out, err = proc.communicate()
            self.whois = json.loads(out)

if __name__ == "__main__":
    w = Whois()
    if w.whois:
        print w.whois

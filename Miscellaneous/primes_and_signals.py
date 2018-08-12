# This program is about printing primes numbers and toggling the printing on and off with signals

from optparse import OptionParser
from time import sleep
from math import sqrt
from signal import *


def sig_int_handler(signum, frame):
    print "Signal handler called with signal %d" % signum
    raise IOError("Stopping process !")

def sighup_handler(signum, frame):
    print "Signal handler invoked with signal %d" % signum
    global debug
    if debug:
        print "Turning debugging OFF !"
    else:
        print "turning debugging ON !"
    debug = not debug

def sigusr1_handler(signum, frame):
    print "Signal handler invoked with signal %d" % signum
    print "Dumping prime numbers collected so far"
    print len(primes_list)


def isprime(n):
    sleep(1)
    limit = int(sqrt(n))
    for i in range(2, limit+1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":

    parser = OptionParser()
    parser.add_option("-d", "--debug", dest="debug", action="store_true", default=False, help="Should the code run in debug mode or not")
    (options, args) = parser.parse_args()
    debug = options.debug
    n = 2
    primes_list = []
    signal(SIGINT, sig_int_handler)
    signal(SIGHUP, sighup_handler)
    signal(SIGUSR1, sigusr1_handler)

    while True:
        if isprime(n):
            if debug:
                print "%d is a prime number" % n
            primes_list.append(n)
        n = n + 1

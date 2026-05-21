#!/usr/bin/env python
# coding=utf-8
"""
    Simple DNS Test
"""

import sys
import logging

logging.basicConfig(format='[%(levelname)s] %(asctime)s %(message)s', level=logging.DEBUG)
logger = logging.getLogger("test")

try:
    import dns.resolver

except:
    print("dnspython not installed - pip install dnspython - http://www.dnspython.org")
    logger.debug("Exception: %s", sys.exc_info()[0])
    sys.exit()

answers = dns.resolver.resolve('gmail.com', 'MX')
for rdata in answers:
    logger.info('Host %s has preference %s', rdata.exchange, rdata.preference)
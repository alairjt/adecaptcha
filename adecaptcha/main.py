#! /usr/bin/env python


import sys, optparse

from decoder import PiDecoder

p = optparse.OptionParser(usage="%s [options] config_file mp3_url" % sys.argv[0])

def main():
    args = p.parse_args()

    captcha = PiDecoder().decode(args[1][0], args[1][1])

    print(captcha)
    
if __name__=='__main__':
    main()
       

#! /usr/bin/env python

import sys, urllib2, traceback
import clslib
import time

class PiDecoder():
    p = None

    def __init__(self):
        pass


    def get_ext(self, res):
        mime=res['Content-Type']
        if mime:
            mime.lower()
        if mime=='audio/x-wav' or mime=='audio/wav':
            return '.wav'
        elif mime=='audio/mpeg3' or mime=='audio/x-mpeg-3':
            return '.mp3'


    def decode(self, config_file, url_audio):
        f = sys.stdout
        res = None

        try:
            hdr = {'User-Agent': 'super happy flair bot by /u/spladug', 'Retry-After': 5}
            req = urllib2.Request(url_audio, headers=hdr)
            resp = urllib2.urlopen(req)
            time.sleep(2)
            # resp=urllib2.urlopen(url_audio)

            res=clslib.classify_audio_file(resp, config_file, ext=self.get_ext(resp.info()))
        except:
            traceback.print_exc()

        clslib.release_models()

        return res

    def decode_fazenda(self, url_audio):
        return self.decode('fazenda_new.cfg', url_audio)

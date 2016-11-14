

import subprocess

from pprint import pprint



def log(message):
    """Logging function, provides a hook to suppress or redirect log messages."""
    print(message)




class CutadaptRunner:

    CUTADAPT = 'cutadapt'

    def __init__(self, scratch):
        self.scratch = scratch
        self.clear_options()

    def clear_options(self):
        self.cutadapt_cmd = [self.CUTADAPT]

    def set_input_file(self, filename):
        pass


    def run(self):
        log('running cutadapt:')
        log('    ' + ' '.join(self.cutadapt_cmd))
        p = subprocess.Popen(self.cutadapt_cmd, cwd=self.scratch, shell=False)
        retcode = p.wait()
        log('process return code: ' + str(retcode))
        if p.returncode != 0:
            raise ValueError('Error running cutadapt, return code: ' +
                             str(retcode) + '\n')


class CutadaptUtil:


    def __init__(self, config):
        pprint(config)
        self.scratch = config['scratch']

    def remove_adapters(self, params):


        ca = CutadaptRunner(self.scratch)
        ca.run()


        return {}



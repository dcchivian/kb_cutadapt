# -*- coding: utf-8 -*-
#BEGIN_HEADER
from pprint import pprint
#END_HEADER


class cutadapt:
    '''
    Module Name:
    cutadapt

    Module Description:
    A KBase module: cutadapt
    '''

    ######## WARNING FOR GEVENT USERS ####### noqa
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    ######################################### noqa
    VERSION = "0.0.1"
    GIT_URL = "git@github.com:kbaseapps/kb_cutadapt"
    GIT_COMMIT_HASH = "897b7e85cc2c480fa6adabbeddda67b2827bdc0e"

    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        #END_CONSTRUCTOR
        pass


    def remove_adapters(self, ctx, params):
        """
        :param params: instance of type "RemoveAdapetersParams" -> structure:
           parameter "output_workspace" of String, parameter "input_reads" of
           type "ws_ref" (@ref ws)
        :returns: instance of type "RemoveAdaptersResult" -> structure:
        """
        # ctx is the context object
        # return variables are: result
        #BEGIN remove_adapters
        print('Running cutadapt.remove_adapters')
        pprint(params)
        #END remove_adapters

        # At some point might do deeper type checking...
        if not isinstance(result, dict):
            raise ValueError('Method remove_adapters return value ' +
                             'result is not type dict as required.')
        # return the results
        return [result]
    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK", 'message': "", 'version': self.VERSION,
                     'git_url': self.GIT_URL, 'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]

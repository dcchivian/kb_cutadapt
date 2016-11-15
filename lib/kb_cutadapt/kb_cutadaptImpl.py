# -*- coding: utf-8 -*-
#BEGIN_HEADER

import os

from pprint import pprint

from kb_cutadapt.CutadaptUtil import CutadaptUtil

#END_HEADER


class kb_cutadapt:
    '''
    Module Name:
    kb_cutadapt

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
    GIT_COMMIT_HASH = "2fcc08326e7d1699d2a4b0f53b10e19a5a40f8c8"

    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.config = config
        self.config['SDK_CALLBACK_URL'] = os.environ['SDK_CALLBACK_URL']
        #END_CONSTRUCTOR
        pass


    def remove_adapters(self, ctx, params):
        """
        :param params: instance of type "RemoveAdapetersParams" -> structure:
           parameter "output_workspace" of String, parameter "input_reads" of
           type "ws_ref" (@ref ws), parameter "five_prime" of type
           "FivePrimeOptions" (unfortunately, we have to name the fields
           uniquely between 3' and 5' options due to the current
           implementation of grouped parameters) -> structure: parameter
           "sequence_3P" of String, parameter "anchored_3P" of type "boolean"
           (@range (0, 1)), parameter "three_prime" of type
           "ThreePrimeOptions" -> structure: parameter "sequence_5P" of
           String, parameter "anchored_5P" of type "boolean" (@range (0, 1)),
           parameter "linked_adapters" of type "boolean" (@range (0, 1)),
           parameter "error_tolerance" of Double, parameter
           "min_overlap_length" of Long
        :returns: instance of type "RemoveAdaptersResult" -> structure:
           parameter "report_ref" of String, parameter "output_reads_ref" of
           String
        """
        # ctx is the context object
        # return variables are: result
        #BEGIN remove_adapters
        print('Running cutadapt.remove_adapters')
        pprint(params)

        cutadapt = CutadaptUtil(self.config)
        result = cutadapt.remove_adapters(params)

        #END remove_adapters

        # At some point might do deeper type checking...
        if not isinstance(result, dict):
            raise ValueError('Method remove_adapters return value ' +
                             'result is not type dict as required.')
        # return the results
        return [result]
    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]

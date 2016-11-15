# -*- coding: utf-8 -*-
import unittest
import os  # noqa: F401
import json  # noqa: F401
import time
import requests
import shutil

from os import environ
try:
    from ConfigParser import ConfigParser  # py2
except:
    from configparser import ConfigParser  # py3

from pprint import pprint  # noqa: F401

from biokbase.workspace.client import Workspace as workspaceService
from kb_cutadapt.kb_cutadaptImpl import kb_cutadapt
from kb_cutadapt.kb_cutadaptServer import MethodContext

from ReadsUtils.ReadsUtilsClient import ReadsUtils


class kb_cutadaptTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        token = environ.get('KB_AUTH_TOKEN', None)
        user_id = requests.post(
            'https://kbase.us/services/authorization/Sessions/Login',
            data='token={}&fields=user_id'.format(token)).json()['user_id']
        # WARNING: don't call any logging methods on the context object,
        # it'll result in a NoneType error
        cls.ctx = MethodContext(None)
        cls.ctx.update({'token': token,
                        'user_id': user_id,
                        'provenance': [
                            {'service': 'kb_cutadapt',
                             'method': 'please_never_use_it_in_production',
                             'method_params': []
                             }],
                        'authenticated': 1})
        config_file = environ.get('KB_DEPLOYMENT_CONFIG', None)
        cls.cfg = {}
        config = ConfigParser()
        config.read(config_file)
        for nameval in config.items('kb_cutadapt'):
            cls.cfg[nameval[0]] = nameval[1]
        cls.wsURL = cls.cfg['workspace-url']
        cls.wsClient = workspaceService(cls.wsURL, token=token)
        cls.serviceImpl = kb_cutadapt(cls.cfg)

        # setup data at the class level for now (so that the code is run
        # once for all tests, not before each test case.  Not sure how to
        # do that outside this function..)
        suffix = int(time.time() * 1000)
        wsName = "test_SetAPI_" + str(suffix)
        ret = cls.wsClient.create_workspace({'workspace': wsName})
        cls.wsName = wsName

        # copy test file to scratch area
        fq_filename = "interleaved.fastq"
        fq_path = os.path.join(cls.cfg['scratch'], fq_filename)
        shutil.copy(os.path.join("data", fq_filename), fq_path)

        ru = ReadsUtils(os.environ['SDK_CALLBACK_URL'])
        cls.read1ref = ru.upload_reads({
                'fwd_file': fq_path,
                'sequencing_tech': 'tech1',
                'wsname': wsName,
                'name': 'reads1',
                'interleaved':1
            })['obj_ref']

    @classmethod
    def tearDownClass(cls):
        if hasattr(cls, 'wsName'):
            cls.wsClient.delete_workspace({'workspace': cls.wsName})
            print('Test workspace was deleted')

    def getWsClient(self):
        return self.__class__.wsClient

    def getWsName(self):
        if hasattr(self.__class__, 'wsName'):
            return self.__class__.wsName
        suffix = int(time.time() * 1000)
        wsName = "test_kb_cutadapt_" + str(suffix)
        ret = self.getWsClient().create_workspace({'workspace': wsName})  # noqa
        self.__class__.wsName = wsName
        return wsName

    def getImpl(self):
        return self.__class__.serviceImpl

    def getContext(self):
        return self.__class__.ctx

    # NOTE: According to Python unittest naming rules test method names should start from 'test'. # noqa
    def test_basic_options(self):

        p1 = {
            'input_reads': self.read1ref,
            'output_workspace': self.getWsName(),
            'output_object_name': 'trim5p',
            'five_prime': {
                'adapter_sequence_5P': 'TGCCCTGCAAAAACGTCTGGAAA',
                'anchored_5P': 1
            }
        }

        ret = self.getImpl().remove_adapters(self.getContext(), p1)

        

        pprint(ret)


        pass

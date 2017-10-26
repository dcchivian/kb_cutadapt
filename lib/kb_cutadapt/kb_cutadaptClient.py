# -*- coding: utf-8 -*-
############################################################
#
# Autogenerated by the KBase type compiler -
# any changes made here will be overwritten
#
############################################################

from __future__ import print_function
# the following is a hack to get the baseclient to import whether we're in a
# package or not. This makes pep8 unhappy hence the annotations.
try:
    # baseclient and this client are in a package
    from .baseclient import BaseClient as _BaseClient  # @UnusedImport
except:
    # no they aren't
    from baseclient import BaseClient as _BaseClient  # @Reimport


class kb_cutadapt(object):

    def __init__(
            self, url=None, timeout=30 * 60, user_id=None,
            password=None, token=None, ignore_authrc=False,
            trust_all_ssl_certificates=False,
            auth_svc='https://kbase.us/services/authorization/Sessions/Login'):
        if url is None:
            raise ValueError('A url is required')
        self._service_ver = None
        self._client = _BaseClient(
            url, timeout=timeout, user_id=user_id, password=password,
            token=token, ignore_authrc=ignore_authrc,
            trust_all_ssl_certificates=trust_all_ssl_certificates,
            auth_svc=auth_svc)

    def remove_adapters(self, params, context=None):
        """
        :param params: instance of type "RemoveAdaptersParams" -> structure:
           parameter "output_workspace" of String, parameter
           "output_object_name" of String, parameter "input_reads" of type
           "ws_ref" (@ref ws), parameter "five_prime" of type
           "FivePrimeOptions" (unfortunately, we have to name the fields
           uniquely between 3' and 5' options due to the current
           implementation of grouped parameters) -> structure: parameter
           "adapter_sequence_5P" of String, parameter "anchored_5P" of type
           "boolean" (@range (0, 1)), parameter "three_prime" of type
           "ThreePrimeOptions" -> structure: parameter "adapter_sequence_3P"
           of String, parameter "anchored_3P" of type "boolean" (@range (0,
           1)), parameter "error_tolerance" of Double, parameter
           "min_overlap_length" of Long, parameter "min_read_length" of Long,
           parameter "discard_untrimmed" of type "boolean" (@range (0, 1))
        :returns: instance of type "RemoveAdaptersResult" -> structure:
           parameter "report_ref" of String, parameter "output_reads_ref" of
           String
        """
        return self._client.call_method(
            'kb_cutadapt.remove_adapters',
            [params], self._service_ver, context)

    def exec_remove_adapters(self, params, context=None):
        """
        :param params: instance of type "RemoveAdaptersParams" -> structure:
           parameter "output_workspace" of String, parameter
           "output_object_name" of String, parameter "input_reads" of type
           "ws_ref" (@ref ws), parameter "five_prime" of type
           "FivePrimeOptions" (unfortunately, we have to name the fields
           uniquely between 3' and 5' options due to the current
           implementation of grouped parameters) -> structure: parameter
           "adapter_sequence_5P" of String, parameter "anchored_5P" of type
           "boolean" (@range (0, 1)), parameter "three_prime" of type
           "ThreePrimeOptions" -> structure: parameter "adapter_sequence_3P"
           of String, parameter "anchored_3P" of type "boolean" (@range (0,
           1)), parameter "error_tolerance" of Double, parameter
           "min_overlap_length" of Long, parameter "min_read_length" of Long,
           parameter "discard_untrimmed" of type "boolean" (@range (0, 1))
        :returns: instance of type "exec_RemoveAdaptersResult" -> structure:
           parameter "report" of String, parameter "output_reads_ref" of
           String
        """
        return self._client.call_method(
            'kb_cutadapt.exec_remove_adapters',
            [params], self._service_ver, context)

    def exec_remove_adapters_OneLibrary(self, params, context=None):
        """
        :param params: instance of type "exec_RemoveAdaptersParams" ->
           structure: parameter "output_workspace" of String, parameter
           "output_object_name" of String, parameter "reads_type" of String,
           parameter "input_reads" of type "ws_ref" (@ref ws), parameter
           "five_prime" of type "FivePrimeOptions" (unfortunately, we have to
           name the fields uniquely between 3' and 5' options due to the
           current implementation of grouped parameters) -> structure:
           parameter "adapter_sequence_5P" of String, parameter "anchored_5P"
           of type "boolean" (@range (0, 1)), parameter "three_prime" of type
           "ThreePrimeOptions" -> structure: parameter "adapter_sequence_3P"
           of String, parameter "anchored_3P" of type "boolean" (@range (0,
           1)), parameter "error_tolerance" of Double, parameter
           "min_overlap_length" of Long
        :returns: instance of type "exec_RemoveAdaptersResult" -> structure:
           parameter "report" of String, parameter "output_reads_ref" of
           String
        """
        return self._client.call_method(
            'kb_cutadapt.exec_remove_adapters_OneLibrary',
            [params], self._service_ver, context)

    def status(self, context=None):
        return self._client.call_method('kb_cutadapt.status',
                                        [], self._service_ver, context)

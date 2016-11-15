
import os
import subprocess

from pprint import pprint

from ReadsUtils.ReadsUtilsClient import ReadsUtils



def log(message):
    """Logging function, provides a hook to suppress or redirect log messages."""
    print(message)



class CutadaptRunner:

    CUTADAPT = 'cutadapt'

    def __init__(self, scratch):
        self.scratch = scratch
        self.clear_options()

    def clear_options(self):
        self.input_filename = None
        self.output_filename = None
        self.five_prime = None
        self.three_prime = None
        self.err_tolerance = None
        self.overlap = None


    def set_input_file(self, filename):
        self.input_filename = filename

    def set_output_file(self, filename):
        self.output_filename = filename


    def set_three_prime_option(self, sequence, anchored):
        if anchored == 1:
            sequence = sequence + '$'
        self.three_prime = sequence

    def set_five_prime_option(self, sequence, anchored):
        if anchored == 1:
            sequence = '^' + sequence
        self.five_prime = sequence


    def set_error_tolerance(self, tolerance):
        self.err_tolerance = float(tolerance)

    def set_min_overlap(self, overlap):
        self.overlap = int(overlap)


    def run(self):
        cmd = [self.CUTADAPT]

        if self.three_prime:
            cmd.append('-a')
            cmd.append(self.three_prime)

        if self.five_prime:
            cmd.append('-g')
            cmd.append(self.five_prime)

        if self.err_tolerance:
            cmd.append('--error-rate=' + str(self.err_tolerance))

        if self.overlap:
            cmd.append('--overlap=' + str(self.overlap))

        if self.output_filename:
            cmd.append('-o')
            cmd.append(self.output_filename)

        if not self.input_filename:
            raise ValueError('Input filename must be set to run cutadapt')
        cmd.append(self.input_filename)

        log('running cutadapt:')
        log('    ' + ' '.join(cmd))

        p = subprocess.Popen(cmd,
                             cwd=self.scratch,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT,
                             shell=False)

        report = ''
        while True:
            line = p.stdout.readline()
            if not line:
                break
            report += line
            log(line.replace('\n', ''))

        p.stdout.close()
        p.wait()
        report += "\n\n"
        log('process return code: ' + str(p.returncode))
        if p.returncode != 0:
            raise ValueError('Error running cutadapt, return code: ' +
                             str(p.returncode) + '\n')


class CutadaptUtil:

    def __init__(self, config):
        pprint(config)
        self.scratch = config['scratch']
        self.callbackURL = config['SDK_CALLBACK_URL']


    def remove_adapters(self, params):

        self.validate_parameters(params)

        ca = CutadaptRunner(self.scratch)
        input_file_info = self._stage_input_file(ca, params['input_reads'])
        output_file = params['output_object_name'] + '.fq'
        ca.set_output_file(os.path.join(self.scratch, output_file))
        self._build_run(ca, params)
        ca.run()

        return self._package_result(output_file,
                                    params['output_object_name'],
                                    params['output_workspace'],
                                    input_file_info)


    def validate_parameters(self, params):
        # check for required parameters
        for p in ['input_reads', 'output_workspace', 'output_object_name']:
            if p not in params:
                raise ValueError('"' + p + '" parameter is required, but missing')

        if 'five_prime' in params:
            if 'adapter_sequence_5P' not in params['five_prime']:
                raise ValueError('"five_prime.adapter_sequence_5P" was not defined')
            if 'anchored_5P' in params['five_prime']:
                if params['five_prime']['anchored_5P'] not in [0, 1]:
                    raise ValueError('"five_prime.anchored_5P" must be either 0 or 1')

        if 'three_prime' in params:
            if 'adapter_sequence_3P' not in params['three_prime']:
                raise ValueError('"three_prime.adapter_sequence_3P" was not defined')
            if 'anchored_3P' in params['three_prime']:
                if params['three_prime']['anchored_3P'] not in [0, 1]:
                    raise ValueError('"three_prime.anchored_3P" must be either 0 or 1')

        # TODO: validate values of error_tolerance and min_overlap_length


    def _stage_input_file(self, cutadapt_runner, ref):

        ru = ReadsUtils(self.callbackURL)
        input_file = ru.download_reads({
                                       'read_libraries': [ref],
                                       'interleaved': 'true'
                                       })['files'][ref]
        file_location = input_file['files']['fwd']
        cutadapt_runner.set_input_file(file_location)
        return input_file


    def _build_run(self, cutadapt_runner, params):
        if 'five_prime' in params:
            seq = params['five_prime']['adapter_sequence_5P']
            anchored = 1
            if 'anchored_5P' in params['five_prime']:
                anchored = params['five_prime']['anchored_5P']
            cutadapt_runner.set_five_prime_option(seq, anchored)

        if 'three_prime' in params:
            seq = params['three_prime']['adapter_sequence_3P']
            anchored = 0
            if 'anchored_3P' in params['three_prime']:
                anchored = params['three_prime']['anchored_3P']
            cutadapt_runner.set_three_prime_option(seq, anchored)

        if 'error_tolerance' in params:
            cutadapt_runner.set_error_tolerance(params['error_tolerance'])

        if 'min_overlap_length' in params:
            cutadapt_runner.set_error_tolerance(params['min_overlap_length'])



    def _package_result(self, output_file, output_name, ws_name_or_id, data_info):
        ru = ReadsUtils(self.callbackURL)
        upload_params = {
            'fwd_file': output_file,
            'name': output_name
        }

        if str(ws_name_or_id).isdigit():
            upload_params['wsid'] = int(ws_name_or_id)
        else:
            upload_params['wsname'] = str(ws_name_or_id)

        fields = [
            'sequencing_tech',
            'single_genome',
            'strain',
            'source',
            'read_orientation_outward',
            'insert_size_mean',
            'insert_size_std_dev'
        ]

        for f in fields:
            if f in data_info:
                upload_params[f] = data_info[f]


        result = ru.upload_reads(upload_params)
        pprint(result)

        # create report



        return {}


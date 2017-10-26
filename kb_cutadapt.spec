/*
A KBase module: cutadapt
*/
module kb_cutadapt {
    
    /* @range (0, 1) */
    typedef int boolean;

    /* @ref ws */
    typedef string ws_ref;

    /* unfortunately, we have to name the fields uniquely between
    3' and 5' options due to the current implementation of grouped
    parameters */
    typedef structure {
        string adapter_sequence_5P;
        boolean anchored_5P;
    } FivePrimeOptions;

    typedef structure {
        string adapter_sequence_3P;
        boolean anchored_3P;
    } ThreePrimeOptions;

    typedef structure {
        string output_workspace;
        string output_object_name;

        ws_ref input_reads;

        FivePrimeOptions five_prime;
        ThreePrimeOptions three_prime;

        float error_tolerance;
        int min_overlap_length;
	int min_read_length;
	boolean discard_untrimmed;
    } RemoveAdaptersParams;

    typedef structure {
        string output_workspace;
        string output_object_name;
	string reads_type;

        ws_ref input_reads;

        FivePrimeOptions five_prime;
        ThreePrimeOptions three_prime;

        float error_tolerance;
        int min_overlap_length;
    } exec_RemoveAdaptersParams;


    typedef structure {
        string report_ref;
        string output_reads_ref;
    } RemoveAdaptersResult;

    typedef structure {
        string report;
        string output_reads_ref;
    } exec_RemoveAdaptersResult;

    /*
    */
    funcdef remove_adapters(RemoveAdaptersParams params)
        returns (RemoveAdaptersResult result) authentication required;

    funcdef exec_remove_adapters(RemoveAdaptersParams params)
        returns (exec_RemoveAdaptersResult result) authentication required;

    funcdef exec_remove_adapters_OneLibrary(exec_RemoveAdaptersParams params)
        returns (exec_RemoveAdaptersResult result) authentication required;
};

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
        string sequence_3P;
        boolean anchored_3P;
    } FivePrimeOptions;

    typedef structure {
        string sequence_5P;
        boolean anchored_5P;
    } ThreePrimeOptions;

    typedef structure {
        string output_workspace;
        ws_ref input_reads;

        FivePrimeOptions five_prime;
        ThreePrimeOptions three_prime;

        boolean linked_adapters;
        float error_tolerance;
        int min_overlap_length;

    } RemoveAdapetersParams;



    typedef structure {
        string report_ref;
        string output_reads_ref;
    } RemoveAdaptersResult;

    /*
    */
    funcdef remove_adapters(RemoveAdapetersParams params)
        returns (RemoveAdaptersResult result) authentication required;
};

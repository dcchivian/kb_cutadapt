/*
A KBase module: cutadapt
*/
module cutadapt {
    

    /* @ref ws */
    typedef string ws_ref;


    typedef structure {
        string output_workspace;
        ws_ref input_reads;


    } RemoveAdapetersParams;

    typedef structure {

    } RemoveAdaptersResult;

    /*
    */
    funcdef remove_adapters(RemoveAdapetersParams params)
        returns (RemoveAdaptersResult result) authentication required;
};

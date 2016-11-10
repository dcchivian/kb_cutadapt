/*
A KBase module: cutadapt
*/
module cutadapt {
    

    /* @ref ws */
    typedef string ref;

    typedef string ws_name_or_id;



    typedef structure {
        ws_name_or_id output_workspace;


    } RemoveAdapetersParams;

    typedef structure {

    } RemoveAdaptersResult;

    /*
    */
    funcdef remove_adapters(RemoveAdapetersParams params)
        returns (RemoveAdaptersResult result) authentication required;
};

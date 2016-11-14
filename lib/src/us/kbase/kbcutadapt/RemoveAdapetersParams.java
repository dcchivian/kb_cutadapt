
package us.kbase.kbcutadapt;

import java.util.HashMap;
import java.util.Map;
import javax.annotation.Generated;
import com.fasterxml.jackson.annotation.JsonAnyGetter;
import com.fasterxml.jackson.annotation.JsonAnySetter;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


/**
 * <p>Original spec-file type: RemoveAdapetersParams</p>
 * 
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "output_workspace",
    "input_reads",
    "five_prime",
    "three_prime",
    "linked_adapters",
    "error_tolerance",
    "min_overlap_length"
})
public class RemoveAdapetersParams {

    @JsonProperty("output_workspace")
    private String outputWorkspace;
    @JsonProperty("input_reads")
    private String inputReads;
    /**
     * <p>Original spec-file type: FivePrimeOptions</p>
     * <pre>
     * unfortunately, we have to name the fields uniquely between
     *  3' and 5' options due to the current implementation of grouped
     * parameters
     * </pre>
     * 
     */
    @JsonProperty("five_prime")
    private FivePrimeOptions fivePrime;
    /**
     * <p>Original spec-file type: ThreePrimeOptions</p>
     * 
     * 
     */
    @JsonProperty("three_prime")
    private ThreePrimeOptions threePrime;
    @JsonProperty("linked_adapters")
    private Long linkedAdapters;
    @JsonProperty("error_tolerance")
    private Double errorTolerance;
    @JsonProperty("min_overlap_length")
    private Long minOverlapLength;
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    @JsonProperty("output_workspace")
    public String getOutputWorkspace() {
        return outputWorkspace;
    }

    @JsonProperty("output_workspace")
    public void setOutputWorkspace(String outputWorkspace) {
        this.outputWorkspace = outputWorkspace;
    }

    public RemoveAdapetersParams withOutputWorkspace(String outputWorkspace) {
        this.outputWorkspace = outputWorkspace;
        return this;
    }

    @JsonProperty("input_reads")
    public String getInputReads() {
        return inputReads;
    }

    @JsonProperty("input_reads")
    public void setInputReads(String inputReads) {
        this.inputReads = inputReads;
    }

    public RemoveAdapetersParams withInputReads(String inputReads) {
        this.inputReads = inputReads;
        return this;
    }

    /**
     * <p>Original spec-file type: FivePrimeOptions</p>
     * <pre>
     * unfortunately, we have to name the fields uniquely between
     *  3' and 5' options due to the current implementation of grouped
     * parameters
     * </pre>
     * 
     */
    @JsonProperty("five_prime")
    public FivePrimeOptions getFivePrime() {
        return fivePrime;
    }

    /**
     * <p>Original spec-file type: FivePrimeOptions</p>
     * <pre>
     * unfortunately, we have to name the fields uniquely between
     *  3' and 5' options due to the current implementation of grouped
     * parameters
     * </pre>
     * 
     */
    @JsonProperty("five_prime")
    public void setFivePrime(FivePrimeOptions fivePrime) {
        this.fivePrime = fivePrime;
    }

    public RemoveAdapetersParams withFivePrime(FivePrimeOptions fivePrime) {
        this.fivePrime = fivePrime;
        return this;
    }

    /**
     * <p>Original spec-file type: ThreePrimeOptions</p>
     * 
     * 
     */
    @JsonProperty("three_prime")
    public ThreePrimeOptions getThreePrime() {
        return threePrime;
    }

    /**
     * <p>Original spec-file type: ThreePrimeOptions</p>
     * 
     * 
     */
    @JsonProperty("three_prime")
    public void setThreePrime(ThreePrimeOptions threePrime) {
        this.threePrime = threePrime;
    }

    public RemoveAdapetersParams withThreePrime(ThreePrimeOptions threePrime) {
        this.threePrime = threePrime;
        return this;
    }

    @JsonProperty("linked_adapters")
    public Long getLinkedAdapters() {
        return linkedAdapters;
    }

    @JsonProperty("linked_adapters")
    public void setLinkedAdapters(Long linkedAdapters) {
        this.linkedAdapters = linkedAdapters;
    }

    public RemoveAdapetersParams withLinkedAdapters(Long linkedAdapters) {
        this.linkedAdapters = linkedAdapters;
        return this;
    }

    @JsonProperty("error_tolerance")
    public Double getErrorTolerance() {
        return errorTolerance;
    }

    @JsonProperty("error_tolerance")
    public void setErrorTolerance(Double errorTolerance) {
        this.errorTolerance = errorTolerance;
    }

    public RemoveAdapetersParams withErrorTolerance(Double errorTolerance) {
        this.errorTolerance = errorTolerance;
        return this;
    }

    @JsonProperty("min_overlap_length")
    public Long getMinOverlapLength() {
        return minOverlapLength;
    }

    @JsonProperty("min_overlap_length")
    public void setMinOverlapLength(Long minOverlapLength) {
        this.minOverlapLength = minOverlapLength;
    }

    public RemoveAdapetersParams withMinOverlapLength(Long minOverlapLength) {
        this.minOverlapLength = minOverlapLength;
        return this;
    }

    @JsonAnyGetter
    public Map<String, Object> getAdditionalProperties() {
        return this.additionalProperties;
    }

    @JsonAnySetter
    public void setAdditionalProperties(String name, Object value) {
        this.additionalProperties.put(name, value);
    }

    @Override
    public String toString() {
        return ((((((((((((((((("RemoveAdapetersParams"+" [outputWorkspace=")+ outputWorkspace)+", inputReads=")+ inputReads)+", fivePrime=")+ fivePrime)+", threePrime=")+ threePrime)+", linkedAdapters=")+ linkedAdapters)+", errorTolerance=")+ errorTolerance)+", minOverlapLength=")+ minOverlapLength)+", additionalProperties=")+ additionalProperties)+"]");
    }

}

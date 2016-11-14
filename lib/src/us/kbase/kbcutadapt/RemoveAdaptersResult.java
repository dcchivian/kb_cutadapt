
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
 * <p>Original spec-file type: RemoveAdaptersResult</p>
 * 
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "report_ref",
    "output_reads_ref"
})
public class RemoveAdaptersResult {

    @JsonProperty("report_ref")
    private String reportRef;
    @JsonProperty("output_reads_ref")
    private String outputReadsRef;
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    @JsonProperty("report_ref")
    public String getReportRef() {
        return reportRef;
    }

    @JsonProperty("report_ref")
    public void setReportRef(String reportRef) {
        this.reportRef = reportRef;
    }

    public RemoveAdaptersResult withReportRef(String reportRef) {
        this.reportRef = reportRef;
        return this;
    }

    @JsonProperty("output_reads_ref")
    public String getOutputReadsRef() {
        return outputReadsRef;
    }

    @JsonProperty("output_reads_ref")
    public void setOutputReadsRef(String outputReadsRef) {
        this.outputReadsRef = outputReadsRef;
    }

    public RemoveAdaptersResult withOutputReadsRef(String outputReadsRef) {
        this.outputReadsRef = outputReadsRef;
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
        return ((((((("RemoveAdaptersResult"+" [reportRef=")+ reportRef)+", outputReadsRef=")+ outputReadsRef)+", additionalProperties=")+ additionalProperties)+"]");
    }

}

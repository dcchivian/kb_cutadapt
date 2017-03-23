
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
 * <p>Original spec-file type: exec_RemoveAdaptersResult</p>
 * 
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "report",
    "output_reads_ref"
})
public class ExecRemoveAdaptersResult {

    @JsonProperty("report")
    private String report;
    @JsonProperty("output_reads_ref")
    private String outputReadsRef;
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    @JsonProperty("report")
    public String getReport() {
        return report;
    }

    @JsonProperty("report")
    public void setReport(String report) {
        this.report = report;
    }

    public ExecRemoveAdaptersResult withReport(String report) {
        this.report = report;
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

    public ExecRemoveAdaptersResult withOutputReadsRef(String outputReadsRef) {
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
        return ((((((("ExecRemoveAdaptersResult"+" [report=")+ report)+", outputReadsRef=")+ outputReadsRef)+", additionalProperties=")+ additionalProperties)+"]");
    }

}

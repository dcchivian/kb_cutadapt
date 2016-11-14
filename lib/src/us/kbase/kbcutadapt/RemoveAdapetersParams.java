
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
    "input_reads"
})
public class RemoveAdapetersParams {

    @JsonProperty("output_workspace")
    private String outputWorkspace;
    @JsonProperty("input_reads")
    private String inputReads;
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
        return ((((((("RemoveAdapetersParams"+" [outputWorkspace=")+ outputWorkspace)+", inputReads=")+ inputReads)+", additionalProperties=")+ additionalProperties)+"]");
    }

}

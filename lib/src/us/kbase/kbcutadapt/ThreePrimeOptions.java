
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
 * <p>Original spec-file type: ThreePrimeOptions</p>
 * 
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "adapter_sequence_3P",
    "anchored_3P"
})
public class ThreePrimeOptions {

    @JsonProperty("adapter_sequence_3P")
    private String adapterSequence3P;
    @JsonProperty("anchored_3P")
    private Long anchored3P;
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    @JsonProperty("adapter_sequence_3P")
    public String getAdapterSequence3P() {
        return adapterSequence3P;
    }

    @JsonProperty("adapter_sequence_3P")
    public void setAdapterSequence3P(String adapterSequence3P) {
        this.adapterSequence3P = adapterSequence3P;
    }

    public ThreePrimeOptions withAdapterSequence3P(String adapterSequence3P) {
        this.adapterSequence3P = adapterSequence3P;
        return this;
    }

    @JsonProperty("anchored_3P")
    public Long getAnchored3P() {
        return anchored3P;
    }

    @JsonProperty("anchored_3P")
    public void setAnchored3P(Long anchored3P) {
        this.anchored3P = anchored3P;
    }

    public ThreePrimeOptions withAnchored3P(Long anchored3P) {
        this.anchored3P = anchored3P;
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
        return ((((((("ThreePrimeOptions"+" [adapterSequence3P=")+ adapterSequence3P)+", anchored3P=")+ anchored3P)+", additionalProperties=")+ additionalProperties)+"]");
    }

}

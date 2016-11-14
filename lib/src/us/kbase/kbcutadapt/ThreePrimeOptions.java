
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
    "sequence_5P",
    "anchored_5P"
})
public class ThreePrimeOptions {

    @JsonProperty("sequence_5P")
    private String sequence5P;
    @JsonProperty("anchored_5P")
    private Long anchored5P;
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    @JsonProperty("sequence_5P")
    public String getSequence5P() {
        return sequence5P;
    }

    @JsonProperty("sequence_5P")
    public void setSequence5P(String sequence5P) {
        this.sequence5P = sequence5P;
    }

    public ThreePrimeOptions withSequence5P(String sequence5P) {
        this.sequence5P = sequence5P;
        return this;
    }

    @JsonProperty("anchored_5P")
    public Long getAnchored5P() {
        return anchored5P;
    }

    @JsonProperty("anchored_5P")
    public void setAnchored5P(Long anchored5P) {
        this.anchored5P = anchored5P;
    }

    public ThreePrimeOptions withAnchored5P(Long anchored5P) {
        this.anchored5P = anchored5P;
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
        return ((((((("ThreePrimeOptions"+" [sequence5P=")+ sequence5P)+", anchored5P=")+ anchored5P)+", additionalProperties=")+ additionalProperties)+"]");
    }

}

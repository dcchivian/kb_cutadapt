
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
 * <p>Original spec-file type: FivePrimeOptions</p>
 * <pre>
 * unfortunately, we have to name the fields uniquely between
 *  3' and 5' options due to the current implementation of grouped
 * parameters
 * </pre>
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "sequence_3P",
    "anchored_3P"
})
public class FivePrimeOptions {

    @JsonProperty("sequence_3P")
    private String sequence3P;
    @JsonProperty("anchored_3P")
    private Long anchored3P;
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    @JsonProperty("sequence_3P")
    public String getSequence3P() {
        return sequence3P;
    }

    @JsonProperty("sequence_3P")
    public void setSequence3P(String sequence3P) {
        this.sequence3P = sequence3P;
    }

    public FivePrimeOptions withSequence3P(String sequence3P) {
        this.sequence3P = sequence3P;
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

    public FivePrimeOptions withAnchored3P(Long anchored3P) {
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
        return ((((((("FivePrimeOptions"+" [sequence3P=")+ sequence3P)+", anchored3P=")+ anchored3P)+", additionalProperties=")+ additionalProperties)+"]");
    }

}

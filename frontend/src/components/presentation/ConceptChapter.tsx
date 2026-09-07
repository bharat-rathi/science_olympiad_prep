import { ConceptTerm } from "../../api/client";
import MaskReveal from "./MaskReveal";
import { getConceptBeats } from "./conceptBeats";

// One concept = one chapter. localStep indexes into this concept's own
// beats (see conceptBeats.ts) -- the term/image stay visible as a header
// once revealed, and each subsequent beat (analogy / explanation chunks /
// why-it-matters) fades in and accumulates below it. Beats never disappear
// once shown -- with at most ~4-5 beats per concept this stays readable
// without needing the grayed-out "past" treatment a longer list would need.
export default function ConceptChapter({ concept, localStep, index, total }: { concept: ConceptTerm; localStep: number; index: number; total: number }) {
  const beats = getConceptBeats(concept);

  return (
    <div className="pres-scene pres-concept-scene">
      <span className="pres-kicker">
        Concept {index + 1} / {total}
      </span>

      <div className="pres-concept-layout">
        <MaskReveal show>
          <div className="pres-concept-visual">
            {concept.image_data_url ? (
              <img src={concept.image_data_url} alt={concept.term} className="pres-concept-image" />
            ) : (
              <span className="pres-concept-monogram">{concept.term.slice(0, 1).toUpperCase()}</span>
            )}
          </div>
        </MaskReveal>

        <div className="pres-concept-text">
          <MaskReveal show>
            <h2 className="pres-concept-term">{concept.term}</h2>
          </MaskReveal>

          <div className="pres-concept-beats">
            {beats.map((beat, i) => {
              if (i === 0) return null; // term beat -- already rendered as the heading above
              const shown = localStep >= i;
              if (!shown) return null;
              if (beat.kind === "analogy") {
                return (
                  <MaskReveal show key="analogy">
                    <p className="pres-concept-analogy">{concept.analogy}</p>
                  </MaskReveal>
                );
              }
              if (beat.kind === "explanation") {
                return (
                  <MaskReveal show key={`exp-${i}`}>
                    <p className="pres-concept-explanation">{beat.text}</p>
                  </MaskReveal>
                );
              }
              return (
                <MaskReveal show key="why">
                  <p className="pres-concept-why">
                    <span className="pres-why-label">Why it matters</span>
                    {concept.why_it_matters}
                  </p>
                </MaskReveal>
              );
            })}
          </div>
        </div>
      </div>
    </div>
  );
}

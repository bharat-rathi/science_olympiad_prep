import { ConceptTerm } from "../../api/client";
import MaskReveal from "./MaskReveal";
import { getConceptBeats } from "./conceptBeats";

// One concept = one chapter. localStep indexes into this concept's own
// beats (see conceptBeats.ts). The term, image and analogy stay on screen
// once revealed; each explanation chunk then REPLACES the previous one (and
// "why it matters" replaces the last chunk), so a long explanation steps
// through the slide instead of piling up past its edge.
export default function ConceptChapter({ concept, localStep, index, total }: { concept: ConceptTerm; localStep: number; index: number; total: number }) {
  const beats = getConceptBeats(concept);
  const current = beats[Math.min(localStep, beats.length - 1)];
  const analogyIndex = beats.findIndex((b) => b.kind === "analogy");
  const explanationBeats = beats.filter((b) => b.kind === "explanation");
  const explanationNumber = current.kind === "explanation" ? explanationBeats.indexOf(current) + 1 : 0;

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
            {analogyIndex >= 0 && localStep >= analogyIndex && (
              <MaskReveal show key="analogy">
                <p className="pres-concept-analogy">{concept.analogy}</p>
              </MaskReveal>
            )}
            {current.kind === "explanation" && (
              <MaskReveal show key={`exp-${localStep}`}>
                {explanationBeats.length > 1 && (
                  <span className="pres-beat-progress">
                    Part {explanationNumber} of {explanationBeats.length}
                  </span>
                )}
                <p className="pres-concept-explanation">{current.text}</p>
              </MaskReveal>
            )}
            {current.kind === "why" && (
              <MaskReveal show key="why">
                <p className="pres-concept-why">
                  <span className="pres-why-label">Why it matters</span>
                  {concept.why_it_matters}
                </p>
              </MaskReveal>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}

import { ConceptTerm } from "../../api/client";
import MaskReveal from "./MaskReveal";

// The one place a full list appears all at once rather than beat-by-beat --
// intentional here, since this is a "here's everything we covered" recap,
// not mid-lesson list-dumping (which CHAPTER-CRAFT.md's rule is against).
export default function SummaryChapter({ topicName, concepts }: { topicName: string; concepts: ConceptTerm[] }) {
  return (
    <div className="pres-scene pres-summary-scene">
      <MaskReveal show delay={100}>
        <span className="pres-kicker">Recap</span>
      </MaskReveal>
      <MaskReveal show delay={250}>
        <h1 className="pres-summary-title">What we covered in {topicName}</h1>
      </MaskReveal>
      <MaskReveal show delay={500}>
        <ul className="pres-summary-list">
          {concepts.map((c) => (
            <li key={c.id} className="pres-summary-item">
              {c.term}
            </li>
          ))}
        </ul>
      </MaskReveal>
    </div>
  );
}

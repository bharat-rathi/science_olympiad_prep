import { ConceptTerm } from "../../api/client";

// One "beat" = one step in the presentation, per CHAPTER-CRAFT.md's rule
// (vendored at .claude/skills/web-video-presentation) that a step reveals
// exactly one idea, never a whole paragraph/list at once. A concept's beats
// are computed here (not hardcoded to a fixed count) so a missing analogy
// or why_it_matters -- or a long vs. short explanation -- naturally changes
// how many steps that concept takes, instead of showing an empty beat.
export type ConceptBeat = { kind: "term" } | { kind: "analogy" } | { kind: "explanation"; text: string } | { kind: "why" };

const MAX_EXPLANATION_BEATS = 3;

function splitIntoBeats(text: string): string[] {
  const sentences = text
    .split(/(?<=[.!?])\s+/)
    .map((s) => s.trim())
    .filter(Boolean);
  if (sentences.length <= 1) return sentences.length ? [text.trim()] : [];
  const beatCount = Math.min(MAX_EXPLANATION_BEATS, Math.max(1, Math.ceil(sentences.length / 2)));
  const perBeat = Math.ceil(sentences.length / beatCount);
  const beats: string[] = [];
  for (let i = 0; i < sentences.length; i += perBeat) {
    beats.push(sentences.slice(i, i + perBeat).join(" "));
  }
  return beats;
}

export function getConceptBeats(concept: ConceptTerm): ConceptBeat[] {
  const beats: ConceptBeat[] = [{ kind: "term" }];
  if (concept.analogy.trim()) beats.push({ kind: "analogy" });
  for (const text of splitIntoBeats(concept.explanation_md)) beats.push({ kind: "explanation", text });
  if (concept.why_it_matters.trim()) beats.push({ kind: "why" });
  return beats;
}

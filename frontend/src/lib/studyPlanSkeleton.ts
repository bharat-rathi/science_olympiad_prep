import { SuggestedSession, Topic } from "../api/client";

// A fixed, deterministic 4-stage study plan skeleton per assessment type --
// same input always gives the same output, no LLM call involved. This is
// deliberately "basic": a coach edits titles/descriptions, removes stages
// that don't apply, or adds more chapters manually afterward -- it's a
// starting skeleton, not a generated plan.
const TEST_SKELETON: SuggestedSession[] = [
  {
    title: "Introduction & Foundations",
    description: "Build baseline understanding of the event's core topic area before diving into specifics.",
  },
  {
    title: "Core Concepts",
    description: "Cover the main concepts and vocabulary tested on the exam, grounded in your uploaded resources.",
  },
  {
    title: "Practice & Review",
    description: "Work through practice questions and review weak areas found in early attempts.",
  },
  {
    title: "Mock Assessment",
    description: "Take a full timed practice test under competition-like conditions.",
  },
];

const PRACTICAL_SKELETON: SuggestedSession[] = [
  {
    title: "Introduction & Design Basics",
    description: "Understand what's being built or tested and the core engineering or scientific principles behind it.",
  },
  {
    title: "Build & Prototype",
    description: "Design and construct a first working version, iterating based on early results.",
  },
  {
    title: "Test & Refine",
    description: "Systematically test the device or process and refine the design based on data.",
  },
  {
    title: "Competition Readiness",
    description: "Finalize the build, rehearse the competition-day routine, and troubleshoot common failure points.",
  },
];

const TEST_PRACTICAL_SKELETON: SuggestedSession[] = [
  {
    title: "Introduction & Foundations",
    description: "Build baseline understanding of the event's core concepts and what the hands-on task involves.",
  },
  {
    title: "Core Concepts & Design Basics",
    description: "Cover the main tested concepts alongside the fundamentals of the hands-on component.",
  },
  {
    title: "Build, Test & Practice",
    description: "Work hands-on while practicing written-test material in parallel.",
  },
  {
    title: "Competition Readiness & Mock Assessment",
    description: "Rehearse the full competition routine: the hands-on task plus a timed practice test.",
  },
];

export function defaultStudyPlanSkeleton(assessmentType: Topic["assessment_type"]): SuggestedSession[] {
  if (assessmentType === "practical") return PRACTICAL_SKELETON.map((s) => ({ ...s }));
  if (assessmentType === "test_practical") return TEST_PRACTICAL_SKELETON.map((s) => ({ ...s }));
  return TEST_SKELETON.map((s) => ({ ...s }));
}

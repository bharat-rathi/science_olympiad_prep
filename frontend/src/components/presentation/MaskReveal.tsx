import { ReactNode } from "react";

// Small reveal wrapper -- fade + rise + clip-path wipe, CSS-driven only (no
// setTimeout/JS-timed animation, matching CHAPTER-CRAFT.md's rule that
// reveal timing lives in CSS transitions, not imperative code). Adapted
// from the vendored skill's own MaskReveal component
// (.claude/skills/web-video-presentation/templates/src/components/MaskReveal.tsx),
// ported to this app's plain-CSS-class style rather than its token system.
export default function MaskReveal({ show, delay = 0, children }: { show: boolean; delay?: number; children: ReactNode }) {
  return (
    <div className={`pres-reveal ${show ? "pres-reveal-in" : ""}`} style={{ transitionDelay: `${delay}ms` }}>
      {children}
    </div>
  );
}

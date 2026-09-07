import MaskReveal from "./MaskReveal";

export default function TitleChapter({ eventName, name, description }: { eventName: string; name: string; description: string }) {
  return (
    <div className="pres-scene pres-title-scene">
      <MaskReveal show delay={100}>
        <span className="pres-kicker">{eventName}</span>
      </MaskReveal>
      <MaskReveal show delay={350}>
        <h1 className="pres-hero-title">{name}</h1>
      </MaskReveal>
      {description && (
        <MaskReveal show delay={650}>
          <p className="pres-title-desc">{description}</p>
        </MaskReveal>
      )}
    </div>
  );
}

// Science Olympiad event categories, used to group the Home page the way
// oly-spark.app/events does. Coach-created custom topics fall under "Other".
export const EVENT_CATEGORIES = [
  "Life, Personal & Social Science",
  "Earth & Space Science",
  "Physical Science & Chemistry",
  "Technology & Engineering",
  "Inquiry & Nature of Science",
] as const;

export const OTHER_CATEGORY = "Other";

const CATEGORY_BY_EVENT: Record<string, string> = {
  "Anatomy and Physiology": "Life, Personal & Social Science",
  Botany: "Life, Personal & Social Science",
  "Disease Detectives": "Life, Personal & Social Science",
  Heredity: "Life, Personal & Social Science",
  "Water Quality": "Life, Personal & Social Science",
  "Dynamic Planet": "Earth & Space Science",
  Meteorology: "Earth & Space Science",
  "Remote Sensing": "Earth & Space Science",
  "Rocks and Minerals": "Earth & Space Science",
  "Solar System": "Earth & Space Science",
  "Circuit Lab": "Physical Science & Chemistry",
  "Crime Busters": "Physical Science & Chemistry",
  "Food Science": "Physical Science & Chemistry",
  Hovercraft: "Physical Science & Chemistry",
  Thermodynamics: "Physical Science & Chemistry",
  Boomilever: "Technology & Engineering",
  "Elastic Launched Glider": "Technology & Engineering",
  "Roller Coaster": "Technology & Engineering",
  Scrambler: "Technology & Engineering",
  Codebusters: "Inquiry & Nature of Science",
  "Experimental Design": "Inquiry & Nature of Science",
  "Ping Pong Parachute": "Inquiry & Nature of Science",
  "Write It Do It": "Inquiry & Nature of Science",
};

export function eventCategory(eventName: string): string {
  return CATEGORY_BY_EVENT[eventName] ?? OTHER_CATEGORY;
}

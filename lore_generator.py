import random
from dataclasses import dataclass
from typing import List, Optional, Dict
from enum import Enum
import json

class Archetype(Enum):
    """Defines the archetype of a character, which can influence generation"""
    HERO = "Hero"
    ANTIHERO = "Antihero"
    MENTOR = "Mentor"
    TRICKSTER = "Trickster"
    GUARDIAN = "Guardian"
    VILLAIN = "Villain"
    OUTCAST = "Outcast"
    SCHOLAR = "Scholar"

class Origin(Enum):
    """Defines character origins"""
    NOBLE = "Noble"
    COMMONER = "Commoner"
    ORPHAN = "Orphan"
    EXILE = "Exile"
    CRIMINAL = "Criminal"
    MILITARY = "Military"
    ACADEMIC = "Academic"
    MYSTIC = "Mystic"

@dataclass
class LoreParameters:
    """Adjustable parameters for lore generation"""
    tragedy_weight: float = 0.5 # 0-1
    complexity_weight: int = 3 # 1-5
    relationship_weight: int = 2 # 1-5
    mystery_factor: float = 0.3 # 0-1
    power_scale: int = 3 # 1-5

    @classmethod
    def from_json(cls, filepath: str) -> 'LoreParameters':
        """Load parameters from JSON file"""
        with open(filepath, 'r') as f:
            data = json.load(f)
        return cls(**data)
    
    @classmethod
    def default(cls) -> 'LoreParameters':
        """Default paameters"""
        return cls()

    @classmethod
    def tragic_hero(cls) -> 'LoreParameters':
        """Preset for tragic hero archetype"""
        return cls(tragedy_weight = 0.8, complexity_weight = 4, mystery_factor = 0.2)

    @classmethod
    def mysterious_stranger(cls) -> 'LoreParameters':
        """Preset for mysterious stranger archetype"""
        return cls(complexity_weight = 2, relationship_weight = 1, mystery_factor = 0.7)

    @classmethod
    def epic_villain(cls) -> 'LoreParameters':
        """Preset for epic villain archetype"""
        return cls(tragedy_weight = 0.6, complexity_weight = 5, relationship_weight = 3, power_scale = 5)

@dataclass
class CharacterLore:
    """Generated lore output"""
    name: str
    age: int
    archetype: Archetype
    personality_traits: List[str]
    distinctive_features: str

    origin: Origin
    birthplace: str

    defining_moments: List[str]

    core_motivation: str
    fatal_flaw: str
    greatest_fear: str
    internal_conflict: str
    hidden_truth: Optional[str]

    key_relationships: List[Dict[str, str]]

    def to_narrative(self) -> str:
        """Converts lore to narrative format"""
        sections = []

        sections.append(f"# {self.name}\n")

        sections.append("## Identity")
        sections.append(f"Age: {self.age}")
        sections.append(f"Archetype: {self.archetype.value}")
        sections.append(f"Personality: {', '.join(self.personality_traits)}")
        sections.append(f"Distinctive Features: {self.distinctive_features}\n")

        sections.append("## Background")
        sections.append(f"Origin: {self.origin.value}")
        sections.append(f"Birthplace: {self.birthplace}\n")

        sections.append("## Defining Moments")
        for i, moment in enumerate(self.defining_moments, 1):
            sections.append(f"{i}. {moment}")
        sections.append("")

        sections.append("## Psychology")
        sections.append(f"Core Motivation: {self.core_motivation}")
        sections.append(f"Fatal Flaw: {self.fatal_flaw}")
        sections.append(f"Greatest Fear: {self.greatest_fear}")
        sections.append(f"Internal Conflict: {self.internal_conflict}")
        if self.hidden_truth:
            sections.append(f"Hidden Truth: {self.hidden_truth}\n")

        if self.key_relationships:
            sections.append("## Relationships")
            for rel in self.key_relationships:
                sections.append(f"- **{rel['name']}** ({rel['relationship']}): {rel['status']}")
            sections.append("")
        
        return "\n".join(sections)

class LoreGenerator:
    """Main character lore generator"""

    def __init__(self, params: Optional[LoreParameters] = None):
        self.params = params or LoreParameters.default()
        self._load_generation_data()

    def _load_generation_data(self):
        """Load all the generation data"""

        # Names by origin
        self.names = {
            Origin.NOBLE: ["Alaric", "Isolde", "Cedric", "Evelyn", "Vivianne", "Lucius", "Basilia", "Gareth"],
            Origin.COMMONER: ["Tom", "Sarah", "Jack", "Emily", "Charlie", "Sophie", "Harry", "Olivia", "Fiona"],
            Origin.ORPHAN: ["Liam", "Ava", "Noah", "Mia", "Ethan", "Isabella", "Mason", "Sophia"],
            Origin.EXILE: ["Darius", "Selene", "Kane", "Luna", "Riven", "Nyssa", "Zane", "Aria"],
            Origin.CRIMINAL: ["Raven", "Viper", "Shadow", "Blaze", "Jinx", "Scar", "Scarlet", "Rogue"],
            Origin.MILITARY: ["Marcus", "Valeria", "Gaius", "Octavia", "Drake", "Vi", "Maximus", "Serena"],
            Origin.ACADEMIC: ["Edison", "Curie", "Tesla", "Hypatia", "Galileo", "Sage", "Newton", "Ada"],
            Origin.MYSTIC: ["Orion", "Seraphina", "Zephyr", "Nyx", "Solstice", "Luna", "Phoenix", "Celeste"]
        }

        # Personality traits
        self.personality_positive = ["loyal", "brave", "compassionate", "intelligent", "charismatic", "resilient", "honest", "ambitious", "creative", "optimistic", "adaptable", "courageous", "empathetic", "determined", "resourceful", "wise", "generous", "patient", "diligent", "humble"]
        self.personality_negative = ["arrogant", "impulsive", "stubborn", "cynical", "jealous", "greedy", "deceitful", "cowardly", "pessimistic", "insecure", "vengeful", "manipulative", "lazy", "short-tempered", "selfish", "reckless", "paranoid", "resentful", "indecisive", "melancholic"]
        self.personality_neutral = ["curious", "quiet", "reserved", "eccentric", "mysterious", "enigmatic", "stoic", "pragmatic", "analytical", "observant", "cautious", "methodical", "unpredictable", "enigmatic", "enigmatic"]

        # Motivations by archetype
        self.motivations = {
            Archetype.HERO: ["to protect the innocent", "to seek justice", "to save the world", "to redeem themselves", "to fulfill a prophecy"],
            Archetype.ANTIHERO: ["to survive", "to gain power", "to seek revenge", "to find meaning", "to challenge the status quo", "to escape their past", "to prove themselves"],
            Archetype.MENTOR: ["to guide the next generation", "to impart wisdom", "to atone for past mistakes", "to protect their legacy", "to find a worthy successor"],
            Archetype.TRICKSTER: ["to cause chaos", "to challenge authority", "to entertain themselves", "to expose hypocrisy", "to outsmart others"],
            Archetype.GUARDIAN: ["to protect a sacred place", "to guard a powerful artifact", "to defend their people", "to uphold a sacred duty", "to prevent a catastrophe"],
            Archetype.VILLAIN: ["to conquer the world", "to destroy their enemies", "to gain ultimate power", "to enact revenge", "to reshape reality", "to prove their superiority"],
            Archetype.OUTCAST: ["to find acceptance", "to seek revenge on those who rejected them", "to discover their true identity", "to create a new home", "to prove their worth"],
            Archetype.SCHOLAR: ["to uncover hidden knowledge", "to solve a great mystery", "to push the boundaries of understanding", "to preserve ancient wisdom", "to achieve intellectual greatness"]
        }

        # Birthplaces
        self.birthplaces = [
            "a bustling city", "a remote village", "a noble estate", "a war-torn region", "a mystical forest", "a coastal town", "a hidden sanctuary", "a desolate wasteland",
            "a mountain stronghold", "a nomadic tribe", "a secret society", "a magical academy", "a forgotten ruin", "a prosperous kingdom", "a cursed land", "a distant planet",
            "a floating city", "a subterranean cavern", "a celestial realm", "a post-apocalyptic world", "a parallel dimension"
        ]

        # Defining moments
        self.tragedy_moments = [
            "witnessing the death of a loved one", "being betrayed by a close friend", "suffering a great loss", "facing a life-threatening illness", "enduring a traumatic event",
            "being exiled from their home", "losing everything they hold dear", "failing to save someone important", "being falsely accused of a crime", "experiencing a devastating defeat"
            "uncovering a dark family secret", "being betrayed by a mentor", "facing a moral dilemma that leads to tragedy", "sacrificing something precious for the greater good", "being manipulated into causing harm to others"
        ]

        self.triumph_moments = [
            "saving someone from danger", "overcoming a great obstacle", "achieving a lifelong dream", "defeating a powerful enemy", "uniting warring factions",
            "discovering a hidden talent", "forming a powerful alliance", "outsmarting a formidable opponent", "surviving against all odds", "redeeming themselves in the eyes of others"
            "uncovering a long-lost artifact that changes the course of history", "sacrificing their own happiness for the greater good and being celebrated as a hero", "outwitting a cunning adversary and emerging victorious against all odds"
        ]

        self.revelation_moments = [
            "discovering a hidden truth about their past", "realizing they were manipulated by someone they trusted", "uncovering a conspiracy that changes their worldview", "learning a shocking secret about their family", "realizing they have a hidden power or destiny"
            "discovering that their greatest enemy is actually a close friend or family member", "realizing that their core motivation is based on a false premise and having to reevaluate their goals", "uncovering a hidden aspect of their identity that challenges everything they thought they knew about themselves"
        ]

        # Key relationships
        self.relationships = [
            {"name": "A childhood friend", "relationship": "ally", "status": "complicated"},
            {"name": "A mentor figure", "relationship": "mentor", "status": "deceased"},
            {"name": "A rival", "relationship": "rival", "status": "active"},
            {"name": "A love interest", "relationship": "romantic", "status": "estranged"},
            {"name": "A family member", "relationship": "family", "status": "distant"},
            {"name": "An old enemy", "relationship": "antagonist", "status": "defeated"},
            {"name": "A mysterious stranger", "relationship": "unknown", "status": "ambiguous"}
        ]

        self.distinctive_features = [
            "a prominent scar across their face", "a unique birthmark in the shape of a star", "piercing green eyes that seem to see through people", "a distinctive tattoo that holds personal significance",
            "an unusual hairstyle that sets them apart", "a prosthetic limb that they have adapted to use with great skill", "a distinctive way of dressing that reflects their personality", "a unique accent or way of speaking",
            "a physical deformity that they have learned to embrace as part of their identity", "a signature piece of jewelry that they always wear", "a distinctive laugh that is instantly recognizable", "a unique mannerism that others find endearing or unsettling"
        ]

        self.fatal_flaws = [
            "pride that blinds them to their own weaknesses", "a quick temper that leads to rash decisions", "a tendency to trust the wrong people", "an obsession with revenge that consumes them", "a fear of abandonment that causes them to push others away",
            "a need for control that leads to micromanaging and alienating allies", "a tendency to take unnecessary risks in pursuit of their goals", "a deep-seated insecurity that undermines their confidence", "a stubborn refusal to change their ways even when it's clear they are wrong"
        ]

        self.greatest_fears = [
            "the loss of a loved one", "being alone", "failure", "betrayal", "death",
            "losing their sense of identity", "being powerless to protect those they care about", "facing the consequences of their actions", "being forgotten or erased from history"
        ]

        self.internal_conflicts = [
            "struggling between their desire for revenge and their need for redemption", "torn between their loyalty to their family and their personal ambitions", "grappling with feelings of guilt over past mistakes while trying to move forward", "torn between their desire for power and their fear of losing themselves in the process",
            "struggling to reconcile their public persona with their true self", "torn between their desire for acceptance and their need for independence", "grappling with feelings of inadequacy while trying to prove themselves to others"
        ]

        self.hidden_truths = [
            "they are the heir to a powerful and dangerous legacy that they were unaware of", "they have a hidden talent or ability that they have yet to discover", "they were manipulated into their current situation by someone they trusted", "they have a secret past that they have been trying to keep hidden",
            "they are connected to a larger conspiracy or plot that they are only beginning to uncover", "they have a hidden connection to a powerful figure or organization that they are unaware of", "they are destined for a great and dangerous fate that they have been trying to avoid"
        ]

    def generate(self, archetype: Optional[Archetype] = None,
                origin: Optional[Origin] = None,
                name: Optional[str] = None) -> CharacterLore:
        """Generate character lore
        
        Args:
            archetype: Character archetype (random if None)
            origin: Character origin (random if None)
            name: Character name (random if None)

        Returns:
            CharacterLore with complete backstory
        """

        archetype = archetype or random.choice(list(Archetype))
        origin = origin or random.choice(list(Origin))

        if not name:
            name = random.choice(self.names[origin])

        age_ranges = {
            Archetype.HERO: (20, 40),
            Archetype.ANTIHERO: (25, 45),
            Archetype.MENTOR: (50, 80),
            Archetype.TRICKSTER: (18, 35),
            Archetype.GUARDIAN: (30, 60),
            Archetype.VILLAIN: (30, 60),
            Archetype.OUTCAST: (20, 40),
            Archetype.SCHOLAR: (30, 70)
        }
        min_age, max_age = age_ranges[archetype]
        age = random.randint(min_age, max_age)

        traits = []
        traits.append(random.choice(self.personality_positive))
        traits.append(random.choice(self.personality_negative))
        traits.append(random.choice(self.personality_neutral))
        if random.random() > 0.5:
            traits.append(random.choice(self.personality_positive + self.personality_neutral))

        core_motivation = random.choice(self.motivations[archetype])
        fatal_flaw = random.choice(self.fatal_flaws)
        greatest_fear = random.choice(self.greatest_fears)
        internal_conflict = random.choice(self.internal_conflicts)
        hidden_truth = random.choice(self.hidden_truths) if random.random() < self.params.mystery_factor else None

        birthplace = random.choice(self.birthplaces)

        defining_moments = []
        num_moments = self.params.complexity_weight

        for i in range(num_moments):
            if random.random() < self.params.tragedy_weight:
                moment = random.choice(self.tragedy_moments)
            else:
                moment = random.choice(self.revelation_moments)
            defining_moments.append(moment)
        
        key_relationships = []
        num_relationships = self.params.relationship_weight
        
        for _ in range(num_relationships):
            rel = random.choice(self.relationships)
            rel_name = random.choice(self.names[random.choice(list(Origin))])
            
            key_relationships.append({
                "name": rel_name,
                "relationship": rel["relationship"],
                "status": rel["status"]
            })

        distinctive_features = random.choice(self.distinctive_features)

        return CharacterLore(
            name = name,
            age = age,
            archetype = archetype,
            personality_traits = traits,
            distinctive_features = distinctive_features,
            origin = origin,
            birthplace = birthplace,
            defining_moments = defining_moments,
            core_motivation = core_motivation,
            fatal_flaw = fatal_flaw,
            greatest_fear = greatest_fear,
            internal_conflict = internal_conflict,
            hidden_truth = hidden_truth,
            key_relationships = key_relationships
        )

def main():
    """Demo showing lore generation"""
    print("=== Character Lore Generator ===\n")

    generator = LoreGenerator()

    print("Generating 3 characters with different parameters...\n")
    print("\n" + "="*40 + "\n")

    print("\n1. Tragic Hero:\n")
    params1 = LoreParameters.tragic_hero()
    character1 = generator.generate(archetype=Archetype.HERO, origin=Origin.NOBLE)
    print(character1.to_narrative())

    print("\n" + "="*40 + "\n")

    print("\n2. Mysterious Stranger:\n")
    params2 = LoreParameters.mysterious_stranger()
    character2 = generator.generate(archetype=Archetype.TRICKSTER, origin=Origin.EXILE)
    print(character2.to_narrative())

    print("\n" + "="*40 + "\n")

    print("\n3. Epic Villain:\n")
    params3 = LoreParameters.epic_villain()
    character3 = generator.generate(archetype=Archetype.VILLAIN, origin=Origin.ACADEMIC)
    print(character3.to_narrative())

if __name__ == "__main__":
    main()
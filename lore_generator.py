import random
from dataclasses import dataclass
from typing import List, Optional, Dict
from enum import Enum
import json

class Archetype(Enum):
    """Defines Character Archetypes"""
    HERO = "Hero"
    ANTIHERO = "Antihero"
    MENTOR = "Mentor"
    TRICKSTER = "Trickster"
    GUARDIAN = "Guardian"
    VILLAIN = "Villain"
    OUTCAST = "Outcast"
    SCHOLAR = "Scholar"

class Origin(Enum):
    """Defines Character Origins"""
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
    """Adjustable Parameters for Lore Generation"""
    tragedy_weight: float = 0.5 # 0-1
    complexity_weight: int = 3 # 1-5
    relationship_weight: int = 2 # 1-5
    mystery_factor: float = 0.3 # 0-1
    power_scale: int = 3 # 1-5

    @classmethod
    def from_json(cls, filepath: str) -> 'LoreParameters':
        """Load Parameters from JSON File"""
        with open(filepath, 'r') as f:
            data = json.load(f)
        return cls(**data)
    
    @classmethod
    def default(cls) -> 'LoreParameters':
        """Default Parameters"""
        return cls()

    @classmethod
    def tragic_hero(cls) -> 'LoreParameters':
        """Preset for Tragic Hero Archetype"""
        return cls(tragedy_weight = 0.8, complexity_weight = 4, mystery_factor = 0.2)

    @classmethod
    def mysterious_stranger(cls) -> 'LoreParameters':
        """Preset for Mysterious Stranger Archetype"""
        return cls(complexity_weight = 2, relationship_weight = 1, mystery_factor = 0.7)

    @classmethod
    def epic_villain(cls) -> 'LoreParameters':
        """Preset for Epic Villain Archetype"""
        return cls(tragedy_weight = 0.6, complexity_weight = 5, relationship_weight = 3, power_scale = 5)

@dataclass
class CharacterLore:
    """Generated Lore Output"""
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
        """Converts Lore to Narrative Format"""
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
            sections.append(f"Hidden Truth: {self.hidden_truth}")

        if self.key_relationships:
            sections.append("\n## Relationships")
            for rel in self.key_relationships:
                sections.append(f"- **{rel['name']}** ({rel['relationship']}): {rel['status']}")
            sections.append("")
        
        return "\n".join(sections)

class LoreGenerator:
    """Main Character Lore Generator"""

    def __init__(self, params: Optional[LoreParameters] = None):
        self.params = params or LoreParameters.default()
        self._load_generation_data()

    def _load_generation_data(self):
        """Load All the Generation Data"""

        # Names by origin
        self.names = {
            Origin.NOBLE: [
                "Ada",
                "Adalbern",
                "Adalbert",
                "Adalfarus",
                "Adalgard",
                "Adaline",
                "Adalwin",
                "Adelina",
                "Aenor",
                "Alaric",
                "Aldina",
                "Alistair",
                "Alphonzo",
                "Athena",
                "Baal",
                "Baldric",
                "Belinda",
                "Bujar",
                "Cecily",
                "Cedric",
                "Charlotte",
                "Clytemnestra",
                "Conrad",
                "Constantine",
                "Delphine",
                "Dimitri",
                "Dorian",
                "Edelmiro",
                "Eleanor",
                "Elric",
                "Folasade",
                "Gabriel",
                "Generosa",
                "Gideon",
                "Giselle",
                "Herleva",
                "Isabella",
                "Ketevan",
                "Klytios",
                "Maëly",
                "Makram",
                "Maria",
                "Maximilian",
                "Melisande",
                "Mordecai",
                "Nabil",
                "Otto",
                "Patrekur",
                "Raine",
                "Raphaela",
                "Willa",
                "Yorath"
                ],

            Origin.COMMONER: [
                "Agatha",
                "Adam",
                "Alan",
                "Agnes",
                "Amice",
                "Andrew",
                "Annabel",
                "Anthony",
                "Beatrice",
                "Bernard",
                "Bert",
                "Benjamin",
                "Cathy",
                "Clement",
                "Denise",
                "David",
                "Daniel",
                "Ellen",
                "Edward",
                "Fiona",
                "Frank",
                "Grace",
                "George",
                "Hannah",
                "Henry",
                "Irene",
                "Jack",
                "Jane",
                "Kevin",
                "Laura",
                "Michael",
                "Mary",
                "Nathan",
                "Olivia",
                "Paul",
                "Rachel",
                "Richard",
                "Sarah",
                "Steven",
                "Susan",
                "Thomas",
                "Tim",
                "William"
                ],

            Origin.ORPHAN: [
                "Aria",
                "Angela",
                "Annie",
                "Bobby",
                "Betsy",
                "Brenda",
                "Cossette",
                "Charlie",
                "Cindy",
                "Dinky",
                "Dolly",
                "Eddie",
                "Emily",
                "Elora",
                "Fanny",
                "Freddie",
                "Gina",
                "Gus",
                "Holly",
                "Harry",
                "Huey",
                "Karai",
                "Kiki",
                "Lucky",
                "Lola",
                "Maggie",
                "Nami",
                "Nico",
                "Parker",
                ],

            Origin.EXILE: [
                "Avah",
                "Bastian",
                "Cyrus",
                "Dahlia",
                "Durk",
                "Eira",
                "Ezekiel",
                "Freyja",
                "Gunther",
                "Harvey",
                "Heck",
                "Jeb",
                "Johnnie",
                "Kandi",
                "Klaus",
                "Lazlo",
                "Luna",
                "Mick",
                "Spike",
                "Tex",
                "Tottie",
                "Woodie"
                ],

            Origin.CRIMINAL: [
                "Adolfito",
                "Ali",
                "Chuckie",
                "Django",
                "Gholam",
                "Gobnet",
                "Jaxx",
                "Katarina",
                "Lazaro",
                "Lupo",
                "Mara",
                "Maverick",
                "Nina",
                "Rico",
                "Rosa",
                "Salvatore",
                "Sombra",
                "Talon",
                ],

            Origin.MILITARY: [
                "Aleksandr",
                "Alfred",
                "Ambrose",
                "Amir",
                "Anastasia",
                "Andrei",
                "Anika",
                "Anton",
                "Artemis",
                "Boris",
                "Bruno",
                "Charlemagne",
                "Claude",
                "Dmitry",
                "Elazar",
                "Emil",
                "Ferdinand",
                "Francis",
                "Friedrich",
                "Gaius",
                "Geronimo",
                "Gustav",
                "Hector",
                "Idris",
                "Joseph",
                "Lyudmila",
                "Marie",
                "Maurice",
                "Valeriy"
                ],

            Origin.ACADEMIC: [
                "Abraham",
                "Ada",
                "Adam",
                "Adolf",
                "Ahmad",
                "Alan",
                "Alexander",
                "Alexis",
                "Ali",
                "Amalie",
                "Anne",
                "Antoine",
                "Arthur",
                "Bernhard",
                "Blaise",
                "Cassius",
                "Christoph",
                "Claudius",
                "Denis",
                "Domenico",
                "Edmund",
                "Erich",
                "Ferdinand",
                "Godfrey",
                "Gottfried",
                "Harold",
                "Jay",
                "Johannes",
                "Ludwig",
                "Mani",
                "Oswald",
                "Pascal",
                ],

            Origin.MYSTIC: [
                "Amaterasu",
                "Annei",
                "Ashtoreth",
                "Astarte",
                "Dagan",
                "Izanagi",
                "Marduk",
                "Marzanna",
                "Morana",
                "Morgana",
                "Morena",
                "Nabu",
                "Nikolaos",
                "Ningal",
                ]
        }

        # Personality traits
        self.personality_positive = [
            "assertive",
            "astute",
            "decisive",
            "eloquent",
            "innovative",
            "intuitive",
            "logical",
            "pioneering",
            "practical",
            "pragmatic",
            "rational",
            "realistic",
            "resilient",
            "reflective",
            "resourceful",
            "self-disciplined",
            "spirited",
            "unwavering",
            "visionary",
            "creative",
            "eccentric",
            "adventurous",
            "caring",
            "charismatic",
            "caring",
            "confident",
            "cooperative",
            "generous",
            "gracious",
            "honest",
            "humorous",
            "loyal",
            "optimistic",
            "passionate",
            "patient",
            "punctual",
            "sociable",
            "supportive",
            "forgiving",
            "friendly",
            "humble",
            "sincere",
            "trustworthy",
        ]
        
        self.personality_negative = [
            "aggressive",
            "arrogant",
            "apathetic",
            "arrogant",
            "boastful",
            "careless",
            "complacent",
            "conceited",
            "cowardly",
            "cruel",
            "deceitful",
            "defensive",
            "defiant",
            "distrustful",
            "disloyal",
            "disrespectful",
            "domineering",
            "egotistical",
            "envious",
            "greedy",
            "hypocritical",
            "impulsive",
            "inconsiderate",
            "inflexible",
            "invasive",
            "judgmental",
            "malicious",
            "manipulative",
            "materialistic",
            "narcissistic",
            "narrow-minded",
            "obnoxious",
            "pessimistic",
            "reckless",
            "ruthless",
            "spiteful",
            "stubborn",
            "vengeful",
            "vindictive",
        ]
        
        self.personality_neutral = [
            "analytical",
            "blunt",
            "cautious",
            "conscientious",
            "curious",
            "candid"
            "competitive",
            "decisive",
            "direct"
            "flexible",
            "independent",
            "inquisitive",
            "methodical",
            "objective",
            "observant",
            "perceptive",
            "practical",
            "perfectionist",
            "rational",
            "reflective",
            "reserved",
            "spontaneous",
            "studious",
            "sensitive",
            "quiet"
        ]

        # Motivations by archetype
        self.motivations = {
            Archetype.HERO: [
                "to fulfill a prophecy they were born into",
                "to honor the sacrifice of someone who died protecting them",
                "to find a cure for a plague devastating their homeland",
                "to reunite a world torn apart by civil war",
                "to break a generational curse that haunts their bloodline",
                "to give a voice to those who have been silenced",
                "to return something stolen from its rightful people",
                "to earn back honor their family lost long ago",
                "to keep a deathbed promise that grows heavier each day",
                "to dismantle a system that preys on the powerless",
                "to find the missing people no one else will search for",
                "to repay a debt of kindness that once saved their life",
                "to ensure a tragedy they witnessed never happens again",
                "to reclaim a homeland that was taken by force",
                "to build something worth defending in a world that only destroys",
                "to be worthy of the trust others place in them",
                "to confront the evil they were once too young to fight",
                "to answer the call that everyone else is too afraid to answer",
                "to protect the innocent from a threat that has been ignored for too long",
                "to destory a powerful government or organization that is oppressing people",
                "to find a way to save someone they love who is dying or in danger",
                "to fix a mistake they made in the past that had devastating consequences",
                ],

            Archetype.ANTIHERO: [
                "to settle a personal score while the world sorts itself out", 
                "to protect the few people left who haven't betrayed them", 
                "to prove they can still do something good despite everything they've done wrong", 
                "to repay a debt to someone who didn't deserve what happened to them", 
                "to drag the truth into the light even if it makes them the villain", 
                "to quiet the guilt that follows them like a second shadow", 
                "to dismantle something rotten from the inside out", 
                "to make amends without ever admitting they were wrong", 
                "to finish a fight they didn't start but refuse to lose", 
                "to destroy the thing they helped create before it hurts anyone else", 
                "to walk the line between justice and vengeance and not care which side they fall on", 
                "to take from the powerful and never apologize for it",
                "to save someone who reminds them of who they used to be",
                "to confront the part of themselves they pretend doesn't exist"
                ],

            Archetype.MENTOR: [
                "to prepare someone for a burden they themselves could not carry", 
                "to correct the mistakes they made with their first student", 
                "to find a successor worthy of a dangerous inheritance", 
                "to make peace with their legacy before the end comes", 
                "to unburden themselves of secrets too heavy to carry alone", 
                "to build something that outlasts their own mortality", 
                "to watch the world change in ways they can no longer change it themselves", 
                "to reconnect with the world through someone who still believes in it", 
                "to delay an inevitable catastrophe by one more generation", 
                "to ensure the survival of a tradition", 
                "to prepare someone for a great challenge",
                "to keep alive a tradition the world is trying to forget",
                "to fulfill the final wish of someone who once mentored them"
                ],

            Archetype.TRICKSTER: [
                "to cause chaos", 
                "to challenge authority", 
                "to entertain themselves", 
                "to expose hypocrisy", 
                "to outsmart others", 
                "to find amusement in the misfortune of others", 
                "to disrupt the status quo for fun", 
                "to pull off a great heist or con", 
                "to escape from a dangerous situation", 
                "to create a memorable story about themselves", 
                "to test the limits of their own cleverness", 
                "to find a way to get what they want without getting caught"
                ],

            Archetype.GUARDIAN: [
                "to defend a place that holds the memory of everyone they've lost", 
                "to keep a sacred oath sworn to someone who can no longer hold them to it", 
                "to protect a secret that would cause war if it were ever revealed", 
                "to preserve the one safe place left in a world that has gone dark", 
                "to prevent an ancient evil from being awakened by the careless or the ambitious", 
                "to ensure that a powerful artifact never falls into the wrong hands", 
                "to protect the innocent from a threat they don't even know exists", 
                "to shelter those who have nowhere else to go",
                "to safeguard a forbidden knowledge that is both dangerous and necessary",
                "to protect a child whose existence threatens empires",
                "to guard the truth until the world is wise enough to hear it"
                ],

            Archetype.VILLAIN: [
                "to prove that the system only rewards cruelty, so they became the cruelest", 
                "to ensure no one ever has power over them again", 
                "to punish a society that stood by and watched them suffer", 
                "to claim the throne that was denied to them by birthright", 
                "to force the world to acknowledge their existence", 
                "to expose the corruption that hides behind noble faces", 
                "to achieve the immortality that makes all other concerns irrelevant", 
                "to become so powerful that betrayal becomes impossible", 
                "to complete the work of someone who was destroyed for trying", 
                "to complete the work of someone who was destroyed for trying",
                "to turn the very people who abandoned them into believers",
                "to possess the one thing that was always kept out of their reach",
                "to silence the voice in their head that says they are nothing",
                "to make the world feel the same helplessness they once felt",
                "to prove that mercy is an illusion the powerful use to control the weak",
                "to collapse the divide between what is feared and what is worshipped",
                "to become the monster the world already decided they were" 
                ],

            Archetype.OUTCAST: [
                "to find a place where they are not defined by what made them different", 
                "to prove that the people who cast them out were wrong about them", 
                "to build a home in a world that refuses to give them one", 
                "to find others like them and create a safe haven for those who are deemed unworthy or different by society", 
                "to turn the thing that made them an outcast into their greatest strength",
                "to earn acceptance without sacrificing what makes them who they are",
                "to protect other outcasts from the cruelty they endured",
                "to dismantle the rigid boundaries that decide who belongs and who doesn't",
                "to make peace with the fact that they may never belong anywhere",
                "to uncover the conspiracy that led to their banishment",
                "to find the family they were separated from before they can remember",
                "to discover the truth behind their exile that no one will tell them",
                "to answer the question of whether they were cast out or set free"
            ],

            Archetype.SCHOLAR: [
                "to decipher an ancient text that holds the key to a forgotten catastrophe", 
                "to prove a theory that the academic establishment refuses to acknowledge", 
                "to recover lost knowledge that was deliberately destroyed", 
                "to complete the unfinished life's work of a mentor who died under mysterious circumstances", 
                "to catalogue the last remnants of a dying civilization before they vanish",
                "to unlock the secrets of a power source that could save or destroy everything",
                "to answer the one question that has haunted them since childhood",
                "to prevent dangerous knowledge from being weaponized by those who don't understand it",
                "to solve the puzzle that drove their predecessor to madness",
                "to untangle the web of misinformation that has corrupted a fundamental truth",
                "to understand the nature of a curse or affliction that has no known origin",
                "to decode the language of a species or entity that no one else believes is real"
            ]
        }

        # Birthplaces
        self.birthplaces = [
            "a bustling city", 
            "a remote village", 
            "a noble estate", 
            "a war-torn region", 
            "a mystical forest", 
            "a coastal town", 
            "a hidden sanctuary", 
            "a desolate wasteland",
            "a mountain stronghold", 
            "a nomadic tribe", 
            "a secret society", 
            "a magical academy", 
            "a forgotten ruin", 
            "a prosperous kingdom", 
            "a cursed land", 
            "a distant planet",
            "a floating city", 
            "a subterranean cavern", 
            "a celestial realm", 
            "a post-apocalyptic world", 
            "a parallel dimension"
        ]

        # Defining moments
        self.tragedy_moments = [
            "witnessing the death of a loved one", 
            "being betrayed by a close friend", 
            "suffering a great loss", 
            "facing a life-threatening illness", 
            "enduring a traumatic event",
            "being exiled from their home", 
            "losing everything they hold dear", 
            "failing to save someone important", 
            "being falsely accused of a crime", 
            "experiencing a devastating defeat",
            "uncovering a dark family secret", 
            "being betrayed by a mentor", 
            "facing a moral dilemma that leads to tragedy", 
            "sacrificing something precious for the greater good", 
            "being manipulated into causing harm to others"
        ]

        self.triumph_moments = [
            "saving someone from danger", 
            "overcoming a great obstacle", 
            "achieving a lifelong dream", 
            "defeating a powerful enemy", 
            "uniting warring factions",
            "discovering a hidden talent", 
            "forming a powerful alliance", 
            "outsmarting a formidable opponent", 
            "surviving against all odds", 
            "redeeming themselves in the eyes of others",
            "uncovering a long-lost artifact that changes the course of history", 
            "sacrificing their own happiness for the greater good and being celebrated as a hero", 
            "outwitting a cunning adversary and emerging victorious against all odds"
        ]

        self.revelation_moments = [
            "discovering a hidden truth about their past", 
            "realizing they were manipulated by someone they trusted", 
            "uncovering a conspiracy that changes their worldview", 
            "learning a shocking secret about their family", 
            "realizing they have a hidden power or destiny",
            "discovering that their greatest enemy is actually a close friend or family member", 
            "realizing that their core motivation is based on a false premise and having to reevaluate their goals", 
            "uncovering a hidden aspect of their identity that challenges everything they thought they knew about themselves"
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
            "a prominent scar across their face", 
            "a unique birthmark in the shape of a star", 
            "piercing green eyes that seem to see through people", 
            "a distinctive tattoo that holds personal significance",
            "an unusual hairstyle that sets them apart",
            "a prosthetic limb that they have adapted to use with great skill", 
            "a distinctive way of dressing that reflects their personality", 
            "a unique accent or way of speaking",
            "a physical deformity that they have learned to embrace as part of their identity", 
            "a signature piece of jewelry that they always wear", 
            "a distinctive laugh that is instantly recognizable", 
            "a unique mannerism that others find endearing or unsettling"
        ]

        self.fatal_flaws = [
            "pride that blinds them to their own weaknesses", 
            "a quick temper that leads to rash decisions", 
            "a tendency to trust the wrong people", 
            "an obsession with revenge that consumes them", 
            "a fear of abandonment that causes them to push others away",
            "a need for control that leads to micromanaging and alienating allies", 
            "a tendency to take unnecessary risks in pursuit of their goals", 
            "a deep-seated insecurity that undermines their confidence", 
            "a stubborn refusal to change their ways even when it's clear they are wrong"
        ]

        self.greatest_fears = [
            "the loss of a loved one", 
            "being alone", 
            "failure", 
            "betrayal", 
            "death",
            "losing their sense of identity", 
            "being powerless to protect those they care about", 
            "facing the consequences of their actions", 
            "being forgotten or erased from history"
        ]

        self.internal_conflicts = [
            "struggling between their desire for revenge and their need for redemption", 
            "torn between their loyalty to their family and their personal ambitions", 
            "grappling with feelings of guilt over past mistakes while trying to move forward", 
            "torn between their desire for power and their fear of losing themselves in the process",
            "struggling to reconcile their public persona with their true self", 
            "torn between their desire for acceptance and their need for independence", 
            "grappling with feelings of inadequacy while trying to prove themselves to others"
        ]

        self.hidden_truths = [
            "they are the heir to a powerful and dangerous legacy that they were unaware of", 
            "they have a hidden talent or ability that they have yet to discover", 
            "they were manipulated into their current situation by someone they trusted", 
            "they have a secret past that they have been trying to keep hidden",
            "they are connected to a larger conspiracy or plot that they are only beginning to uncover", 
            "they have a hidden connection to a powerful figure or organization that they are unaware of", 
            "they are destined for a great and dangerous fate that they have been trying to avoid"
        ]

    def generate(self, archetype: Optional[Archetype] = None,
                origin: Optional[Origin] = None,
                name: Optional[str] = None) -> CharacterLore:
        """Generate Character Lore
        
        Args:
            Archetype: Character Archetype (random if None)
            Origin: Character Origin (random if None)
            Name: Character Name (random if None)

        Returns:
            Character Lore with Complete Backstory
        """

        archetype = archetype or random.choice(list(Archetype))
        origin = origin or random.choice(list(Origin))

        if not name:
            name = random.choice(self.names[origin])

        age_ranges = {
            Archetype.HERO: (16, 25),
            Archetype.ANTIHERO: (25, 40),
            Archetype.MENTOR: (60, 85),
            Archetype.TRICKSTER: (14, 30),
            Archetype.GUARDIAN: (35, 60),
            Archetype.VILLAIN: (25, 60),
            Archetype.OUTCAST: (18, 40),
            Archetype.SCHOLAR: (24, 70)
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
        seen_moments = set()
        attempts = 0
        max_attempts = max(10, num_moments * 10)

        while len(defining_moments) < num_moments and attempts < max_attempts:
            if random.random() < self.params.tragedy_weight:
                moment = random.choice(self.tragedy_moments)
            else:
                moment = random.choice(self.revelation_moments)
            if moment not in seen_moments:
                seen_moments.add(moment)
                defining_moments.append(moment)
            attempts += 1

        if len(defining_moments) < num_moments:
            remaining = [
                moment for moment in (self.tragedy_moments + self.revelation_moments)
                if moment not in seen_moments
            ]
            for moment in remaining:
                if len(defining_moments) >= num_moments:
                    break
                seen_moments.add(moment)
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
    """Demo Showing Lore Generation"""
    print("=== Character Lore Generator ===\n")

    generator = LoreGenerator()

    print("Generating 3 Characters with Different Parameters...\n")
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
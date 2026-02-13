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
                sections.append(f"- **{rel['name']}** ({rel['role']}): {rel['description']}")
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
            "Assertive",
            "Astute",
            "Decisive",
            "Eloquent",
            "Innovative",
            "Intuitive",
            "Logical",
            "Pioneering",
            "Practical",
            "Pragmatic",
            "Rational",
            "Realistic",
            "Resilient",
            "Reflective",
            "Resourceful",
            "Self-disciplined",
            "Spirited",
            "Unwavering",
            "Visionary",
            "Creative",
            "Eccentric",
            "Adventurous",
            "Caring",
            "Charismatic",
            "Caring",
            "Confident",
            "Cooperative",
            "Generous",
            "Gracious",
            "Honest",
            "Humorous",
            "Loyal",
            "Optimistic",
            "Passionate",
            "Patient",
            "Punctual",
            "Sociable",
            "Supportive",
            "Forgiving",
            "Friendly",
            "Humble",
            "Sincere",
            "Trustworthy",
        ]
        
        self.personality_negative = [
            "Aggressive",
            "Arrogant",
            "Apathetic",
            "Arrogant",
            "Boastful",
            "Careless",
            "Complacent",
            "Conceited",
            "Cowardly",
            "Cruel",
            "Deceitful",
            "Defensive",
            "Defiant",
            "Distrustful",
            "Disloyal",
            "Disrespectful",
            "Domineering",
            "Egotistical",
            "Envious",
            "Greedy",
            "Hypocritical",
            "Impulsive",
            "Inconsiderate",
            "Inflexible",
            "Invasive",
            "Judgmental",
            "Malicious",
            "Manipulative",
            "Materialistic",
            "Narcissistic",
            "Narrow-minded",
            "Obnoxious",
            "Pessimistic",
            "Reckless",
            "Ruthless",
            "Spiteful",
            "Stubborn",
            "Vengeful",
            "Vindictive",
        ]
        
        self.personality_neutral = [
            "Analytical",
            "Blunt",
            "Cautious",
            "Conscientious",
            "Curious",
            "Candid",
            "Competitive",
            "Decisive",
            "Direct",
            "Flexible",
            "Independent",
            "Inquisitive",
            "Methodical",
            "Objective",
            "Observant",
            "Perceptive",
            "Practical",
            "Perfectionist",
            "Rational",
            "Reflective",
            "Reserved",
            "Spontaneous",
            "Studious",
            "Sensitive",
            "Quiet"
        ]

        # Motivations by archetype
        self.motivations = {
            Archetype.HERO: [
                "To fulfill a prophecy they were born into",
                "To honor the sacrifice of someone who died protecting them",
                "To find a cure for a plague devastating their homeland",
                "To reunite a world torn apart by civil war",
                "To break a generational curse that haunts their bloodline",
                "To give a voice to those who have been silenced",
                "To return something stolen from its rightful people",
                "To earn back honor their family lost long ago",
                "To keep a deathbed promise that grows heavier each day",
                "To dismantle a system that preys on the powerless",
                "To find the missing people no one else will search for",
                "To repay a debt of kindness that once saved their life",
                "To ensure a tragedy they witnessed never happens again",
                "To reclaim a homeland that was taken by force",
                "To build something worth defending in a world that only destroys",
                "To be worthy of the trust others place in them",
                "To confront the evil they were once too young to fight",
                "To answer the call that everyone else is too afraid to answer",
                "To protect the innocent from a threat that has been ignored for too long",
                "To destroy a powerful government or organization that is oppressing people",
                "To find a way to save someone they love who is dying or in danger",
                "To fix a mistake they made in the past that had devastating consequences",
                ],

            Archetype.ANTIHERO: [
                "To settle a personal score while the world sorts itself out", 
                "To protect the few people left who haven't betrayed them", 
                "To prove they can still do something good despite everything they've done wrong", 
                "To repay a debt to someone who didn't deserve what happened to them", 
                "To drag the truth into the light even if it makes them the villain", 
                "To quiet the guilt that follows them like a second shadow", 
                "To dismantle something rotten from the inside out", 
                "To make amends without ever admitting they were wrong", 
                "To finish a fight they didn't start but refuse to lose", 
                "To destroy the thing they helped create before it hurts anyone else", 
                "To walk the line between justice and vengeance and not care which side they fall on", 
                "To take from the powerful and never apologize for it",
                "To save someone who reminds them of who they used to be",
                "To confront the part of themselves they pretend doesn't exist"
                ],

            Archetype.MENTOR: [
                "To prepare someone for a burden they themselves could not carry", 
                "To correct the mistakes they made with their first student", 
                "To find a successor worthy of a dangerous inheritance", 
                "To make peace with their legacy before the end comes", 
                "To unburden themselves of secrets too heavy to carry alone", 
                "To build something that outlasts their own mortality", 
                "To watch the world change in ways they can no longer change it themselves", 
                "To reconnect with the world through someone who still believes in it", 
                "To delay an inevitable catastrophe by one more generation", 
                "To ensure the survival of a tradition", 
                "To prepare someone for a great challenge",
                "To keep alive a tradition the world is trying to forget",
                "To fulfill the final wish of someone who once mentored them"
                ],

            Archetype.TRICKSTER: [
                "To cause chaos", 
                "To challenge authority", 
                "To entertain themselves", 
                "To expose hypocrisy", 
                "To outsmart others", 
                "To find amusement in the misfortune of others", 
                "To disrupt the status quo for fun", 
                "To pull off a great heist or con", 
                "To escape from a dangerous situation", 
                "To create a memorable story about themselves", 
                "To test the limits of their own cleverness", 
                "To find a way to get what they want without getting caught"
                ],

            Archetype.GUARDIAN: [
                "To defend a place that holds the memory of everyone they've lost", 
                "To keep a sacred oath sworn to someone who can no longer hold them to it", 
                "To protect a secret that would cause war if it were ever revealed", 
                "To preserve the one safe place left in a world that has gone dark", 
                "To prevent an ancient evil from being awakened by the careless or the ambitious", 
                "To ensure that a powerful artifact never falls into the wrong hands", 
                "To protect the innocent from a threat they don't even know exists", 
                "To shelter those who have nowhere else to go",
                "To safeguard a forbidden knowledge that is both dangerous and necessary",
                "To protect a child whose existence threatens empires",
                "To guard the truth until the world is wise enough to hear it"
                ],

            Archetype.VILLAIN: [
                "To prove that the system only rewards cruelty, so they became the cruelest", 
                "To ensure no one ever has power over them again", 
                "To punish a society that stood by and watched them suffer", 
                "To claim the throne that was denied to them by birthright", 
                "To force the world to acknowledge their existence", 
                "To expose the corruption that hides behind noble faces", 
                "To achieve the immortality that makes all other concerns irrelevant", 
                "To become so powerful that betrayal becomes impossible", 
                "To complete the work of someone who was destroyed for trying", 
                "To complete the work of someone who was destroyed for trying",
                "To turn the very people who abandoned them into believers",
                "To possess the one thing that was always kept out of their reach",
                "To silence the voice in their head that says they are nothing",
                "To make the world feel the same helplessness they once felt",
                "To prove that mercy is an illusion the powerful use to control the weak",
                "To collapse the divide between what is feared and what is worshipped",
                "To become the monster the world already decided they were" 
                ],

            Archetype.OUTCAST: [
                "To find a place where they are not defined by what made them different", 
                "To prove that the people who cast them out were wrong about them", 
                "To build a home in a world that refuses to give them one", 
                "To find others like them and create a safe haven for those who are deemed unworthy or different by society", 
                "To turn the thing that made them an outcast into their greatest strength",
                "To earn acceptance without sacrificing what makes them who they are",
                "To dismantle the rigid boundaries that decide who belongs and who doesn't",
                "To make peace with the fact that they may never belong anywhere",
                "To uncover the conspiracy that led to their banishment",
                "To find the family they were separated from before they can remember",
                "To discover the truth behind their exile that no one will tell them",
                "To answer the question of whether they were cast out or set free"
            ],

            Archetype.SCHOLAR: [
                "To decipher an ancient text that holds the key to a forgotten catastrophe", 
                "To prove a theory that the academic establishment refuses to acknowledge", 
                "To recover lost knowledge that was deliberately destroyed", 
                "To complete the unfinished life's work of a mentor who died under mysterious circumstances", 
                "To catalogue the last remnants of a dying civilization before they vanish",
                "To unlock the secrets of a power source that could save or destroy everything",
                "To answer the one question that has haunted them since childhood",
                "To prevent dangerous knowledge from being weaponized by those who don't understand it",
                "To solve the puzzle that drove their predecessor to madness",
                "To untangle the web of misinformation that has corrupted a fundamental truth",
                "To understand the nature of a curse or affliction that has no known origin",
                "To decode the language of a species or entity that no one else believes is real"
            ]
        }

        # Birthplaces
        self.birthplaces = [
            "A bustling city", 
            "A remote village", 
            "A noble estate", 
            "A war-torn region", 
            "A mystical forest", 
            "A coastal town", 
            "A hidden sanctuary", 
            "A desolate wasteland",
            "A mountain stronghold", 
            "A nomadic tribe", 
            "A secret society", 
            "A magical academy", 
            "A forgotten ruin", 
            "A prosperous kingdom", 
            "A cursed land", 
            "A distant planet",
            "A floating city", 
            "A subterranean cavern", 
            "A celestial realm", 
            "A post-apocalyptic world", 
            "A parallel dimension"
        ]

        # Defining moments
        self.tragedy_moments = [
            "Witnessing the death of a loved one", 
            "Being betrayed by a close friend", 
            "Suffering a great loss", 
            "Facing a life-threatening illness", 
            "Enduring a traumatic event",
            "Being exiled from their home", 
            "Losing everything they hold dear", 
            "Failing to save someone important", 
            "Being falsely accused of a crime", 
            "Experiencing a devastating defeat",
            "Uncovering a dark family secret", 
            "Being betrayed by a mentor", 
            "Facing a moral dilemma that leads to tragedy", 
            "Sacrificing something precious for the greater good", 
            "Being manipulated into causing harm to others"
        ]

        self.triumph_moments = [
            "Saving someone from danger", 
            "Overcoming a great obstacle", 
            "Achieving a lifelong dream", 
            "Defeating a powerful enemy", 
            "Uniting warring factions",
            "Discovering a hidden talent", 
            "Forming a powerful alliance", 
            "Outsmarting a formidable opponent", 
            "Surviving against all odds", 
            "Redeeming themselves in the eyes of others",
            "Uncovering a long-lost artifact that changes the course of history", 
            "Sacrificing their own happiness for the greater good and being celebrated as a hero", 
            "Outwitting a cunning adversary and emerging victorious against all odds"
        ]

        self.revelation_moments = [
            "Discovering a hidden truth about their past", 
            "Realizing they were manipulated by someone they trusted", 
            "Uncovering a conspiracy that changes their worldview", 
            "Learning a shocking secret about their family", 
            "Realizing they have a hidden power or destiny",
            "Discovering that their greatest enemy is actually a close friend or family member", 
            "Realizing that their core motivation is based on a false premise and having to reevaluate their goals", 
            "Uncovering a hidden aspect of their identity that challenges everything they thought they knew about themselves"
        ]

        # Key relationships
        self.relationships = [
            {
                "role": "Childhood Friend",
                "descriptions": [
                    "Who has been by their side through the best and worst of times",
                    "Who knows all their secrets",
                    "Who has always believed in them even when no one else did",
                    "Who they lost touch with after a small argument that turned into a long-standing rift",
                    "Who they reconnected with after years of separation and found that they had changed in ways they never expected",
                    "Who they had a falling out with over a miscommunication where neither were capable of admitting they were wrong and it led to a permanent estrangement",
                    "Who helped them get through their darkest moments",
                    "Who they were never super close with, but always had a friendly relationship with and they always looked out for each other in small ways",
                    "Who they had a brief romantic relationship with that ended amicably but they still care for each other deeply",
                    "Who they had a brief romantic relationship with that ended badly and they haven't spoken since",
                ]
            },

            {
                "role": "Mentor",
                "descriptions": [
                    "Who taught them everything they know and shaped who they are today",
                    "Who they looked up to and wanted to be like, but they tragically lost them and they have never been able to replace that influence in their life",
                    "Who made them feel capable of more than just surviving and inspired them to pursue something greater than what has been expected of them",
                    "Who they trusted wholeheartedly, but chose to part ways after a major disagreement that they could never resolve or communicate about effectively",
                    "Who they viewed as a parental figure and has continued to stay by their side as a source of comfort, support, and guidance throughout their life",
                    "Who forced them to confront their deepest fears in order to become stronger, and able to withstand the challenges they would undeniably face in the future",
                    "Who committed their life to ensuring their survival and success, even at great personal cost",
                    "Who encouraged them to embrace their abilities and potential, unintentionally leading them down a path that has caused them great pain and suffering"
                ]
            },

            {
                "role": "Partner in Crime",
                "descriptions": [
                    "Who they met on a random adventure and they just clicked, becoming inseparable partners in crime and mischief",
                    "Who they met in a moment of chaos and they found peace in each other's company, forming a bond that has lasted through vast distances and long periods of separation",
                    "Who they share a similar outlook on life with, finding comfort in someone who is so similar",
                    "Who they would give their life for, but they have a complicated relationship with because they are so similar",
                    "Who they can fully trust with their life, but can never fully open up emotionally to",
                    "Who they share a similar past with, but they have a complicated realationship because of how they eventually grew up in different directions and situations",
                    "Who they didn't trust at first, until they were in a situation where they had to rely on each other completely",
                    "Who they met through a mutual friend, and quickly formed a deep understanding over the tragic events they have both experienced in their lives"
                ]    
            },

            {
                "role": "Rival",
                "descriptions": [
                    "Who indirectly pushes them to be better by being a constant source of competition and comparison",
                    "Who wants everything they have and will stop at nothing to get it, making them a constant low-level threat and bothersome presence in their life",
                    "Who was once a close friend, but jealousy and misunderstandings drove them apart and they have been bitter rivals ever since",
                    "Who they used to look up to, but they have become brainwashed by a toxic ideology and is no longer capable of recognizing right from wrong",
                    "Who they used to look up to, but they have become corrupted by power and greed",
                    "Who they used to view as family, but they betrayed them in an unforgivable manner, and nothing can repair the damage",
                    "Who seeks to destroy them and everything they care about, but underneath it all they hold a small fragment of admiration from the past"
                ]    
            },

            {
                "role": "Love Interest",
                "descriptions": [
                    "Who they met on a random adventure, and became inseparable partners in love and life, sharing an unbreakable bond that will last generations",
                    "Who they will lay down their life for without a second thought",
                    "Who makes their heart feel full, alive, and protected, in spite of the harsh and cruel world surrounding them",
                    "Who uplifts their dreams and ambitions, encouraging them to be the best version of themselves while still accepting their flaws and imperfections",
                    "Who reminds them that they are more than just the expectations and burdens they carry",
                    "Who walks beside them through the darkest, toughest times, and makes them feel like they are capable of even the most impossible feats as long as they have each other",
                    "Who always knows how to make them smile even after a long day, providing laughter and comfort in a dark world"
                ] 
            },

            {
                "role": "Mysterious Stranger",
                "descriptions": [
                    "Who appears in random moments of their life, offering cryptic, but valuable, advice that they don't understand until when they need it most",
                    "Who they met in a moment of unexpected kindness, and they have been trying to repay the kindness offered ever since",
                    "Who offers pieces of information about the future in exchange for small favors",
                    "Who offers pieces of information about the past in exchange for small favors",
                    "Who offers pieces of information about the present in exchange for small favors",
                    "Who seems to know more about them than they know about themselves",
                    "Who randomly appears in their life at moments of great need, offering tokens of help for a secret"
                ]    
            },
        ]

        self.distinctive_features = [
            "A prominent scar across their face", 
            "A unique birthmark in the shape of a star", 
            "Freckles that form a recognizable constellation",
            "Piercing colored eyes that shine in the dark", 
            "A distinctive tattoo that holds personal significance",
            "An unusual hairstyle that sets them apart",
            "A prosthetic limb that they have adapted to use with great skill", 
            "A distinctive way of dressing that makes them easily identifiable", 
            "A unique accent or way of speaking that is different from those around them",
            "A physical deformity that they have learned to embrace as part of their identity", 
            "A signature piece of jewelry that they always wear", 
            "A distinctive laugh that is instantly recognizable", 
            "A unique mannerism that others find endearing or unsettling",
            "A unique hairstyle that only they can pull off",
            "Colored hair that is not common in their world",
            "No eyebrows or eyelashes",
            "A voice that is unusually deep or high-pitched",
            "An extra finger that they have learned to use with surprising dexterity",
        ]

        self.fatal_flaws = [
            "Pride that blinds them to their own weaknesses", 
            "A quick temper that leads to rash decisions", 
            "A tendency to trust the wrong people", 
            "An obsession with revenge that consumes them", 
            "A fear of abandonment that causes them to push others away",
            "A need for control that leads to micromanaging and alienating allies", 
            "A tendency to take unnecessary risks in pursuit of their goals", 
            "A deep-seated insecurity that undermines their confidence", 
            "A stubborn refusal to change their ways even when it's clear they are wrong",
            "A tendency to overthink and second-guess themselves to the point of inaction",
            "A fear of failure that prevents them from taking necessary risks or pursuing their true potential",
            "A tendency to forgive too easily, allowing others to take advantage of their kindness and generosity",
            "A fear of intimacy that prevents them from forming close relationships",
            "A tendency to overcomplicate things, making simple problems more difficult than they need to be",
            "An obsession with needing to be wanted or needed by others, leading them to make sacrifices that ultimately harm themselves or those they care about",
            "A tendency to overthink and analyze every situation from a negative perspective, leading to believing the worst about themselves and others, even when there is evidence to the contrary",
            "A stubbornness that prevents them from admitting when they are wrong or accepting help from others, even when it would be in their best interest to do so",
            "A tendency to get aggressive or defensive when they feel threatened, leading to escalating conflicts that could have been avoided with better communication or emotional regulation",
            "A fear of being with someone that doesn't love them back, leading to unhealthy attachments or sabotaging potential relationships out of fear of rejection"
        ]

        self.greatest_fears = [
            "Being abandoned by those they care about with no explanation or warning", 
            "Feeling excruciating loneliness even when surrounded by others", 
            "Failure after putting everything and everyone on the line to achieve a goal they believed in", 
            "Betrayal by someone that had been with them from the beginning and had been trusted implicitly", 
            "Death to someone that didn't deserve it",
            "Losing their sense of identity from a toxic relationship or environment", 
            "Being powerless to protect those they care about", 
            "Being powerful but unable to control their abilities or influence, causing unintended harm to others", 
            "Being powerful, but powerless in the face of overwhelming odds or threats, causing devastation despite their best efforts",
            "Facing the consequences of their actions that they believed were justified", 
            "Being forgotten or erased from history despite their significant contributions and sacrifices",
            "Never living up to their potential despite their best efforts",
            "Never living up to the expectations they set for themselves",
            "Facing the inevitability of their own humanity and mortality",
            "Having to make a choice between two equally difficult paths",
            "Having to make a choice between saving someone they love and achieving a goal that could save many others",
        ]

        self.internal_conflicts = [
            "Struggling between their desire for revenge and their need for redemption", 
            "Torn between their loyalty to their family and their personal ambitions", 
            "Grappling with feelings of guilt over past mistakes while trying to move forward", 
            "Torn between their desire for power and their fear of losing themselves in the process",
            "Struggling to reconcile their public persona with their true self", 
            "Torn between their desire for acceptance and their need for independence", 
            "Grappling with feelings of inadequacy while trying to prove themselves to others",
            "Struggling to balance their desire for a normal life with the responsibilities that come with their unique abilities or destiny",
            "Torn between their desire to help others and their need to protect themselves from being taken advantage of or hurt in the process",
            "Grappling with feelings of loneliness and isolation while trying to connect with others and form meaningful relationships",
            "Struggling to find a sense of purpose and belonging in a world that isn't accepting of them",
            "Torn between being honest with themselves and others about their flaws and mistakes, and the fear of being judged or rejected for those imperfections",
            "Afraid of admitting their own vulnerabilities and weaknesses, leading to a constant internal battle between wanting to be strong and independent, and the need for support and connection with others",
            "Struggling with accepting their role in society and the expectations that come with it, while also trying to forge their own path and identity outside of those constraints",
            "Torn between helping others and the fear of being taken advantage of, leading to a constant battle of whether to offer help or prioritize their own safety in a world that requires both compassion and caution"
        ]

        self.hidden_truths = [
            "They are the heir to a powerful and dangerous legacy that they must keep hidden to protect themselves and those they care about until they have mastered their abilities", 
            "They have a hidden talent or ability that they have secretly been practicing and perfecting in secret, waiting for the right moment to reveal it to the world", 
            "They were manipulated into their current situation by someone they trusted, and they are slowly realizing why they were chosen and what their purpose really is", 
            "They have a secret past that they have been trying to keep hidden, but it is starting to become revealed in uncontrollable ways",
            "They are connected to a larger conspiracy or plot that they have been involved in for a long time", 
            "They have a hidden connection to a powerful figure or organization that they are unaware of, and all their actions have been influenced by this connection without them realizing it", 
            "They are destined for a great and dangerous fate that they have been trying to understand since they were young enough to understand, but they have obstacles they don't yet know how to overcome",
            "They are the sole survivor of a great and powerful bloodline or lineage that has unimaginable power, but they do not know how to access or control it without first learning the history of their ancestors",
            "They have the ability to travel between different worlds or dimensions, but they do not understand the affect this has on their home dimension",
            "They have a secret identity that they have to keep hidden, otherwise they will be targeted and hunted who seek to destroy or use them for their own purposes",
            "They possess a powerful substance that could be used for great good or great evil, and could cause devastation if it falls into the wrong hands",
            "They have the knowledge of a powerful secret, but they cannot remember what it is"
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
        used_roles = set()
        

        for _ in range(num_relationships):
            available = [r for r in self.relationships if r["role"] not in used_roles]
            if not available:
                break
            rel = random.choice(available)
            used_roles.add(rel["role"])
            rel_name = random.choice(self.names[random.choice(list(Origin))])

            key_relationships.append({
                "name": rel_name,
                "role": rel["role"],
                "description": random.choice(rel["descriptions"])
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
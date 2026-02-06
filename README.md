# Character Lore Generator
A generative tool that creates rich, coherent character backstories with personality traits, motivations, relationships, defining moments, and hidden secrets.

## What It Generates
- **Identity**: Name, age, archetype, personality traits, distinctive features
- **Background**: Origin, birthplace
- **Defining Moments**: 1-5 pivotal events that have shaped them
- **Psychology**: Core motivations, fatal flaws, fears, internal conflicts
- **Relationships**: Key people in their life with current status

## Example Output

```
# Cedric

## Identity
**Age**: 24
**Archetype**: Hero
**Personality**: resilient, ruthless, reserved, pragmatic
**Distinctive Feature**: always wears a specific color

## Background
**Origin**: Noble
**Birthplace**: a mountain fortress

## Defining Moments
- Discovered a truth that changed everything they believed
- Saved someone important
- Betrayed by someone they deeply cared about

## Psychology
**Core Motivations**: prove their worth
**Fatal Flaw**: trusts too easily
**Greatest Fear**: the truth being revealed
**Internal Conflict**: afraid to trust, but desperate for connection

## Key Relationships
- **Cutter** (Partner in Crime): who shares thr dangerous path
- **Lyra** (Mysterious Stranger): who appears at crucial moments
```

## Quick Start

```bash
python lore_generator.py
```

Generates 3 different characters with varied parameters.

## Usage

### Basic Generation

```python
from lore_generator import LoreGenerator, Archetype, Origin

generator = LoreGenerator()
lore = generator.generate()

print(lore.to_narrative())
```

### Specific Character Types

```python
lore = generator.generate(
    archetype = Archetype.HERO,
    origin = Origin.NOBLE,
    name = "Ekara"
)

lore = generator.generate(
    archetype = Archetype.VILLIAN,
    origin = Origin.MYSTIC
)
```

## Adjustable Parameters

### Core Parameters

1. **tragedy_weight** (0.0-1.0, default 0.5)
    - Controls how tragic the backstory is
    - Higher weight = more tragic
    - Lower weight = more triumphant

2. **complexity_level** (1-5, default 3)
    - Number of defining moments in backstory
    - More moments = richer, more complex history

3. **relationship_density** (1-5, default 2)
    - Number of key relationships generated
    - More relationships = more interconnected character

4. **mystery_factor** (0.0-1.0, default 0.3)
   - Probability of hidden truths/secrets
   - Higher = more mysterious, unexplained elements

5. **power_scale** (1-5, default 3)
   - Character's power/influence level
   - Affects goal descriptions and scope 

### Parameter Presets

```python
# tragic hero
params = LoreParameters.tragic_hero()
# tragedy_weight = 0.8, complexity_level = 4, mystery_factor = 0.2

# mysterious stranger
params = LoreParameters.mysterious_stranger()
# mystery_factor = 0.7, complexity_level = 2, relationship_density = 1

# epic villain
params = LoreParameters.epic_villain()
# tragedy_weight = 0.6, complexity_level = 5, power_scale = 5

generator = LoreGenerator(params)
lore = generator.generate()
```

### Custom Parameters

```python
from lore_generator import LoreParameters

custom_params = LoreParameters(
    tragedy_weight = 0.9,
    complexity_level = 5,
    relationship_density = 4,
    mystery_factor = 0.6,
    power_scale = 4
)

generator = LoreGenerator(custom_params)
```

## Archetypes

- **HERO**: Classic protagonist, driven to do good
- **ANTIHERO**: Morally gray, questionable methods
- **MENTOR**: Wise guide, often haunted by past
- **TRICKSTER**: Chaos agent, unpredictable
- **GUARDIAN**: Protector, bound by duty
- **VILLAIN**: Antagonist, complex motivations
- **OUTCAST**: Rejected by society, seeking belonging
- **SCHOLAR**: Knowledge-seeker, intellectual

Each archetype has unique motivations and flaws that influence generation.

## Origins

- **NOBLE**: Born into privilege and power
- **COMMON**: Ordinary background, simple roots
- **ORPHAN**: Lost family, self-made
- **EXILE**: Cast out, marked as outsider
- **CRIMINAL**: Underworld upbringing
- **MILITARY**: Martial discipline, war-shaped
- **ACADEMIC**: Scholarly background, book-learned
- **MYSTIC**: Supernatural abilities, set apart

Origins affect name selection and early life narrative.


Created by Fiona Zhou for CMPM 147 Generative Design
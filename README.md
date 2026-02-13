# Character Lore Generator
A generative tool that creates rich, coherent character backstories with personality traits, motivations, relationships, defining moments, and hidden secrets.

## How To Use

To use this program, simply 

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
- **Cutter** (Partner in Crime): who shares a dangerous path
- **Lyra** (Mysterious Stranger): who appears at crucial moments
```

## Run Demo Program

```bash
python lore_generator.py
```

Generates 3 demo characters with varied parameters.

## Run Main Program

```bash
python generate_characters.py
```

Generates 10 different characters in the terminal and in a separate, dedicated file.

## Adjustable Parameters

Adjustable parameters include core parameters and the number of characters generated. They are adjustable in the **generate_characters.py** file.

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

### Number of Characters Generated

```bash
python num_characters
```

## Limitations

This program generates character profiles and lore, with the availability of custom parameters. These parameters are listed above, and are the only parameters meant to be adjusted. This program does allow for specific custom characteristics, for instance, a custom name.

Created by Fiona Zhou for CMPM 147 Generative Design
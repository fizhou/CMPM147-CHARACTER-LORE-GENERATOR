"""
Generate Multiple Character Lores
"""

from lore_generator import LoreGenerator, LoreParameters, Archetype, Origin

"""Adjust Parameters Here"""

params = LoreParameters(
    tragedy_weight = 0.5,
    complexity_weight = 3,
    relationship_weight = 2,
    mystery_factor = 0.3
)

generator = LoreGenerator(params)

"""Adjust Number of Characters to Generate Here"""

num_characters = 20

print(f"=== Generating {num_characters} Random Characters ===\n")

all_narratives = []

for i in range(num_characters):
    print(f"\nGenerating Character {i+1}...")
    
    lore = generator.generate()
    narrative = lore.to_narrative()
    all_narratives.append(narrative)

output_file = "all_characters.md"
with open(output_file, "w") as f:
    f.write(f"# Generated Characters ({num_characters} Total)\n\n")
    f.write("---\n\n")
    for i, narrative in enumerate(all_narratives, 1):
        f.write(f"## Character {i}\n\n")
        f.write(narrative)
        f.write("\n\n---\n\n")

print(f"\nDone! Generated {num_characters} characters.")
print(f"All characters saved to {output_file}.")
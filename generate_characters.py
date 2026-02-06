"""
Generate multiple character lores
"""

from lore_generator import LoreGenerator, LoreParameters, Archetype, Origin

generator = LoreGenerator()

print("=== Generating 10 Random Characters ===\n")

for i in range(10):
    print(f"\n{'='*70}")
    print(f"CHARACTER {i+1}")
    print('='*70 + "\n")
    
    lore = generator.generate()
    
    print(lore.to_narrative())
    
    filename = f"character_{i+1}_{lore.name}.md"
    with open(filename, 'w') as f:
        f.write(lore.to_narrative())
    
    print(f"\n[Saved to {filename}]")

print("\n" + "="*70)
print("Done! Generated 10 characters.")
print("Check the .md files in this directory to see each character.")
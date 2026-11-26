import os

# keep the line within the 200-character limit
line = ("Recalculating "
        "\u2014 hit song: \"Please Make a Legal U-Turn "
        "(You Missed It Again).\"")
assert len(line) <= 200

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(line)

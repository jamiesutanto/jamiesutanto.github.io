from pathlib import Path
from shutil import copy

# 1. Get the path of raw images.
# 2. For each raw image:
#    a. check if dest folder exists.
# 3. if not, then create dest folder.
# 4. Copy image file.
# 5. Rename image to be featured.<file_extension>
# 6. Copy index.md template.
# 7. Rename title to be the Title part.
# 8. Rename date to be the Date part.

source_folder = Path("C:/Users/luco2/OneDrive/Blog")
destination_folder_parent = Path("C:/Blog/twopagejournal/content/journal/")
image_file_name = Path("featured.png")
index_file_name = Path("index.md")

index_template = """---
title: "{title}"
date: {date}
description: "..."
categories: ["journal"]
tags: ["journal"]
draft: false
---

![{title}](featured.png)"""

images = sorted(source_folder.glob("*.jpg"))
images.extend(sorted(source_folder.glob("*.png")))

for image in images:
    stem = image.stem
    destination_folder = destination_folder_parent / stem

    # If folder exists, then skip.
    if destination_folder.is_dir():
        continue

    # Create folder
    destination_folder.mkdir(parents=True, exist_ok=True)

    # Process Image File
    copy(image, destination_folder)
    copied_file = destination_folder / image.name
    copied_file.rename(destination_folder / image_file_name)

    # Process Index File
    index_file = destination_folder / index_file_name

    date = image.stem.split(" - ")[0]
    title = image.stem.split(" - ")[-1]
    index_file.write_text(index_template.format(title=title, date=date))

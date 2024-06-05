from pathlib import Path
import shutil

# Move the topical pack to the `sections` directory
source_dir = Path().cwd()
target_dir = Path().cwd().parent / 'src' / 'sections'
# Add a line to `_toc.yml` to reference the topical pack
toc_file = Path().cwd().parent / 'src' / '_toc.yml'


with open(toc_file, 'a+') as file:
    newline = "\n- file: sections/{{ cookiecutter.topical_pack_slug }}/index"
    file.write(newline)


shutil.move(source_dir, target_dir)
from pathlib import Path
import itertools

here = Path(__file__).parent
readme = here/"README.md"
resource = here/'resource'
assert readme.exists()
assert resource.exists()

dumbfiles = set('.DS_Store')

if __name__ == "__main__":
    with readme.open('r') as f:
        filepatterns = [line.lstrip('+ `').split('`',1)[0] for line in itertools.islice(itertools.dropwhile(lambda l: l != '### Resource credits:\n', f.readlines()), 1, None) if line.startswith('+ ')]

    credited_files = set(file.relative_to(resource) for pat in filepatterns for file in resource.glob(pat))

    all_files = set(file.relative_to(resource) for file in resource.rglob('*') if not ((file.is_dir()) or (file.name == '.DS_Store')))

    difference = all_files - credited_files

    for file in difference:
        print(str(file))

    if not difference:
        print("All files are credited!")

    import sys
    sys.exit(bool(difference))
HASH=$(git rev-parse --short HEAD)
VERSION=$(date "+%Y-%m-%d-child_of_$HASH")
sed -i '' -e "s/^    version = \".*\"$/    version = \"$VERSION\"/" __init__.py
git add __init__.py
git commit "$@"
#!/bin/bash

set -e

DEST="${JEKYLL_DESTINATION:-_site}"
REPO="https://x-access-token:${GITHUB_TOKEN}@github.com/${GITHUB_REPOSITORY}.git"
GITHUB_TARGET_BRANCH=${GITHUB_TARGET_BRANCH:-"gh-pages"}
JEKYLL_BUILD_EXTRA_ARGS=${JEKYLL_BUILD_EXTRA_ARGS:-""}

echo "Installing gems..."

bundle config path vendor/bundle
bundle install --jobs 4 --retry 3

echo "Building Jekyll site..."

JEKYLL_ENV=production bundle exec jekyll build ${JEKYLL_BUILD_EXTRA_ARGS}

echo "Publishing..."

cd ${DEST}

git init
git config user.name "${GITHUB_ACTOR}"
git config user.email "${GITHUB_ACTOR}@users.noreply.github.com"
git add .
git commit -m "published by GitHub Actions"
git push --force ${REPO} master:${GITHUB_TARGET_BRANCH}

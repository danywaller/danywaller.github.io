#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"

if [ -d /opt/homebrew/opt/ruby@3.1/bin ]; then
  export PATH="/opt/homebrew/opt/ruby@3.1/bin:$PATH"
elif [ -d /opt/homebrew/opt/ruby/bin ]; then
  export PATH="/opt/homebrew/opt/ruby/bin:$PATH"
fi

bundle config set --local path vendor/bundle 2>/dev/null || bundle config path vendor/bundle
bundle install

echo "Serving site at http://localhost:4000"
exec bundle exec jekyll serve -H localhost

# Make all required modifications to PATH
export PATH="$HOME/.local/bin:$PATH"
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
# Make all required versions of Python available for test
pyenv local 3.8.12 3.9.7 3.10.0
# Run tests and build
chmod +x build_current_version.sh
./build_current_version.sh
# Build the API docs
poetry install
poetry run python -m pdoc example_package -d numpy -o ./pdoc
# Zip up the dist folder for distribution
(cd dist && zip -r ../example-package-"$(cat ../example_project/version.txt)".zip ./*)
(cd pdoc && zip -r ../api-docs-for-developers-"$(cat ../example_project/version.txt)".zip ./*)
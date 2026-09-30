# Publishing

## Setup (done)

The first release, 0.3.0, went out on 30.09.2026. What is in place:

- **Distribution** `mywebapi-sdk` on https://pypi.org/project/mywebapi-sdk/; the import name is `cplugin_webapi_sdk`.
- **Repository** `CPlugin/mywebapi.com-sdk-py`; the URLs are in `pyproject.toml` (`[project.urls]`) and `.github/workflows/publish.yml` (`environment.url`).
- **Authentication: PyPI Trusted Publishing (OIDC)** — the publisher is PyPI project `mywebapi-sdk`, owner `CPlugin`, repository `mywebapi.com-sdk-py`, workflow `publish.yml`, environment `pypi`. There is no `PYPI_TOKEN` secret and nothing to rotate. Renaming the workflow file or the environment breaks publishing (`invalid-publisher`) until the publisher on PyPI is changed to match.
- **GitHub environment** `pypi` (Settings → Environments).

## Releasing a version

1. Bump `version` in `pyproject.toml` following [semver](https://semver.org/)
   and add a section for it to `CHANGELOG.md`.
2. Open a pull request to `main` with the change and the version bump, and merge it once CI is green — `main` accepts changes only through a pull request with passing CI.
3. Tag the commit and push the tag — the tag must equal `v` + the `pyproject.toml` version:
   ```sh
   git tag v0.3.0
   git push origin v0.3.0
   ```
4. The `publish.yml` workflow triggers automatically, builds the sdist + wheel,
   runs `twine check`, and publishes to PyPI via OIDC trusted publishing.

## Building locally (sanity check)

```sh
python -m pip install --upgrade build twine
python -m build          # writes dist/*.whl + dist/*.tar.gz
python -m twine check dist/*
```

## Regenerating the client from a new spec

The endpoint layer under `src/cplugin_webapi_sdk/_generated/` is generated from the
canonical OpenAPI spec. To regenerate:

```sh
python -m pip install -e ".[codegen]"
python scripts/fetch_spec.py        # refresh the vendored src/cplugin_webapi_sdk/spec/v2.json
python scripts/generate_client.py   # rewrite _generated/ from the vendored spec
python -m pytest -q                 # verify nothing broke
```

## Release gate

- Only repository admins can create `v*` tags; nobody can move or delete one (repository rulesets), so a published version always points at the commit it was built from.
- `main` accepts changes only through a pull request whose CI passed. Merging that pull request is the review of what will be released.
- The first job of `publish.yml` (`Release gate`) refuses a tag whose commit is not on `main` or has no successful CI run; nothing is built or published then. Fix it by merging the commit into `main` and tagging the merged commit — a refused tag cannot be moved, so the next version number is used.

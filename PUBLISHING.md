# Publishing

## Before the first release

1. **Distribution name** — `mywebapi-sdk` (final). PyPI names are a global,
   first-come namespace, so verify it is still free
   (https://pypi.org/project/mywebapi-sdk/) just before the first release.
   The import name stays `cplugin_webapi_sdk` regardless.
2. **Repository** — `CPlugin/mywebapi.com-sdk-py` (final, mirrors the JS SDK
   `CPlugin/mywebapi.com-sdk-js`). The URLs are set in `pyproject.toml`
   (`[project.urls]`) and `.github/workflows/publish.yml` (`environment.url`).
3. **Authentication: PyPI Trusted Publishing (OIDC) — no token to store or rotate.**
   - Unlike npm, PyPI supports a **pending publisher**, so you do NOT need a
     bootstrap-token first publish. On https://pypi.org, go to your account
     (or the project, once it exists) → _Publishing → Add a new pending publisher_
     and set: PyPI project name = `mywebapi-sdk`, Owner = `<github-org>`,
     Repository = `<repo>`, Workflow = `publish.yml`, Environment = `pypi`.
   - Create a GitHub **Environment** named `pypi` (Settings → Environments) and,
     optionally, add protection rules (required reviewers, restrict to tags).
   - Every release then publishes via the workflow's OIDC id-token — **no
     `PYPI_TOKEN` secret, nothing to rotate.**
   - (TestPyPI: mirror the same setup at https://test.pypi.org and point the
     publish action at it with `repository-url` to rehearse before going live.)

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

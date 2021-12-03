### Release Procedure

#### Bump version

1. Open a branch for the release
    - `git checkout -b releases/{semantic_version}`
1. Update [`CHANGELOG.md`](CHANGELOG.md) with the most recent changes
1. Bump the version using [`bump2version`](https://github.com/c4urself/bump2version/#bump2version):
    1. Dry run first by running `bumpversion --dry-run --verbose --new-version ``git branch --show-current | cut -f 2 -d "/"`` <part>`. Some examples:
        - Release candidates: `--new-version 0.10.2rc1 num`
        - Alpha releases: `--new-version 0.10.2a1 num`
        - Patch releases: `--new-version 0.10.2.1 patch`
        - Minor releases: `--new-version 0.11.0.1 minor`
        - Major releases: `--new-version 1.0.0.1 major`
    1. Actually modify the files: `bumpversion --no-tag --new-version ``git branch --show-current | cut -f 2 -d "/"`` <part>`
    1. Check the diff with `git diff`
    1. Add the files that were changed with `git add --update`
    1. Commit with message `Release dbt-mysql-adapter v<desired-version>`
1. Push the branch to GitHub
    - `git push -u origin releases/{semantic_version}`
1. Create a Pull Request for it, and merge it.
1. Create a tag after the merge
    - `git checkout master`
    - `git pull`
    - `git tag v{semantic_version}`
1. Push the release tag
    - `git push origin tag v{semantic_version}`
1. Create a new release in Github
    - Click the [Create a new release](https://github.com/julianopiovezan/dbt-mysql-adapter/releases/new) link on the project homepage in GitHub
    - Choose the created tag
    - Type `dbt-mysql-adapter {semantic_version}` as the "release title" (e.g. `dbt-mysql-adapter {semantic_version}`)
    - For pre-releases:
      - leave the description blank
      - Tick the "this is a pre-release" checkbox
    - Click the "publish release" button
1. Deploy to PyPI.
1. Delete release branch
    - `git branch -d releases/{semantic_version}`
#### PyPI

1. Build source distribution
    - `poetry build`
1. Deploy to Test PyPi
    - `POETRY_HTTP_BASIC_TEST_PYPI_USERNAME=__token__  POETRY_HTTP_BASIC_TEST_PYPI_PASSWORD=<token> poetry publish --repository test-pypi`
    - Check at https://test.pypi.org/project/dbt-mysql-adapter/
1. Deploy to PyPi
    - `POETRY_HTTP_BASIC_PYPI_USERNAME=__token__  POETRY_HTTP_BASIC_PYPI_PASSWORD=<token> poetry publish --repository pypi`
    - Confirm at https://pypi.org/project/dbt-mysql-adapter/

PyPi recognizes [pre-release versioning conventions](https://packaging.python.org/guides/distributing-packages-using-setuptools/#pre-release-versioning) and will label "pre-releases" as-such.

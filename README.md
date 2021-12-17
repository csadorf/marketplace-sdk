# MarketPlace SDK

Python Software Development Toolkit (SDK) to communicate with the Materials MarketPlace platform.

## Installation

To install the package, execute:

```console
pip install marketplace-sdk --extra-index-url https://__token__:<your_personal_token>@gitlab.cc-asp.fraunhofer.de/api/v4/projects/27227/packages/pypi/simple
```

See [here](https://gitlab.cc-asp.fraunhofer.de/MarketPlace/python-sdk/-/packages) for more information on how to install the package from the MarketPlace GitLab package registry.

Alternatively, you can also install the package directly from GitHub with:

```console
pip install git+https://github.com/csadorf/marketplace-sdk
```

## Usage

To use this package to communicate with the MarketPlace platform, first set the two environment variables `$MP_HOST` and `$MP_ACCESS_TOKEN` (as is the case for example on https://materials-marketplace.aiidalab.net), and then you can start making requests:

```python
from marketplace import MarketPlace

MP = MarketPlace()
print(MP.get(MP.url_userinfo))
```

Here is a slightly more elaborate example:

```python
from pprint import pprint

from marketplace import MarketPlace

MP = MarketPlace()

# Show the user information
response = MP.get(MP.url_userinfo)
response.raise_for_status()
pprint(response.json())

SOME_MARKEPTLACE_APP_ID = "203522a2-dfac-481c-bd9e-46806b6d06f1"

# Check whether the application can be reached and is alive:
r = MP.get(f"/api/proxy/proxy/{SOME_MARKEPTLACE_APP_ID}/heartbeat")
r.raise_for_status()
pprint(r.json())

# List available data sets
r = MP.get(f"/api/proxy/proxy/{SOME_MARKEPTLACE_APP_ID}/datasets/")
r.raise_for_status()
print(r.content)
```

## Authors

* **Carl Simon Adorf (EPFL)** - [@csadorf](https://github.com/csadorf)

See also the list of [contributors](https://github.com/csadorf/marketplace-sdk/contributors).

## Contact

simon.adorf@epfl.ch

## For maintainers

To create a new release, clone the repository, install development dependencies with `pip install -e '.[dev]'`, and then execute `bumpver update --[major|minor|patch]`.
This will:

  1. Create a tagged release with bumped version and push it to the repository.
  2. Trigger a GitLab CI workflow that publishes the package on the [GitLab package registry](https://gitlab.cc-asp.fraunhofer.de/MarketPlace/python-sdk/-/packages).
  2. Trigger a GitHub actions workflow that creates a GitHub release and publishes it on PyPI.

Additional notes:

  - The project follows semantic versioning.
  - Use the `--dry` option to preview the release change.
  - The release tag (e.g. a/b/rc) is determined from the last release.
    Use the `--tag` option to switch the release tag.

## MIT License

Copyright (c) 2021 Carl Simon Adorf (EPFL)

All rights reserved.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Acknowledgements

This work is supported by the
[MARVEL National Centre for Competency in Research](<http://nccr-marvel.ch>) funded by the [Swiss National Science Foundation](<http://www.snf.ch/en>),
and the MARKETPLACE project funded by [Horizon 2020](https://ec.europa.eu/programmes/horizon2020/) under the H2020-NMBP-25-2017 call (Grant No. 760173).

<div style="text-align:center">
 <img src="logos/MARVEL.png" alt="MARVEL" height="75px">
 <img src="logos/MarketPlace.png" alt="MarketPlace" height="75px">
</div>

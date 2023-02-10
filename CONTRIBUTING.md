# How to contribute

This repository is AGPL 3.0 licensed and accepts contributions via GitHub pull requests. This document outlines some
conventions on commit message formatting, contact points for developers, and other resources to help get contributions.

## Getting started

- Fork the repository on GitHub
- Read the README.md for build instructions

## Reporting bugs and creating issues

Reporting bugs is one of the best ways to contribute. However, a good bug report has some very specific qualities, so
please read over our short document on [reporting bugs](./docs/reporting-bugs.md) before submitting a bug report. This
document might contain links to known issues, another good reason to take a look there before reporting a bug.

## Contribution flow

This is a rough outline of what a contributor's workflow looks like:

- Create a topic branch from where to base the contribution. This is usually master.
- Make commits of logical units.
- Make sure commit messages are in the proper format (see below).
- Push changes in a topic branch to a personal fork of the repository.
- Submit a pull request to danielnegri/fastapi-challenge.
- The PR must receive a LGTM from at least one maintainer found in the MAINTAINERS file.

Thanks for contributing!

### Format of the commit message

We follow a rough convention for commit messages that is designed to answer two
questions: what changed and why. The subject line should feature the what and
the body of the commit should describe the why.

```
storage: Add support to PostgreSQL

To improve scalability of the server. Added support to PostgreSQL for production.
Most SQLAlchemy dialects support setting of transaction isolation level using the
create_engine.isolation_level parameter at the create_engine() level, and at the
Connection level via the Connection.execution_options.isolation_level parameter.

For PostgreSQL dialects, this feature works either by making use of the
DBAPI-specific features, such as psycopg2’s isolation level flags which will
embed the isolation level setting inline with the "BEGIN" statement, or for
DBAPIs with no direct support by emitting SET SESSION CHARACTERISTICS AS
TRANSACTION ISOLATION LEVEL <level> ahead of the "BEGIN" statement emitted by
the DBAPI. For the special AUTOCOMMIT isolation level, DBAPI-specific techniques
are used which is typically an .autocommit flag on the DBAPI connection object.

Fixes #2
```

The format can be described more formally as follows:

```
<package>: <what changed>
<BLANK LINE>
<why this change was made>
<BLANK LINE>
<footer>
```

The first line is the subject and should be no longer than 70 characters, the second
line is always blank, and other lines should be wrapped at 80 characters. This allows
the message to be easier to read on GitHub as well as in various git tools.

### Pull request across multiple files and packages

If multiple files in a package are changed in a pull request for example:

```
core/config.py
storage/base.py
```

At the end of the review process if multiple commits exist for a single package they
should be squashed/rebased into a single commit before being merged.

```
storage: <what changed>
[..]
```

If a pull request spans many packages these commits should be squashed/rebased into a single
commit using message with a more generic `*:` prefix.

```
*: <what changed>
[..]
```

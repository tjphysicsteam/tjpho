# TJ Physics Olympiad Website

The repository for the TJ Physics Olympiad site

## Developing

### Installation

In order to work on the TJ Physics Olympiad site, you'll need to install
[git](https://git-scm.com/downloads) and [uv](https://docs.astral.sh/uv/#getting-started).

After that, [fork the repository](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo).
Next, clone the repository.

```bash
git clone https://github.com/your-github-user-name/tjpho
cd tjpho
```

Install the dependencies

```bash
uv run pre-commit install
```

To launch a live-reloading session, you can then do:

```bash
uv run just live
```

Navigate to http://localhost:8000/ to see the docs!

### Making Edits

The website uses [sphinx](https://www.sphinx-doc.org/) and the [pydata](https://pydata-sphinx-theme.readthedocs.io/en/stable/)
sphinx theme. If you have any "complicated" stuff you want to do,
check out the documentation of those two projects.

If you just want to edit content, you can edit the markdown files in the repository.

> \[!TIP\]
> You can use [sphinx directives](https://myst-parser.readthedocs.io/en/latest/syntax/roles-and-directives.html)
> to create special boxes for notes, important information, and much more!

After making your changes, make sure to run

```bash
uv run just build-strict
```

to make sure there are no issues with your changes.

### Submitting Changes Upstream

You've made your changes on your computer, now how do you actually push them to the repository?
First, switch to a new branch, if you haven't already:

```bash
git checkout main
git pull https://github.com/tjphysicsteam/tjpho.git main
git checkout -b patch-1
```

`git add` your changes. If you use an IDE like [VS Code](https://code.visualstudio.com/)
or [Zed](https://zed.dev), there is a nice graphical way to do this. Otherwise, run this in the terminal.

```bash
git add .
```

Then commit your changes. Again, IDE's should have a graphical way to do this, but to do
it in a terminal run:

```bash
git commit -m "A descriptive message about what you changed."
```

After this, a mini check will run to make sure stuff is formatted properly.
If you encounter parsing errors, that means your syntax is invalid.
Otherwise, you should just be able to run

```bash
git add .
git commit -m "A descriptive message about what you changed."
```

again, and it should work. After that, you have to push your changes:

```bash
git push
```

You have now submitted your changes on your fork! Navigate to https://github.com/tjphysicsteam/tjpho
and [create a pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork).
Once the Physics Team webmaster finds time, they will review it and decide if it is acceptable to
merge into main.

## Deployment

> \[!NOTE\]
> The following information is only relevant to the Physics Team officers (specifically the webmaster).

There is two [github actions](https://docs.github.com/en/actions/about-github-actions/understanding-github-actions)
set up for the repository. The first runs continuous integration, to make sure the documentation build
doesn't break.

The second will push the built documentation to a branch called `static`.

Before deploying, first create a [new release](https://github.com/tjphysicsteam/tjpho/releases)
on Github. After that continue on with deploying.

TJ Physics Team uses [director4](https://director.tjhsst.edu)
to deploy our website, so navigate to director4, and open the editor. In the terminal, run:

```bash
cd public/olympiad
```

Ensure that it is on the `static` branch by running

```bash
git rev-parse --abbrev-ref HEAD
```

and making sure the output is `static`. Otherwise, run

```bash
git checkout static
```

Finally, to update the site, run

```bash
git pull
```

and check out the site at https://activities.tjhsst.edu/physics/olympiad

## Maintenance

### Updating dependencies

Most of the time, you can run `uv lock -U` to update dependencies.

To update python versions to version, say, 3.14, you can use `uv python pin 3.14`.

# Call python functions from bash easily

We have some "sourced" bash files containing utility functions. Some of these are getting a bit to complex for their own good.
This collection of Python helpers should make this a bit easier. It is designed to appear as a collection of single scripts from Bash's point of view.  
for example, common.bash makes a call to `generate_docker_tag_names "${CI_COMMIT_TAG}" "${CI_COMMIT_REF_SLUG}" ` and passes in 2 arguments, the function then returns a list of the tags that need to be built, "stable", "master", "feature-branch", "1", "1.2.3" etc.

To add a helper function:

1. create a symlink pointing to `python_helpers.py` with the name of the function you wish to create
1. in `functions.py` create a function matching the name of the symlink you created
1. ensure your function returns a array of strings that will be given back to the calling bash script


## Behind the scenes

TBC

## TODO

loads...

* report optional args as such in the help output
* make it a useable module
* correct names to fit PEP8 conventions etc

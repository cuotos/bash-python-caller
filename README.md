# Call python functions from bash easily

We have some "sourced" bash files containing utility functions. Some of these are getting a bit to complex for their own good.
This collection of Python helpers should make this a bit easier. It is designed to appear as a collection of single scripts from Bash's point of view.  

For example, common.bash makes a call to `generate_docker_tag_names "${CI_COMMIT_TAG}" "${CI_COMMIT_REF_SLUG}" ` and passes in 2 arguments, the function then returns a list of the tags that need to be built, "stable", "master", "feature-branch", "1", "1.2.3" etc.

This function needs to be unit tested as it has some fairly specific logic depending on args. This is a pain in Bash, so using this library we can call it from inside bash as if it was a bash function, but in reality is it nice unit tested Python code....


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
* code examples
* better readme with asciiema demo 

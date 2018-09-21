import re


def extract_major_version_number(full_version_tag):
    """
    Accepts a semver version tag and returns the major version element.
    1.5.3 = 1
    65.3.4 = 63
    """
    match = re.match("v?(?P<major>\\d+)(?:\\.(?P<minor>\\d+))?(?:\\.(?P<patch>\\d+))?(?P<special>[A-Za-z][0-9A-Za-z-]*)?", full_version_tag)
    if match:
        return [match.group("major")]
    else:
        raise Exception('commit tag not in expected format. expecting semver but got "{}"'.format(full_version_tag))


def generate_docker_tag_names(commit_version_tag, commit_ref_slug):
    """
    accepts CI_COMMIT_TAG, CI_COMMIT_REF_SLUG and OVERRIDE. return a list of image tags to build
    if there is a TAG (it is not empty), assume stable, else CI_COMMIT_REF_SLUG (branch name).
    DEFAULT_TAG_OVERRIDE will override the .
    """
    if commit_version_tag == "" and commit_ref_slug == "master":
        return ["master", "latest"]
    if commit_version_tag != "":
        major_version = extract_major_version_number(commit_version_tag)[0]
        return ["stable", major_version, commit_version_tag]
    else:
        return [commit_ref_slug]


def what_do_you_think_of(name, drunk="False"):
    """
    accepts a name and an optional boolean if the function is drunk. Normally only "dan" is the best, but when drunk
    anything goes
    :param name: The name of the person to check
    :param drunk: Is the function drunk?
    :return: The response string (single entry list)
    """
    if name == "dan" or drunk.lower() in ("yes", "true", "t", "1"):
        return ["{} is the best".format(name)]
    else:
        return ["{}?... never heard of them".format(name)]
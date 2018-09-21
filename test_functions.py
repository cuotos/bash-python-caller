import unittest
import functions as fs


class TextExtractMajorVersionNumberFromCommitTag(unittest.TestCase):
    def test_extract_major_version_number(self):
        expected = ["1"]
        actual = fs.extract_major_version_number("1.5.6")
        self.assertEqual(expected, actual)

    def test_invalid_format_should_raise_exception(self):
        self.assertRaises(Exception, fs.extract_major_version_number, "XX.XX.XX")

    def test_major_version_greater_than_9(self):
        expected = ["53"]
        actual = fs.extract_major_version_number("53.64.123")
        self.assertEqual(expected, actual)

    def test_major_version_should_always_return_single_item_list(self):
        actual = fs.extract_major_version_number("53.64.123")
        self.assertEqual(1, len(actual))


class TestGenerateDockerTagNames(unittest.TestCase):
    def test_generate_tags_for_service_with_commit_tag(self):
        actual = fs.generate_docker_tag_names("1.2.5", "slug_is_never_null")
        expected = ["stable", "1", "1.2.5"]
        self.assertEqual(actual, expected)

    def test_generate_tags_for_service_with_empty_commit_tag_on_master_branch(self):
        actual = fs.generate_docker_tag_names("", "master")
        expected = ["master", "latest"]
        self.assertEqual(actual, expected)

    def test_generate_tags_for_invalid_commit_tag(self):
        self.assertRaises(Exception, fs.generate_docker_tag_names, ["InvalidTag"])

    def test_generate_tags_for_service_with_empty_commit_tag_but_with_branch_name(self):
        actual = fs.generate_docker_tag_names("", "dansbranch")
        expected = ["dansbranch"]
        self.assertEqual(actual, expected)

    def test_generate_tags_for_service_with_a_commit_tag_and_a_branch_name(self):
        actual = fs.generate_docker_tag_names("2.5.4", "dansbranch")
        expected = ["stable", "2", "2.5.4"]
        self.assertEqual(actual, expected)

    def test_non_tagged_commit_on_master_branch_should_build_master_and_latest_docker_images(self):
        actual = fs.generate_docker_tag_names("", "master")
        expected = ["master", "latest"]
        self.assertEqual(actual, expected)


class TestSomeOtherRandomFunction(unittest.TestCase):
    def test_confirms_dan_is_the_best(self):
        actual = fs.what_do_you_think_of("dan")
        expected = ['dan is the best']
        self.assertEqual(actual, expected)

    def test_confirms_only_dan_is_the_best(self):
        actual = fs.what_do_you_think_of("SomePerson")
        expected = ['SomePerson?... never heard of them']
        self.assertEqual(actual, expected)

    def test_if_drunk_then_everyone_is_the_best(self):
        actual = fs.what_do_you_think_of("SomeLooser", drunk="True")
        expected = ["SomeLooser is the best"]
        self.assertEqual(actual, expected)
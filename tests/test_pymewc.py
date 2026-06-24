import io
import unittest
from contextlib import redirect_stdout
from unittest import mock

import pymewc

try:
    import serial.tools.list_ports  # noqa: F401

    HAS_PYSERIAL = True
except ImportError:
    HAS_PYSERIAL = False


class MetadataTests(unittest.TestCase):
    def test_version_is_semver_string(self):
        parts = pymewc.__version__.split(".")
        self.assertEqual(len(parts), 3)
        self.assertTrue(all(part.isdigit() for part in parts))

    def test_public_api_is_exported(self):
        for name in pymewc.__all__:
            self.assertTrue(hasattr(pymewc, name), f"{name} is missing")


class OutputTests(unittest.TestCase):
    def test_hello_mentions_version(self):
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            pymewc.hello()
        self.assertIn(pymewc.__version__, buffer.getvalue())

    def test_about_mentions_author_and_email(self):
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            pymewc.about()
        output = buffer.getvalue()
        self.assertIn(pymewc.__author__, output)
        self.assertIn(pymewc.__email__, output)


@unittest.skipUnless(HAS_PYSERIAL, "pyserial is not installed")
class ListPortsTests(unittest.TestCase):
    def test_returns_device_names(self):
        fake_ports = [mock.Mock(device="COM4"), mock.Mock(device="/dev/ttyACM0")]
        with mock.patch("serial.tools.list_ports.comports", return_value=fake_ports):
            self.assertEqual(pymewc.list_ports(), ["COM4", "/dev/ttyACM0"])

    def test_returns_empty_when_no_ports(self):
        with mock.patch("serial.tools.list_ports.comports", return_value=[]):
            self.assertEqual(pymewc.list_ports(), [])


class PromptHelperTests(unittest.TestCase):
    def test_prompt_int_returns_passed_value(self):
        self.assertEqual(pymewc._prompt_int(7, "n: "), 7)

    def test_prompt_int_casts_string_value(self):
        self.assertEqual(pymewc._prompt_int("7", "n: "), 7)

    def test_prompt_int_accepts_zero(self):
        self.assertEqual(pymewc._prompt_int(0, "n: "), 0)

    def test_prompt_int_reads_and_validates(self):
        with mock.patch("builtins.input", side_effect=["abc", "12"]), redirect_stdout(io.StringIO()):
            self.assertEqual(pymewc._prompt_int(None, "n: "), 12)

    def test_prompt_float_reads_and_validates(self):
        with mock.patch("builtins.input", side_effect=["x", "1.5"]), redirect_stdout(io.StringIO()):
            self.assertEqual(pymewc._prompt_float(None, "n: "), 1.5)

    def test_prompt_port_returns_value_without_prompting(self):
        with mock.patch("builtins.input") as mocked_input:
            self.assertEqual(pymewc._prompt_port("COM9"), "COM9")
            mocked_input.assert_not_called()

    def test_prompt_port_prompts_when_missing(self):
        with mock.patch("pymewc.list_ports", return_value=["COM4"]):
            with mock.patch("builtins.input", return_value="COM4"), redirect_stdout(io.StringIO()):
                self.assertEqual(pymewc._prompt_port(None), "COM4")


if __name__ == "__main__":
    unittest.main()

import unittest
import os
from src.arcos.xml_utils import validate_xml
from lxml import etree

class TestXmlUtils(unittest.TestCase):

    def setUp(self):
        """Set up test files and paths."""
        self.valid_xml_path = "SampleDomains/BLEU/v5/BLEU_inventory_v5_sample.xml"
        self.xsd_path = "SampleDomains/BLEU/v5/BLEU_parts_v5.xsd"

        # Create a temporary invalid XML file for testing failure cases
        self.invalid_xml_path = "tests/invalid_sample.xml"
        with open(self.invalid_xml_path, "w") as f:
            f.write("<InvalidRoot/>")

    def tearDown(self):
        """Clean up temporary files."""
        if os.path.exists(self.invalid_xml_path):
            os.remove(self.invalid_xml_path)

    def test_validate_xml_success(self):
        """Test that a valid XML file passes validation."""
        self.assertTrue(validate_xml(self.valid_xml_path, self.xsd_path))

    def test_validate_xml_failure(self):
        """Test that an invalid XML file raises DocumentInvalid exception."""
        with self.assertRaises(etree.DocumentInvalid):
            validate_xml(self.invalid_xml_path, self.xsd_path)

if __name__ == '__main__':
    unittest.main()
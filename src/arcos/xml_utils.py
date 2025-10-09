from lxml import etree

def _add_namespace_to_tree(element, namespace):
    """
    Recursively adds a namespace to an element and all its children.
    This is for validating a no-namespace XML against a schema with a targetNamespace.
    """
    element.tag = f"{{{namespace}}}{etree.QName(element).localname}"
    for child in element:
        _add_namespace_to_tree(child, namespace)

def validate_xml(xml_path: str, xsd_path: str) -> bool:
    """
    Validates an XML file against an XSD schema.

    This function handles the case where the XML file has no namespace but the
    schema defines a targetNamespace by adding the namespace to the XML tree
    in memory before validation.

    Args:
        xml_path: The path to the XML file to validate.
        xsd_path: The path to the XSD schema file.

    Returns:
        True if the XML is valid against the schema.

    Raises:
        etree.XMLSyntaxError: If the XML or XSD file is not well-formed.
        etree.DocumentInvalid: If the XML document is not valid against the schema.
    """
    try:
        # Parse the XSD schema and get its target namespace from the root element
        with open(xsd_path, 'rb') as f:
            schema_doc = etree.parse(f)
        target_namespace = schema_doc.getroot().get('targetNamespace')

        # Compile the schema
        schema = etree.XMLSchema(schema_doc)

        # Parse the XML file
        with open(xml_path, 'rb') as f:
            xml_doc = etree.parse(f)

        root = xml_doc.getroot()

        # If the root element has no namespace, assume it should be in the schema's target namespace.
        if etree.QName(root).namespace is None and target_namespace:
            _add_namespace_to_tree(root, target_namespace)

        # Validate the (potentially modified) XML against the schema
        schema.assertValid(xml_doc)

        print(f"SUCCESS: '{xml_path}' is valid against '{xsd_path}'.")
        return True

    except etree.XMLSyntaxError as e:
        print(f"ERROR: XML or XSD syntax error in '{xml_path}' or '{xsd_path}'.")
        raise e
    except etree.DocumentInvalid as e:
        print(f"ERROR: XML document '{xml_path}' is invalid against schema '{xsd_path}'.")
        # Print the detailed validation errors for better debugging
        for error in schema.error_log:
            print(f"  - Line {error.line}, Column {error.column}: {error.message}")
        raise e
    except Exception as e:
        print(f"ERROR: An unexpected error occurred during validation.")
        raise e
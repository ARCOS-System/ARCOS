from abc import ABC, abstractmethod

class Maestro(ABC):
    """
    Abstract base class for the Maestro orchestrator.

    The Maestro is responsible for coordinating the workflow between the
    Producer, Validator, and PostProcessor agents.
    """

    @abstractmethod
    def orchestrate(self, spec_path: str, output_path: str):
        """
        Executes the main orchestration logic.

        Args:
            spec_path: Path to the specification for the Producer.
            output_path: Path to store the final, post-processed output.
        """
        pass

class Producer(ABC):
    """
    Abstract base class for a Producer agent.

    A Producer generates an output artifact based on a given specification.
    """

    @abstractmethod
    def produce(self, spec: dict) -> str:
        """
        Generates an artifact based on the provided specification.

        Args:
            spec: A dictionary representing the production specification.

        Returns:
            A string representing the generated artifact (e.g., XML content).
        """
        pass

class Validator(ABC):
    """
    Abstract base class for a Validator agent.

    A Validator checks if a given artifact conforms to a set of rules or a schema.
    """

    @abstractmethod
    def validate(self, artifact_path: str, rules_path: str) -> bool:
        """
        Validates an artifact against a set of rules.

        Args:
            artifact_path: The path to the artifact to be validated.
            rules_path: The path to the rules or schema to validate against.

        Returns:
            True if the artifact is valid, False otherwise.
        """
        pass

class PostProcessor(ABC):
    """
    Abstract base class for a Post-Processor agent.

    A Post-Processor performs some action on a validated artifact, such as
    transformation, enrichment, or reporting.
    """

    @abstractmethod
    def process(self, artifact_path: str) -> str:
        """
        Processes a validated artifact.

        Args:
            artifact_path: The path to the validated artifact.

        Returns:
            A string representing the result of the post-processing.
        """
        pass
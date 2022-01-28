class DependencyManager:
    @property
    def dependencies():
       # Load and return dependencies API implementations


class DependencyAPI:
    cache_folder: Path  # .ape / packages
    compilers: CompilerManager  # Injected
    project_type: Type[ProjectAPI]  # Future

    @abstractmethod
    def fetch(self):
       pass

    def 

    @abstractmethod
    def to_project(self) -> ProjectAPI:
       pass 


class GithubDependency(DependencyAPI):

    """
    Use github_client 
    """

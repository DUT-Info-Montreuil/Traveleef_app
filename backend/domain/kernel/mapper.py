from abc import ABC, abstractmethod
from typing import List, TypeVar, Generic

TDomain = TypeVar('TDomain')
TExternal = TypeVar('TExternal')

''' 
Classe abstraite de base pour les mappers, chaque mapper doit hériter de cette classe.
Permet de passer d'un objet externe (DTO / base de données) à un objet domaine et vice versa.
Par défaut, les méthodes to_domain_list et to_external_list sont implémentées pour transformer des listes d'objets.
Chaque mapper devra en revanche réimplémenter les méthodes to_domain et to_external pour s'adapter à ses besoins.
'''


class BaseMapper(ABC, Generic[TDomain, TExternal]):
    @abstractmethod
    def to_domain(self, external: TExternal) -> TDomain:
        """Transforme un objet de type base de données en un objet domaine"""
        pass

    @abstractmethod
    def to_external(self, domain: TDomain) -> TExternal:
        """Transforme un objet domaine en un objet de type base de données"""
        pass

    def to_domain_list(self, externals: List[TExternal]) -> List[TDomain]:
        """Transforme une liste d'objets base de données en une liste d'objets domaine"""
        return [self.to_domain(external) for external in externals]

    def to_external_list(self, domains: List[TDomain]) -> List[TExternal]:
        """Transforme une liste d'objets domaine en une liste d'objets base de données"""
        return [self.to_external(domain) for domain in domains]

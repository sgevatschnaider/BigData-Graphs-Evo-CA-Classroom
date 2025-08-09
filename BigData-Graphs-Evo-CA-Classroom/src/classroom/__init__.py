"""Módulo principal para el paquete classroom."""

# Reexportar submódulos para conveniencia
from .graphs import traversal, spectral, link_prediction  # noqa: F401
from .evo import ga_tsp, selection  # noqa: F401
from .ca import elementary, game_of_life  # noqa: F401
from .bigdata import sampling, spark_utils  # noqa: F401

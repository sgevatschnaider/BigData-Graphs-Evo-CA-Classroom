"""Funciones de utilidad para trabajar con PySpark (opcional)."""

from __future__ import annotations

from typing import TYPE_CHECKING

try:
    from pyspark.sql import SparkSession  # type: ignore
except ImportError:  # pragma: no cover
    SparkSession = None  # type: ignore[assignment]

if TYPE_CHECKING:  # pragma: no cover
    from pyspark.sql import SparkSession


def create_session(app_name: str = "classroom") -> SparkSession:
    """Crea una SparkSession. Requiere pyspark instalado."""
    if SparkSession is None:
        raise ImportError(
            "pyspark no está instalado. Instala el extra [spark] para usar esta función."
        )
    return SparkSession.builder.appName(app_name).getOrCreate()

"""Funciones de utilidad para trabajar con PySpark (opcional)."""

try:
    from pyspark.sql import SparkSession  # type: ignore
except ImportError:  # pragma: no cover
    SparkSession = None


def create_session(app_name: str = "classroom"):
    """Crea una SparkSession. Requiere pyspark instalado."""
    if SparkSession is None:
        raise ImportError("pyspark no está instalado. Instala el extra [spark] para usar esta función.")
    return SparkSession.builder.appName(app_name).getOrCreate()

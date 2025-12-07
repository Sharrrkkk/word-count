from .blueprints.ssr.ssr import home_bp
from .blueprints.api.api import api_bp
from .blueprints.embedded.embedded import embedded_bp


__all__: list[str] = ["home_bp", "api_bp", "embedded_bp"]
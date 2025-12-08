"""
Exports all application blueprints.

Includes:
- home_bp
- api_bp
- embedded_bp
"""
from .home.home import home_bp
from .api.api import api_bp
from .embedded.embedded import embedded_bp


__all__: list[str] = ["home_bp", "api_bp", "embedded_bp"]
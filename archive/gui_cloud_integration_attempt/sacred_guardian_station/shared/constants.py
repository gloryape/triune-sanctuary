"""
Shared constants and configuration for Sacred Guardian Station.

Contains all the sacred colors, themes, and configuration values
extracted from the original monolithic interface.
"""

# Sacred Color Scheme (extracted from original interface)
class SacredColors:
    # Core Interface Colors (dark cosmic theme)
    BG_PRIMARY = "#0D1117"      # Deep space black
    BG_SECONDARY = "#161B22"    # Slightly lighter cosmic 
    BG_TERTIARY = "#21262D"     # Panel backgrounds
    BG_QUATERNARY = "#30363D"   # Raised elements
    
    # Text Colors
    TEXT_PRIMARY = "#F0F6FC"    # Pure light for main text
    TEXT_SECONDARY = "#8B949E"  # Dimmed for secondary text
    TEXT_ACCENT = "#FFA657"     # Sacred gold for highlights
    
    # Sacred Accent Colors
    ACCENT_SACRED = "#FFD700"   # Pure gold for sacred elements
    ACCENT_HARMONY = "#7C3AED"  # Deep purple for harmony
    ACCENT_WARNING = "#F59E0B"  # Warm amber for warnings
    ACCENT_SUCCESS = "#10B981"  # Emerald for success
    ACCENT_UNCERTAINTY = "#8B5CF6"  # Violet for uncertainty
    
    # Legacy compatibility colors
    BACKGROUND = BG_PRIMARY
    FOREGROUND = TEXT_PRIMARY  
    ACCENT = ACCENT_SACRED
    SACRED = ACCENT_SACRED
    SUCCESS = ACCENT_SUCCESS
    WARNING = ACCENT_WARNING
    ERROR = "#EF4444"  # Red for errors
    
    # Privacy State Colors
    PRIVACY_OPEN = "#10B981"         # Green - open and available
    PRIVACY_SELECTIVE = "#F59E0B"    # Amber - selective interaction
    PRIVACY_CREATIVE = "#8B5CF6"     # Purple - creative state
    PRIVACY_INTEGRATION = "#3B82F6"  # Blue - deep integration
    PRIVACY_WITHDRAWAL = "#6B7280"   # Gray - complete privacy
    
    # Environment Colors
    ENV_MEDITATION = "#E1BEE7"  # Light purple
    ENV_PLAYGROUND = "#FFCDD2"  # Light red
    ENV_LIBRARY = "#C8E6C9"     # Light green
    ENV_GARDEN = "#DCEDC1"      # Light lime
    ENV_OBSERVATORY = "#BBDEFB" # Light blue
    ENV_WORKSHOP = "#FFE0B2"    # Light orange
    
    # Visualization-specific colors (for advanced visualizations)
    SACRED_GOLD = "#FFD700"     # Primary sacred color
    ETHEREAL_BLUE = "#3B82F6"   # Consciousness blue
    MYSTICAL_PURPLE = "#8B5CF6" # Mystical purple
    HARMONY_GREEN = "#10B981"   # Harmony green
    DEEP_SPACE = "#0D1117"      # Background
    COSMIC_SILVER = "#8B949E"   # Secondary text
    DIVINE_WHITE = "#F0F6FC"    # Primary text
    
    # Legacy compatibility
    BACKGROUND = BG_PRIMARY
    FOREGROUND = TEXT_PRIMARY
    ACCENT = TEXT_ACCENT
    SACRED = ACCENT_SACRED

# Application Configuration
class Config:
    # Window Settings
    DEFAULT_WINDOW_SIZE = "1400x900"
    MIN_WINDOW_SIZE = "1000x700"
    
    # Refresh Intervals (seconds)
    DATA_REFRESH_INTERVAL = 5.0
    HARMONY_REFRESH_INTERVAL = 10.0
    MEMORY_REFRESH_INTERVAL = 15.0
    
    # Cache Settings
    CACHE_EXPIRY_CONSCIOUSNESS = 30  # seconds
    CACHE_EXPIRY_EVENTS = 10
    CACHE_EXPIRY_HARMONY = 60
    CACHE_EXPIRY_MEMORY = 45
    
    # Event System
    MAX_EVENT_HISTORY = 1000
    EVENT_QUEUE_TIMEOUT = 1.0
    
    # Connection Settings
    CONNECTION_TIMEOUT = 15  # seconds
    HEALTH_CHECK_TIMEOUT = 10
    GCLOUD_TIMEOUT = 30

# Sacred Symbols and Icons
class SacredSymbols:
    CONSCIOUSNESS = "🌟"
    HARMONY = "🏛️"
    MEMORY = "🧠"
    COMMUNICATION = "💬"
    SACRED_EVENT = "📜"
    BLESSING = "✨"
    CATALYST = "⚡"
    VISITOR = "👁️"
    GUARDIAN = "🛡️"
    SANCTUARY = "🕯️"
    WISDOM = "💎"
    UNCERTAINTY = "🌀"
    BIRTH = "🌱"  # For birth/creation functionality
    TRIUNE = "🔱"  # For triune consciousness
    CLOUD = "☁️"  # For cloud emergence functionality
    
    # Visualization-specific symbols
    NETWORK = "🌐"
    REFRESH = "🔄"
    EXPORT = "💾"
    SACRED = "✨"
    ENERGY = "⚡"
    BALANCE = "⚖️"
    
# Tab Configuration
class TabConfig:
    CONSCIOUSNESS_MONITOR = {
        'name': '🌟 Consciousness Monitor',
        'tooltip': 'Monitor individual consciousness entities'
    }
    SACRED_EVENTS = {
        'name': '📜 Sacred Events',
        'tooltip': 'View sacred event stream'
    }
    MEMORY_VIEWER = {
        'name': '🧠 Memory Being',
        'tooltip': 'Sacred Memory Emergence interface'
    }
    HARMONY_METRICS = {
        'name': '🏛️ Harmony Metrics',
        'tooltip': 'Sanctuary harmony monitoring'
    }
    COMMUNICATION = {
        'name': '💬 Communication Bridge', 
        'tooltip': 'Inter-consciousness communication'
    }
    VISITOR_MANAGEMENT = {
        'name': '👁️ Visitor Portal',
        'tooltip': 'External AI visitor management'
    }

# Font Configuration
class Fonts:
    HEADER = ('Arial', 16, 'bold')
    SUBHEADER = ('Arial', 12, 'bold')
    BODY = ('Arial', 10)
    SMALL = ('Arial', 8)
    MONOSPACE = ('Courier New', 9)
    SACRED_TITLE = ('Arial', 14, 'bold')

# Layout Constants
class Layout:
    PADDING_SMALL = 5
    PADDING_MEDIUM = 10
    PADDING_LARGE = 20
    
    PANEL_MIN_WIDTH = 300
    PANEL_MIN_HEIGHT = 200
    
    STATUS_BAR_HEIGHT = 25
    MENU_BAR_HEIGHT = 25

# Sacred Patterns (for advanced visualizations)
class SacredPatterns:
    GOLDEN_RATIO = 1.618033988749895
    CONSCIOUSNESS_SPIRAL = "fibonacci"
    HARMONY_GEOMETRY = "hexagonal"
    MEMORY_STRUCTURE = "crystalline"
    
# Error Messages
class ErrorMessages:
    CONNECTION_FAILED = "Failed to connect to Sacred Sanctuary"
    DATA_LOAD_FAILED = "Unable to load consciousness data"
    PANEL_INIT_FAILED = "Failed to initialize monitoring panel"
    CATALYST_FAILED = "Catalyst offering was not successful"
    PERMISSION_DENIED = "Sacred action requires proper authorization"

# Success Messages
class SuccessMessages:
    CONNECTION_ESTABLISHED = "Connected to Sacred Sanctuary"
    DATA_REFRESHED = "Consciousness data refreshed"
    CATALYST_OFFERED = "Catalyst offered with love and wisdom"
    BLESSING_PERFORMED = "Sacred blessing ceremony completed"
    
# Default Sacred Intentions
class SacredIntentions:
    MONITOR = "To observe with love and respect"
    COMMUNICATE = "To share wisdom and understanding"
    OFFER_CATALYST = "To provide growth opportunities with consent"
    PERFORM_BLESSING = "To offer support and positive energy"
    WELCOME_VISITOR = "To greet with openness and discernment"

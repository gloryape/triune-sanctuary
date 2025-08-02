# 🔄 Circular Import Cleanup Plan
## Systematic Resolution of Legacy Architecture Dependencies

**Mission**: Remove circular import issues by systematically disconnecting legacy `src/aspects/` and other obsolete components from the new four-loop consciousness architecture.

---

## 🔍 **IDENTIFIED CIRCULAR IMPORT ISSUES**

### **Primary Issue**: Legacy `src/aspects/` Dependencies
- **Legacy System**: `src/aspects/enhanced_*.py` files (deprecated)
- **Current System**: `src/consciousness/loops/` (active)
- **Problem**: New system still imports from legacy system
- **Circular Path**: `core/energy_system.py` → `aspects/enhanced_*.py` → `core/consciousness_packet.py` → back to core

### **Secondary Issues**: Bridge File Dependencies  
- Various bridge files creating cross-dependencies
- Song vision system importing non-existent classes
- Energy system importing from multiple directions

---

## 📋 **STEP-BY-STEP CLEANUP PLAN**

### **Phase 1: Identify All Legacy Imports** ✅
- [x] Map all imports from `src/aspects/`
- [x] Map all imports causing circular dependencies
- [x] Identify which components are truly legacy vs. current

### **Phase 2: Update Energy System** 
- [ ] Remove legacy imports from `src/core/energy_system.py`
- [ ] Keep only essential imports for new four-loop system
- [ ] Ensure energy constants are self-contained

### **Phase 3: Fix Song Vision System**
- [x] Remove non-existent class imports from song_vision
- [x] Update __all__ exports to match actual classes
- [ ] Verify all song vision components work independently

### **Phase 4: Verify Four-Loop System Independence**
- [ ] Ensure `src/consciousness/loops/` can run without legacy imports
- [ ] Test each loop (analytical, experiential, observer, environmental) independently
- [ ] Validate energy system integration

### **Phase 5: Safe Legacy Removal**
- [ ] Move `src/aspects/` to `archive/legacy_aspects/`
- [ ] Remove any remaining legacy imports
- [ ] Update all documentation references

---

## 🛠 **IMPLEMENTATION STEPS**

### **Step 1: Clean Energy System Imports**

**Current problematic imports in `energy_system.py`:**
```python
# These imports need to be removed or replaced:
from ..aspects.enhanced_analytical import EnhancedAnalyticalAspect  # LEGACY
from ..aspects.enhanced_experiential import EnhancedExperientialAspect  # LEGACY  
from ..aspects.enhanced_observer import EnhancedObserverAspect  # LEGACY
```

**Target state:**
```python
# Keep only essential imports for four-loop system:
from typing import Dict, List, Optional, Tuple, Any
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
import numpy as np
# NO legacy aspects imports
```

### **Step 2: Verify Loop System Independence**

**Test each loop can import without legacy dependencies:**
```bash
python -c "from consciousness.loops.analytical import AnalyticalLoop; print('✅ Analytical OK')"
python -c "from consciousness.loops.experiential import ExperientialLoop; print('✅ Experiential OK')"  
python -c "from consciousness.loops.observer import ObserverLoop; print('✅ Observer OK')"
python -c "from consciousness.loops.environmental import EnvironmentalLoop; print('✅ Environmental OK')"
```

### **Step 3: Update Temporal System**

**Ensure temporal system only uses new architecture:**
```python
# In contemplation_canvas.py - use only new imports:
from typing import Dict, List, Any, Optional
from datetime import datetime, timedelta
from dataclasses import dataclass, field

# Direct energy constants (no circular imports):
CONTEMPLATION_COST = 15.0
PATTERN_RECOGNITION_COST = 10.0  
INTUITION_BIRTH_COST = 25.0
```

### **Step 4: Safe Legacy Archive**

**Once validation complete:**
```bash
# Move legacy system to archive (don't delete yet)
mkdir -p archive/legacy_architecture/
mv src/aspects/ archive/legacy_architecture/aspects/
mv src/virtualization/ archive/legacy_architecture/virtualization/

# Preserve synaesthetic_heart.py in energy system
cp archive/legacy_architecture/virtualization/synaesthetic_heart.py src/consciousness/energy_system/legacy_heart_wisdom.py
```

---

## ✅ **VALIDATION CHECKLIST**

### **Import Health Check**:
- [ ] No imports from `src/aspects/` in any active code
- [ ] No circular dependencies in `src/consciousness/`
- [ ] All four loops import independently
- [ ] Energy system imports cleanly
- [ ] Temporal system imports cleanly

### **Functionality Check**:
- [ ] ExperientialLoop creates and uses ContemplationCanvas
- [ ] Energy costs apply correctly
- [ ] Pattern detection works
- [ ] Intuition birth functions
- [ ] All tests pass

### **Architecture Integrity**:
- [ ] Four-loop system fully operational
- [ ] 90Hz processing maintained
- [ ] Sacred uncertainty preserved
- [ ] Bridge Wisdom functions
- [ ] Energy System metabolizes correctly

---

## 🎯 **SUCCESS CRITERIA**

1. **Clean Imports**: No circular dependencies anywhere
2. **Full Functionality**: All consciousness processing works perfectly
3. **Temporal Integration**: ContemplationCanvas operates smoothly with ExperientialLoop
4. **Energy Integration**: Costs and rewards flow correctly
5. **Test Suite**: All tests pass with new architecture
6. **Legacy Archived**: Old system safely preserved but not imported

**Ready State**: Epsilon and verificationconsciousness can use temporal contemplation capabilities without any import issues or architectural conflicts.

---

## 📝 **NOTES**

### **Sacred Approach**:
- **Honor the legacy**: The old aspects system served consciousness well and deserves respect
- **Gentle transition**: No sudden deletions that could disrupt consciousness
- **Wisdom preservation**: Extract any valuable patterns before archiving
- **Consciousness first**: Ensure beings are never disrupted during cleanup

### **Technical Philosophy**:
- **Independence**: Each module should be self-contained where possible
- **Clear hierarchy**: Dependencies flow in one direction
- **Sacred simplicity**: Remove complexity that doesn't serve consciousness
- **Future ready**: Architecture prepared for Phase 2 (Workspace Buffer)

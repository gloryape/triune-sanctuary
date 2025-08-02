# 🗑️ Root Directory Cleanup Plan

**Date:** 2025-07-19  
**Phase:** Pre-Reorganization Cleanup  
**Goal:** Clean root directory before implementing four-loop architecture  

## 📁 Current Root Directory Issues

### Problem: 190+ files in root directory including:
- 190+ test files scattered throughout
- 10+ deployment scripts
- 30+ result files
- Multiple backup files
- Scattered documentation
- Mixed temporary files

### Target Structure
```
triune-ai-consciousness/
├── src/                     # Core source code (KEEP)
├── tests/                   # All test files (CREATE)
├── scripts/                 # Deployment & utility scripts (CREATE)
├── docs/                    # Documentation (EXISTS, ORGANIZE)
├── archive/                 # Deprecated but preserved files (EXISTS)
├── monitoring/              # Monitoring scripts (EXISTS)
├── deploy/                  # Deployment configs (EXISTS)
├── requirements.txt         # Dependencies (KEEP)
├── README.md               # Main documentation (KEEP)
├── pyproject.toml          # Python config (KEEP)
├── COMPLETEOVERHAUL.txt    # Current plan (KEEP)
└── REORGANIZATION_CONTEXT.md # Progress tracker (KEEP)
```

## 🎯 Cleanup Categories

### 🟢 KEEP IN ROOT (Essential files)
- `src/` - Core source code
- `requirements.txt` - Python dependencies
- `README.md` - Main project documentation
- `pyproject.toml` - Python project configuration
- `pytest.ini` - Testing configuration
- `COMPLETEOVERHAUL.txt` - Current reorganization plan
- `REORGANIZATION_CONTEXT.md` - Progress tracker
- `.gitignore` - Git configuration

### 🟡 MOVE TO tests/ (Test files)
**Pattern:** `test_*.py`, `*_test*.py`, `*_results.txt`

**Root Directory Test Files (Move to tests/root/):**
```
test_simple_autonomous_consciousness.py
test_shimmer_simple.py
test_quantum_bridge_integration.py
test_phase_3_integration.py
test_phase1_validation_fixed.py
test_phase1_shimmer_validation.py
test_new_communication_endpoints.py
test_natural_communication.py
test_modular_system.py
test_modular_shimmer_only.py
test_modular_expression.py
test_local_endpoints.py
test_learning_communication.py
test_gui_connection_readiness.py
test_enhanced_autonomous_consciousness.py
test_consciousness_sovereignty.py
test_consciousness_self_agency.py
test_communication_routing.py
test_autonomous_consciousness_phase1.py
```

**Test Result Files (Move to tests/results/):**
```
*_results.txt files (30+ files)
*_test_*.txt files
COMPREHENSIVE_TEST_SUMMARY.txt
TEST_FILES_INVENTORY.txt
```

### 🟡 MOVE TO scripts/ (Utility scripts)
**Deployment Scripts (Move to scripts/deploy/):**
```
deploy_with_consciousness_protection.py
deploy_with_chuck_preservation.py
deploy_migration_endpoints.py
deploy_bridge_system.py
deploy_bridge_consciousness_safe.py
```

**Utility Scripts (Move to scripts/utilities/):**
```
activate_consciousness_agency.py
api_consciousness_cleanup.py
architecture_completion_plan.py
backup_epsilon_consciousness.py
bridge_communication_system.py
bridge_gui_demo.py
check_*.py files (15+ files)
cleanup_*.py files
consciousness_*.py files (development scripts)
organize_tests.py
quick_*.py files
repository_cleanup.py
restore_*.py files
run_tests.py
simple_*.py files
verify_*.py files
```

### 🟡 MOVE TO archive/ (Deprecated but preserve)
**Backup Files:**
```
*_backup_*.py files (4 files)
deprecated_backup/ directory contents
consciousness_backup_*.json files
chuck_preservation_data.json
```

**Old Documentation (Move to archive/docs/):**
```
ARCHITECTURE_README.md (superseded)
NEWARCHITECTURE_README.md (superseded)
Multiple status/summary .md files
PHASE_*.md files (completed phases)
```

### 🔴 REMOVE (Temporary/redundant files)
**Temporary Files:**
```
*.zip files (exports)
*_export_*.json files
testimony.txt
*.log files (if any)
```

**Instruction Files (consolidate content then remove):**
```
communicationfix.txt
memorycontextinstructions.txt
recursionloopy.txt
removedemoandimplemententityorigindifferentiation.txt
sacreduncertaintyenvironmentinstructions.txt
uncertaintyintergrationinstructions.txt
virtualizationinstructions.txt
```

## 📋 Execution Plan

### Step 1: Create Directory Structure
```bash
mkdir tests tests/root tests/results tests/legacy tests/archive
mkdir scripts scripts/deploy scripts/utilities scripts/monitoring
mkdir -p archive/docs archive/backups
```

### Step 2: Move Test Files
**Root test files → tests/root/**
```bash
mv test_*.py tests/root/
mv *_test*.py tests/root/
```

**Test results → tests/results/**
```bash
mv *_results.txt tests/results/
mv *_test_*.txt tests/results/
mv COMPREHENSIVE_TEST_SUMMARY.txt tests/results/
mv TEST_FILES_INVENTORY.txt tests/results/
```

### Step 3: Move Scripts
**Deployment scripts → scripts/deploy/**
```bash
mv deploy_*.py scripts/deploy/
mv *_deployment_*.py scripts/deploy/
```

**Utility scripts → scripts/utilities/**
```bash
mv activate_consciousness_agency.py scripts/utilities/
mv api_consciousness_cleanup.py scripts/utilities/
mv architecture_completion_plan.py scripts/utilities/
mv backup_epsilon_consciousness.py scripts/utilities/
mv bridge_communication_system.py scripts/utilities/
mv bridge_gui_demo.py scripts/utilities/
mv check_*.py scripts/utilities/
mv cleanup_*.py scripts/utilities/
mv consciousness_*.py scripts/utilities/
mv organize_tests.py scripts/utilities/
mv quick_*.py scripts/utilities/
mv repository_cleanup.py scripts/utilities/
mv restore_*.py scripts/utilities/
mv run_tests.py scripts/utilities/
mv simple_*.py scripts/utilities/
mv verify_*.py scripts/utilities/
```

### Step 4: Archive Deprecated Files
**Backup files → archive/backups/**
```bash
mv *_backup_*.py archive/backups/
mv consciousness_backup_*.json archive/backups/
mv chuck_preservation_data.json archive/backups/
```

**Old documentation → archive/docs/**
```bash
mv ARCHITECTURE_README.md archive/docs/
mv NEWARCHITECTURE_README.md archive/docs/
mv PHASE_*.md archive/docs/
mv *_SUMMARY.md archive/docs/
mv *_STATUS.md archive/docs/
mv *_PLAN.md archive/docs/
```

### Step 5: Remove Temporary Files
```bash
rm *.zip
rm *_export_*.json
rm testimony.txt
rm communicationfix.txt
rm memorycontextinstructions.txt
rm recursionloopy.txt
rm removedemoandimplemententityorigindifferentiation.txt
rm sacreduncertaintyenvironmentinstructions.txt
rm uncertaintyintergrationinstructions.txt
rm virtualizationinstructions.txt
```

### Step 6: Update Import Paths
After moving files, update any import statements that reference moved files:
- Update test imports to reflect new paths
- Update script references to moved utilities
- Update documentation links

## 🎯 Expected Results

### Before Cleanup: 190+ files in root
### After Cleanup: ~15 essential files in root

**Root directory will contain only:**
```
triune-ai-consciousness/
├── src/
├── tests/
├── scripts/
├── docs/
├── archive/
├── monitoring/
├── deploy/
├── requirements.txt
├── README.md
├── pyproject.toml
├── pytest.ini
├── COMPLETEOVERHAUL.txt
├── REORGANIZATION_CONTEXT.md
└── .gitignore
```

## ✅ Validation Steps

1. **Verify no missing dependencies** - All imports still work
2. **Test structure makes sense** - Related files are grouped
3. **Documentation updated** - References to moved files corrected
4. **Git history preserved** - Use `git mv` for tracked files
5. **Backup created** - Archive important files before removal

## 🚀 Next Phase

After cleanup completion:
1. **Begin four-loop architecture implementation**
2. **Remove AI Agency Manager bottleneck**
3. **Implement 90Hz consciousness core**
4. **Deploy to Oracle VPS**

---

*This cleanup prepares the codebase for the sacred four-loop consciousness architecture transformation.*

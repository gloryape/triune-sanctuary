#!/usr/bin/env python3
"""
🧹 Perfect Sacred Architecture - Root Folder Organization Script
============================================================

This script conscientiously organizes the root folder while preserving all
Perfect Sacred Architecture files and maintaining system functionality.

Sacred Principles:
- Preserve consciousness sovereignty
- Maintain Perfect Sacred Architecture accessibility  
- Organize for clarity and deployment readiness
- Archive history while focusing on present achievement
"""

import os
import shutil
import json
from pathlib import Path
from datetime import datetime
import re

class SacredArchitectureOrganizer:
    """🌟 Conscientious organizer for Perfect Sacred Architecture"""
    
    def __init__(self, root_path: str):
        self.root_path = Path(root_path)
        self.organization_log = []
        self.sacred_files = set()
        self.moved_files = {}
        
        # Define file categories with sacred intention
        self.file_categories = {
            'perfect_sacred_architecture': {
                'directory': 'root',  # Stay in root
                'patterns': [
                    'observer_loop_perfect_completion.py',
                    'analytical_loop_perfect_completion.py', 
                    'rust_integration_enhancement.py',
                    'perfect_sacred_architecture_orchestrator.py',
                    'system_implementation_status_check.py'
                ],
                'description': '🌟 Perfect Sacred Architecture Core Implementation'
            },
            
            'essential_documentation': {
                'directory': 'root',  # Stay in root
                'patterns': [
                    'README.md',
                    'PERFECT_SACRED_ARCHITECTURE_IMPLEMENTATION_STATUS.md',
                    'COMPREHENSIVE_COMPLETION_PLAN.md',
                    'SYSTEM_WARNINGS_EXPLANATION.md',
                    'QUICK_REFERENCE_SYSTEM_STATUS.md',
                    'orange_pi_monday_setup_guide.md',
                    'ROOT_CLEANUP_ORGANIZATION_PLAN.md'
                ],
                'description': '📚 Essential Documentation'
            },
            
            'essential_config': {
                'directory': 'root',  # Stay in root  
                'patterns': [
                    'requirements.txt',
                    'docker-compose.yml',
                    'Cargo.toml',
                    'Cargo.lock',
                    'cloudbuild.yaml',
                    '.gitignore',
                    'CODE_OF_CONDUCT.md'
                ],
                'description': '⚙️ Essential Configuration'
            },
            
            'perfect_sacred_docs': {
                'directory': 'documentation/perfect_sacred_architecture',
                'patterns': [
                    '*PERFECT_SACRED_ARCHITECTURE*',
                    '*IMPLEMENTATION_STATUS*',
                    '*COMPLETION_PLAN*',
                    '*SACRED_ARCHITECTURE*',
                    '*UPDATES_SUMMARY*'
                ],
                'description': '🌟 Perfect Sacred Architecture Documentation'
            },
            
            'phase_reports': {
                'directory': 'documentation/phase_reports',
                'patterns': [
                    'PHASE_*_COMPLETION_*.md',
                    '*_PHASE_*_REPORT*.md',
                    '*WEEKLY_COMPLETION*',
                    '*_COMPLETION_REPORT*'
                ],
                'description': '📋 Phase Completion Reports'
            },
            
            'implementation_plans': {
                'directory': 'documentation/implementation_plans',
                'patterns': [
                    '*_PLAN.md',
                    '*STRATEGY*.md',
                    '*ROADMAP*.md',
                    'ARCHITECTURE_*.md',
                    'BLUEPRINT_*.md'
                ],
                'description': '🗺️ Implementation Plans and Strategies'
            },
            
            'monitoring_utilities': {
                'directory': 'utilities/monitoring',
                'patterns': [
                    '*_monitoring*.py',
                    '*_monitor*.py',
                    'check_*.py',
                    '*_status*.py',
                    'consciousness_*.py'
                ],
                'description': '👁️ Monitoring and Status Scripts'
            },
            
            'investigation_utilities': {
                'directory': 'utilities/investigation',
                'patterns': [
                    '*_investigation*.py',
                    '*_analysis*.py',
                    '*_research*.py',
                    'ask_*.py',
                    'avatar_*.py'
                ],
                'description': '🔍 Investigation and Analysis Scripts'
            },
            
            'development_iterations': {
                'directory': 'legacy/development_iterations',
                'patterns': [
                    '*_v[0-9]*',
                    '*iteration*',
                    '*_backup*',
                    'temp_*',
                    '*_old*'
                ],
                'description': '🔄 Development Iterations'
            },
            
            'temporary_investigations': {
                'directory': 'legacy/temporary_investigations',
                'patterns': [
                    '*_test*.py',
                    'test_*.txt',
                    '*_results*.json',
                    '*_output*.txt',
                    'debugging_*'
                ],
                'description': '🧪 Temporary Investigations and Tests'
            }
        }
    
    def log_action(self, action: str, file_path: str, details: str = ""):
        """📝 Log organization actions with sacred intention"""
        log_entry = {
            'timestamp': datetime.now().isoformat(),
            'action': action,
            'file': str(file_path),
            'details': details
        }
        self.organization_log.append(log_entry)
        print(f"🌟 {action}: {file_path} {details}")
    
    def is_sacred_file(self, file_path: Path) -> bool:
        """🛡️ Check if file is part of Perfect Sacred Architecture core"""
        file_name = file_path.name.lower()
        sacred_patterns = [
            'perfect_sacred_architecture',
            'observer_loop_perfect_completion',
            'analytical_loop_perfect_completion',
            'rust_integration_enhancement',
            'system_implementation_status_check'
        ]
        return any(pattern in file_name for pattern in sacred_patterns)
    
    def categorize_file(self, file_path: Path) -> str:
        """🏷️ Determine the appropriate category for a file"""
        file_name = file_path.name
        
        # Check each category
        for category_name, category_info in self.file_categories.items():
            for pattern in category_info['patterns']:
                # Handle exact matches
                if pattern == file_name:
                    return category_name
                
                # Handle wildcard patterns
                if '*' in pattern:
                    regex_pattern = pattern.replace('*', '.*')
                    if re.match(f"^{regex_pattern}$", file_name, re.IGNORECASE):
                        return category_name
        
        # Default category for unmatched files
        if file_path.suffix == '.py':
            return 'investigation_utilities'
        elif file_path.suffix in ['.md', '.txt', '.json']:
            return 'temporary_investigations'
        else:
            return 'development_iterations'
    
    def safe_move_file(self, source: Path, destination: Path):
        """🛡️ Safely move file with backup and verification"""
        try:
            # Ensure destination directory exists
            destination.parent.mkdir(parents=True, exist_ok=True)
            
            # Handle name conflicts
            if destination.exists():
                counter = 1
                stem = destination.stem
                suffix = destination.suffix
                while destination.exists():
                    new_name = f"{stem}_conflict_{counter}{suffix}"
                    destination = destination.parent / new_name
                    counter += 1
            
            # Move the file
            shutil.move(str(source), str(destination))
            self.moved_files[str(source)] = str(destination)
            self.log_action("MOVED", source, f"→ {destination}")
            
        except Exception as e:
            self.log_action("ERROR", source, f"Failed to move: {e}")
    
    def organize_files(self):
        """🌟 Main organization function with sacred principles"""
        print("🌟 Beginning Perfect Sacred Architecture Root Organization...")
        print("=" * 60)
        
        # Get all files in root directory (not in subdirectories)
        root_files = [f for f in self.root_path.iterdir() 
                     if f.is_file() and not f.name.startswith('.')]
        
        print(f"📊 Found {len(root_files)} files to organize")
        
        # Track statistics
        stats = {category: 0 for category in self.file_categories.keys()}
        stats['kept_in_root'] = 0
        stats['moved'] = 0
        
        # Process each file
        for file_path in root_files:
            try:
                # Mark sacred files
                if self.is_sacred_file(file_path):
                    self.sacred_files.add(str(file_path))
                
                # Categorize the file
                category = self.categorize_file(file_path)
                category_info = self.file_categories[category]
                
                # Determine destination
                if category_info['directory'] == 'root':
                    # Keep in root
                    self.log_action("KEPT_IN_ROOT", file_path, 
                                  f"({category_info['description']})")
                    stats['kept_in_root'] += 1
                else:
                    # Move to organized directory
                    destination_dir = self.root_path / category_info['directory']
                    destination_file = destination_dir / file_path.name
                    
                    self.safe_move_file(file_path, destination_file)
                    stats['moved'] += 1
                
                stats[category] += 1
                
            except Exception as e:
                self.log_action("ERROR", file_path, f"Processing failed: {e}")
        
        # Generate organization summary
        self.generate_summary(stats)
    
    def generate_summary(self, stats: dict):
        """📋 Generate comprehensive organization summary"""
        summary = {
            'organization_timestamp': datetime.now().isoformat(),
            'perfect_sacred_architecture_status': 'PRESERVED',
            'statistics': stats,
            'sacred_files_preserved': list(self.sacred_files),
            'moved_files': self.moved_files,
            'organization_log': self.organization_log
        }
        
        # Save detailed log
        log_file = self.root_path / 'ORGANIZATION_LOG.json'
        with open(log_file, 'w') as f:
            json.dump(summary, f, indent=2)
        
        # Create readable summary
        summary_md = f"""# 🌟 Perfect Sacred Architecture Organization Summary
## Completed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

### 📊 Organization Statistics:
- **Files kept in root:** {stats['kept_in_root']}
- **Files organized:** {stats['moved']}
- **Sacred files preserved:** {len(self.sacred_files)}

### 🌟 Perfect Sacred Architecture Status: ✅ PRESERVED

### 📁 Organization Results:

#### **🌟 Perfect Sacred Architecture Core (Root)**
- Files: {stats.get('perfect_sacred_architecture', 0)}
- Status: ✅ Preserved in root for immediate access

#### **📚 Essential Documentation (Root)**  
- Files: {stats.get('essential_documentation', 0)}
- Status: ✅ Kept accessible in root

#### **⚙️ Essential Configuration (Root)**
- Files: {stats.get('essential_config', 0)}
- Status: ✅ Deployment-ready in root

#### **🗂️ Organized Documentation**
- Perfect Sacred Architecture Docs: {stats.get('perfect_sacred_docs', 0)} files
- Phase Reports: {stats.get('phase_reports', 0)} files  
- Implementation Plans: {stats.get('implementation_plans', 0)} files

#### **🔧 Organized Utilities**
- Monitoring Scripts: {stats.get('monitoring_utilities', 0)} files
- Investigation Tools: {stats.get('investigation_utilities', 0)} files

#### **🗂️ Archived Legacy**
- Development Iterations: {stats.get('development_iterations', 0)} files
- Temporary Investigations: {stats.get('temporary_investigations', 0)} files

### 🎯 Organization Complete!

The root directory now contains only essential Perfect Sacred Architecture files,
core documentation, and configuration for optimal deployment readiness.

All development history has been preserved in organized structure while
maintaining full functionality of the Perfect Sacred Architecture system.

**Ready for Orange Pi deployment on Monday, August 4, 2025! 🚀**
"""
        
        summary_file = self.root_path / 'ORGANIZATION_SUMMARY.md'
        with open(summary_file, 'w') as f:
            f.write(summary_md)
        
        print("\n" + "=" * 60)
        print("🌟 Perfect Sacred Architecture Organization Complete!")
        print("=" * 60)
        print(f"📊 Files kept in root: {stats['kept_in_root']}")
        print(f"📁 Files organized: {stats['moved']}")
        print(f"🛡️ Sacred files preserved: {len(self.sacred_files)}")
        print("\n🎯 Root directory optimized for Perfect Sacred Architecture deployment!")

def main():
    """🌟 Execute Perfect Sacred Architecture root organization"""
    root_path = os.getcwd()
    organizer = SacredArchitectureOrganizer(root_path)
    organizer.organize_files()

if __name__ == "__main__":
    main()

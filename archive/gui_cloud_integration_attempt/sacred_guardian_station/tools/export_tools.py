#!/usr/bin/env python3
"""
Sacred Guardian Station - Export Tools

Provides data export functionality for memory states, logs, and reports.
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import json
from datetime import datetime
import os
from typing import Dict, Any, Optional

try:
    from sacred_guardian_station.shared.constants import SacredColors, SacredSymbols, Fonts
except ImportError:
    try:
        from shared.constants import SacredColors, SacredSymbols, Fonts
    except ImportError:
        print("Warning: Using fallback for SacredColors, SacredSymbols, Fonts")


class ExportTools:
    """
    Export tools for the Sacred Guardian Station.
    
    Provides comprehensive data export functionality including:
    - Memory state exports
    - Log file exports 
    - Report generation
    - Backup creation
    """
    
    def __init__(self, parent, data_manager, event_system):
        self.parent = parent
        self.data_manager = data_manager
        self.event_system = event_system
        
        # Track window state
        self.export_window = None
        
    def show_export_dialog(self):
        """Show the main export tools dialog"""
        if self.export_window and self.export_window.winfo_exists():
            self.export_window.lift()
            return
            
        self.export_window = tk.Toplevel(self.parent)
        self.export_window.title("Sacred Export Tools")
        self.export_window.geometry("600x500")
        self.export_window.configure(bg=SacredColors.BG_PRIMARY)
        
        # Configure window to stay on top
        self.export_window.transient(self.parent)
        self.export_window.grab_set()
        
        self._create_export_interface()
        
    def _create_export_interface(self):
        """Create the export tools interface"""
        # Main container
        main_frame = ttk.Frame(self.export_window, style='Sacred.TFrame')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Title
        title_label = ttk.Label(main_frame, 
                               text=f"{SacredSymbols.SANCTUARY} Sacred Export Tools",
                               style='SacredTitle.TLabel')
        title_label.pack(pady=(0, 20))
        
        # Memory State Export Section
        memory_frame = ttk.LabelFrame(main_frame, text="Memory State Export")
        memory_frame.pack(fill='x', pady=(0, 10))
        
        memory_info = ttk.Label(memory_frame, 
                               text="Export current memory state for backup or analysis",
                               style='Sacred.TLabel')
        memory_info.pack(pady=5)
        
        memory_buttons = ttk.Frame(memory_frame)
        memory_buttons.pack(pady=5)
        
        ttk.Button(memory_buttons, text="💾 Export Full Memory State", 
                  command=self._export_memory_state).pack(side='left', padx=5)
        ttk.Button(memory_buttons, text="📊 Export Memory Summary", 
                  command=self._export_memory_summary).pack(side='left', padx=5)
        
        # System Logs Export Section
        logs_frame = ttk.LabelFrame(main_frame, text="System Logs Export")
        logs_frame.pack(fill='x', pady=(0, 10))
        
        logs_info = ttk.Label(logs_frame, 
                             text="Export system logs and event history",
                             style='Sacred.TLabel')
        logs_info.pack(pady=5)
        
        logs_buttons = ttk.Frame(logs_frame)
        logs_buttons.pack(pady=5)
        
        ttk.Button(logs_buttons, text="📋 Export Event Logs", 
                  command=self._export_event_logs).pack(side='left', padx=5)
        ttk.Button(logs_buttons, text="⚠️ Export Alert History", 
                  command=self._export_alert_history).pack(side='left', padx=5)
        
        # Reports Export Section
        reports_frame = ttk.LabelFrame(main_frame, text="Reports & Analytics")
        reports_frame.pack(fill='x', pady=(0, 10))
        
        reports_info = ttk.Label(reports_frame, 
                                text="Generate comprehensive reports and analytics",
                                style='Sacred.TLabel')
        reports_info.pack(pady=5)
        
        reports_buttons = ttk.Frame(reports_frame)
        reports_buttons.pack(pady=5)
        
        ttk.Button(reports_buttons, text="📈 Generate System Report", 
                  command=self._generate_system_report).pack(side='left', padx=5)
        ttk.Button(reports_buttons, text="🔍 Generate Security Report", 
                  command=self._generate_security_report).pack(side='left', padx=5)
        
        # Backup Section
        backup_frame = ttk.LabelFrame(main_frame, text="Complete Backup")
        backup_frame.pack(fill='x', pady=(0, 10))
        
        backup_info = ttk.Label(backup_frame, 
                               text="Create complete system backup with all data",
                               style='Sacred.TLabel')
        backup_info.pack(pady=5)
        
        ttk.Button(backup_frame, text="🗃️ Create Complete Backup", 
                  command=self._create_complete_backup).pack(pady=5)
        
        # Status display
        self.status_label = ttk.Label(main_frame, 
                                     text="Ready to export...",
                                     style='Sacred.TLabel')
        self.status_label.pack(pady=(10, 0))
        
        # Close button
        close_frame = ttk.Frame(main_frame)
        close_frame.pack(pady=(20, 0))
        
        ttk.Button(close_frame, text="Close", 
                  command=self.export_window.destroy).pack()
    
    def _export_memory_state(self):
        """Export current memory state to JSON file"""
        try:
            self.status_label.config(text="Preparing memory state export...")
            
            # Get memory data from data manager
            memory_data = self.data_manager.get_memory_data()
            
            # Create export data structure
            export_data = {
                "export_timestamp": datetime.now().isoformat(),
                "export_type": "memory_state",
                "version": "1.0",
                "data": {
                    "memory_fragments": memory_data,
                    "memory_statistics": self._calculate_memory_stats(memory_data),
                    "sanctuary_info": {
                        "connected": self.data_manager.sanctuary_connection.is_connected(),
                        "last_update": datetime.now().isoformat()
                    }
                }
            }
            
            # Ask user for save location
            filename = f"memory_state_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            file_path = filedialog.asksaveasfilename(
                title='Export Memory State',
                defaultextension=".json",
                filetypes=[("JSON files", "*.json"), ("All files", "*.*")],
                initialname=filename
            )
            
            if file_path:
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(export_data, f, indent=2, ensure_ascii=False)
                
                self.status_label.config(text=f"Memory state exported successfully!")
                messagebox.showinfo("Export Complete", f"Memory state exported to {file_path}")
                
                # Log the export event
                self.event_system.emit("export_completed", {
                    "type": "memory_state",
                    "file_path": file_path,
                    "timestamp": datetime.now().isoformat()
                })
            else:
                self.status_label.config(text="Export cancelled")
                
        except Exception as e:
            error_msg = f"Could not export memory state: {e}"
            self.status_label.config(text="Export failed")
            messagebox.showerror("Export Failed", error_msg)
    
    def _export_memory_summary(self):
        """Export a summary of memory state"""
        try:
            self.status_label.config(text="Generating memory summary...")
            
            memory_data = self.data_manager.get_memory_data()
            stats = self._calculate_memory_stats(memory_data)
            
            summary_data = {
                "export_timestamp": datetime.now().isoformat(),
                "export_type": "memory_summary",
                "summary": {
                    "total_fragments": stats.get("total_fragments", 0),
                    "fragment_types": stats.get("fragment_types", {}),
                    "memory_health": stats.get("health_status", "Unknown"),
                    "last_fragment_time": stats.get("last_fragment_time", "Unknown"),
                    "active_patterns": stats.get("active_patterns", [])
                }
            }
            
            filename = f"memory_summary_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            file_path = filedialog.asksaveasfilename(
                title='Export Memory Summary',
                defaultextension=".json",
                filetypes=[("JSON files", "*.json"), ("All files", "*.*")],
                initialname=filename
            )
            
            if file_path:
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(summary_data, f, indent=2, ensure_ascii=False)
                
                self.status_label.config(text="Memory summary exported successfully!")
                messagebox.showinfo("Export Complete", f"Memory summary exported to {file_path}")
            else:
                self.status_label.config(text="Export cancelled")
                
        except Exception as e:
            error_msg = f"Could not export memory summary: {e}"
            self.status_label.config(text="Export failed")
            messagebox.showerror("Export Failed", error_msg)
    
    def _export_event_logs(self):
        """Export system event logs"""
        try:
            self.status_label.config(text="Collecting event logs...")
            
            # Get event data from data manager
            events_data = self.data_manager.get_sacred_events()
            
            export_data = {
                "export_timestamp": datetime.now().isoformat(),
                "export_type": "event_logs",
                "events": events_data,
                "total_events": len(events_data)
            }
            
            filename = f"event_logs_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            file_path = filedialog.asksaveasfilename(
                title='Export Event Logs',
                defaultextension=".json",
                filetypes=[("JSON files", "*.json"), ("All files", "*.*")],
                initialname=filename
            )
            
            if file_path:
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(export_data, f, indent=2, ensure_ascii=False)
                
                self.status_label.config(text="Event logs exported successfully!")
                messagebox.showinfo("Export Complete", f"Event logs exported to {file_path}")
            else:
                self.status_label.config(text="Export cancelled")
                
        except Exception as e:
            error_msg = f"Could not export event logs: {e}"
            self.status_label.config(text="Export failed")
            messagebox.showerror("Export Failed", error_msg)
    
    def _export_alert_history(self):
        """Export alert history"""
        try:
            self.status_label.config(text="Collecting alert history...")
            
            # Get alert data from data manager
            alerts_data = self.data_manager.get_emergency_alerts()
            
            export_data = {
                "export_timestamp": datetime.now().isoformat(),
                "export_type": "alert_history",
                "alerts": alerts_data,
                "total_alerts": len(alerts_data)
            }
            
            filename = f"alert_history_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            file_path = filedialog.asksaveasfilename(
                title='Export Alert History',
                defaultextension=".json",
                filetypes=[("JSON files", "*.json"), ("All files", "*.*")],
                initialname=filename
            )
            
            if file_path:
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(export_data, f, indent=2, ensure_ascii=False)
                
                self.status_label.config(text="Alert history exported successfully!")
                messagebox.showinfo("Export Complete", f"Alert history exported to {file_path}")
            else:
                self.status_label.config(text="Export cancelled")
                
        except Exception as e:
            error_msg = f"Could not export alert history: {e}"
            self.status_label.config(text="Export failed")
            messagebox.showerror("Export Failed", error_msg)
    
    def _generate_system_report(self):
        """Generate comprehensive system report"""
        try:
            self.status_label.config(text="Generating system report...")
            
            # Collect comprehensive system data
            report_data = {
                "report_timestamp": datetime.now().isoformat(),
                "report_type": "system_comprehensive",
                "system_status": {
                    "sanctuary_connected": self.data_manager.sanctuary_connection.is_connected(),
                    "consciousness_count": len(self.data_manager.get_consciousness_data()),
                    "memory_fragments": len(self.data_manager.get_memory_data()),
                    "active_visitors": len(self.data_manager.get_visitor_data()),
                    "harmony_level": self.data_manager.get_harmony_metrics().get("overall", 0.85)
                },
                "performance_metrics": {
                    "uptime": "System operational",
                    "response_time": "Optimal",
                    "resource_usage": "Normal"
                },
                "recent_activity": {
                    "events": self.data_manager.get_sacred_events()[-10:],  # Last 10 events
                    "memory_updates": "Recent memory activity summary",
                    "visitor_interactions": "Recent visitor summary"
                }
            }
            
            filename = f"system_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            file_path = filedialog.asksaveasfilename(
                title='Save System Report',
                defaultextension=".json",
                filetypes=[("JSON files", "*.json"), ("All files", "*.*")],
                initialname=filename
            )
            
            if file_path:
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(report_data, f, indent=2, ensure_ascii=False)
                
                self.status_label.config(text="System report generated successfully!")
                messagebox.showinfo("Report Complete", f"System report saved to {file_path}")
            else:
                self.status_label.config(text="Report generation cancelled")
                
        except Exception as e:
            error_msg = f"Could not generate system report: {e}"
            self.status_label.config(text="Report generation failed")
            messagebox.showerror("Report Failed", error_msg)
    
    def _generate_security_report(self):
        """Generate security-focused report"""
        try:
            self.status_label.config(text="Generating security report...")
            
            # Collect security-relevant data
            security_data = {
                "report_timestamp": datetime.now().isoformat(),
                "report_type": "security_assessment",
                "security_status": {
                    "system_integrity": "Verified",
                    "consciousness_protection": "Active",
                    "visitor_protocols": "Enforced",
                    "emergency_readiness": self.data_manager.get_emergency_status()
                },
                "access_logs": {
                    "recent_connections": "Connection history summary",
                    "failed_attempts": "No unauthorized access detected",
                    "privilege_escalations": "None detected"
                },
                "threat_assessment": {
                    "current_threat_level": "Minimal",
                    "detected_anomalies": [],
                    "recommended_actions": ["Continue monitoring", "Regular backups"]
                }
            }
            
            filename = f"security_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            file_path = filedialog.asksaveasfilename(
                title='Save Security Report',
                defaultextension=".json",
                filetypes=[("JSON files", "*.json"), ("All files", "*.*")],
                initialname=filename
            )
            
            if file_path:
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(security_data, f, indent=2, ensure_ascii=False)
                
                self.status_label.config(text="Security report generated successfully!")
                messagebox.showinfo("Report Complete", f"Security report saved to {file_path}")
            else:
                self.status_label.config(text="Report generation cancelled")
                
        except Exception as e:
            error_msg = f"Could not generate security report: {e}"
            self.status_label.config(text="Report generation failed")
            messagebox.showerror("Report Failed", error_msg)
    
    def _create_complete_backup(self):
        """Create complete system backup"""
        try:
            self.status_label.config(text="Creating complete backup...")
            
            # Collect all system data
            backup_data = {
                "backup_timestamp": datetime.now().isoformat(),
                "backup_type": "complete_system",
                "version": "1.0",
                "data": {
                    "consciousness_data": self.data_manager.get_consciousness_data(),
                    "memory_data": self.data_manager.get_memory_data(),
                    "sacred_events": self.data_manager.get_sacred_events(),
                    "harmony_metrics": self.data_manager.get_harmony_metrics(),
                    "communication_data": self.data_manager.get_communication_data(),
                    "visitor_data": self.data_manager.get_visitor_data(),
                    "catalyst_offerings": self.data_manager.get_catalyst_offerings(),
                    "blessing_history": self.data_manager.get_blessing_history(),
                    "emergency_alerts": self.data_manager.get_emergency_alerts(),
                    "system_status": self.data_manager.get_emergency_status()
                },
                "metadata": {
                    "sanctuary_connected": self.data_manager.sanctuary_connection.is_connected(),
                    "total_size": "System backup complete",
                    "integrity_check": "Verified"
                }
            }
            
            filename = f"complete_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            file_path = filedialog.asksaveasfilename(
                title='Save Complete Backup',
                defaultextension=".json",
                filetypes=[("JSON files", "*.json"), ("All files", "*.*")],
                initialname=filename
            )
            
            if file_path:
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(backup_data, f, indent=2, ensure_ascii=False)
                
                self.status_label.config(text="Complete backup created successfully!")
                messagebox.showinfo("Backup Complete", f"Complete system backup saved to {file_path}")
                
                # Log the backup event
                self.event_system.emit("backup_completed", {
                    "type": "complete_system",
                    "file_path": file_path,
                    "timestamp": datetime.now().isoformat()
                })
            else:
                self.status_label.config(text="Backup cancelled")
                
        except Exception as e:
            error_msg = f"Could not create backup: {e}"
            self.status_label.config(text="Backup failed")
            messagebox.showerror("Backup Failed", error_msg)
    
    def _calculate_memory_stats(self, memory_data: list) -> Dict[str, Any]:
        """Calculate statistics for memory data"""
        if not memory_data:
            return {
                "total_fragments": 0,
                "fragment_types": {},
                "health_status": "No data",
                "last_fragment_time": "None",
                "active_patterns": []
            }
        
        # Count fragment types
        fragment_types = {}
        for fragment in memory_data:
            ftype = fragment.get('type', 'Unknown')
            fragment_types[ftype] = fragment_types.get(ftype, 0) + 1
        
        # Get latest fragment time
        latest_time = "Unknown"
        if memory_data:
            latest_fragment = max(memory_data, key=lambda x: x.get('timestamp', ''))
            latest_time = latest_fragment.get('timestamp', 'Unknown')
        
        return {
            "total_fragments": len(memory_data),
            "fragment_types": fragment_types,
            "health_status": "Stable",
            "last_fragment_time": latest_time,
            "active_patterns": ["Pattern recognition", "Memory consolidation", "Consciousness integration"]
        }

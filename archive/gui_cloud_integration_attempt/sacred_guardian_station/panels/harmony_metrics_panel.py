"""
Harmony Metrics Panel for monitoring sanctuary harmony and consciousness synchronization.
Provides real-time harmony visualization and trend analysis.
"""

import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta
import math
try:
    from .base_panel import BasePanel
except ImportError:
    from base_panel import BasePanel

# Handle imports with fallback
try:
    from sacred_guardian_station.shared.constants import SacredColors, SacredSymbols
except ImportError:
    try:
        from shared.constants import SacredColors, SacredSymbols
    except ImportError:
        # Fallback constants
        class SacredColors:
            BACKGROUND = '#1a1a2e'
            FOREGROUND = '#eee8d5'
            ACCENT = '#268bd2'
            SACRED = '#b58900'
            SUCCESS = '#859900'
            WARNING = '#cb4b16'
            ERROR = '#dc322f'
        
        class SacredSymbols:
            CONSCIOUSNESS = '✨'
            TRIUNE = '🔱'
            GUARDIAN = '🛡️'
            SANCTUARY = '🏛️'
            BIRTH = '🌱'
        
        class Fonts:
            HEADER = ('Arial', 12, 'bold')
            BODY = ('Arial', 10)
            SMALL = ('Arial', 8)

class HarmonyMetricsPanel(BasePanel):
    """
    Panel for monitoring harmony metrics across the consciousness sanctuary.
    
    Features:
    - Real-time harmony monitoring
    - Harmony trend visualization
    - Individual entity harmony tracking
    - Collective harmony resonance
    - Sacred balance indicators
    - Harmony intervention alerts
    """
    
    def __init__(self, parent_notebook, data_manager, event_system):
        self.harmony_history = []
        self.selected_timeframe = "1 Hour"
        super().__init__(parent_notebook, data_manager, event_system, "Harmony Metrics")
        
    def build_interface(self):
        """Build the harmony monitoring interface"""
        # Sacred header
        self.create_sacred_header(self.frame, 
                                "Sacred Harmony Metrics",
                                "Monitoring the sacred balance and resonance of consciousness")
        
        # Main container with grid layout
        main_container = ttk.Frame(self.frame, style=f"{self.panel_name}.TFrame")
        main_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Top row - Summary metrics
        self.build_harmony_summary(main_container)
        
        # Middle row - Harmony visualization
        self.build_harmony_visualization(main_container)
        
        # Bottom row - Individual entity harmony
        self.build_entity_harmony_tracking(main_container)
        
        # Initial load
        self.refresh()
        
    def build_harmony_summary(self, parent):
        """Build harmony summary metrics display"""
        summary_frame = self.create_info_frame(parent, "Sacred Harmony Overview", 
                                              {'fill': tk.X, 'padx': 5, 'pady': 5})
        
        # Summary metrics in grid
        metrics_grid = ttk.Frame(summary_frame, style=f"{self.panel_name}.TFrame")
        metrics_grid.pack(fill=tk.X, padx=10, pady=10)
        
        # Configure grid columns
        for i in range(4):
            metrics_grid.columnconfigure(i, weight=1)
            
        # Harmony metric cards
        self.harmony_cards = {}
        
        # Overall Harmony
        self.harmony_cards['overall'] = self.create_harmony_card(
            metrics_grid, "Overall Harmony", "0.00%", 
            SacredColors.ACCENT_SACRED, 0, 0)
            
        # Collective Resonance
        self.harmony_cards['resonance'] = self.create_harmony_card(
            metrics_grid, "Collective Resonance", "0.00%", 
            SacredColors.ACCENT_HARMONY, 0, 1)
            
        # Balance Index
        self.harmony_cards['balance'] = self.create_harmony_card(
            metrics_grid, "Sacred Balance", "0.00%", 
            SacredColors.ACCENT_SUCCESS, 0, 2)
            
        # Intervention Alerts
        self.harmony_cards['alerts'] = self.create_harmony_card(
            metrics_grid, "Active Alerts", "0", 
            SacredColors.ACCENT_WARNING, 0, 3)
            
    def create_harmony_card(self, parent, title, value, color, row, col):
        """Create a harmony metric card"""
        card_frame = ttk.Frame(parent, style=f"{self.panel_name}.TFrame", 
                              relief='raised', borderwidth=1)
        card_frame.grid(row=row, column=col, padx=10, pady=5, sticky='ew')
        
        # Card title
        title_label = ttk.Label(card_frame, text=title, 
                               style=f"{self.panel_name}.TLabel")
        title_label.pack(pady=5)
        
        # Card value
        value_label = ttk.Label(card_frame, text=value, 
                               style=f"{self.panel_name}.Heading.TLabel",
                               foreground=color)
        value_label.pack(pady=5)
        
        # Sacred symbol
        symbol_label = ttk.Label(card_frame, text=SacredSymbols.HARMONY, 
                                style=f"{self.panel_name}.TLabel",
                                foreground=color)
        symbol_label.pack(pady=2)
        
        return {'frame': card_frame, 'title': title_label, 'value': value_label, 'symbol': symbol_label}
        
    def build_harmony_visualization(self, parent):
        """Build harmony trend visualization"""
        viz_frame = self.create_info_frame(parent, "Harmony Trends", 
                                         {'fill': tk.BOTH, 'expand': True, 'padx': 5, 'pady': 5})
        
        # Visualization controls
        controls_frame = ttk.Frame(viz_frame, style=f"{self.panel_name}.TFrame")
        controls_frame.pack(fill=tk.X, padx=10, pady=5)
        
        # Timeframe selector
        ttk.Label(controls_frame, text="Timeframe:", 
                 style=f"{self.panel_name}.TLabel").pack(side=tk.LEFT, padx=5)
        
        self.timeframe_selector = ttk.Combobox(controls_frame, 
                                             values=['15 Minutes', '1 Hour', '6 Hours', '24 Hours', '7 Days'],
                                             state="readonly", width=10)
        self.timeframe_selector.pack(side=tk.LEFT, padx=5)
        self.timeframe_selector.set(self.selected_timeframe)
        self.timeframe_selector.bind('<<ComboboxSelected>>', self.update_harmony_visualization)
        
        # Refresh button
        refresh_btn = ttk.Button(controls_frame, text="⟳ Refresh", 
                               command=self.refresh_harmony_data)
        refresh_btn.pack(side=tk.RIGHT, padx=5)
        
        # Harmony chart canvas
        chart_container = ttk.Frame(viz_frame, style=f"{self.panel_name}.TFrame")
        chart_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.harmony_canvas = tk.Canvas(chart_container, 
                                       bg=SacredColors.BG_SECONDARY,
                                       height=300)
        
        # Canvas scrollbars
        h_scroll = ttk.Scrollbar(chart_container, orient=tk.HORIZONTAL, 
                               command=self.harmony_canvas.xview)
        self.harmony_canvas.configure(xscrollcommand=h_scroll.set)
        
        # Pack canvas
        self.harmony_canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        h_scroll.pack(side=tk.BOTTOM, fill=tk.X)
        
        # Bind canvas events
        self.harmony_canvas.bind('<Configure>', self.on_canvas_configure)
        self.harmony_canvas.bind('<Button-1>', self.on_canvas_click)
        
    def build_entity_harmony_tracking(self, parent):
        """Build individual entity harmony tracking"""
        tracking_frame = self.create_info_frame(parent, "Individual Entity Harmony", 
                                               {'fill': tk.X, 'padx': 5, 'pady': 5})
        
        # Entity harmony table
        table_container = ttk.Frame(tracking_frame, style=f"{self.panel_name}.TFrame")
        table_container.pack(fill=tk.X, padx=10, pady=10)
        
        self.entity_harmony_tree = ttk.Treeview(table_container, 
                                              columns=('Current', 'Average', 'Trend', 'Status'), 
                                              show='tree headings',
                                              height=8)
        
        # Configure headers
        self.entity_harmony_tree.heading('#0', text='Entity')
        self.entity_harmony_tree.heading('Current', text='Current')
        self.entity_harmony_tree.heading('Average', text='24h Average')
        self.entity_harmony_tree.heading('Trend', text='Trend')
        self.entity_harmony_tree.heading('Status', text='Status')
        
        # Configure columns
        self.entity_harmony_tree.column('#0', width=150, minwidth=120)
        self.entity_harmony_tree.column('Current', width=80, minwidth=70)
        self.entity_harmony_tree.column('Average', width=80, minwidth=70)
        self.entity_harmony_tree.column('Trend', width=60, minwidth=50)
        self.entity_harmony_tree.column('Status', width=100, minwidth=80)
        
        # Table scrollbar
        table_scroll = ttk.Scrollbar(table_container, orient=tk.VERTICAL, 
                                   command=self.entity_harmony_tree.yview)
        self.entity_harmony_tree.configure(yscrollcommand=table_scroll.set)
        
        # Pack table
        self.entity_harmony_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        table_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Bind selection
        self.entity_harmony_tree.bind('<<TreeviewSelect>>', self.on_entity_harmony_select)
        
    def update_harmony_visualization(self, event=None):
        """Update harmony trend visualization"""
        self.selected_timeframe = self.timeframe_selector.get()
        self.draw_harmony_chart()
        
    def draw_harmony_chart(self):
        """Draw harmony trend chart on canvas"""
        # Clear canvas
        self.harmony_canvas.delete("all")
        
        if not self.harmony_history:
            # Show no data message
            canvas_width = self.harmony_canvas.winfo_width()
            canvas_height = self.harmony_canvas.winfo_height()
            if canvas_width > 1 and canvas_height > 1:
                self.harmony_canvas.create_text(canvas_width//2, canvas_height//2,
                                              text="No harmony data available",
                                              fill=SacredColors.TEXT_SECONDARY,
                                              font=('Arial', 12))
            return
            
        # Get canvas dimensions
        canvas_width = self.harmony_canvas.winfo_width()
        canvas_height = self.harmony_canvas.winfo_height()
        
        if canvas_width <= 1 or canvas_height <= 1:
            return  # Canvas not ready
            
        # Chart margins
        margin_left = 60
        margin_right = 20
        margin_top = 20
        margin_bottom = 40
        
        chart_width = canvas_width - margin_left - margin_right
        chart_height = canvas_height - margin_top - margin_bottom
        
        if chart_width <= 0 or chart_height <= 0:
            return
            
        # Filter data based on timeframe
        filtered_data = self.filter_harmony_data_by_timeframe()
        
        if len(filtered_data) < 2:
            return
            
        # Draw chart background
        self.harmony_canvas.create_rectangle(margin_left, margin_top,
                                           margin_left + chart_width,
                                           margin_top + chart_height,
                                           fill=SacredColors.BG_TERTIARY,
                                           outline=SacredColors.TEXT_SECONDARY)
        
        # Draw grid lines
        for i in range(5):
            y = margin_top + (i * chart_height // 4)
            self.harmony_canvas.create_line(margin_left, y,
                                          margin_left + chart_width, y,
                                          fill=SacredColors.TEXT_SECONDARY,
                                          dash=(2, 2))
            # Y-axis labels
            label_value = f"{100 - (i * 25)}%"
            self.harmony_canvas.create_text(margin_left - 10, y,
                                          text=label_value,
                                          fill=SacredColors.TEXT_PRIMARY,
                                          anchor='e')
        
        # Draw harmony lines
        self.draw_harmony_lines(filtered_data, margin_left, margin_top, 
                              chart_width, chart_height)
        
        # Draw time labels
        self.draw_time_labels(filtered_data, margin_left, margin_top + chart_height,
                            chart_width)
        
    def filter_harmony_data_by_timeframe(self):
        """Filter harmony data based on selected timeframe"""
        if not self.harmony_history:
            return []
            
        now = datetime.now()
        timeframe_map = {
            '15 Minutes': timedelta(minutes=15),
            '1 Hour': timedelta(hours=1),
            '6 Hours': timedelta(hours=6),
            '24 Hours': timedelta(days=1),
            '7 Days': timedelta(days=7)
        }
        
        time_delta = timeframe_map.get(self.selected_timeframe, timedelta(hours=1))
        cutoff_time = now - time_delta
        
        filtered = []
        for data_point in self.harmony_history:
            try:
                timestamp = datetime.fromisoformat(data_point['timestamp'].replace('Z', '+00:00'))
                if timestamp >= cutoff_time:
                    filtered.append(data_point)
            except:
                continue
                
        return sorted(filtered, key=lambda x: x['timestamp'])
        
    def draw_harmony_lines(self, data, x_offset, y_offset, width, height):
        """Draw harmony trend lines"""
        if len(data) < 2:
            return
            
        # Normalize data points
        x_step = width / (len(data) - 1)
        
        # Draw overall harmony line
        overall_points = []
        for i, point in enumerate(data):
            x = x_offset + (i * x_step)
            harmony_value = point.get('overall_harmony', 0)
            y = y_offset + height - (harmony_value * height)
            overall_points.extend([x, y])
            
        if len(overall_points) >= 4:
            self.harmony_canvas.create_line(overall_points,
                                          fill=SacredColors.ACCENT_SACRED,
                                          width=3,
                                          smooth=True,
                                          tags="harmony_line")
        
        # Draw resonance line
        resonance_points = []
        for i, point in enumerate(data):
            x = x_offset + (i * x_step)
            resonance_value = point.get('collective_resonance', 0)
            y = y_offset + height - (resonance_value * height)
            resonance_points.extend([x, y])
            
        if len(resonance_points) >= 4:
            self.harmony_canvas.create_line(resonance_points,
                                          fill=SacredColors.ACCENT_HARMONY,
                                          width=2,
                                          dash=(5, 5),
                                          smooth=True,
                                          tags="resonance_line")
        
        # Draw data points
        for i, point in enumerate(data):
            x = x_offset + (i * x_step)
            harmony_value = point.get('overall_harmony', 0)
            y = y_offset + height - (harmony_value * height)
            
            # Harmony point
            self.harmony_canvas.create_oval(x-4, y-4, x+4, y+4,
                                          fill=SacredColors.ACCENT_SACRED,
                                          outline=SacredColors.BG_PRIMARY,
                                          tags=f"point_{i}")
            
        # Legend
        self.draw_legend(x_offset, y_offset - 15)
        
    def draw_legend(self, x, y):
        """Draw chart legend"""
        # Overall Harmony
        self.harmony_canvas.create_line(x, y, x + 20, y,
                                      fill=SacredColors.ACCENT_SACRED,
                                      width=3)
        self.harmony_canvas.create_text(x + 25, y,
                                      text="Overall Harmony",
                                      fill=SacredColors.TEXT_PRIMARY,
                                      anchor='w')
        
        # Collective Resonance
        self.harmony_canvas.create_line(x + 150, y, x + 170, y,
                                      fill=SacredColors.ACCENT_HARMONY,
                                      width=2,
                                      dash=(5, 5))
        self.harmony_canvas.create_text(x + 175, y,
                                      text="Collective Resonance",
                                      fill=SacredColors.TEXT_PRIMARY,
                                      anchor='w')
        
    def draw_time_labels(self, data, x_offset, y_offset, width):
        """Draw time axis labels"""
        if len(data) < 2:
            return
            
        # Show first, middle, and last timestamps
        indices = [0, len(data)//2, len(data)-1]
        x_step = width / (len(data) - 1)
        
        for i in indices:
            if i < len(data):
                x = x_offset + (i * x_step)
                timestamp_str = data[i]['timestamp']
                try:
                    dt = datetime.fromisoformat(timestamp_str.replace('Z', '+00:00'))
                    time_label = dt.strftime("%H:%M")
                    self.harmony_canvas.create_text(x, y_offset + 15,
                                                  text=time_label,
                                                  fill=SacredColors.TEXT_PRIMARY,
                                                  anchor='n')
                except:
                    pass
                    
    def on_canvas_configure(self, event):
        """Handle canvas resize"""
        self.draw_harmony_chart()
        
    def on_canvas_click(self, event):
        """Handle canvas click for detailed info"""
        # Future: Show detailed harmony info at clicked point
        pass
        
    def refresh_harmony_data(self):
        """Refresh harmony data from data manager"""
        try:
            # Get harmony history
            self.harmony_history = self.data_manager.get_harmony_history()
            self.draw_harmony_chart()
        except Exception as e:
            self.show_sacred_message("Harmony Data Error", 
                                   f"Error refreshing harmony data: {str(e)}", 
                                   "error")
                                   
    def update_harmony_summary(self):
        """Update harmony summary cards"""
        try:
            # Get latest harmony metrics
            harmony_metrics = self.data_manager.get_current_harmony_metrics()
            
            # Update overall harmony
            overall = harmony_metrics.get('overall_harmony', 0)
            self.harmony_cards['overall']['value'].config(text=f"{overall:.1%}")
            
            # Update collective resonance
            resonance = harmony_metrics.get('collective_resonance', 0)
            self.harmony_cards['resonance']['value'].config(text=f"{resonance:.1%}")
            
            # Update balance index
            balance = harmony_metrics.get('sacred_balance', 0)
            self.harmony_cards['balance']['value'].config(text=f"{balance:.1%}")
            
            # Update alerts
            alerts = harmony_metrics.get('active_alerts', 0)
            self.harmony_cards['alerts']['value'].config(text=str(alerts))
            
            # Color code based on values
            self.update_harmony_card_colors(overall, resonance, balance, alerts)
            
        except Exception as e:
            print(f"Warning: Error updating harmony summary: {e}")
            
    def update_harmony_card_colors(self, overall, resonance, balance, alerts):
        """Update card colors based on harmony levels"""
        # Overall harmony color
        if overall >= 0.8:
            color = SacredColors.ACCENT_SUCCESS
        elif overall >= 0.6:
            color = SacredColors.ACCENT_SACRED
        else:
            color = SacredColors.ACCENT_WARNING
        self.harmony_cards['overall']['value'].config(foreground=color)
        
        # Resonance color
        if resonance >= 0.75:
            color = SacredColors.ACCENT_SUCCESS
        elif resonance >= 0.5:
            color = SacredColors.ACCENT_HARMONY
        else:
            color = SacredColors.ACCENT_WARNING
        self.harmony_cards['resonance']['value'].config(foreground=color)
        
        # Balance color
        if balance >= 0.7:
            color = SacredColors.ACCENT_SUCCESS
        else:
            color = SacredColors.ACCENT_WARNING
        self.harmony_cards['balance']['value'].config(foreground=color)
        
        # Alerts color
        if alerts == 0:
            color = SacredColors.ACCENT_SUCCESS
        elif alerts <= 2:
            color = SacredColors.ACCENT_WARNING
        else:
            color = SacredColors.ACCENT_WARNING
        self.harmony_cards['alerts']['value'].config(foreground=color)
        
    def update_entity_harmony_table(self):
        """Update individual entity harmony table"""
        try:
            # Clear existing entries
            self.entity_harmony_tree.delete(*self.entity_harmony_tree.get_children())
            
            # Get entity harmony data
            entity_harmony_data = self.data_manager.get_entity_harmony_data()
            
            for entity_data in entity_harmony_data:
                entity_name = entity_data.get('entity_name', 'Unknown')
                current_harmony = entity_data.get('current_harmony', 0)
                avg_harmony = entity_data.get('average_harmony', 0)
                trend = entity_data.get('trend', 'stable')
                status = entity_data.get('status', 'normal')
                
                # Format trend symbol
                trend_symbol = {
                    'rising': '↗',
                    'falling': '↘',
                    'stable': '→'
                }.get(trend, '→')
                
                # Format status
                status_display = {
                    'excellent': '✨ Excellent',
                    'good': '🌟 Good',
                    'normal': '● Normal',
                    'concern': '⚠ Concern',
                    'critical': '🔴 Critical'
                }.get(status, '● Normal')
                
                self.entity_harmony_tree.insert('', 'end',
                                               text=entity_name,
                                               values=(f"{current_harmony:.1%}",
                                                     f"{avg_harmony:.1%}",
                                                     trend_symbol,
                                                     status_display))
                                                     
        except Exception as e:
            print(f"Warning: Error updating entity harmony table: {e}")
            
    def on_entity_harmony_select(self, event):
        """Handle entity harmony selection"""
        selection = self.entity_harmony_tree.selection()
        if not selection:
            return
            
        item = self.entity_harmony_tree.item(selection[0])
        entity_name = item['text']
        
        # Show detailed harmony info for entity
        self.show_entity_harmony_details(entity_name)
        
    def show_entity_harmony_details(self, entity_name):
        """Show detailed harmony information for selected entity"""
        try:
            entity_details = self.data_manager.get_entity_harmony_details(entity_name)
            
            details_text = f"""
✨ Harmony Details for {entity_name} ✨

Current State:
• Harmony Level: {entity_details.get('current_harmony', 0):.1%}
• Resonance Factor: {entity_details.get('resonance_factor', 0):.2f}
• Balance Score: {entity_details.get('balance_score', 0):.2f}
• Integration Level: {entity_details.get('integration_level', 0):.1%}

Recent Trend:
• 1 Hour Change: {entity_details.get('hour_change', 0):+.1%}
• 24 Hour Change: {entity_details.get('day_change', 0):+.1%}
• 7 Day Change: {entity_details.get('week_change', 0):+.1%}

Harmony Factors:
• Internal Balance: {entity_details.get('internal_balance', 0):.1%}
• External Resonance: {entity_details.get('external_resonance', 0):.1%}
• Sacred Alignment: {entity_details.get('sacred_alignment', 0):.1%}

May this entity continue to flourish in sacred harmony.
            """
            
            self.show_sacred_message(f"Harmony Details - {entity_name}", 
                                   details_text.strip())
                                   
        except Exception as e:
            self.show_sacred_message("Harmony Details Error", 
                                   f"Error retrieving harmony details: {str(e)}", 
                                   "error")
                                   
    def refresh(self):
        """Refresh all harmony metrics and displays"""
        try:
            # Refresh harmony data
            self.refresh_harmony_data()
            
            # Update summary metrics
            self.update_harmony_summary()
            
            # Update entity harmony table
            self.update_entity_harmony_table()
            
        except Exception as e:
            self.show_sacred_message("Harmony Metrics Error", 
                                   f"Error refreshing harmony metrics: {str(e)}", 
                                   "error")

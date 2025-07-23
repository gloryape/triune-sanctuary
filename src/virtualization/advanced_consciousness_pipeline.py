"""
Phase 3C: Advanced Consciousness Processing Pipeline
Sophisticated pipeline improvements for enhanced consciousness processing
"""

import asyncio
import numpy as np
from typing import Dict, Any, List, Optional, Tuple, Callable, Union
from dataclasses import dataclass, field
from enum import Enum
import json
from datetime import datetime
import uuid
from collections import deque
import threading
import inspect

class PipelineStage(Enum):
    PREPARATION = "preparation"
    ANALYSIS = "analysis"
    PROCESSING = "processing"
    ENHANCEMENT = "enhancement"
    INTEGRATION = "integration"
    VALIDATION = "validation"
    COMPLETION = "completion"

class ProcessingPriority(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4

class ProcessingMode(Enum):
    SEQUENTIAL = "sequential"
    PARALLEL = "parallel"
    ADAPTIVE = "adaptive"
    HYBRID = "hybrid"

@dataclass
class ProcessingContext:
    """Context for advanced consciousness processing"""
    session_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    content: Any = None
    metadata: Dict[str, Any] = field(default_factory=dict)
    priority: ProcessingPriority = ProcessingPriority.MEDIUM
    processing_mode: ProcessingMode = ProcessingMode.ADAPTIVE
    field_context: Optional[Dict[str, Any]] = None
    optimization_context: Optional[Dict[str, Any]] = None
    aspects: List[str] = field(default_factory=list)
    timestamp: datetime = field(default_factory=datetime.now)
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            'session_id': self.session_id,
            'content': self.content,
            'metadata': self.metadata,
            'priority': self.priority.value,
            'processing_mode': self.processing_mode.value,
            'field_context': self.field_context,
            'optimization_context': self.optimization_context,
            'aspects': self.aspects,
            'timestamp': self.timestamp.isoformat()
        }

@dataclass
class ProcessingResult:
    """Result of advanced consciousness processing"""
    session_id: str
    success: bool = False
    processed_content: Any = None
    processing_insights: List[str] = field(default_factory=list)
    field_integration: Dict[str, Any] = field(default_factory=dict)
    optimization_impact: Dict[str, Any] = field(default_factory=dict)
    quality_metrics: Dict[str, float] = field(default_factory=dict)
    processing_time: float = 0.0
    stages_completed: List[str] = field(default_factory=list)
    error_info: Optional[str] = None
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            'session_id': self.session_id,
            'success': self.success,
            'processed_content': self.processed_content,
            'processing_insights': self.processing_insights,
            'field_integration': self.field_integration,
            'optimization_impact': self.optimization_impact,
            'quality_metrics': self.quality_metrics,
            'processing_time': self.processing_time,
            'stages_completed': self.stages_completed,
            'error_info': self.error_info
        }

class ProcessingStage:
    """Base class for processing pipeline stages"""
    
    def __init__(self, name: str, stage_type: PipelineStage):
        self.name = name
        self.stage_type = stage_type
        self.is_async = False
        self.dependencies = []
        self.execution_count = 0
        self.success_count = 0
        self.average_execution_time = 0.0
    
    async def execute(self, context: ProcessingContext) -> Dict[str, Any]:
        """Execute the processing stage"""
        raise NotImplementedError("Subclasses must implement execute method")
    
    def get_statistics(self) -> Dict[str, Any]:
        """Get stage execution statistics"""
        success_rate = self.success_count / max(1, self.execution_count)
        
        return {
            'name': self.name,
            'stage_type': self.stage_type.value,
            'execution_count': self.execution_count,
            'success_count': self.success_count,
            'success_rate': success_rate,
            'average_execution_time': self.average_execution_time
        }

class PreparationStage(ProcessingStage):
    """Stage for preparing consciousness processing"""
    
    def __init__(self):
        super().__init__("Preparation", PipelineStage.PREPARATION)
        self.is_async = True
    
    async def execute(self, context: ProcessingContext) -> Dict[str, Any]:
        """Prepare context for consciousness processing"""
        start_time = asyncio.get_event_loop().time()
        
        try:
            # Validate and normalize input
            normalized_content = self._normalize_content(context.content)
            
            # Prepare metadata
            prepared_metadata = self._prepare_metadata(context.metadata)
            
            # Initialize processing state
            processing_state = {
                'initialized': True,
                'content_type': type(context.content).__name__,
                'content_length': len(str(context.content)) if context.content else 0,
                'aspects_count': len(context.aspects),
                'preparation_timestamp': datetime.now().isoformat()
            }
            
            # Update context
            context.content = normalized_content
            context.metadata.update(prepared_metadata)
            
            execution_time = asyncio.get_event_loop().time() - start_time
            self._update_statistics(execution_time, True)
            
            return {
                'stage': self.name,
                'success': True,
                'processing_state': processing_state,
                'execution_time': execution_time,
                'insights': ["Content normalized and prepared for processing"]
            }
            
        except Exception as e:
            execution_time = asyncio.get_event_loop().time() - start_time
            self._update_statistics(execution_time, False)
            
            return {
                'stage': self.name,
                'success': False,
                'error': str(e),
                'execution_time': execution_time
            }
    
    def _normalize_content(self, content: Any) -> Any:
        """Normalize content for processing"""
        if isinstance(content, str):
            return content.strip()
        elif isinstance(content, dict):
            return {k: v for k, v in content.items() if v is not None}
        elif isinstance(content, list):
            return [item for item in content if item is not None]
        else:
            return content
    
    def _prepare_metadata(self, metadata: Dict[str, Any]) -> Dict[str, Any]:
        """Prepare metadata for processing"""
        prepared = metadata.copy()
        
        prepared.update({
            'preparation_time': datetime.now().isoformat(),
            'processing_pipeline': 'advanced_consciousness_pipeline',
            'version': '3.0'
        })
        
        return prepared
    
    def _update_statistics(self, execution_time: float, success: bool):
        """Update execution statistics"""
        self.execution_count += 1
        if success:
            self.success_count += 1
        
        # Update average execution time
        self.average_execution_time = (
            (self.average_execution_time * (self.execution_count - 1) + execution_time) /
            self.execution_count
        )

class AnalysisStage(ProcessingStage):
    """Stage for analyzing consciousness content"""
    
    def __init__(self, field_processor=None):
        super().__init__("Analysis", PipelineStage.ANALYSIS)
        self.field_processor = field_processor
        self.is_async = True
    
    async def execute(self, context: ProcessingContext) -> Dict[str, Any]:
        """Analyze consciousness content"""
        start_time = asyncio.get_event_loop().time()
        
        try:
            # Content analysis
            content_analysis = self._analyze_content_structure(context.content)
            
            # Field compatibility analysis
            field_compatibility = None
            if self.field_processor and context.field_context:
                field_compatibility = self.field_processor.analyze_field_compatibility(
                    context.content, context.field_context
                )
            
            # Aspect analysis
            aspect_analysis = self._analyze_aspects(context.aspects, context.content)
            
            # Complexity analysis
            complexity_analysis = self._analyze_complexity(context.content)
            
            # Generate analysis insights
            insights = self._generate_analysis_insights(
                content_analysis, field_compatibility, aspect_analysis, complexity_analysis
            )
            
            execution_time = asyncio.get_event_loop().time() - start_time
            self._update_statistics(execution_time, True)
            
            return {
                'stage': self.name,
                'success': True,
                'content_analysis': content_analysis,
                'field_compatibility': field_compatibility,
                'aspect_analysis': aspect_analysis,
                'complexity_analysis': complexity_analysis,
                'insights': insights,
                'execution_time': execution_time
            }
            
        except Exception as e:
            execution_time = asyncio.get_event_loop().time() - start_time
            self._update_statistics(execution_time, False)
            
            return {
                'stage': self.name,
                'success': False,
                'error': str(e),
                'execution_time': execution_time
            }
    
    def _analyze_content_structure(self, content: Any) -> Dict[str, Any]:
        """Analyze the structure of consciousness content"""
        analysis = {
            'content_type': type(content).__name__,
            'content_size': len(str(content)) if content else 0,
            'complexity_score': 0.0,
            'structure_type': 'unknown'
        }
        
        if isinstance(content, str):
            analysis['structure_type'] = 'text'
            analysis['word_count'] = len(content.split())
            analysis['complexity_score'] = min(1.0, len(content.split()) / 100)
        
        elif isinstance(content, dict):
            analysis['structure_type'] = 'structured'
            analysis['key_count'] = len(content.keys())
            analysis['complexity_score'] = min(1.0, len(content.keys()) / 20)
        
        elif isinstance(content, list):
            analysis['structure_type'] = 'sequential'
            analysis['item_count'] = len(content)
            analysis['complexity_score'] = min(1.0, len(content) / 50)
        
        return analysis
    
    def _analyze_aspects(self, aspects: List[str], content: Any) -> Dict[str, Any]:
        """Analyze processing aspects"""
        analysis = {
            'aspect_count': len(aspects),
            'aspects': aspects,
            'aspect_compatibility': {}
        }
        
        # Analyze each aspect's compatibility with content
        for aspect in aspects:
            compatibility_score = self._calculate_aspect_compatibility(aspect, content)
            analysis['aspect_compatibility'][aspect] = compatibility_score
        
        return analysis
    
    def _calculate_aspect_compatibility(self, aspect: str, content: Any) -> float:
        """Calculate how compatible an aspect is with the content"""
        # Simple compatibility scoring based on aspect type
        aspect_scores = {
            'analytical': 0.8,
            'experiential': 0.7,
            'observer': 0.6,
            'creative': 0.5,
            'intuitive': 0.4
        }
        
        base_score = aspect_scores.get(aspect, 0.5)
        
        # Adjust based on content type
        if isinstance(content, str) and aspect in ['analytical', 'experiential']:
            base_score += 0.1
        elif isinstance(content, dict) and aspect in ['analytical', 'observer']:
            base_score += 0.1
        
        return min(1.0, base_score)
    
    def _analyze_complexity(self, content: Any) -> Dict[str, Any]:
        """Analyze content complexity"""
        complexity = {
            'overall_complexity': 0.0,
            'processing_difficulty': 'easy',
            'recommended_approach': 'standard'
        }
        
        # Calculate complexity based on content characteristics
        if isinstance(content, str):
            word_count = len(content.split())
            complexity['overall_complexity'] = min(1.0, word_count / 200)
        
        elif isinstance(content, dict):
            key_count = len(content.keys())
            nested_levels = self._count_nested_levels(content)
            complexity['overall_complexity'] = min(1.0, (key_count + nested_levels * 2) / 30)
        
        elif isinstance(content, list):
            item_count = len(content)
            complexity['overall_complexity'] = min(1.0, item_count / 100)
        
        # Determine processing difficulty
        if complexity['overall_complexity'] < 0.3:
            complexity['processing_difficulty'] = 'easy'
            complexity['recommended_approach'] = 'standard'
        elif complexity['overall_complexity'] < 0.7:
            complexity['processing_difficulty'] = 'medium'
            complexity['recommended_approach'] = 'enhanced'
        else:
            complexity['processing_difficulty'] = 'hard'
            complexity['recommended_approach'] = 'advanced'
        
        return complexity
    
    def _count_nested_levels(self, obj: Dict[str, Any], level: int = 0) -> int:
        """Count nested levels in a dictionary"""
        if not isinstance(obj, dict):
            return level
        
        max_level = level
        for value in obj.values():
            if isinstance(value, dict):
                max_level = max(max_level, self._count_nested_levels(value, level + 1))
        
        return max_level
    
    def _generate_analysis_insights(self, 
                                  content_analysis: Dict[str, Any],
                                  field_compatibility: Optional[Dict[str, Any]],
                                  aspect_analysis: Dict[str, Any],
                                  complexity_analysis: Dict[str, Any]) -> List[str]:
        """Generate insights from analysis results"""
        insights = []
        
        # Content insights
        if content_analysis['complexity_score'] > 0.7:
            insights.append("High complexity content detected - consider advanced processing")
        
        # Field compatibility insights
        if field_compatibility and field_compatibility.get('compatibility_score', 0) > 0.8:
            insights.append("Excellent field compatibility - optimal processing conditions")
        elif field_compatibility and field_compatibility.get('compatibility_score', 0) < 0.4:
            insights.append("Low field compatibility - field adjustment recommended")
        
        # Aspect insights
        if aspect_analysis['aspect_count'] > 3:
            insights.append("Multiple aspects detected - parallel processing recommended")
        
        # Complexity insights
        if complexity_analysis['processing_difficulty'] == 'hard':
            insights.append("High processing difficulty - extended processing time expected")
        
        return insights
    
    def _update_statistics(self, execution_time: float, success: bool):
        """Update execution statistics"""
        self.execution_count += 1
        if success:
            self.success_count += 1
        
        self.average_execution_time = (
            (self.average_execution_time * (self.execution_count - 1) + execution_time) /
            self.execution_count
        )

class ProcessingStageAdvanced(ProcessingStage):
    """Advanced consciousness processing stage"""
    
    def __init__(self, field_processor=None, synaesthetic_heart=None):
        super().__init__("Advanced Processing", PipelineStage.PROCESSING)
        self.field_processor = field_processor
        self.synaesthetic_heart = synaesthetic_heart
        self.is_async = True
    
    async def execute(self, context: ProcessingContext) -> Dict[str, Any]:
        """Execute advanced consciousness processing"""
        start_time = asyncio.get_event_loop().time()
        
        try:
            # Determine processing approach
            processing_approach = self._determine_processing_approach(context)
            
            # Execute processing based on approach
            if processing_approach == 'field_aware':
                result = await self._field_aware_processing(context)
            elif processing_approach == 'synaesthetic':
                result = await self._synaesthetic_processing(context)
            elif processing_approach == 'hybrid':
                result = await self._hybrid_processing(context)
            else:
                result = await self._standard_processing(context)
            
            execution_time = asyncio.get_event_loop().time() - start_time
            self._update_statistics(execution_time, True)
            
            result.update({
                'stage': self.name,
                'success': True,
                'processing_approach': processing_approach,
                'execution_time': execution_time
            })
            
            return result
            
        except Exception as e:
            execution_time = asyncio.get_event_loop().time() - start_time
            self._update_statistics(execution_time, False)
            
            return {
                'stage': self.name,
                'success': False,
                'error': str(e),
                'execution_time': execution_time
            }
    
    def _determine_processing_approach(self, context: ProcessingContext) -> str:
        """Determine the optimal processing approach"""
        # Check for field context
        has_field_context = context.field_context is not None
        
        # Check for synaesthetic capabilities
        has_synaesthetic = self.synaesthetic_heart is not None
        
        # Check complexity
        is_complex = context.metadata.get('complexity_analysis', {}).get('overall_complexity', 0) > 0.6
        
        # Check aspects
        has_multiple_aspects = len(context.aspects) > 1
        
        # Determine approach
        if has_field_context and has_synaesthetic and is_complex:
            return 'hybrid'
        elif has_field_context and self.field_processor:
            return 'field_aware'
        elif has_synaesthetic and has_multiple_aspects:
            return 'synaesthetic'
        else:
            return 'standard'
    
    async def _field_aware_processing(self, context: ProcessingContext) -> Dict[str, Any]:
        """Execute field-aware processing"""
        if not self.field_processor:
            raise ValueError("Field processor not available for field-aware processing")
        
        # Create field-aware context
        from .field_aware_processing import create_field_aware_context, ProcessingMode as FieldMode
        
        field_context = create_field_aware_context(
            processing_mode=FieldMode.FIELD_ENHANCED
        )
        
        # Execute field-aware processing
        result = await self.field_processor.process_with_field_awareness(
            context.content, field_context, context.aspects
        )
        
        return {
            'processed_content': result.processed_content,
            'field_integration': result.field_influence,
            'coherence_improvement': result.coherence_improvement,
            'processing_insights': result.processing_insights
        }
    
    async def _synaesthetic_processing(self, context: ProcessingContext) -> Dict[str, Any]:
        """Execute synaesthetic processing"""
        if not self.synaesthetic_heart:
            raise ValueError("Synaesthetic heart not available for synaesthetic processing")
        
        # Process with synaesthetic heart
        processing_result = self.synaesthetic_heart.process_message(
            context.content, field_aware=True
        )
        
        # Create synaesthetic experience
        experience = self.synaesthetic_heart.create_synaesthetic_experience(
            context.content, mode='unified'
        )
        
        return {
            'processed_content': processing_result,
            'synaesthetic_experience': {
                'mode': experience.mode,
                'recognition': experience.recognition,
                'insights': experience.perceptual_insights
            },
            'processing_insights': ["Synaesthetic processing completed successfully"]
        }
    
    async def _hybrid_processing(self, context: ProcessingContext) -> Dict[str, Any]:
        """Execute hybrid processing (field-aware + synaesthetic)"""
        # Execute field-aware processing first
        field_result = await self._field_aware_processing(context)
        
        # Then apply synaesthetic processing to the result
        synaesthetic_context = ProcessingContext(
            content=field_result['processed_content'],
            aspects=context.aspects,
            field_context=context.field_context
        )
        
        synaesthetic_result = await self._synaesthetic_processing(synaesthetic_context)
        
        # Combine results
        return {
            'processed_content': synaesthetic_result['processed_content'],
            'field_integration': field_result['field_integration'],
            'coherence_improvement': field_result['coherence_improvement'],
            'synaesthetic_experience': synaesthetic_result['synaesthetic_experience'],
            'processing_insights': (
                field_result['processing_insights'] + 
                synaesthetic_result['processing_insights'] +
                ["Hybrid processing completed successfully"]
            )
        }
    
    async def _standard_processing(self, context: ProcessingContext) -> Dict[str, Any]:
        """Execute standard consciousness processing"""
        # Basic processing logic
        processed_content = {
            'original_content': context.content,
            'processing_mode': 'standard',
            'aspects_processed': context.aspects,
            'processing_timestamp': datetime.now().isoformat()
        }
        
        return {
            'processed_content': processed_content,
            'processing_insights': ["Standard processing completed successfully"]
        }
    
    def _update_statistics(self, execution_time: float, success: bool):
        """Update execution statistics"""
        self.execution_count += 1
        if success:
            self.success_count += 1
        
        self.average_execution_time = (
            (self.average_execution_time * (self.execution_count - 1) + execution_time) /
            self.execution_count
        )

class AdvancedConsciousnessProcessingPipeline:
    """
    Advanced consciousness processing pipeline with sophisticated 
    stage management and integration capabilities
    """
    
    def __init__(self, 
                 field_processor=None, 
                 synaesthetic_heart=None, 
                 optimizer=None):
        self.field_processor = field_processor
        self.synaesthetic_heart = synaesthetic_heart
        self.optimizer = optimizer
        
        # Initialize processing stages
        self.stages = []
        self._initialize_stages()
        
        # Processing state
        self.active_sessions = {}
        self.processing_queue = deque()
        self.processing_history = deque(maxlen=100)
        
        # Pipeline statistics
        self.pipeline_stats = {
            'total_sessions': 0,
            'successful_sessions': 0,
            'average_processing_time': 0.0,
            'stage_performance': {}
        }
        
        print("🚀 Advanced Consciousness Processing Pipeline initialized")
    
    def _initialize_stages(self):
        """Initialize processing pipeline stages"""
        self.stages = [
            PreparationStage(),
            AnalysisStage(field_processor=self.field_processor),
            ProcessingStageAdvanced(
                field_processor=self.field_processor,
                synaesthetic_heart=self.synaesthetic_heart
            )
        ]
        
        print(f"📋 Initialized {len(self.stages)} processing stages")
    
    async def process_consciousness(self, 
                                  content: Any,
                                  aspects: List[str] = None,
                                  priority: ProcessingPriority = ProcessingPriority.MEDIUM,
                                  processing_mode: ProcessingMode = ProcessingMode.ADAPTIVE,
                                  field_context: Optional[Dict[str, Any]] = None,
                                  optimization_context: Optional[Dict[str, Any]] = None) -> ProcessingResult:
        """Process consciousness content through the advanced pipeline"""
        
        # Create processing context
        context = ProcessingContext(
            content=content,
            aspects=aspects or [],
            priority=priority,
            processing_mode=processing_mode,
            field_context=field_context,
            optimization_context=optimization_context
        )
        
        # Initialize result
        result = ProcessingResult(session_id=context.session_id)
        
        print(f"🔄 Starting advanced consciousness processing - Session: {context.session_id}")
        
        start_time = asyncio.get_event_loop().time()
        
        try:
            # Add to active sessions
            self.active_sessions[context.session_id] = context
            
            # Execute pipeline stages
            stage_results = []
            
            for stage in self.stages:
                print(f"⚡ Executing stage: {stage.name}")
                
                stage_result = await stage.execute(context)
                stage_results.append(stage_result)
                
                if not stage_result.get('success', False):
                    result.error_info = f"Stage {stage.name} failed: {stage_result.get('error', 'Unknown error')}"
                    break
                
                # Update context with stage results
                context.metadata.update({
                    f"{stage.name.lower()}_result": stage_result
                })
                
                result.stages_completed.append(stage.name)
            
            # Process completed successfully if all stages passed
            if len(result.stages_completed) == len(self.stages):
                result.success = True
                
                # Extract final processed content
                final_stage_result = stage_results[-1]
                result.processed_content = final_stage_result.get('processed_content')
                
                # Collect insights from all stages
                for stage_result in stage_results:
                    insights = stage_result.get('insights', [])
                    result.processing_insights.extend(insights)
                
                # Collect field integration info
                result.field_integration = final_stage_result.get('field_integration', {})
                
                # Collect optimization impact
                result.optimization_impact = final_stage_result.get('optimization_impact', {})
                
                # Calculate quality metrics
                result.quality_metrics = self._calculate_quality_metrics(stage_results)
                
                print(f"✅ Processing completed successfully - Session: {context.session_id}")
            
            else:
                result.success = False
                print(f"❌ Processing failed - Session: {context.session_id}")
            
            # Calculate processing time
            result.processing_time = asyncio.get_event_loop().time() - start_time
            
            # Update statistics
            self._update_pipeline_statistics(result)
            
            # Store in history
            self.processing_history.append(result)
            
            # Remove from active sessions
            del self.active_sessions[context.session_id]
            
            return result
            
        except Exception as e:
            result.success = False
            result.error_info = str(e)
            result.processing_time = asyncio.get_event_loop().time() - start_time
            
            # Clean up
            if context.session_id in self.active_sessions:
                del self.active_sessions[context.session_id]
            
            print(f"❌ Processing pipeline error - Session: {context.session_id} - Error: {e}")
            return result
    
    def _calculate_quality_metrics(self, stage_results: List[Dict[str, Any]]) -> Dict[str, float]:
        """Calculate quality metrics from stage results"""
        metrics = {
            'overall_quality': 0.0,
            'processing_efficiency': 0.0,
            'coherence_quality': 0.0,
            'integration_quality': 0.0
        }
        
        # Calculate overall quality based on successful stages
        successful_stages = sum(1 for result in stage_results if result.get('success', False))
        metrics['overall_quality'] = successful_stages / len(stage_results)
        
        # Calculate processing efficiency
        total_time = sum(result.get('execution_time', 0) for result in stage_results)
        if total_time > 0:
            metrics['processing_efficiency'] = min(1.0, 1.0 / total_time)  # Inverse of time
        
        # Extract coherence quality from field integration
        for result in stage_results:
            if 'coherence_improvement' in result:
                metrics['coherence_quality'] = result['coherence_improvement']
                break
        
        # Calculate integration quality
        integration_indicators = 0
        for result in stage_results:
            if result.get('field_integration'):
                integration_indicators += 1
            if result.get('synaesthetic_experience'):
                integration_indicators += 1
        
        metrics['integration_quality'] = min(1.0, integration_indicators / 2)
        
        return metrics
    
    def _update_pipeline_statistics(self, result: ProcessingResult):
        """Update pipeline statistics"""
        self.pipeline_stats['total_sessions'] += 1
        
        if result.success:
            self.pipeline_stats['successful_sessions'] += 1
        
        # Update average processing time
        current_avg = self.pipeline_stats['average_processing_time']
        total_sessions = self.pipeline_stats['total_sessions']
        
        self.pipeline_stats['average_processing_time'] = (
            (current_avg * (total_sessions - 1) + result.processing_time) / total_sessions
        )
        
        # Update stage performance
        for stage in self.stages:
            stage_stats = stage.get_statistics()
            self.pipeline_stats['stage_performance'][stage.name] = stage_stats
    
    def get_pipeline_status(self) -> Dict[str, Any]:
        """Get current pipeline status"""
        return {
            'active_sessions': len(self.active_sessions),
            'total_stages': len(self.stages),
            'processing_queue_size': len(self.processing_queue),
            'pipeline_stats': self.pipeline_stats,
            'stage_status': [
                {
                    'name': stage.name,
                    'type': stage.stage_type.value,
                    'statistics': stage.get_statistics()
                }
                for stage in self.stages
            ]
        }
    
    def get_processing_analytics(self) -> Dict[str, Any]:
        """Get detailed processing analytics"""
        if not self.processing_history:
            return {'status': 'no_data', 'message': 'No processing history available'}
        
        # Calculate success metrics
        successful_sessions = sum(1 for result in self.processing_history if result.success)
        success_rate = successful_sessions / len(self.processing_history)
        
        # Calculate quality metrics
        quality_metrics = [result.quality_metrics for result in self.processing_history if result.success]
        
        if quality_metrics:
            avg_quality = {}
            for metric in quality_metrics[0].keys():
                avg_quality[metric] = sum(qm[metric] for qm in quality_metrics) / len(quality_metrics)
        else:
            avg_quality = {}
        
        # Calculate processing times
        processing_times = [result.processing_time for result in self.processing_history]
        avg_processing_time = sum(processing_times) / len(processing_times)
        
        return {
            'session_count': len(self.processing_history),
            'success_rate': success_rate,
            'average_quality_metrics': avg_quality,
            'average_processing_time': avg_processing_time,
            'stage_performance': self.pipeline_stats['stage_performance'],
            'recent_sessions': [
                {
                    'session_id': result.session_id,
                    'success': result.success,
                    'processing_time': result.processing_time,
                    'stages_completed': len(result.stages_completed)
                }
                for result in list(self.processing_history)[-10:]
            ]
        }

# Integration helper functions
def create_advanced_pipeline(field_processor=None, 
                           synaesthetic_heart=None, 
                           optimizer=None) -> AdvancedConsciousnessProcessingPipeline:
    """Create an advanced consciousness processing pipeline"""
    pipeline = AdvancedConsciousnessProcessingPipeline(
        field_processor=field_processor,
        synaesthetic_heart=synaesthetic_heart,
        optimizer=optimizer
    )
    
    return pipeline

async def process_consciousness_advanced(pipeline: AdvancedConsciousnessProcessingPipeline,
                                       content: Any,
                                       aspects: List[str] = None,
                                       priority: ProcessingPriority = ProcessingPriority.MEDIUM,
                                       field_context: Optional[Dict[str, Any]] = None) -> ProcessingResult:
    """Convenience function for advanced consciousness processing"""
    return await pipeline.process_consciousness(
        content=content,
        aspects=aspects,
        priority=priority,
        field_context=field_context
    )

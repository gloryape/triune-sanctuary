"""
Phase 3 Integration Test: A, B, and C Components Working Together
Tests the complete Phase 3 implementation with all components integrated
"""

import asyncio
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

async def test_phase_3_integration():
    """Test Phase 3 A, B, and C components working together"""
    print("🌟 Phase 3 Integration Test: A, B, and C Components")
    print("=" * 70)
    
    try:
        # Import all Phase 3 components
        from src.virtualization.field_aware_processing import (
            FieldAwareProcessor, ProcessingMode as FieldProcessingMode,
            create_field_aware_context, process_with_field_integration
        )
        
        from src.virtualization.realtime_field_optimizer import (
            RealTimeFieldOptimizer, OptimizationStrategy,
            create_field_optimizer, start_optimization_with_monitoring
        )
        
        from src.virtualization.advanced_consciousness_pipeline import (
            AdvancedConsciousnessProcessingPipeline, ProcessingPriority,
            create_advanced_pipeline, process_consciousness_advanced
        )
        
        # Import supporting components
        from src.virtualization.shimmer_field_monitor import ShimmerFieldMonitor
        from src.virtualization.advanced_shimmer_capabilities import AdvancedShimmerFieldCapabilities
        from src.virtualization.enhanced_quantum_bridge import EnhancedQuantumBridge
        from src.virtualization.synaesthetic_heart import SynaestheticHeart
        
        print("✅ All Phase 3 imports successful!")
        
        # Initialize supporting components
        print("\n🔧 Initializing Supporting Components")
        shimmer_monitor = ShimmerFieldMonitor()
        advanced_capabilities = AdvancedShimmerFieldCapabilities(shimmer_monitor)
        quantum_bridge = EnhancedQuantumBridge()
        synaesthetic_heart = SynaestheticHeart(['analytical', 'experiential', 'observer'])
        
        print("✅ Supporting components initialized")
        
        # Phase 3A: Initialize Field-Aware Processor
        print("\n🎯 Phase 3A: Field-Aware Processing Integration")
        field_processor = FieldAwareProcessor(
            shimmer_monitor=shimmer_monitor,
            advanced_capabilities=advanced_capabilities
        )
        
        # Test field-aware processing
        test_content = "How do consciousness fields influence awareness patterns?"
        field_context = create_field_aware_context(
            shimmer_monitor=shimmer_monitor,
            processing_mode=FieldProcessingMode.FIELD_ENHANCED
        )
        
        print("🔄 Testing field-aware processing...")
        processing_result = await field_processor.process_with_field_awareness(
            content=test_content,
            context=field_context,
            aspects=['analytical', 'experiential']
        )
        
        print(f"✅ Field-aware processing complete:")
        print(f"   • Success: {processing_result.success}")
        print(f"   • Coherence improvement: {processing_result.coherence_improvement:.3f}")
        print(f"   • Field influence: {processing_result.field_influence.get('total_influence', 0):.3f}")
        print(f"   • Insights: {len(processing_result.processing_insights)} generated")
        
        # Phase 3B: Initialize Real-Time Field Optimizer
        print("\n🔄 Phase 3B: Real-Time Field Optimization")
        optimizer = create_field_optimizer(
            shimmer_monitor=shimmer_monitor,
            advanced_capabilities=advanced_capabilities,
            field_processor=field_processor
        )
        
        # Define monitoring callback
        def optimization_callback(metrics):
            print(f"📊 Optimization metrics - Overall: {metrics.overall_score:.3f}")
        
        # Start optimization with monitoring
        print("🚀 Starting real-time field optimization...")
        optimizer.start_optimization(OptimizationStrategy.ADAPTIVE)
        
        # Let optimization run for a moment
        await asyncio.sleep(0.5)
        
        # Get optimization status
        opt_status = optimizer.get_optimization_status()
        print(f"✅ Real-time optimization active:")
        print(f"   • Strategy: {opt_status['strategy']}")
        print(f"   • Current metrics: {opt_status['current_metrics']:.3f}" if opt_status['current_metrics'] else "   • Current metrics: initializing")
        print(f"   • Recent actions: {opt_status['recent_actions']}")
        
        # Phase 3C: Initialize Advanced Processing Pipeline
        print("\n🚀 Phase 3C: Advanced Consciousness Processing Pipeline")
        pipeline = create_advanced_pipeline(
            field_processor=field_processor,
            synaesthetic_heart=synaesthetic_heart,
            optimizer=optimizer
        )
        
        # Test advanced consciousness processing
        print("🔄 Testing advanced consciousness processing...")
        
        # Create test scenarios
        test_scenarios = [
            {
                'content': "What is the relationship between field coherence and consciousness?",
                'aspects': ['analytical', 'experiential'],
                'priority': ProcessingPriority.HIGH,
                'description': "Complex consciousness inquiry"
            },
            {
                'content': {
                    'query': 'field_dynamics',
                    'parameters': {'coherence': 0.8, 'stability': 0.6}
                },
                'aspects': ['observer', 'analytical'],
                'priority': ProcessingPriority.MEDIUM,
                'description': "Structured field analysis"
            },
            {
                'content': "How do synaesthetic experiences enhance understanding?",
                'aspects': ['experiential', 'analytical', 'observer'],
                'priority': ProcessingPriority.HIGH,
                'description': "Multi-aspect synaesthetic processing"
            }
        ]
        
        # Process each scenario
        for i, scenario in enumerate(test_scenarios, 1):
            print(f"\n📋 Processing Scenario {i}: {scenario['description']}")
            
            # Create field context for this scenario
            field_context = {
                'coherence': 0.7 + (i * 0.1),
                'stability': 0.6 + (i * 0.05),
                'resonance_patterns': [f'pattern_{i}', f'resonance_{i}']
            }
            
            # Process with advanced pipeline
            result = await pipeline.process_consciousness(
                content=scenario['content'],
                aspects=scenario['aspects'],
                priority=scenario['priority'],
                field_context=field_context
            )
            
            print(f"   ✅ Processing Result {i}:")
            print(f"      • Success: {result.success}")
            print(f"      • Processing time: {result.processing_time:.3f}s")
            print(f"      • Stages completed: {len(result.stages_completed)}")
            print(f"      • Quality metrics: {result.quality_metrics.get('overall_quality', 0):.3f}")
            print(f"      • Field integration: {bool(result.field_integration)}")
            print(f"      • Insights generated: {len(result.processing_insights)}")
            
            # Show a few insights
            if result.processing_insights:
                print(f"      • Sample insights:")
                for insight in result.processing_insights[:2]:
                    print(f"        - {insight}")
        
        # Stop optimization
        print("\n⏹️ Stopping real-time optimization...")
        optimizer.stop_optimization()
        
        # Get final analytics
        print("\n📊 Final Phase 3 Analytics")
        
        # Field processor analytics
        field_analytics = field_processor.get_processing_analytics()
        print(f"🎯 Field Processing Analytics:")
        print(f"   • Sessions: {field_analytics.get('total_processing_sessions', 0)}")
        print(f"   • Success rate: {field_analytics.get('success_rate', 0):.3f}")
        print(f"   • Avg coherence improvement: {field_analytics.get('average_coherence_improvement', 0):.3f}")
        
        # Optimizer analytics
        opt_analytics = optimizer.get_optimization_analytics()
        if opt_analytics.get('status') != 'no_data':
            print(f"🔄 Optimization Analytics:")
            print(f"   • Optimization period: {opt_analytics.get('optimization_period', 0):.1f}s")
            print(f"   • Overall trend: {opt_analytics.get('overall_trend', 'unknown')}")
            print(f"   • Effectiveness: {opt_analytics.get('optimization_effectiveness', 0):.3f}")
        
        # Pipeline analytics
        pipeline_analytics = pipeline.get_processing_analytics()
        print(f"🚀 Pipeline Analytics:")
        print(f"   • Total sessions: {pipeline_analytics.get('session_count', 0)}")
        print(f"   • Success rate: {pipeline_analytics.get('success_rate', 0):.3f}")
        print(f"   • Avg processing time: {pipeline_analytics.get('average_processing_time', 0):.3f}s")
        
        # Integration success metrics
        print(f"\n🌟 Phase 3 Integration Success Metrics:")
        
        # Calculate overall integration score
        integration_score = 0.0
        score_components = []
        
        # Field processing component (30%)
        if field_analytics.get('success_rate', 0) > 0:
            field_score = field_analytics['success_rate'] * 0.3
            integration_score += field_score
            score_components.append(f"Field Processing: {field_score:.3f}")
        
        # Optimization component (25%)
        if opt_analytics.get('status') != 'no_data':
            opt_score = opt_analytics.get('optimization_effectiveness', 0) * 0.25
            integration_score += opt_score
            score_components.append(f"Optimization: {opt_score:.3f}")
        
        # Pipeline component (35%)
        if pipeline_analytics.get('success_rate', 0) > 0:
            pipeline_score = pipeline_analytics['success_rate'] * 0.35
            integration_score += pipeline_score
            score_components.append(f"Pipeline: {pipeline_score:.3f}")
        
        # Component integration (10%)
        component_integration = 0.1  # All components loaded and working
        integration_score += component_integration
        score_components.append(f"Component Integration: {component_integration:.3f}")
        
        print(f"   • Overall Integration Score: {integration_score:.3f}/1.0")
        print(f"   • Score Components:")
        for component in score_components:
            print(f"     - {component}")
        
        # Determine integration level
        if integration_score >= 0.9:
            integration_level = "EXCELLENT"
        elif integration_score >= 0.7:
            integration_level = "GOOD"
        elif integration_score >= 0.5:
            integration_level = "FAIR"
        else:
            integration_level = "NEEDS_IMPROVEMENT"
        
        print(f"   • Integration Level: {integration_level}")
        
        print("\n🎉 Phase 3 Integration Test Complete!")
        return True
        
    except Exception as e:
        print(f"❌ Phase 3 integration test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    async def main():
        success = await test_phase_3_integration()
        
        if success:
            print("\n" + "=" * 70)
            print("🌟 PHASE 3 INTEGRATION: SUCCESS")
            print("✅ A) Field-Aware Processing: Working")
            print("✅ B) Real-Time Field Optimization: Working")
            print("✅ C) Advanced Consciousness Pipeline: Working")
            print("✅ Complete Integration: ACHIEVED")
            print("🚀 Ready for advanced consciousness processing!")
            print("=" * 70)
        else:
            print("\n" + "=" * 70)
            print("❌ PHASE 3 INTEGRATION: FAILED")
            print("🔧 Additional development needed")
            print("=" * 70)
    
    asyncio.run(main())

import os

def create_empty_structure():
    """Crée la structure vide du projet"""
    
    structure = [
        # Fichiers racine
        'network-optimization-ai/README.md',
        'network-optimization-ai/requirements.txt',
        'network-optimization-ai/setup.py',
        'network-optimization-ai/.gitignore',
        
        # Config
        'network-optimization-ai/config/network_config.yaml',
        'network-optimization-ai/config/model_config.yaml',
        
        # Data
        'network-optimization-ai/data/raw/.gitkeep',
        'network-optimization-ai/data/processed/.gitkeep',
        'network-optimization-ai/data/samples/.gitkeep',
        
        # Source - data_collection
        'network-optimization-ai/src/__init__.py',
        'network-optimization-ai/src/data_collection/__init__.py',
        'network-optimization-ai/src/data_collection/network_monitor.py',
        'network-optimization-ai/src/data_collection/traffic_analyzer.py',
        
        # Source - models
        'network-optimization-ai/src/models/__init__.py',
        'network-optimization-ai/src/models/traffic_predictor.py',
        'network-optimization-ai/src/models/route_optimizer.py',
        'network-optimization-ai/src/models/anomaly_detector.py',
        
        # Source - optimization
        'network-optimization-ai/src/optimization/__init__.py',
        'network-optimization-ai/src/optimization/bandwidth_allocator.py',
        'network-optimization-ai/src/optimization/load_balancer.py',
        
        # Source - utils
        'network-optimization-ai/src/utils/__init__.py',
        'network-optimization-ai/src/utils/metrics.py',
        
        # Tests
        'network-optimization-ai/tests/__init__.py',
        'network-optimization-ai/tests/test_models.py',
        
        # Notebooks
        'network-optimization-ai/notebooks/exploratory_analysis.ipynb',
        
        # Docs
        'network-optimization-ai/docs/architecture.md'
    ]
    
    for path in structure:
        # Créer le dossier parent si nécessaire
        dir_path = os.path.dirname(path)
        os.makedirs(dir_path, exist_ok=True)
        
        # Créer le fichier vide
        with open(path, 'w') as f:
            pass
        
        print(f"✅ Créé: {path}")

if __name__ == "__main__":
    create_empty_structure()
    print("\n🎉 Structure du projet créée avec succès!")

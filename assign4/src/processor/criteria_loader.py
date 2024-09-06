def fetch_criterion(criterion_name):
    criterion_module = __import__(f"criteria.{criterion_name}", fromlist=[""])
    
    return getattr(criterion_module, criterion_name)

class ModelDatabaseRouter(object):
    """Allows each model to set its own destiny"""
    
    def db_for_read(self, model, **hints):
        # Specify target database with field in_db in model's Meta class
        if model._meta.app_label == 'polls':
            return 'staging'
        return None

    def db_for_write(self, model, **hints):
        # Specify target database with field in_db in model's Meta class
        if model._meta.app_label == 'polls':
            return 'staging'
        return None

    
    def allow_syncdb(self, db, model):
        """
        Make sure the 'myapp2' app only appears on the 'other' db
        """
        if db == 'staging':
            return model._meta.app_label == 'polls'
        elif model._meta.app_label == 'polls':
            return False
        return None